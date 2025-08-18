\
#!/usr/bin/env bash
set -euo pipefail

PASS=0
FAIL=0
WARN=0

ok()   { PASS=$((PASS+1)); echo "[OK]    $*"; }
bad()  { FAIL=$((FAIL+1)); echo "[FAIL]  $*" >&2; }
warn() { WARN=$((WARN+1)); echo "[WARN]  $*"; }

if ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"; then :; else
  bad "Not a git repo. Run inside your Diplomagic repo."
  exit 2
fi
SITE="$ROOT/ops/site"

[ -f "$SITE/mkdocs.yml" ] && ok "ops/site/mkdocs.yml exists" || bad "Missing ops/site/mkdocs.yml"
[ -d "$SITE/docs" ] && ok "ops/site/docs/ exists" || bad "Missing ops/site/docs/"
if [ -f "$SITE/docs/index.md" ] || [ -f "$SITE/docs/README.md" ]; then ok "Landing page exists"; else bad "Missing docs/index.md"; fi

if [ -f "$SITE/requirements.txt" ]; then
  if grep -qi 'mkdocs' "$SITE/requirements.txt"; then ok "mkdocs deps listed"; else warn "requirements.txt lacks mkdocs deps"; fi
else
  warn "No ops/site/requirements.txt"
fi

if command -v mkdocs >/dev/null 2>&1; then ok "mkdocs on PATH ($(mkdocs --version | head -n1))"; else bad "mkdocs not on PATH"; fi

if mkdocs build --strict --config-file "$SITE/mkdocs.yml" --site-dir "$SITE/site" >/dev/null 2>&1; then ok "local mkdocs build OK"; else bad "mkdocs build failed"; fi

REMOTE="${REMOTE:-origin}"
if git ls-remote --exit-code --heads "$REMOTE" gh-pages >/dev/null 2>&1; then ok "gh-pages exists on $REMOTE"; else warn "gh-pages not found on $REMOTE"; fi

remote_url="$(git remote get-url "$REMOTE" 2>/dev/null || true)"
owner=""; repo=""
if [[ "$remote_url" =~ ^git@github.com:(.+)/(.+)\.git$ ]]; then owner="${BASH_REMATCH[1]}"; repo="${BASH_REMATCH[2]}";
elif [[ "$remote_url" =~ ^https://github.com/([^/]+)/([^/]+)(\.git)?$ ]]; then owner="${BASH_REMATCH[1]}"; repo="${BASH_REMATCH[2]}"; fi
if [ -n "$owner" ] && [ -n "$repo" ]; then ok "Detected GitHub repo: $owner/$repo"; else warn "Cannot parse GitHub repo from $remote_url"; fi

if command -v gh >/dev/null 2>&1 && [ -n "$owner" ] && [ -n "$repo" ]; then
  has_pages="$(gh api "repos/$owner/$repo" --jq '.has_pages' 2>/dev/null || echo "")"
  if [ "$has_pages" = "true" ]; then
    ok "GitHub Pages enabled"
    page_url="$(gh api "repos/$owner/$repo/pages" --jq '.html_url' 2>/dev/null || echo "")"
    if [ -n "$page_url" ]; then ok "Pages URL: $page_url"; fi
  else
    warn "GitHub Pages not enabled (Settings → Pages)"
  fi
else
  warn "Skip Pages API checks (gh CLI missing or repo unknown)"
fi

if git show "$REMOTE/gh-pages:.nojekyll" >/dev/null 2>&1; then ok ".nojekyll present on gh-pages"; else warn "No .nojekyll (not required but recommended)"; fi
if git show "$REMOTE/gh-pages:CNAME" >/dev/null 2>&1; then cname="$(git show "$REMOTE/gh-pages:CNAME" 2>/dev/null | tr -d '\r' | head -n1)"; ok "CNAME set: $cname"; else warn "No CNAME on gh-pages"; fi

echo
echo "Summary: $PASS ok, $WARN warn, $FAIL fail"
exit $([ "$FAIL" -eq 0 ] && echo 0 || echo 1)
