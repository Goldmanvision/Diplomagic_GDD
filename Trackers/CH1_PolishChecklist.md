# CH1 — “Simple Curiosity” Polish Checklist
Version: v0.1
Date: 2025-08-14 12:25:18 UTC
Owner: Nick Goldman

Scope: Final pass items for Clara Brightstar leg and Avery roadside stop.

## A. Canon & Gates
- Clara: **card inserted → Notes unlocked**; toast shows; CaseNote created. ✔/✖
- Avery: **custody_complete==true** before debrief. ✔/✖
- No FieldPad/TAPLINE in CH1; MEDSTAT only for Clara. ✔/✖
- Symbol handling stays **lore-only**; no WS effect. ✔/✖

## B. Level Script
- Clara: sign-in required before tour. ✔/✖
- Clara: stealth admonish → resume, no hard fail. ✔/✖
- Clara: care task optional, tracked. ✔/✖
- Avery: unjustified shot → admonish + partial rewind. ✔/✖
- Avery: mobile locker handoff confirms checklist. ✔/✖

## C. UI/UX
- Prompts ≤14 chars per TutorialCopy. ✔/✖
- Prompt placement near focus; 2s toast max. ✔/✖
- Hold↔press toggles work for interact/cuff. ✔/✖
- Subtitles ON with speaker tags; UI scale 0.85–1.50. ✔/✖
- High-contrast skins persist (MEDSTAT/prompts). ✔/✖

## D. Audio
- Dialogue −16 LUFS; SFX duck −6 dB under VO. ✔/✖
- Room tone: foyer/classroom/storage/roadside distinct. ✔/✖

## E. VFX/Art
- Interior fluorescent flicker subtle; dusk rig believable. ✔/✖
- Roadside heat shimmer subtle; no modern props. ✔/✖
- MEDSTAT note-card insert anim readable. ✔/✖

## F. Performance
- Perf spots med/95p within SEC‑11 targets for all listed locations. ✔/✖
- Soak 2h; save/load loop; memory growth <5%. ✔/✖

## G. Telemetry
- Events fire and write local JSON; opt‑in upload. ✔/✖
- Flags set: `medstat_upgrade_card_found/inserted`, `pin_auto_log_created`, `custody_complete`. ✔/✖

## H. Localization
- All prompt strings exist; pseudo‑loc pass done. ✔/✖
- Glossary tags present for MEDSTAT terms. ✔/✖

## I. Compliance/AX
- AX items pass (subs, scale, contrast, non‑color cues). ✔/✖
- Capture shotlists executed; perf CSV attached. ✔/✖

## Sign‑off
- Design ☐  Tech ☐  Art ☐  Audio ☐  UI/UX ☐  QA ☐  Narrative ☐
