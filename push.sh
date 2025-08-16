#!/usr/bin/env bash
set -euo pipefail

BRANCH="${1:-feat/ch7-packaging-placeholder}"
REPO_DIR="${2:-.}"

echo "[i] Branch: $BRANCH"
echo "[i] Repo dir: $REPO_DIR"

cd "$REPO_DIR"

git checkout -b "$BRANCH"

mkdir -p Patches Trackers
cp -v "$(dirname "$0")/Patches/CH7-placeholder.md" Patches/CH7-placeholder.md
cp -v "$(dirname "$0")/Trackers/CH7-state.md" Trackers/CH7-state.md

git add Patches/CH7-placeholder.md Trackers/CH7-state.md
git commit -m "chore(ch7): add packaging-only placeholder and state tracker"
git push --set-upstream origin "$BRANCH"

if command -v gh >/dev/null 2>&1; then
  gh pr create --fill --title "chore(ch7): packaging-only placeholder" --body-file "$(dirname "$0")/PR_BODY.md"
else
  echo "[i] GitHub CLI not found. Open a PR manually using the branch $BRANCH and PR_BODY.md."
fi
