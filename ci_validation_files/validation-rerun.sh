#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports
if [ -x scripts/ch6_validation_rerun.sh ]; then
  ./scripts/ch6_validation_rerun.sh "$@"
else
  echo "Placeholder validation run: ch6_validation_rerun not present on runner" > reports/validation-rerun.log
  echo "Hits (>=1 expected):" >> reports/validation-rerun.log
  echo "- Evidence 0/3 = 0" >> reports/validation-rerun.log
  echo "- BlueOnBlue = 0" >> reports/validation-rerun.log
fi
