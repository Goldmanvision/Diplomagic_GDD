# CH1 — “Simple Curiosity” Outline
Version: v0.2
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Canon
- Year: 1994. Location: **Brightstar Daycare, Jackson, SC**.
- POV rule: strict in‑character. No omniscient cuts.
- Devices: **Clara** MEDSTAT (+ PCMCIA Type II **note‑card** unlocks **Notes** mid‑chapter; Newton‑compatible; **no camera/internet**). **No FieldPad/TAPLINE** yet. **Avery** analog (camera, paper, radio). MEDSTAT links via **SENTINEL** to other MEDSTATs for patient‑band breadcrumb only.

Goals
- Introduce Brightstar space and tone without overt threat.
- Give Clara a light stealth/care loop and unlock MEDSTAT Notes.
- Give Avery a field ROE showcase with arrest‑first scoring.
- Seed symbol lore without naming it.

Structure
- Interleaved legs (default). Option: sequential if production needs it.

Leg A — Clara + Reddy at Brightstar (day → dusk)
Beats
1) Intake desk: sign‑in; ambient red flags (locked doors, odd signage).
2) Find **MEDSTAT note‑card** in supply drawer; **insert → Notes unlock**; auto‑log prior pin note.
3) Guided tour: classroom, infirmary, storage; light **stealth** to avoid staffer; overhear coded phrase — “the stars are right tonight.”
4) Quiet incident: optional **care task** for a child; mark for follow‑up.
5) Exit prompt: Reddy wants to leave; schedule return visit.

Objectives
- Sign‑in completed.
- Note‑card inserted; toast confirms “Note logged from earlier chart.”
- Stealth pass without confrontation (soft fail: admonish).
- Optional care task complete.

Leg B — Avery near Jackson (same day)
Beats
1) Briefing with local deputy (**name randomized per save** from whitelist: H. Collins, S. Alvarez, J. Whitaker); complaint about suspicious activity near Brightstar.
2) **ROE field stop**: challenge → cuff → search a belligerent adult; no shots on compliant.
3) Analog custody: photo of contraband; bag → tag → log; handoff at mobile locker case.
4) Debrief scorecard; hint that federal attention on Brightstar is increasing.

Objectives
- Complete arrest‑first loop without ROE violations.
- Custody checklist complete.
- Debrief viewed.

Fail/Reset
- Clara: caught during stealth → admonish and reposition; no hard fail here.
- Avery: unjustified shot → admonish + partial rewind; score penalty; continue.

Devices & Data
- MEDSTAT Notes enabled; CaseNote created for pin symbol (SYM‑001).
- Save flags touched: `medstat_upgrade_card_found=true`, `medstat_upgrade_card_inserted=true`, `pin_auto_log_created=true`.
- No EvidenceItem yet unless later photographed.

Dependencies
- SEC‑06: Brightstar layout (intake, classroom, infirmary, storage).
- SEC‑07: MEDSTAT Notes UI; stealth prompts.
- SEC‑05/TDD: CaseNote schema; save flags.
- SEC‑11/14: perf spots and AX tests mirrored from prologues.

Open Questions
- Deputy VO style.
