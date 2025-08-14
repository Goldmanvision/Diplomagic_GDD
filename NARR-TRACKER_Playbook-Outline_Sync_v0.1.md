# NARR-TRACKER — Playbook + Outline Sync v0.1
Version: v0.1
Date: 2025-08-14 09:09:00 UTC
Owner: Nick Goldman
Scope: Merge the “DIPLOMAGIC Narrative Playbook” and “Diplomagic Outline 2025” into the chapter-by-chapter review. Flag conflicts, lock canon, and list required edits across GDD sections.

## Summary
- Two Prologues: Clara (1994 tutorial) and Avery (1989 Hogan's Alley tutorial). Low stakes; teach character loops.
- Choice hooks: finding Cultist Literature affects Ch.5 Betsy encounter; Avery range score unlock path for Hauser pistol.
- Cinematic rules: diegetic-only; strict POV per character; device-driven scenes.
- Chapter 6 includes UN HQ endgame plus SRS/D-LAMP connective thread.

## Decisions — Locked Canon
- Intake site: Brightstar Daycare, Jackson, SC (canon). Update SEC-06 locations; retire NY references.
- Name: Brightstar Daycare (canon). Replace “Massapequa Kids Kamp” or keep only as in-world alias.
- Cutscene POV: strict POV. For Clara’s prologue, jump to Reddy’s POV to show Clara’s face while hiding the knife behind Reddy.
- Possession logic: event-driven; day/night only adjusts spawns.
- Chapter 6 legs: Clara -> SRS; Avery -> UN HQ. Structure: single mission with interleaved legs (switchable to sequential if production requires).
- Easter egg legality: Conan-style homage only if PD is clear in target regions; no trademarked name; no film look; no Schwarzenegger likeness/voice. Prepare alt concept.

## Chapter deltas and actions
- Prologue: align tutorials per canon; wire pin pickup -> Ch.5 branch.
- Ch.1 “Simple Curiosity”: Clara stealth escape; Avery arrest-first scoring. Verify arrest-first UI and evidence gating.
- Ch.2 “Passing Interest”: Clara survival in backwoods; optional Rolodex calls; Avery promotion and meeting Krill. Add Krill flags.
- Ch.3 “Innocent Fascination”: Reddy playable; non-lethal rewarded; Avery suspended; spectral equipment gate; forced push to Unknown Kadath; Clara/Reddy rescue.
- Ch.4 “Undying Obsession”: Swap-play traversal; spare cultists bonus; shared statlines.
- Ch.5 “Renewed Purpose”: Avery rogue; seized-site revisits; car mini-base; day/night variants; Betsy confrontation or arrest based on Prologue pickup.
- Ch.6 “Glorious Quest”: Interleaved UN HQ and SRS legs; device outcomes feed epilogue tags.
- Epilogue “Reorientation”: Mixed endings based on Final Score; NG+ variants.

## Required GDD updates
- SEC-01 Front: executive summary reflects two-prologue structure.
- SEC-02 Pillars: add POV/cutscene rule and choice->consequence hooks.
- SEC-04 Loops: wire Prologue->Ch.5 branch; add Reddy telekinesis loop.
- SEC-05 Systems: update Evidence/Warrant ties to Final Score; Krill moral flags; shared Clara/Avery statlines for Ch.4.
- SEC-06 World: lock location canon; federally seized map variants; day/night spawn tables.
- SEC-07 UI/UX: Reddy input context; arrest-first prompts; diegetic interactables catalog.
- SEC-08 Art/Audio: audio layering; Mystical Heads VFX budget; spectral readability.
- SEC-09 Tech: spectral-phase equipment; diegetic video playback; NG+ save flags.
- SEC-11/14 QA: CM/AX tests for diegetic scenes; Prologue->Ch.5 branch tests; Ch.6 dual-leg perf spots.
- SEC-12 Risks: IP risk management for homage; narrative-location mismatch risk until canon locked.

## Data & flags
- Score thresholds for endings and NG+ unlocks.
- Prologue pickup boolean -> Betsy branch.
- Krill moral-alignment flag.
- Ch.4 no-harm-to-cultists bonus flag.
- Ch.6 device outcome tags (Destroy vs Banish) -> epilogue variant.

## Next actions
- Approve and then patch SEC-01/02/04/05/06/07/08/09/11/12/14 with exact language in v-bumped docs.
- Build a Choice & Consequence grid with IDs and owners.

## Changelog
- v0.1: Initial merge and decisions locked.
