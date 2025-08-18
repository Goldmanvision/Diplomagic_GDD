#!/usr/bin/env bash
set -euo pipefail
if [ -x /c/Windows/py.exe ]; then PY="/c/Windows/py.exe -3"
elif command -v py >/dev/null 2>&1; then PY="py -3"
elif command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python >/dev/null 2>&1; then PY=python
else echo "Python 3 not found"; exit 1; fi
ROOT="$(git rev-parse --show-toplevel)"
SITE="$ROOT/ops/site"
cd "$SITE"
$PY -m venv .venv || true
if [ -f ".venv/Scripts/activate" ]; then source ".venv/Scripts/activate"
elif [ -f ".venv/bin/activate" ]; then source ".venv/bin/activate"; fi
python -m pip install -U pip
pip install -r requirements.txt
echo "MkDocs ready."
