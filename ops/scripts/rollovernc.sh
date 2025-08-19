#!/usr/bin/env bash
set -euo pipefail
dept="${1:-Mail Department}"
codename="${2:-Postmaster}"
suffix="${3:-Ops Thread 2}"
channel="${4:-#ops}"
link="${5:-/DECISIONS.md}"
note="${6:-}"
date="$(date +%Y-%m-%d)"
slug="$(printf '%s' "$dept" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g;s/^-+|-+$//g')"
out="ops/reports"; mkdir -p "$out"
cat > "$out/ptcork_${slug}_rollover_${date}.md" <<EOF
ptcork v2
title: ${dept} rollover
channel: ${channel}
content: ${dept} is moving to “${codename} — ${suffix}” due to log size. Old thread enters naptime. All routing and logs continue in the new thread. Double-Confirm remains for multi-file batches. ${note}
link: ${link}
---
EOF
printf '## %s
- %s chat rollover to “%s — %s”; prior thread archived with naptime; routing unchanged.
' "$date" "$dept" "$codename" "$suffix" >> DECISIONS.md
git add DECISIONS.md "$out/ptcork_${slug}_rollover_${date}.md"
echo "Created: $out/ptcork_${slug}_rollover_${date}.md"
