#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)/ops/site"
python3 -m venv .venv || true
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
echo "MkDocs ready."
