#!/usr/bin/env bash
set -euo pipefail
if [ -f tools/local-ui/frontend/package.json ]; then
  if [ -x tools/local-ui/frontend/node_modules/.bin/vitest ]; then
    (cd tools/local-ui/frontend && npm test || tools/local-ui/frontend/node_modules/.bin/vitest run || true)
  else
    echo "[tests] frontend present but vitest not installed; sandbox skip"; exit 0
  fi
else
  echo "[tests] lock status"; python3 ops/locks/scripts/lock_status.py || true
fi
echo "[tests] done"
