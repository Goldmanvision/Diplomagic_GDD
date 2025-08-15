# Merge Conflict Resolution — CH5–CH6
Repo dir: /Patches

## Typical conflicts
- `SEC-03` headers around `## CH5` or `## CH6`
- `SEC-05` headings where blocks insert
- `SEC-07` prompts table duplicates

## Strategy
1) Keep our CH5/CH6 full replacements intact.
2) For `SEC-05/06/07`, prefer our blocks; re‑add any unique upstream lines above/below.
3) Remove duplicate prompts; keep ≤14‑char list and **Ward Jam** form.

## Quick anchors
- `CH6 is a raid` line must exist verbatim.
- Evidence cap **3** present.
- Blue‑on‑Blue fail present with exceptions.
- Ambient phrase line present.

## Final pass
Run validation grep and smoke checks.
