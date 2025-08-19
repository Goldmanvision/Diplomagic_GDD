#!/usr/bin/env bash
set -euo pipefail
MAPFILE="${1:-ops/maintenance/ascii-safe-mapping-20250817.md}"

if [ ! -f "$MAPFILE" ]; then
  echo "Mapping not found: $MAPFILE" >&2
  exit 1
fi

# Move mapping and zip if still in ascii-safe root
if [ -f "ascii-safe/ascii-safe-mapping-20250817.md" ]; then
  mkdir -p ops/maintenance
  mv -f "ascii-safe/ascii-safe-mapping-20250817.md" "$MAPFILE"
fi
if [ -f "ascii-safe-20250817.zip" ]; then
  mkdir -p ops/artifacts
  mv -f "ascii-safe-20250817.zip" "ops/artifacts/"
fi

# Process rows (skip header lines)
awk -F '|' 'NR>2 {print $2 "|" $3}' "$MAPFILE" | while IFS='|' read -r orig safe; do
  orig="$(echo "$orig" | sed -e 's/^ *//' -e 's/ *$//')"
  safe="$(echo "$safe" | sed -e 's/^ *//' -e 's/ *$//')"
  [ -z "$orig" ] && continue
  [ -z "$safe" ] && continue
  target="${safe#ascii-safe/}"
  mkdir -p "$(dirname "$target")"
  if [ -f "$safe" ]; then
    git mv -f "$safe" "$target" 2>/dev/null || mv -f "$safe" "$target"
  fi
  if [ -f "$orig" ] && [ "$orig" != "$target" ]; then
    git rm -f "$orig" 2>/dev/null || rm -f "$orig"
  fi
  echo "Moved: $safe -> $target; removed: $orig"
done

echo "Done. Review with: git status"
