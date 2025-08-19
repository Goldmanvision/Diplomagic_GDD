#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
SITE="$ROOT/ops/site"
cd "$SITE"
if [ -x ".venv/Scripts/python.exe" ]; then PY=".venv/Scripts/python.exe"
elif command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python >/dev/null 2>&1; then PY=python
elif [ -x /c/Windows/py.exe ]; then PY="/c/Windows/py.exe -3"
else echo "Python not found"; exit 1; fi
"$PY" -m mkdocs build --strict --config-file mkdocs.yml --site-dir site
echo "Built site at $SITE/site"
