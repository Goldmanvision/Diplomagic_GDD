#!/usr/bin/env bash
set -euo pipefail
PASS=0; FAIL=0; WARN=0
ok(){ PASS=$((PASS+1)); echo "[OK]    $*"; }
bad(){ FAIL=$((FAIL+1)); echo "[FAIL]  $*" >&2; }
warn(){ WARN=$((WARN+1)); echo "[WARN]  $*"; }
if ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"; then :; else bad "Not a git repo."; exit 2; fi
SITE="$ROOT/ops/site"
[ -f "$SITE/mkdocs.yml" ] && ok "mkdocs.yml exists" || bad "missing mkdocs.yml"
[ -d "$SITE/docs" ] && ok "docs/ exists" || bad "missing docs/"
if command -v mkdocs >/dev/null 2>&1; then ok "mkdocs on PATH ($(mkdocs --version | head -n1))"; else warn "mkdocs not on PATH"; fi
if mkdocs build --strict --config-file "$SITE/mkdocs.yml" --site-dir "$SITE/site" >/dev/null 2>&1; then ok "local build OK"; else bad "mkdocs build failed"; fi
echo "Summary: $PASS ok, $WARN warn, $FAIL fail"
exit $([ "$FAIL" -eq 0 ] && echo 0 || echo 1)
