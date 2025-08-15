# SEC-01 — Integration Plan (CH5→CH6)
Repo dir: /Patches

## Scope
Wire CH5 rogue pivot, deep D‑LAMP/Iron Highway, and CH6 raid into the repo and GDD.

## Steps
1) **Narrative (root):** Update CH5/CH6 sections in `SEC-03-NARRATIVE - Narrative.md` using:
   - CH5: `CH5_DLamp_IronHighway_Underground.md`, `SEC-06-CH5-6_World_DLamp_IronHighway.md`, `CH5_DLamp_Betsy_Rework.md`.
   - CH6: `CH6_SRS_Apocalypse_Narrative.md`, `SEC-03-CH6_BeatSheet_Raid.md`, `SEC-03-CH6_Raid_Addendum.md`.
2) **Systems (root):** Merge into `SEC-05-SYSTEMS - Systems & Mechanics.md`:
   - Spell equip model, raid ROE, vault mechanics, AI FSM, combat tuning, BlueOnBlue detection.
3) **World (root):** Append nodes from:
   - `SEC-06-CH6_SRS_Secret_Annex_World.md`, `SEC-06-CH6_Route_Encounter_Tables.md`, ASCII map.
4) **UI (root):** Consolidate prompts and flows from:
   - `SEC-07-CH5-6_UI_Prompts_Consolidated.md`, `SEC-07-CH6_Raid_UI_Prompts.md`, `SEC-07-CH6_UI_Flow.md`, prompts length check.
5) **Trackers:** Add/refresh:
   - `CH5_Tracker.md`, `CH6_Tracker.md`, `CH6_Flags_Endings.md`, `CH6_Scoring_Raid.md`, `CH6_QA_Test_Cases.md`, `CH5-6_DeepDLamp_Flags.md`, `CH5-6_Combat_Evidence_Scoring.md`, `CH5-6_Krill_Handler_Log.md`, `CH5-6_DLamp_Evidence_Index.md`, `CH6_Balance_Telemetry_Spec.md`, `CH6_Operational_Checklist.md`, `CH6_Playtest_Log_Sheet.md`.
6) **Period Audit:** Keep `SEC-09-Period_Audit_CH5-CH6_1994.md` visible.
7) **Naming:** Respect deputy randomizer: `SEC-05-Deputy_Name_Randomizer_Spec.md`.
8) **Tests:** Run QA checklist; verify evidence cap and BlueOnBlue fail.
9) **Exports:** Limit to 3 files per batch; note repo dir in each file header.

## Risks
- Evidence cap regressions, valve order clarity, BlueOnBlue false positives.
