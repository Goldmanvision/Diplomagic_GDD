#!/usr/bin/env bash
set -euo pipefail

TAG="v0.1-docs-structure"
MSG="v0.1 docs structure: epilogue packaging, CH7 placeholder, CH6 hotfix, validation rerun, period sweep, StarTAC->MicroTAC"

# From repo root
git add CHANGELOG.md
git commit -m "docs(changelog): add ${TAG} entry"
git push

git tag -a "${TAG}" -m "${MSG}"
git push origin "${TAG}"

echo "[i] Created and pushed tag ${TAG}."
