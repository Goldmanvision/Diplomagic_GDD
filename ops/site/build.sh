#!/usr/bin/env bash
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root="$(cd "$here/../.." && pwd)"
docs="$here/docs"

usage() {
  echo "Usage: $0 {sync|serve|build|clean}"
  exit 1
}

sync() {
  mkdir -p "$docs"
  while IFS= read -r line || [ -n "$line" ]; do
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    src="$root/$line"
    dst="$docs/$line"
    mkdir -p "$(dirname "$dst")"
    cp -f "$src" "$dst"
  done < "$here/mirror.lst"
  echo "Synced files to docs/"
}

serve() {
  sync
  cd "$here"
  mkdocs serve
}

build() {
  sync
  cd "$here"
  mkdocs build
}

clean() {
  rm -rf "$here/site"
  echo "Cleaned site/"
}

[[ $# -lt 1 ]] && usage
cmd="$1"; shift || true
case "$cmd" in
  sync|serve|build|clean) "$cmd" "$@" ;;
  *) usage ;;
esac
