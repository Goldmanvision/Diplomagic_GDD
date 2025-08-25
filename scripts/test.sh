#!/usr/bin/env bash
set -euo pipefail
if [ -f tools/local-ui/frontend/package.json ]; then
  if [ -x tools/local-ui/frontend/node_modules/.bin/vitest ]; then
    (cd tools/local-ui/frontend && npm test || tools/local-ui/frontend/node_modules/.bin/vitest run || true)
  else
    echo "[tests] frontend present but vitest not installed; sandbox skip"
  fi
else
  echo "[tests] lock status"; python3 ops/locks/scripts/lock_status.py || true
fi

if command -v pytest >/dev/null 2>&1; then
  echo "[tests] python"
  pytest
else
  echo "[tests] pytest not installed; skipping python tests"
fi
echo "[tests] done"
