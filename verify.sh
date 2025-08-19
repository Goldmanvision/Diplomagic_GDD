#!/usr/bin/env bash
set -euo pipefail
usage(){ echo "Usage: $0 <snapshot_dir_or_archive>"; exit 1; }
[[ $# -ne 1 ]] && usage
INPUT="$1"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

BASE=""
if [[ -f "$INPUT" ]]; then
  tar -xzf "$INPUT" -C "$TMP"
  BASE="$TMP"
elif [[ -d "$INPUT" ]]; then
  BASE="$INPUT"
else
  echo "Input is neither file nor directory" >&2
  exit 2
fi

cd "$BASE"
sha256sum -c MANIFEST.sha256
echo "Verification OK"
