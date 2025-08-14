# Prologues — Polish Checklist (0A/0B)
Version: v0.1
Date: 2025-08-14 11:30:45 UTC
Owner: Nick Goldman

Scope: Final pass items for 0A Avery (1989 Quantico) and 0B Clara (1994 Betsy apt). Aligns with NARR-TRACKER_Prologues v0.3.

## A. Canon & Gates (confirm)
- Hauser pistol award: **score ≥90 AND ROE violations == 0** (0A). ✔/✖
- Eddie shows pistol regardless; award line branches. ✔/✖
- Pin symbol == pistol symbol; **player-knowledge only**. ✔/✖
- `cult_symbol_link_active = hauser_pistol_awarded && brightstar_pin_found`. ✔/✖
- 0B has **MEDSTAT+RF only**; no FieldPad/TAPLINE. ✔/✖
- CH1: MEDSTAT **note-card** enables Notes; auto-log prior pin note. ✔/✖
- Reddy‑POV not rewatchable in Prologue. ✔/✖

## B. Level Script
- 0A: soft rewind on unjustified shot; keep score intact. ✔/✖
- 0A: escort unlocks only after non‑lethal ammo tutorial. ✔/✖
- 0A: debrief card branches (award vs admonish). ✔/✖
- 0B: vitals gate before care tasks; no hard fail. ✔/✖
- 0B: Reddy‑POV trigger single‑fire; mark played. ✔/✖
- 0B: pin inspect sets `brightstar_pin_found`. ✔/✖

## C. UI/UX
- Prompts ≤14 chars per TutorialCopy. ✔/✖
- Prompt placement near focus ring; 2s toast max. ✔/✖
- Hold↔press toggles work for cuff, interact. ✔/✖
- Subtitle tags ON, readable at scale 0.85–1.50. ✔/✖
- High‑contrast theme/skin select persists. ✔/✖

## D. Audio
- LUFS targets: dialogue −16, range SFX duck −6 dB under VO. ✔/✖
- Clean tails on VO; no clipped consonants. ✔/✖
- Range indoor/outdoor reverb profiles tested. ✔/✖

## E. VFX/Art
- 0A: muzzle flash small, paper tear FX OK; symbol **obscured in press**. ✔/✖
- 0B: kettle steam subtle; dust motes low. ✔/✖
- Symbol mask shared between pistol/pin materials. ✔/✖
- Period audit: no modern props/UI. ✔/✖

## F. Performance
- 0A perf spots med/95p within SEC‑11 targets. ✔/✖
- 0B perf spots med/95p within SEC‑11 targets. ✔/✖
- Soak: 2h idle/walk; save/load memory growth <5%. ✔/✖

## G. Telemetry
- Events fire per QATelemetry docs (0A/0B). ✔/✖
- Derived flag recomputed on load. ✔/✖
- Local JSON write + opt‑in upload wired. ✔/✖

## H. Localization
- Strings exist for all prompts and VO captions. ✔/✖
- 7–14 char prompt budget met in target langs (pseudo‑loc pass). ✔/✖
- No slang; glossary tags present (ROE, MEDSTAT terms). ✔/✖

## I. Compliance/AX
- AX matrix items pass (subs, remap, scale, contrast). ✔/✖
- Ratings check: no graphic harm; knife remains off‑focus. ✔/✖
- Privacy/telemetry consent screen present. ✔/✖

## J. Capture
- Shotlists executed; internal vs press variants labeled. ✔/✖
- Perf CSVs attached to perf spot shots. ✔/✖

## K. Risks & Mitigations (spot)
- UI overload in 0A range → ensure step gating; fewer on‑screen tips. ✔/✖
- Player misses pin in 0B → allow repeat inspect zone until wrap. ✔/✖
- Over‑tight award gate → track P75; consider ≥85 fallback later. ✔/✖

## Sign‑off
- Design ☐  Tech ☐  Art ☐  Audio ☐  UI/UX ☐  QA ☐  Narrative ☐
