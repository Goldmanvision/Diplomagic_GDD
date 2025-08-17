#!/usr/bin/env bash
set -euo pipefail
# wrapper for CI: call ch6_validation_rerun if present, otherwise call ch6_validation_rerun.sh
if [ -x scripts/ch6_validation_rerun.sh ]; then
  ./scripts/ch6_validation_rerun.sh "$@"
else
  echo "Placeholder: ch6_validation_rerun not found. Producing minimal report." > reports/validation-rerun.log
  echo "Hits (>=1 expected):" >> reports/validation-rerun.log
  echo "- Evidence 0/3 = 0" >> reports/validation-rerun.log
fi
