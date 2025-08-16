# [SEC-01-FRONT] Front Matter & Executive Summary
Version: v0.2  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-03-NARRATIVE` — Narrative
- `SEC-04-LOOPS` — Core Gameplay Loops

## **Title**

**DIPLOMAGIC** — Investigative horror with dual protagonists and procedural realism (1994).

## **Executive Summary (≈300 words)**

Diplomagic is a single‑player investigative horror game set in 1994 America. Players alternate between FBI Special Agent **Avery Jordan** and civilian survivor **Clara Winston**. Their stories begin apart and converge mid‑campaign. The design blends procedural realism, period‑correct tools, and cosmic horror centered on the **Splinter of Azathoth**. Gameplay shifts between methodical evidence‑driven investigation, tense exploration, and tactical combat that punishes carelessness.

Avery’s chapters emphasize federal procedure, chain‑of‑custody, and coordinated operations using the FieldPad, TAPLINE, and MEDSTAT device UIs. Clara’s chapters emphasize survival, improvisation, and analog problem‑solving while protecting Reddy. The two perspectives expose the same conspiracy from different vectors, creating mechanical contrast and narrative friction.

Moment‑to‑moment play focuses on information gathering, risk assessment, and decisive execution. Systems support first‑person play with an optional over‑the‑shoulder toggle; Avery can use decoupled aiming for tactical positioning while Clara uses a more traditional feel. The world aesthetic mixes **PS1‑era 3D** fidelity with modern post‑processing and lighting to deliver dread without sacrificing readability.

The project targets **PC first**, with potential console ports **post‑launch**. It is built in **Unreal Engine 5.6**. A staged release plan calls for a **Halloween 2025 demo**, **Early Access in Q2 2026**, and **full release in Q1 2027**, resources permitting. **Mod tools** will be released in a supported beta **after Early Access**. Accessibility and localization are planned from the outset.

This GDD is structured for contractor and publisher use. Each section is self‑contained, versioned, and cross‑referenced. Narrative canon is maintained in the Narrative Playbook and linked where required. This section provides the concise product definition used by external stakeholders and anchors downstream scope decisions.

## **One‑Sheet Facts**

| Field | Value |
| ----- | ----- |
| Genre | Single‑player investigative horror; tactical shooter; light RPG |
| Mode | Single‑player |
| Perspective | First‑person with optional OTS toggle; decoupled aiming for Avery |
| Setting | United States, 1994 |
| Protagonists | Avery Jordan (FBI), Clara Winston (civilian) |
| Core Pillars | Dual‑protagonist structure; procedural realism; integrated cosmic horror |
| Engine | Unreal Engine 5.6 |
| Platforms | **PC at full release; next‑gen console ports post‑launch** |
| Visual Style | PS1‑era 3D with modern VFX |
| Device UIs | FieldPad, TAPLINE, MEDSTAT |
| Release Plan | Demo Halloween 2025; Early Access Q2 2026; **Mod tools beta post‑EA**; Full Release Q1 2027 |
| Accessibility & Localization | Planned from project start |
| Influences | The X‑Files; H.P. Lovecraft; Peter Clines; Annie Jacobsen |

## **Contacts & Document Control**

* Owner: Nick Goldman

* Document ID: DIPLOMAGIC\_GDD

* Master copy: `[SEC-01-FRONT] v0.2`

# Patch Instructions for Existing MASTER — SEC-02

## 1) Replace this single manifest row

Find the row that begins with \`| SEC-02-PILLARS |\` and replace the entire line with:

\`| SEC-02-PILLARS | Pillars + audience | v0.1 | 2025-08-11 | approved | archived to Master |\`

## 2) Append this section to the end of MASTER (add a \`\` before it)

\\[\\[PAGEBREAK]]

# **\\[SEC-02-PILLARS] Design Pillars & Target Audience**

## **2.1 Product Pillars**

Each pillar includes guardrails and checks used in reviews and greenlight gates.

### **P1. Dual‑Protagonist Parallax Narrative**

**Definition.** The story alternates between Avery (procedural, institutional) and Clara (survival, improvisational). They converge mid‑campaign and affect shared world state.

**Why.** Contrast keeps pacing fresh and reinforces theme: human systems vs the unknowable.

**Design Rules.**

* Do: Give each character exclusive mechanics, verbs, and UI affordances.

* Do: Mirror key events from different viewpoints.

* Don’t: Duplicate missions one‑to‑one or let skill trees collapse into sameness.

  **Checks.** ≥30% missions feature explicit cross‑impact; shared state is reflected in dialog, evidence, and encounters.

### **P2. Procedural Realism (1994)**

**Definition.** FBI‑accurate process for Avery; era‑correct civilian problem‑solving for Clara. Evidence handling, communications, and tactics reflect 1994 constraints.

**Why.** Grounded realism amplifies dread and differentiates the game.

**Design Rules.**

* Do: Enforce chain‑of‑custody, warrants, ROE for Avery.

* Do: Prefer analog friction for Clara: paper trails, payphones, physical locks.

* Don’t: Add modern conveniences (GPS, smartphones, cloud saves in‑fiction).

  **Checks.** Every Avery mission features at least one procedural gate; Clara scenarios require at least one analog workaround.

### **P3. Investigative Agency → Consequence**

**Definition.** Player‑led inquiry drives outcomes. Evidence unlocks dialog, access, and tactical options; poor prep increases risk.

**Why.** Investigation is core loop glue between exploration and combat.

**Design Rules.**

* Do: Score evidence quality; branch encounters by prep level.

* Do: Surface inference tools and uncertainty.

* Don’t: Solve with canned cutscene reveals after linear set pieces.

  **Checks.** Each mission supports ≥2 materially different resolutions tied to evidence tiers.

### **P4. Devices as Mechanics (FieldPad, TAPLINE, MEDSTAT)**

**Definition.** Diegetic UIs modeled on IBM Simon/Palm/Apple Newton. They gate features and tutorialize through use.

**Why.** Cohesive UX and fiction alignment.

**Design Rules.**

* Do: Keep screens two‑tone, large hit targets, latency modeled.

* Do: Unlock apps through story beats; respect battery/connection constraints.

* Don’t: Add non‑diegetic overlays that duplicate device functions.

  **Checks.** ≥70% mission interactions route through device apps; device upgrades change play, not stats alone.

### **P5. Dread‑First Aesthetics, PS1‑era Readability**

**Definition.** Low‑poly silhouettes with modern lighting and post‑FX. Horror tone favors implication over gore.

**Why.** Distinct look with high performance and clear gameplay readability.

**Design Rules.**

* Do: Prioritize silhouette, texture economy, fog volumes, limited palette.

* Don’t: Photoreal blood‑porn; avoid comedic gore.

  **Checks.** Heuristic readability pass per level; \<5% of playtest deaths attributed to visual ambiguity.

## **2.2 Player Experience Goals (PXG)**

* Feel competent assembling truth from scraps under time pressure.

* Feel the weight of procedure versus urgency.

* Fear the unknown without losing mechanical clarity.

* See choices echoed later by changed spaces, NPCs, and evidence trails.

## **2.3 Target Audience**

**Primary.** PC players 18–45 who enjoy investigative horror, immersive sims, and tactical shooters.

**Secondary.** Narrative RPG and survival horror fans; mod‑curious PC communities.

**Accessibility baseline.** Subtitles, color‑blind safe palettes, remappable inputs, aim assist options, difficulty modifiers for information density.

## **2.4 Competitive Comps & Positioning**

| Title/Ref               | Why it’s relevant              | Our differentiation                           |

| \----------------------- | \------------------------------ | \--------------------------------------------- |

| The X‑Files (TV)        | Tone, 1990s federal milieu     | Playable procedure, dual‑POV convergence      |

| Resident Evil (classic) | Survival horror pacing         | Investigation and procedure drive fights      |

| Signalis                | Low‑poly austerity, dread      | Dual devices + institutional realism          |

| Disco Elysium           | Evidence‑led narrative systems | First‑person, tactical risk, 1994 constraints |

**Positioning Statement.** An investigative horror where dual protagonists use period‑authentic tools to expose a cosmic intrusion, delivering grounded tension and meaningful agency.

## **2.5 Platform & Input Assumptions**

* PC first. Keyboard/mouse and gamepad parity targets.

* Haptics optional on supported controllers.

* No mandatory online features for core loop.

## **2.6 Content Rating Strategy**

Target: ESRB **M** / PEGI **18**. Violence, language, horror themes. Avoid sexual content and torture porn. Use content warnings for specific scenes.

## **2.7 Success Criteria**

**Qualitative.** Playtesters describe “investigation mattered,” “devices felt real,” “deaths felt fair.”

**Quantitative.**

* Evidence systems used in ≥80% of missions.

* Two or more valid mission resolutions logged in ≥60% of missions.

* \<5% UI errors from discoverability in device apps by final beta.

* Day‑1 crash‑free rate P90 ≥ 99.5% on min‑spec PC.

## **2.8 Risks & Mitigations**

* **Procedural friction** may frustrate: provide optional briefs, tooltips, and case files.

* **Dual‑protagonist scope**: share assets via locations re‑used with altered objectives.

* **Device UI overload**: progressive disclosure; tutorialize via cases, not modal popups.

## **2.9 Terminology**

* **FieldPad**: evidence capture and casework.

* **TAPLINE**: communications interception and analysis.

* **MEDSTAT**: biometrics, triage, and team status.

## **2.10 Approvals**

On approval: archive to MASTER as \`[SEC-02-PILLARS] v0.1\` and add manifest row. Next section: **SEC‑03 Narrative**.

# **Patch Instructions for Existing MASTER — SEC-03**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-03-NARRATIVE |` and replace the entire line with:

`| SEC-03-NARRATIVE | Narrative | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

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
