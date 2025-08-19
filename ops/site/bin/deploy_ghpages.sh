#!/usr/bin/env bash
set -euo pipefail
REMOTE="${REMOTE:-origin}"
BRANCH="${BRANCH:-gh-pages}"
CNAME="${CNAME:-}"
ROOT="$(git rev-parse --show-toplevel)"
SITE="$ROOT/ops/site"
BUILD_DIR="$SITE/site"
PAGES_DIR="$ROOT/.gh-pages"
[ -d "$BUILD_DIR" ] || { echo "Build dir missing. Run build.sh first." >&2; exit 1; }
git fetch "$REMOTE" --prune
if ! git show-ref --quiet "refs/heads/$BRANCH" && ! git ls-remote --exit-code --heads "$REMOTE" "$BRANCH" >/dev/null 2>&1; then
  git checkout --orphan "$BRANCH"
  git reset --hard
  echo init > .init && git add .init && git commit -m "Initialize $BRANCH"
  git push "$REMOTE" "$BRANCH"
  git checkout -
fi
rm -rf "$PAGES_DIR"
git worktree add --force "$PAGES_DIR" "$BRANCH"
mkdir -p "$PAGES_DIR"
shopt -s dotglob nullglob
rm -rf "$PAGES_DIR"/*
cp -r "$BUILD_DIR"/* "$PAGES_DIR"/
: > "$PAGES_DIR/.nojekyll"
[ -n "$CNAME" ] && printf "%s\n" "$CNAME" > "$PAGES_DIR/CNAME"
pushd "$PAGES_DIR" >/dev/null
git add -A
if git diff --cached --quiet; then
  echo "No changes to publish."
else
  git commit -m "Deploy MkDocs $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
  git push "$REMOTE" "$BRANCH"
fi
popd >/dev/null
if [ -d "$PAGES_DIR/.git" ]; then git worktree remove "$PAGES_DIR" || true; else rm -rf "$PAGES_DIR"; fi
git worktree prune
