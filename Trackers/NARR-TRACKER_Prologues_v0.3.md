# Narrative Tracker — Prologues v0.3 (Canonical)
Version: v0.3
Date: 2025-08-14 09:59:10 UTC
Owner: Nick Goldman
Status: Canonical. Replaces prior Prologue tracker.

Linked: SEC-03-NARRATIVE, SEC-04-LOOPS, SEC-05-SYSTEMS, SEC-06-WORLD, SEC-07-UI, SEC-11-QA, PERIOD-ACCURACY-AUDIT_1994

## Canon locks
- Location: Brightstar Daycare, Jackson, SC.
- Name: Brightstar Daycare (retire “Massapequa Kids Kamp” or use as in-world alias only).
- POV: strict in-character only. Clara Prologue uses Reddy-POV for the face/knife beat.
- Possession: event-driven; day/night only alters spawns.
- Period: 1989 analog; 1994 uses FieldPad in later chapters with PCMCIA Type-II or CF Type-I via adapter. Caller ID not guaranteed.
- Exception (0B only): Clara has no FieldPad or TAPLINE in her Prologue; MEDSTAT only.

---

## 0A — Avery Jordan (1989, Quantico — Hogan’s Alley)
**Goal:** Tutorialize ROE, challenge→cuff→search, analog custody; teach combat once for both characters.  
**Tone:** No danger; scored exercise by Eddie Paldino.  
**Target duration:** **15 min** first-time critical path (can run longer if the player explores/roleplays).

### Beats
1) Orientation with **Eddie Paldino**: safety, ROE, objectives.  
2) Contact drill: **challenge → compliance check → cuff → search** (mock contraband).  
3) Analog evidence: **35mm photo**, **bag→tag→log** on paper; handoff at **locker window**.  
4) Range block: marksmanship + **dual‑wield** + **decoupled aim**; **non‑lethal ammo** tutorial; targets clearly marked.  
5) **Non‑lethal takedown/escort drill:** restrain and escort a role‑player to a safe zone without injury.  
6) **Debrief:** scoring on ROE and custody; **signifier: Hauser’s pistol bearing a cult symbol**; Eddie hints at Hauser’s occult ties and asks for discretion.

### Mechanics checklist
- Arrest‑first prompts; **non‑lethal takedown/escort** taught; lethal fire never against people in this chapter.  
- Range includes **non‑lethal ammo** safety tutorial.  
- No FieldPad/PCMCIA/CF in 1989.  
- Telephonic warrant referenced as minutes‑scale; not executed in‑mission.

**Crosslinks:** SEC‑04 (Investigate→Act→Record), SEC‑05 (ROE, Evidence), SEC‑11 (AX subtitles default on).

---

## 0B — Clara Winston (1994, Home Visit — Betsy Lumbar)
**Goal:** Tutorialize **MEDSTAT** vitals and caregiving. **No FieldPad or TAPLINE** in this scene.  
**Tone:** Supportive, no danger.  
**Target duration:** **15 min** first-time critical path.

### Beats
1) Arrival (buzzer/landline), small‑talk; start **morning → transitions to afternoon** by scene end.  
2) **MEDSTAT** vitals: pulse‑ox, BP cuff, temp → confirm → log.  
3) Care tasks: tea, pill organizer, light tidy; optional brief hallway chat only.  
4) **Devices:** **MEDSTAT handheld** paired to **RF wrist‑band module**; **record visit notes on paper chart** for later transcription when FieldPad is available in later chapters.  
5) **Reddy‑POV** beat shows Clara’s face while a knife is unsheathed behind Reddy.  
6) Discovery: **Clara finds the Brightstar pin**.  
7) Wrap: schedule follow‑up via landline note; no digital scheduling.

### Mechanics checklist
- MEDSTAT tutorial **single‑pass**.  
- **Devices present:** MEDSTAT handheld + RF wrist‑band; **no FieldPad, no TAPLINE**.  
- No outside walk test; if used later, failure → Clara fired (narrative flag only).  
- Caller ID not guaranteed; do not rely on it for puzzles.

**Crosslinks:** SEC‑07 (MEDSTAT UI), SEC‑11 (AX audio ducking, subtitle tags), SEC‑05 (pin discovery flag stored later once FieldPad is introduced).

---

## QA/Telemetry flags
- Events: `prologue_avery_complete`, `prologue_clara_complete`, `brightstar_pin_found` (true/false), `nonlethal_takedown_done`, `escort_done`, `nonlethal_ammo_trained`.  
- KPIs: tutorial completion ≤ 20 min P75; arrest:kill ratio ≥ 2:1 in Avery exercise.

## Update actions
- Mirror beats into `SEC‑03` Chapter List and Synopsis.  
- Add Avery range drill + dual‑wield + decoupled aim + non‑lethal ammo to `SEC‑04` input/loop.  
- Add **Hauser pistol signifier** and pin discovery boolean to `SEC‑05`/TDD (logged later).  
- Lock location/name in `SEC‑06` and VO barks.  
- Add AX checks to `SEC‑11`/`SEC‑14` suites.

## Status
- 0A Avery: ☐ Pending  
- 0B Clara: ☐ Pending  
- Cross‑section propagation: ☐ Pending
