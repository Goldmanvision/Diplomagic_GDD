#!/usr/bin/env bash
set -euo pipefail

REMOTE="${REMOTE:-origin}"
BRANCH="${BRANCH:-gh-pages}"
CNAME="${CNAME:-}"   # set to custom domain if used

ROOT="$(git rev-parse --show-toplevel)"
SITE_ROOT="$ROOT/ops/site"
BUILD_DIR="$SITE_ROOT/site"
PAGES_DIR="$ROOT/.gh-pages"

if [ ! -d "$BUILD_DIR" ]; then
  echo "Build dir missing. Run build.sh first." >&2
  exit 1
fi

git fetch "$REMOTE" --prune

# Create branch if missing
if ! git show-ref --quiet "refs/heads/$BRANCH"; then
  git checkout --orphan "$BRANCH"
  git reset --hard
  echo "init" > .init
  git add .init
  git commit -m "Initialize $BRANCH"
  git push "$REMOTE" "$BRANCH"
  git checkout -
fi

# Worktree deploy
rm -rf "$PAGES_DIR"
git worktree add --force "$PAGES_DIR" "$BRANCH"

rsync -a --delete "$BUILD_DIR"/ "$PAGES_DIR"/
touch "$PAGES_DIR/.nojekyll"
if [ -n "$CNAME" ]; then echo "$CNAME" > "$PAGES_DIR/CNAME"; fi

pushd "$PAGES_DIR" >/dev/null
git add -A
if git diff --cached --quiet; then
  echo "No changes to publish."
else
  git commit -m "Deploy MkDocs $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
  git push "$REMOTE" "$BRANCH"
  echo "Published to $BRANCH."
fi
popd >/dev/null

git worktree remove "$PAGES_DIR"
