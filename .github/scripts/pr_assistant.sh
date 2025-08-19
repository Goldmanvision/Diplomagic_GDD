#!/usr/bin/env bash
set -euo pipefail
BASE_SHA="${1:-}"
HEAD_SHA="${2:-}"
PR_NUM="${3:-}"
OUT=".github/scripts/_pr_assistant_out.md"
if [[ -z "$BASE_SHA" || -z "$HEAD_SHA" ]]; then echo "Missing SHAs"; exit 1; fi
CHANGED_FILES=$(git diff --name-status "$BASE_SHA" "$HEAD_SHA" | sed "s/\t/ /g")
LINES_ADDED=$(git diff --numstat "$BASE_SHA" "$HEAD_SHA" | awk "{a+=\$1} END{print a+0}")
LINES_REMOVED=$(git diff --numstat "$BASE_SHA" "$HEAD_SHA" | awk "{a+=\$2} END{print a+0}")
TOTAL_FILES=$(git diff --name-only "$BASE_SHA" "$HEAD_SHA" | wc -l | awk "{print \$1}")
RISK=()
echo "$CHANGED_FILES" | grep -E "^\s*D" >/dev/null && RISK+=("Deletes present") || true
echo "$CHANGED_FILES" | grep -E "\.github/workflows|\.ps1$|\.sh$" >/dev/null && RISK+=("Workflow/script changes") || true
[[ $((LINES_ADDED + LINES_REMOVED)) -gt 800 ]] && RISK+=("Large diff")
{
  echo "<!-- PR_ASSISTANT_MARKER -->"
  echo "# PR Assistant Summary"
  echo "**PR #${PR_NUM}**"
  echo "Files: **$TOTAL_FILES**  Lines + / - : **$LINES_ADDED** / **$LINES_REMOVED**"
  echo "## Changed files"
  echo '```text'; echo "$CHANGED_FILES" | head -n 200; echo '```'
  echo "## Risk notes"; if [[ ${#RISK[@]} -gt 0 ]]; then for r in "${RISK[@]}"; do echo "- $r"; done; else echo "- None"; fi
  echo "## Merge gate"; echo "- [ ] Tests done  - [ ] Secrets ok  - [ ] Deploy impact  - [ ] Rollback plan"
} > "$OUT"
echo "Wrote $OUT"
