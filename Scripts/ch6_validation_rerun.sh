#!/usr/bin/env bash
set -euo pipefail

TS="$(TZ=America/New_York date '+%Y-%m-%d %H:%M ET')"

must=(
  "Evidence 0/3"
  "BlueOnBlue"
  "CH6 = raid"
  "Blue-on-Blue"
  "No CCTV in Vault"
  "K-9 reroute"
)

forbid=(
  "smartphone"
  "Wi-Fi"
  "Bluetooth"
  "GPS"
  "SMS"
)

count_hits () {
  pat="$1"
  grep -R -n --binary-files=without-match -F "$pat" . 2>/dev/null | wc -l | tr -d ' '
}

# collect counts
report="PR CH5-CH6 validation re-run ($TS)

Hits (>=1 expected):"
for p in "${must[@]}"; do
  c="$(count_hits "$p")"
  report="$report
- $p = $c"
done

report="$report

Zero-hits check (0 expected):"
for p in "${forbid[@]}"; do
  c="$(grep -R -ni --binary-files=without-match -F "$p" . 2>/dev/null | wc -l | tr -d ' ')"
  report="$report
- $p = $c"
done

# append to tracker and also print
tracker="Trackers/PR_Validation_Results_Summary_CH5-CH6.md"
echo "
---
$report
" | tee -a "$tracker"
