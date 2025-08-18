#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)/ops/site"
# use venv if present
[ -f .venv/bin/activate ] && source .venv/bin/activate || true
mkdocs build --strict --site-dir site
echo "Site built at ops/site/site"
