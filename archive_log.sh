#!/usr/bin/env bash
set -euo pipefail

BRANCH="${1:-$(git rev-parse --abbrev-ref HEAD)}"
BASE="${2:-main}"

# derive web URL from origin
ORIGIN_URL="$(git remote get-url origin)"
if [[ "$ORIGIN_URL" =~ ^git@github.com:(.*)\.git$ ]]; then
  REPO_WEB="https://github.com/${BASH_REMATCH[1]}"
elif [[ "$ORIGIN_URL" =~ ^https://github.com/(.*)\.git$ ]]; then
  REPO_WEB="https://github.com/${BASH_REMATCH[1]}"
else
  echo "Unsupported remote URL: $ORIGIN_URL" >&2; exit 1
fi

SHA="$(git rev-parse HEAD)"
PR_URL="${REPO_WEB}/compare/${BASE}...${BRANCH}"

mkdir -p Archive

STAMP="$(date +%Y%m%d-%H%M)"
SAFE_BRANCH="${BRANCH//\//_}"   # replace / with _ for filenames
FILE="Archive/ARCHIVE_PACK_${STAMP}_${SAFE_BRANCH}.md"

cat > "$FILE" <<EOF
ARCHIVE PACK — Epilogue CI Assertions

PR URL:
- ${BRANCH}: ${PR_URL}

SHAs:
- ${BRANCH} = ${SHA}
EOF

git add "$FILE"
git commit -m "docs(archive): log ${BRANCH} PR + SHA (${SHA:0:7})"
git push

# Open PR if possible; otherwise print the link
if command -v gh >/dev/null 2>&1; then
  if ! gh pr view --repo "${REPO_WEB#https://github.com/}" >/dev/null 2>&1; then
    gh pr create       --title "ci(epilogue): add validation workflow and archive log"       --body-file "$FILE"       --base "$BASE"
  fi
else
  echo "[i] Open PR manually:"
  echo "    ${PR_URL}"
fi

echo "[i] Archive block written to $FILE"
echo "----"
cat "$FILE"
