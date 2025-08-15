# PR: CH5–CH6 Root Merge (Narrative/Systems/World/UI)

## Summary
Integrates CH5–CH6 across root docs. CH6 reframed as a raid with lethal ROE and Blue‑on‑Blue fail; evidence cap 3; prompts ≤14; 1994 period. Ambient phrase retained: “the stars are right tonight.”

## Changes
- Replaced CH5 and CH6 in SEC-03.
- Appended systems blocks (phrases/scrolls, ROE, cameras, endings, tuning, failure).
- Added world nodes and UI prompts/flows; referenced ASCII map.
- Updated README/ToC inserts.

## Files to paste (entry points)
- Narrative: `/Patches/ROOT_SEC-03_Narrative_CH5-CH6_Merge.md` (or split CH5/CH6 paste blocks)
- Systems: `/Patches/ROOT_Systems_Snippet_Replacements.md`
- World+UI: `/Patches/ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md`
- Prompts: `/Patches/ROOT_SEC-07_UI_Prompts_Master.md`
- Helpers: see `/Patches/ROOT_Merge_Index_CH5-CH6.md`

## Checks
- [ ] 1994 audit passes (MicroTAC only; no Wi‑Fi/Bluetooth/GPS/SMS)
- [ ] Prompts ≤14 chars
- [ ] Ambient phrase is ambient-only
- [ ] CH6 ROE: lethal authorized; Blue‑on‑Blue = fail
- [ ] Evidence cap 3 enforced
- [ ] Crosslinks validated

## Test
Follow `/Patches/ROOT_EndToEnd_Test_Script_CH5-CH6.md`.

## Risks/Mitigations
See `/Trackers/ROOT_Merge_Risk_Register.md`.

## Notes
Text-only PR.
