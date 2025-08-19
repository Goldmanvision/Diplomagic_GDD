#!/usr/bin/env bash
set -euo pipefail
usage(){ echo "Usage: $0 <archive|snapshot_dir> <target_dir> [--decrypt] [--passphrase-file <file>]"; exit 1; }

[[ $# -lt 2 ]] && usage
INPUT="$1"; TARGET="$2"; shift 2 || true

TMP="$(mktemp -d)"
cleanup(){ rm -rf "$TMP"; }
trap cleanup EXIT

ARCHIVE="$INPUT"
if [[ "$INPUT" == *.gpg ]]; then
  if [[ "${1:-}" == "--decrypt" ]]; then
    shift
    if [[ "${1:-}" == "--passphrase-file" ]]; then
      gpg --batch --passphrase-file "$2" --decrypt "$INPUT" > "$TMP/archive.tar.gz"
      shift 2
    else
      gpg --decrypt "$INPUT" > "$TMP/archive.tar.gz"
    fi
  else
    echo "Encrypted archive requires --decrypt" >&2
    exit 2
  fi
  ARCHIVE="$TMP/archive.tar.gz"
fi

if [[ -f "$ARCHIVE" ]]; then
  tar -xzf "$ARCHIVE" -C "$TMP"
  SRC_DIR="$TMP/data"
elif [[ -d "$INPUT" ]]; then
  SRC_DIR="$INPUT/data"
else
  echo "Input is neither file nor directory" >&2
  exit 2
fi

mkdir -p "$TARGET"
rsync -a --delete "$SRC_DIR"/ "$TARGET"/
echo "Restored to $TARGET"
