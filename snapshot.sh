#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 -s <source_dir> -n <project_name> [-o <backup_root>] [-k <retention>] [--encrypt <recipient>|--passphrase-file <file>]"
  exit 1
}

BACKUP_ROOT="${HOME}/backups"
RETENTION=10
ENCRYPT_MODE="none"
RECIPIENT=""
PASSPHRASE_FILE=""
SRC=""
NAME=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -s|--src) SRC="$2"; shift 2;;
    -n|--name) NAME="$2"; shift 2;;
    -o|--out) BACKUP_ROOT="$2"; shift 2;;
    -k|--keep) RETENTION="$2"; shift 2;;
    --encrypt) ENCRYPT_MODE="recipient"; RECIPIENT="$2"; shift 2;;
    --passphrase-file) ENCRYPT_MODE="symmetric"; PASSPHRASE_FILE="$2"; shift 2;;
    -h|--help) usage;;
    *) echo "Unknown arg: $1"; usage;;
  esac
done

if [[ -z "${SRC}" || -z "${NAME}" ]]; then
  usage
fi
if [[ ! -d "${SRC}" ]]; then
  echo "Source dir not found: ${SRC}" >&2
  exit 2
fi

TS=$(date -u +"%Y%m%dT%H%M%SZ")
DEST="${BACKUP_ROOT}/${NAME}/${TS}"
mkdir -p "$DEST"

echo "[1/5] rsync snapshot -> $DEST/data"
rsync -a --delete --info=progress2 "$SRC"/ "$DEST"/data/

echo "[2/5] build manifest"
find "$DEST/data" -type f -print0 | sort -z | xargs -0 sha256sum > "$DEST/MANIFEST.sha256"

echo "[3/5] write metadata"
COUNT=$(wc -l < "$DEST/MANIFEST.sha256")
BYTES=$(du -sb "$DEST/data" | awk '{print $1}')
OS=$(uname -a | sed 's/"//g')
HOST=$(hostname)

{
  echo "{"
  echo "  \"name\": \"${NAME}\","
  echo "  \"timestamp_utc\": \"${TS}\","
  echo "  \"source\": \"${SRC}\","
  echo "  \"host\": \"${HOST}\","
  echo "  \"os\": \"${OS}\","
  echo "  \"count_files\": ${COUNT},"
  echo "  \"bytes\": ${BYTES}"
  if git -C "$SRC" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    BRANCH=$(git -C "$SRC" rev-parse --abbrev-ref HEAD)
    COMMIT=$(git -C "$SRC" rev-parse HEAD)
    if [[ -z "$(git -C "$SRC" status --porcelain)" ]]; then CLEAN=true; else CLEAN=false; fi
    echo "  ,\"git\": {"
    echo "    \"branch\": \"${BRANCH}\","
    echo "    \"commit\": \"${COMMIT}\","
    echo "    \"status_clean\": ${CLEAN}"
    echo "  }"
  fi
  echo "}"
} > "$DEST/METADATA.json"

echo "[4/5] archive bundle"
tar -C "$DEST" -cf "$DEST/archive.tar" data MANIFEST.sha256 METADATA.json
gzip -n "$DEST/archive.tar"
ARCHIVE="$DEST/archive.tar.gz"

echo "[5/5] optional encryption + retention"
if [[ "$ENCRYPT_MODE" == "recipient" ]]; then
  gpg --output "$ARCHIVE.gpg" --encrypt --recipient "$RECIPIENT" "$ARCHIVE"
  rm "$ARCHIVE"
  ARCHIVE="$ARCHIVE.gpg"
elif [[ "$ENCRYPT_MODE" == "symmetric" ]]; then
  gpg --batch --passphrase-file "$PASSPHRASE_FILE" --symmetric --output "$ARCHIVE.gpg" "$ARCHIVE"
  rm "$ARCHIVE"
  ARCHIVE="$ARCHIVE.gpg"
fi

if [[ "$RETENTION" -gt 0 ]]; then
  mapfile -t snaps < <(find "$BACKUP_ROOT/$NAME" -maxdepth 1 -type d -name "20*" | sort)
  count=${#snaps[@]}
  if (( count > RETENTION )); then
    to_delete=$((count - RETENTION))
    for d in "${snaps[@]:0:to_delete}"; do
      rm -rf "$d"
    done
  fi
fi

echo "$ARCHIVE"
