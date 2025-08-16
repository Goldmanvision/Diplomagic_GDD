# DIPLOMAGIC – Combined GDD (Auto-Rebuilt)

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

# [SEC-02-PILLARS] Pillars & Audience
Version: v0.1 (no change to Master header)  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-01-FRONT — Front Matter & Executive Summary`
- `SEC-03-NARRATIVE — Narrative`
- `SEC-04-LOOPS — Core Gameplay Loops`

\# Patch Instructions for Existing MASTER — SEC-02



\#\# 1\) Replace this single manifest row


\`| SEC-02-PILLARS | Pillars \+ audience | v0.1 | 2025-08-11 | approved | archived to Master |\`

\#\# 2\) Append this section to the end of MASTER (add a \`\[\[PAGEBREAK\]\]\` before it)

\\\[\\\[PAGEBREAK\]\]

\# \*\*\\\[SEC-02-PILLARS\] Design Pillars & Target Audience\*\*


Owner: Nick Goldman

\#\# \*\*2.1 Product Pillars\*\*

Each pillar includes guardrails and checks used in reviews and greenlight gates.

\#\#\# \*\*P1. Dual‑Protagonist Parallax Narrative\*\*

\*\*Definition.\*\* The story alternates between Avery (procedural, institutional) and Clara (survival, improvisational). They converge mid‑campaign and affect shared world state.

\*\*Why.\*\* Contrast keeps pacing fresh and reinforces theme: human systems vs the unknowable.

\*\*Design Rules.\*\*

\* Do: Give each character exclusive mechanics, verbs, and UI affordances.

\* Do: Mirror key events from different viewpoints.

\* Don’t: Duplicate missions one‑to‑one or let skill trees collapse into sameness.

  \*\*Checks.\*\* ≥30% missions feature explicit cross‑impact; shared state is reflected in dialog, evidence, and encounters.

\#\#\# \*\*P2. Procedural Realism (1994)\*\*

\*\*Definition.\*\* FBI‑accurate process for Avery; era‑correct civilian problem‑solving for Clara. Evidence handling, communications, and tactics reflect 1994 constraints.

\*\*Why.\*\* Grounded realism amplifies dread and differentiates the game.

\*\*Design Rules.\*\*

\* Do: Enforce chain‑of‑custody, warrants, ROE for Avery.

\* Do: Prefer analog friction for Clara: paper trails, payphones, physical locks.

\* Don’t: Add modern conveniences (GPS, smartphones, cloud saves in‑fiction).

  \*\*Checks.\*\* Every Avery mission features at least one procedural gate; Clara scenarios require at least one analog workaround.

\#\#\# \*\*P3. Investigative Agency → Consequence\*\*

\*\*Definition.\*\* Player‑led inquiry drives outcomes. Evidence unlocks dialog, access, and tactical options; poor prep increases risk.

\*\*Why.\*\* Investigation is core loop glue between exploration and combat.

\*\*Design Rules.\*\*

\* Do: Score evidence quality; branch encounters by prep level.

\* Do: Surface inference tools and uncertainty.

\* Don’t: Solve with canned cutscene reveals after linear set pieces.

  \*\*Checks.\*\* Each mission supports ≥2 materially different resolutions tied to evidence tiers.

\#\#\# \*\*P4. Devices as Mechanics (FieldPad, TAPLINE, MEDSTAT)\*\*

\*\*Definition.\*\* Diegetic UIs modeled on IBM Simon/Palm/Apple Newton. They gate features and tutorialize through use.

\*\*Why.\*\* Cohesive UX and fiction alignment.

\*\*Design Rules.\*\*

\* Do: Keep screens two‑tone, large hit targets, latency modeled.

\* Do: Unlock apps through story beats; respect battery/connection constraints.

\* Don’t: Add non‑diegetic overlays that duplicate device functions.

  \*\*Checks.\*\* ≥70% mission interactions route through device apps; device upgrades change play, not stats alone.

\#\#\# \*\*P5. Dread‑First Aesthetics, PS1‑era Readability\*\*

\*\*Definition.\*\* Low‑poly silhouettes with modern lighting and post‑FX. Horror tone favors implication over gore.

\*\*Why.\*\* Distinct look with high performance and clear gameplay readability.

\*\*Design Rules.\*\*

\* Do: Prioritize silhouette, texture economy, fog volumes, limited palette.

\* Don’t: Photoreal blood‑porn; avoid comedic gore.

  \*\*Checks.\*\* Heuristic readability pass per level; \<5% of playtest deaths attributed to visual ambiguity.

\#\# \*\*2.2 Player Experience Goals (PXG)\*\*

\* Feel competent assembling truth from scraps under time pressure.

\* Feel the weight of procedure versus urgency.

\* Fear the unknown without losing mechanical clarity.

\* See choices echoed later by changed spaces, NPCs, and evidence trails.

\#\# \*\*2.3 Target Audience\*\*

\*\*Primary.\*\* PC players 18–45 who enjoy investigative horror, immersive sims, and tactical shooters.

\*\*Secondary.\*\* Narrative RPG and survival horror fans; mod‑curious PC communities.

\*\*Accessibility baseline.\*\* Subtitles, color‑blind safe palettes, remappable inputs, aim assist options, difficulty modifiers for information density.

\#\# \*\*2.4 Competitive Comps & Positioning\*\*

| Title/Ref               | Why it’s relevant              | Our differentiation                           |

| \----------------------- | \------------------------------ | \--------------------------------------------- |

| The X‑Files (TV)        | Tone, 1990s federal milieu     | Playable procedure, dual‑POV convergence      |

| Resident Evil (classic) | Survival horror pacing         | Investigation and procedure drive fights      |

| Signalis                | Low‑poly austerity, dread      | Dual devices \+ institutional realism          |

| Disco Elysium           | Evidence‑led narrative systems | First‑person, tactical risk, 1994 constraints |

\*\*Positioning Statement.\*\* An investigative horror where dual protagonists use period‑authentic tools to expose a cosmic intrusion, delivering grounded tension and meaningful agency.

\#\# \*\*2.5 Platform & Input Assumptions\*\*

\* PC first. Keyboard/mouse and gamepad parity targets.

\* Haptics optional on supported controllers.

\* No mandatory online features for core loop.

\#\# \*\*2.6 Content Rating Strategy\*\*

Target: ESRB \*\*M\*\* / PEGI \*\*18\*\*. Violence, language, horror themes. Avoid sexual content and torture porn. Use content warnings for specific scenes.

\#\# \*\*2.7 Success Criteria\*\*

\*\*Qualitative.\*\* Playtesters describe “investigation mattered,” “devices felt real,” “deaths felt fair.”

\*\*Quantitative.\*\*

\* Evidence systems used in ≥80% of missions.

\* Two or more valid mission resolutions logged in ≥60% of missions.

\* \<5% UI errors from discoverability in device apps by final beta.

\* Day‑1 crash‑free rate P90 ≥ 99.5% on min‑spec PC.

\#\# \*\*2.8 Risks & Mitigations\*\*

\* \*\*Procedural friction\*\* may frustrate: provide optional briefs, tooltips, and case files.

\* \*\*Dual‑protagonist scope\*\*: share assets via locations re‑used with altered objectives.

\* \*\*Device UI overload\*\*: progressive disclosure; tutorialize via cases, not modal popups.

\#\# \*\*2.9 Terminology\*\*

\* \*\*FieldPad\*\*: evidence capture and casework.

\* \*\*TAPLINE\*\*: communications interception and analysis.

\* \*\*MEDSTAT\*\*: biometrics, triage, and team status.

\#\# \*\*2.10 Approvals\*\*

On approval: archive to MASTER as \`\[SEC-02-PILLARS\] v0.1\` and add manifest row. Next section: \*\*SEC‑03 Narrative\*\*.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# [SEC-03-NARRATIVE] Narrative
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-01-FRONT` — Front Matter & Executive Summary
- `SEC-04-LOOPS` — Core Gameplay Loops
- `SEC-05-SYSTEMS` — Systems & Mechanics

## **3.1 Structure & Tone**

Dual‑protagonist split: **Clara Winston** (survival, analogue) and **Avery Jordan** (procedural, FBI realism). Timelines interleave and converge in Chapter 4\. Themes: institutional systems vs the unknowable; cosmic intrusion; moral cost. Influences: The X‑Files, H.P. Lovecraft, Peter Clines, Annie Jacobsen.

## **3.2 Chapter List — Official Titles**

Use these exact titles in all builds, docs, and UI.

* **00 PROLOGUE: “DISORIENTATION”**  
   Clara escorts Reddy to Brightstar Daycare in liminal **New Kadath**; agency is subverted. Parallel: Avery’s 1989 training with Eddie Paldino and first case setup.

* **01 CHAPTER 1: “SIMPLE CURIOSITY”**  
   Clara fights and stealths out of Kids Kamp with Reddy. Avery travels to **Jackson, SC** to investigate Langston Gromley; arrests favored over kills.

* **02 CHAPTER 2: “PASSING INTEREST”**  
   Clara survives in the backwoods between Brightstar and reality; resource and noise management around Reddy. Avery’s clearance jumps to **Level X**; shadow counsel pushes lethal latitude.

* **03 CHAPTER 3: “INNOCENT FASCINATION”**  
   Reddy’s latent power surges; Clara collapses. Suspended Avery returns to Brightstar, is driven into **Unknown Kadath**, and reunites with Clara after time dilation.

* **04 CHAPTER 4: “UNDYING OBSESSION”**  
   Antagonist focus: **Qin Xu Qi**. Player swaps between Clara and Avery; escort and rescue dynamics with Reddy across surreal spaces toward New York.

* **05 CHAPTER 5: “RENEWED PURPOSE”**  
   Antagonist focus: **Paul Kent**. Avery goes rogue from a NYC base of operations; open returns to seized prior locations. Clara confronts Betsy Lumbar.

* **06 CHAPTER 6: “GLORIOUS QUEST”**  
   Antagonist focus: **Richard Tack**. Dual ascent through a transdimensional complex; swap‑driven objectives. Setpiece: device self‑destruct and escape.

* **07 EPILOGUE: “REORIENTATION”**  
   Post‑climax resolution with multiple endings: Clara arc (good/bad), Avery arc (good/bad), NG+ cosmic variant(s). Final Score gates outcomes.

## **3.3 Narrative Systems Hooks**

* **Shared world state:** Evidence and outcomes echo across POVs.

* **Consequences matrix:** Arrest/kill, noise, and Reddy care feed epilogue variants.

* **Diegetic devices:** FieldPad/TAPLINE/MEDSTAT drive clue capture and gating.

## **3.4 Deliverables**

* Chapter title sheet for UI and localization.

* Beat outlines per chapter (owner: Narrative Playbook).

* Cinematic list with triggers and dependencies.

## **3.5 Approvals**

On approval: archive to MASTER as `[SEC-03-NARRATIVE] v0.1` and update manifest.

# **Patch Instructions for Existing MASTER — SEC-04**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-04-LOOPS |` and replace the entire line with:

`| SEC-04-LOOPS | Core loops | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# MANIFEST addendum — SEC-03 CH1 synopsis
Date: 2025-08-14 22:50:08 UTC

Section: SEC-03-NARRATIVE
Change:
- Add §3.5 “Chapter 1 — Simple Curiosity” using `Patches/SEC-03_3.5_CH1_SimpleCuriosity_ADD.md`.

Version bump:
- SEC-03 minor +1

Cross-refs:
- Trackers/CH1_Outline_SimpleCuriosity.md
- Trackers/CH1_Beat2Objective.md
- Trackers/AssetList_CH1_Brightstar.md
- Trackers/QATelemetry_CH1.md

# MANIFEST addendum — SEC-03 Prologues integration
Date: 2025-08-14T11:24Z

Section: SEC-03-NARRATIVE
Change:
- Replace §3.2 Chapter List with `Patches/SEC-03_3.2_Chapter_List_REPLACE.md`.
- Prepend §3.4 with `Patches/SEC-03_3.4_Synopsis_Prologues_ADD.md` (already in Patches).

Version bump:
- Previous: vX.Y  →  New: vX.(Y+1)  (minor bump)

Cross-refs:
- Trackers/NARR-TRACKER_Prologues_v0.3.md
- Trackers/NARR-TRACKER_Playbook-Outline_Sync_v0.1.md
- Trackers/Prop_SEC-04_Loops_Prologues.md
- Trackers/Prop_SEC-05_Systems_ProloguesFlags.md
- Trackers/Prop_TDD_Evidence_FieldPad_ProloguesHooks.md

QA/Telemetry:
- Ensure events in Trackers/QATelemetry_* are referenced in SEC-11/14.

# [SEC-03] Chapter 5 — Renewed Purpose (Narrative Paste)

> Source of truth: Narrative Playbook • Outline 2025. Period: 1994. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Ambient phrase only: “the stars are right tonight.”

## Scope
- Protagonists: Avery (primary), Clara (secondary thread).
- Setting: New York City and surrounding tri‑state travel hub. Avery’s car acts as a mobile base.
- Structure: Open‑world hub unlock + parallel Clara beat.

## Avery Beats
- Returns to NYC with Clara and Reddy; learns Fred Franklin has been murdered and is framed as a suspect.
- Chooses to operate off‑book while clearing his name. Contacts use landlines, pagers, fax. Evidence is walked to drop sites.
- World opens with **Federally Seized** variants of past locations. New enemy mixes appear only in seized sites.
- Day/Night cycle alters spawns and civilians:
  - Day: mind‑swapped civilians in public spaces; crowd‑control favored. Friendly hits fail states.
  - Night: ghosts and abominations increase; patrol density reduced.
- Vehicle loop: plan at trunk loadout, drive to site, park legally or risk tow, approach on foot. No GPS; rely on printed maps and signage.

## Clara Beats
- Tracks Betsy Lumbar and confirms allegiance to **Qin Xu Qi**.
- Boss branch:
  - If player found **Cultist Literature** in Prologue: Suzanne Cutlass intercepts; arrest sequence replaces fight.
  - Else: Betsy transforms into a **wendigo**; combat boss with environmental hazards.

## Systems Hooks
- FieldPad/MEDSTAT are cable‑synced or SENTINEL‑linked only; no internet.
- Spells: **Phrases equip L/R**, **Scrolls single‑use**, **Mana calm‑regen** (no combat regen spike).
- Deputy name must be randomized per session. Use placeholder `<DEPUTY_NAME>` in text.
- Only ambient phrase permitted globally: “the stars are right tonight.”

## Fail/State Rules
- City friendly/civilian hits = fail.
- Maintain 1994 authenticity in UI prompts, signage, and comms.
- Persist clues that set up Chapter 6 objectives without revealing SRS details.

## Deliverables in SEC‑03
- Replace CH5 narrative with this paste.
- Preserve anchors used by SEC‑05/06/07 cross‑refs.

# [SEC-03] Chapter 6 — Glorious Quest (Narrative Paste)

> Source of truth: Narrative Playbook • Outline 2025. Period: 1994. Ambient phrase only: “the stars are right tonight.”

## Scope
- Dual path operation against **Richard Tack** culminating at the **Savannah River Site (SRS)** with interlocks to **D‑LAMP (WV)**.
- Player alternates between locations via open‑world travel unlocked in CH5.
- New enemy type: **Mystical Heads**; spawn in distorted reactor chambers.

## Core Objective
Disable the **Transdimensional Complex Device** before Tack triggers cross‑dimensional brainwashing; overload leads to timed escape through collapsing, reality‑warped corridors.

## Path Structure
- **Clara — Stealth/Infiltration**
  - Goals: disable security systems, avoid detection by cultists and possessed security personnel.
  - Tools: ward jamming, valves, plant/detonate charges, photo/sample evidence.
- **Avery — Assault/Fireteam**
  - Goals: clear hostile forces, disable protective wards, cover Clara’s objectives.
  - Tools: cast/equip phrases, breaching, K‑9 reroute triggers, valve operations.

## Raid Rules (live in helpers)
- **CH6 = raid. Lethal authorized.** Neutralizations are **score‑neutral**.
- **Blue‑on‑Blue = hard fail (−10).** Exceptions:
  - **Shield‑absorbed** friendly hit.
  - A **single shotgun pellet** striking a friendly from **>10 m**.
- **Evidence cap in CH6 = 3 total.** HUD must show `Evidence 0/3` and `BlueOnBlue` flag.
- **Cameras only** in **Service Passage**. **No CCTV in Vault**.
- **Breaker ≈90 s** to cycle after trip. **K‑9 reroute** available via handler diversion or scent decoy.

## 1994 Constraints
- No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Navigation via printed maps, posted site diagrams, radio freqs.
- Comms over analog radios; logging on paper, Polaroids, and film camera; lab hand‑offs by courier.

## Spell/Item System
- **Phrases equip L/R**; **Scrolls single‑use**; **Mana calm‑regen**.
- Only ambient phrase in VO/text: “the stars are right tonight.”
- Deputy name randomized per session. Use `<DEPUTY_NAME>` placeholder where referenced.

## Evidence & Cameras
- Max three pieces of evidence total in CH6. Choice tension: tactical vs investigative.
- Photographic evidence is permitted in **Service Passage** where cameras exist.
- No photography in Vault due to zero CCTV and radiation protocols; rely on samples/logs.

## Deliverables in SEC‑03
- Replace CH6 narrative with this paste.
- Ensure cross‑refs to SEC‑05/06/07 remain intact.

# [SEC-03] Chapter 7 — Aftermath & Apparitions (Narrative Paste)

> Sources: Narrative Playbook • Outline 2025. Period: 1994. Ambient phrase only: “the stars are right tonight.”

## Scope
- Locale: New York City and nearby boroughs after SRS fallout.
- Frame on Avery for the Franklin murder is lifted; public trust remains low.
- Antagonist: **Krill** (Hauser’s successor). Modus: mind control, illusions, psychic bleed.
- Encounter arc: street-level investigations → mind-hazards → **Mindscape** confrontation hook.
- City evidence cap = **2**. Non‑lethal favored. Friendly/civilian hits = **fail**.

## Systems Constraints
- 1994 authenticity: landlines, pagers, fax, payphones, film, Polaroid. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS.
- FieldPad/MEDSTAT: cable sync or SENTINEL link only.
- Spells: **Phrases equip L/R**, **Scrolls single‑use**, **Mana calm‑regen**.
- Deputy identity randomized per session. Use `<DEPUTY_NAME>` token in text.
- Only ambient phrase allowed globally: “the stars are right tonight.”

## Avery Thread
- Goal: unwind remaining cover‑up, locate Krill’s control nodes, clear public narrative without breaking FBI rules.
- Play: surveillance on payphones and safehouses; interviews with mind‑swapped civilians; forensic drops at precincts.
- Mechanics:
  - **Non‑lethal priority**: tasers/batons; firearm discharge near civilians triggers fail.
  - **Evidence cap 2**: city HUD shows `Evidence 0/2` during Avery segments.
  - **Illusion checks**: compare FieldPad sensor drift vs. MEDSTAT samples to expose false cues.

## Clara Thread
- Goal: protect witnesses targeted by Krill’s proxies; gather ritual counter‑phrases; trace EM anomalies.
- Play: escort routes, decoy tactics, controlled reveals of **Reddy** to startle cult footmen.
- Mechanics:
  - **Calm‑regen** pacing; scroll scarcity; phrase loadout puzzle for **Mindscape** entry.
  - Cameras limited to public spaces; consent needed for photo evidence in private interiors.

## Mindscape Hook (Boss Setup)
- Trigger: complete both protagonists’ node objectives; locate Krill’s anchor object (artifact or sigil series).
- Environment: fractured NYC landmarks; visual glitches, doubled NPCs; sound desync.
- Boss: **Krill** deploys illusions that copy friendly silhouettes to bait Blue‑on‑Blue; city rules still apply.
- Outcome: defeat forces Krill to retreat; leaves a **Krill_Remnant** flag for Epilogue routing.

## Fail/State Rules
- Any friendly/civilian hit = immediate fail in city scenes.
- Evidence beyond 2 is denied with “Evidence full.”
- Public panic escalations persist into Epilogue scoring if siren thresholds are exceeded.

## Deliverables in SEC‑03
- Replace CH7 narrative section with this paste.
- Preserve anchors used by SEC‑06/07 for UI and world references.

# SEC-03 — Narrative CH5–CH6 Merge (Entry Point)
Repo dir: /Patches

Use this file as the **entry point** when opening the PR. It references the split paste blocks (kept separate for clarity).

## Paste order
1) Replace `## CH5` with the contents of:
   - `/Patches/ROOT_SEC-03_CH5_Narrative_Paste.md`
2) Replace `## CH6` with the contents of:
   - `/Patches/ROOT_SEC-03_CH6_Narrative_Paste.md`

## Post‑paste checks
- CH6 states the raid ROE, lethal authorized, **Blue‑on‑Blue = fail**.
- Evidence cap **3** is present.
- 1994 lock maintained; **MicroTAC/pagers/payphones/Polaroids/analog CCTV** only.
- Ambient phrase appears only as ambient text: “the stars are right tonight.”
- Deputy name randomized.

## Note
We keep CH5 and CH6 as two paste files to reduce conflicts and ease review. This entry file exists to satisfy the PR body pointer.

## CH2 — Avery: Inner Checkpoint

### Goal
Infiltrate the Jackson, SC compound. Pass the inner gate. Detain a leader. Secure evidence. Avoid civilian harm.

### Setting
Barn and backlot compound outside Jackson, South Carolina. Night.

### Cast
Avery Jordan. ASAC Franklin. SA Lewis Krill. Aiken Co. Deputy {DeputyName}. Gate guard. Deacon analogue. Civilians.

### 1994 kit
SIG P226 or S&W 13. Limited magazines. Paper maps. Polaroid. Payphone. Fax. Teletype. No weapon lights.

### Beats
1) Briefing. Passphrase issued: "the stars are right tonight." ROE emphasized.  
2) Recon. Guard rotations logged. Civilians identified. Inner gate protocol observed.  
3) Approach. Use cover or distraction. Optional payphone to SO for timing.  
4) Inner gate. Respond with exact passphrase. One Badge plus Warrant bluff retry. Second failure sets Alert High.  
5) Search. Outbuilding A cash ledger and rosters. Shed B generator. Office shack tapes and logbook.  
6) Detain. Non-lethal takedown of Deacon analogue. Secure .38.  
7) Chain of custody. Bag and tag. Complete FD-302. Fax to field office. Send teletype BOLOs. Coordinate bookings with {DeputyName}.  
8) Exfil. Save F_GromleyCleared=1. Hook to Clara via deputy remark about the trail.

### ROE note
If an NPC initiates lethal force then a player lethal response in that encounter is score neutral.

### Failure and branches
Wrong passphrase twice sets Alert High. Civilian endangered reduces score. Excessive force reduces score unless NPC initiated lethal force first.

### Prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

## CH2 — Clara: Kadath Survival

### Goal
Survive, feed Reddy, attempt escape, alert parents to collect children.

### Setting
Kadath forest beyond “Pine Break” portal behind Brightstar. Brightstar interior is liminal and scrambled except anchors.

### Cast
Clara Winston; Reddy; wardens; staff; distant children.

### 1994 Kit
Maglite, Polaroid, twine, chalk, matches, microcassette recorder, paper map, canteen, iodine, first-aid. MEDSTAT note-card (text only; intermittent SENTINEL).

### Beats
1) **Bivouac:** Learn portal at Pine Break. Forage. Set chalk mark.  
2) **Water run:** Culvert found. Boil or iodine → `WaterSafe`.  
3) **Loop demo:** Trails A–D loop. Chalk fades past 30 m from Brightstar.  
4) **Stash Reddy:** Use nearest Safe Nest (Bivouac/Bus/Locker). Carry = +noise, −stealth.  
5) **Infiltration I — Kitchen:** Food, can opener, canteen → `FoodSecured`.  
6) **Infiltration II — Nurse:** Iodine, gauze, D-cells; unlock Nurse Locker Safe Nest.  
7) **Office break-in:** Emergency Contact ledger + attendance log. Transcribe to MEDSTAT.  
8) **Parent calls:** Use landline. Call Intercept meter visible while connected; hang up to avoid intercept.  
9) **Brightstar Brawl (mandatory):** Multipurpose room fight. Non-lethal favored. Loot Master Keys, Admin map, Medkit → `F_BrawlWon=1`, `F_MasterKeys=1`.  
10) **Admin sweep:** Roster, delivery slips. Record vent whisper “the stars are right tonight.” Playback opens one warded cabinet.  
11) **Backtrack:** Return via portal. Feed Reddy. Manage meters.  
12) **Exit test:** Even with `FoodSecured & WaterSafe & ParentsConfirmed≥NMin`, outer trail collapses. Chapter wall holds.

### Failure/Branches
- Cry ping while carrying Reddy draws sweep.  
- Intercept at 100 cancels call and raises Alert.  
- Brawl defeat or Reddy harmed → soft reset to pre-call checkpoint; inventory kept; +Alert on retry.

### Evidence Log (text only)
Emergency ledger pages, attendance, roster, delivery slips, phrase notes, loop map, breaker/anchor notes.

### Scoring
See Patch file. Non-lethal and SafeCall bonuses prioritized.

### Prompts (≤14 chars)
Hush, Hide, Crouch, Throw, Listen, Use, Inspect, Pick Up, Forage, Gather, Boil, Purify, Eat, Drink, Rest, Soothe, Record, Play, Dial, Call Parent, Note, Map, Open, Unlock, Carry, Stash, Retrieve, Block, Dodge, Shove, Grapple, Swing, Spray, Trip, Sand, Lights, Wedge

# SEC-03 — CH3 Narrative Sections (Consolidated)

## CH3 — Clara & Reddy: “Innocent Fascination”
**Goal:** Survive Kadath, protect Reddy, repel scavengers without lethal force.  
**Setting:** Kadath forest near warped Brightstar (Jackson, SC). Time dilation persists.  
**Beats:**
1) Forage & trace a scavenger trail.  
2) Ambush springs; Clara shields Reddy.  
3) Swap to **Reddy Playable** telekinesis (infinite energy this chapter).  
4) Crowd control with non-lethal TK: pin, stack, block.  
5) Ethics check: wanton destruction reduces score.  
6) Clara collapses from concussion; Reddy powers down and returns to her side.  
7) Audio hook from Brightstar interior sets up convergence.

**Evidence:** Trail notes, delivery slips, ledger snapshots.  
**Phrase:** Ambient only: “the stars are right tonight.”  
**Failure/Retry:** Clara downed → Reddy rescue window; timer fail → soft reset; inventory persists.

## CH3 — Avery: “Suspension & Daycare Haunting”
**Goal:** Investigate condemned Brightstar while suspended; survive spectral threat; get forced into Kadath.  
**Setting:** Condemned Brightstar interior → Kadath threshold. Night.  
**Beats:**
1) Suspension notice from Franklin; fallout from Phillips.  
2) Solo return to condemned daycare.  
3) Spectral hunt; retrieve key evidence.  
4) Unwinnable fight; chase through threshold into Kadath.  
5) Rescue by Clara & Reddy; time-skew exchange.  
6) Save team-up flag for Chapter 4.

**Systems:** Spectral-Phased Muzzle Brake consumable enables limited damage; otherwise avoidance.  
**Evidence:** Condemnation copy, key ring, gate log fragment.  
**ROE:** Lethal allowed on spectral; civilian harm penalized.  
**Phrase:** Ambient only.

## Interlock & Continuity
- Jackson, SC continuity for Brightstar.  
- Time dilation acknowledged at rescue.  
- No dialogue use of the phrase in CH3.

# SEC-03 — CH4 Narrative (Revised)

## Title
Toward the Walled City

## Goal
Escape Kadath by reaching the Walled City; secure temporary refuge.

## Setting
Kadath forest near Brightstar’s Pine Break → hostile outskirts → South Gate of the Walled City (Kadath of Nyarlathotep inspiration). Night-dusk cycle.

## Cast
Clara Winston; Reddy; SA Avery Jordan; Outskirt Scavengers; Wall Wardens; slain Beast (on entry).

## Beats
1) **Pine Break kill:** Beast chases Avery. Reddy unleashes one telekinetic **Burst** and kills it.  
2) **Meet & align:** Clara, Reddy, Avery align. Clara confirms days of failed exit attempts via Brightstar and Pine Break.  
3) **Systems down:** Avery’s FieldPad and **TAPLINE** cannot connect to **SENTINEL**; devices run **offline** and store evidence locally only.  
4) **Recon ridge:** City spotted with binoculars. Decision to approach despite hostile outskirts.  
5) **Prep & pack:** Water safe, food packed, safe nest marked.  
6) **Traverse outskirts:** Stealth through hostile territory; optional barter. Whispered phrase present as ambient only.  
7) **Skirmish to ditch:** Brief chase; reach cover within bowshot of the South Gate.  
8) **Gate standoff:** Wardens watch; horn-call. No entry yet. Camp outside. Plan parley next.

## Failure/Branches
- Alert escalates during traverse → bigger skirmish and lower end score.  
- Injury without camp → fatigue penalties at start of next chapter.

## Evidence Log
Gate silhouettes, horn-call pattern, wall measurements, scavenger signs, SENTINEL/TAPLINE offline notes.

## Carryover Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-03 — CH5→CH6 Narrative Insert: Deep D‑LAMP & Iron Highway
Repo dir: /Patches

## CH5 Insert — Descent and Drive
- **WV River Island Shaft:** Avery locates the disguised elevator kiosk; descends ~1 mile to the abandoned D‑LAMP deep site.  
- **Abandoned Complex:** AEC→DOE exit paperwork, 1980s–1990s cult occupation, undead outbreaks.  
- **Mini‑Boss:** Star Vampire in Pump Cavern; victory grants Route Control Key.  
- **Rover Bay:** Acquire D‑LAMP utility rover; signage for **Iron Highway**.  
- **Iron Highway:** Drive the tunnel road toward **SRS Secret Annex**; zombies/night gaunts/cultists as encounters.  
- **Seal Gate:** Stop at Annex bulkhead. Flag handoff to CH6.

## CH6 Insert — SRS Secret Annex Entry
- **Ingress:** From Iron Highway pull‑off to man‑door; enter Core Galleries.  
- **Objective:** Reach Splinter Vault pre‑ritual and choose Contain/Sever/Black File path.  
- **Comms:** Rogue; Krill via pager/payphone only. Evidence capped.

## Continuity Notes
- 1994 constraints enforced (MicroTAC, Polaroid, paper logs).  
- Phrases equip L/R with Mana; scrolls single‑use.

# SEC-03 — CH5 Narrative Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Avery — D-LAMP Lead
1) **Franklin packet:** Faxed list points to D-LAMP vendor/site.  
2) **Recon + approach:** Night drive; perimeter sweep.  
3) **Inside or stakeout:** Front pretext/service tail vs camera-count + shipment log.  
4) **Findings:** Lab POs, occult-adjacent supplies, phone logs intersect Brightstar.  
5) **Hook:** Fold D-LAMP suppliers into SRS warrants. Flags: `F_DLampLocated`, `F_DLampEntered?`, `F_DLampLead`.

## Clara — Betsy Resolution
**Branch gate:** `BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)`

- **Raid bypass (if ineligible):** Multi-agency serve; quick clear; evidence sweep. Flags: `F_BetsyRaidBypass=1`, `F_BetsyHouseCleared=1`.  
- **Boss fight (if eligible):** **Wendigo Betsy** set piece at the house. Phases: Lunge/Grab → Wall-scramble shrieks → Frenzy. Use **Shield**, **Ward Jam**, furniture shove. Flags: `F_BetsyBossDefeated=1`, `F_BetsyHouseCleared=1`.

## Convergence
- **Motel rendezvous:** Clara + Reddy link with Avery. Packet sync. Set `F_ClaraFollowsAvery=1`.  
- **Forward:** Prepare CH6 warrants (SRS + D-LAMP) and UC brief.

## Evidence
- Raid: itemized seizure list, Polaroid refs.  
- Boss: recovered notes, floor-scratch glyph rubbings.

# SEC-03 — CH5 Narrative (Rework)
Repo dir: /Patches

## Title
NYFO: The Last Call

## Goals
Keep Avery out of custody; secure SRS undercover warrant; set Clara→Betsy guardianship path.

## Beats
1) **Hotel night:** Check-in near NYFO. POI status active.  
2) **NYFO debrief:** Interrogation on Kadath; FieldPad/TAPLINE queue evidence; uploads only at NYFO line.  
3) **Krill hallway:** Raises Avery’s clearance; “buckle up.” Confirms real magic exists beyond Kadath. `F_ClearanceRaised=1`, `F_KrillBriefed=1`.  
4) **Franklin killed (night):** Pager/news. `F_FranklinMurdered=1`.  
5) **Hotel morning raid:** Agents arrive to detain Avery. **Stealth exit** or **non-lethal takedown** path. `F_EscapeHotel=1`.  
6) **Warrant work (day):** Build **OpsOrder_SRS**, **Affidavit_EvidenceIndex**, **Warrant_Safehouse**; sign-offs: NYFO ASAC → USAO SDGA → magistrate. `F_WarrantSRS=1`.  
7) **Clara decision:** Clara travels to **Betsy** to address guardianship for Reddy. `F_ClaraToBetsy=1`, `F_GuardianshipPending=1`.  
8) **Close:** Avery slated for SRS UC brief; Clara departs NYC. Hooks to CH6/CH7.

## Evidence
Debrief summary, Krill memo, MicroTAC call logs, hotel register, warrant packet (ops order, affidavit, warrant), guardianship notes.

## Failure/Branches
- Flee or unreachable during POI window → harsher CH6 start.  
- Excessive force on agents → IA penalties that persist.

## Carryover
Spell phrases remain L/R equipped with Mana; scrolls remain single-use items.

# SEC-03 — CH6 Beat Sheet (Raid)
Repo dir: /Patches

## Scope
Sanctioned raid vs hostile combatants; lethal authorized; blue-on-blue fail. Evidence cap 3.

## Beats
1) **UC Pre-brief (Rogue):** Krill pager check, loadout set (phrases L/R, scrolls).  
2) **Safehouse Sting:** Buy/bust with {DeputyName}; seize ledgers/reagents/maps. `F_SafehouseSting=1`.  
3) **Ingress:** Iron Highway pull-off → SRS Secret Annex bulkhead. `F_SRSBreach=1`.  
4) **Service Passage:** K-9 arcs; analog cams; breaker shortcut.  
5) **Valve Row:** Tag A/B/C with Polaroid for Contain path.  
6) **Dead Piping:** Ritual prep tables; evidence (if cap allows). `F_CoreFound=1`.  
7) **Ritual Ignition:** Space fold; spawn waves. `F_RitualIgnited=1`.  
8) **Path A — Contain:** Jam Wards, cycle valves A→B→C, lock gimbal. `F_End_Contain=1`.  
9) **Path B — Sever:** Plant charges, interrupt chant, detonate, run. `F_End_Escape=1`.  
10) **Path C — Black File:** Photo, sample, bag+tag, exfil late. `F_End_BlackFile=1`.  
11) **Extraction:** Fence gap rendezvous with {DeputyName}; FD-302 queued.

## ROE Banner
- Lethal authorized. No score penalty for neutralizations.  
- Blue-on-blue = −10 and abort. No civilians expected.

## UI prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Crouch, Hide, Dodge, Breach, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

# SEC-03 — CH6 Epilogue
Repo dir: /Patches

## Overview
Final outcomes after the SRS raid. No civilians present. Phrase remains ambient: “the stars are right tonight.”

### Ending A — Contain (Seal)
- **Public face:** minor incident, localized blackout.  
- **Internal:** commendations in sealed annex; Krill message: “not over.”  
- **Hooks:** legal pressure on D‑LAMP vendors; Clara/Reddy low profile.  
- **Slides:** injured saved count; splinter stabilized.

### Ending B — Sever (Escape)
- **Public face:** unexplained anomalies near fence line; whispers.  
- **Internal:** reprimand avoided; Krill prioritizes damage control.  
- **Hooks:** rogue cells scatter; Iron Highway collapse risks.  
- **Slides:** team intact; area warped.

### Ending C — Black File (Evidence-first)
- **Public face:** nothing on record.  
- **Internal:** evidence maximum; reputation hit logged.  
- **Hooks:** secret indictments; Krill warns of fallout.  
- **Slides:** dossiers filled; trust eroded.

## Postcards (optional stingers)
- Clara & Reddy: roadside diner, 3 a.m., pager buzz.  
- Avery: MicroTAC rings from an unknown exchange.  
- Deputy {DeputyName}: radio silence, then a single horn-call on scan.

## **3.2 Chapter List**  _(Replace this entire subsection)_
Date: 2025-08-14T11:24Z

- **PROLOGUES — Tutorials**
  - **0A — Avery Jordan (1989, Quantico — Hogan’s Alley):** ROE, challenge→cuff→search, analog custody; range drill; dual‑wield + decoupled aim; non‑lethal ammo; escort drill; no FieldPad.
  - **0B — Clara Winston (1994, Betsy Lumbar’s Apt):** MEDSTAT vitals and caregiving; Reddy‑POV beat; Clara finds the Brightstar pin; no FieldPad/TAPLINE.

- **01 CHAPTER 1: “SIMPLE CURIOSITY”**
- **02 CHAPTER 2: “PASSING INTEREST”**
- **03 CHAPTER 3: “INNOCENT FASCINATION”**
- **04 CHAPTER 4: “UNDYING OBSESSION”**
- **05 CHAPTER 5: “RENEWED PURPOSE”**
- **06 CHAPTER 6: “GLORIOUS QUEST”**

_Canon locks:_ Location/Name = **Brightstar Daycare, Jackson, SC**. Possession = **event‑driven**; day/night adjusts spawns only. POV = **strict in‑character**; Clara Prologue uses **Reddy‑POV** for face/knife beat.

## **3.4 Synopsis — Prologues (Canonical)**  _(2025-08-14)_

### 0A — Avery Jordan (1989, Quantico — Hogan’s Alley)
**Goal:** Teach ROE and analog evidence. **Tone:** no danger. **Target:** ~15 min first‑time critical path.  
**Beats:** Orientation with Eddie Paldino → challenge→cuff→search drill → 35mm photo; bag→tag→log on paper; locker window handoff → range block with dual‑wield + decoupled aim → debrief. **Notes:** Brightstar signifier appears among props (not the pin). **Devices:** no FieldPad/PCMCIA/CF; telephonic warrant referenced only.

### 0B — Clara Winston (1994, Home Visit — Betsy Lumbar)
**Goal:** Teach MEDSTAT + caregiving. **Tone:** supportive. **Target:** ~15 min first‑time critical path.  
**Beats:** Arrival via buzzer/landline → MEDSTAT vitals (pulse‑ox, BP, temp) log → tea/pills/tidy → **Reddy‑POV** beat shows Clara’s face while a knife is unsheathed behind Reddy → **Clara finds the Brightstar pin** → schedule follow‑up by landline. **Devices:** **MEDSTAT handheld + RF wrist‑band** only; no FieldPad/TAPLINE.

### POV & Cinematic Canon
- Diegetic delivery; strict in‑character POV. Exceptions only when **POV changes to Reddy** are explicit and player‑driven.  
- Possession events are **scripted/event‑driven**; day/night only affects spawn composition and patrol density.

_Propagation:_ Update SEC‑04 loops (tutorial prompts, dual‑wield/decoupled aim), SEC‑05 evidence flags (pin boolean), SEC‑06 locations (Jackson, SC), SEC‑07 MEDSTAT UI, SEC‑11/14 QA tests.

## **3.5 Chapter 1 — “Simple Curiosity”** _(ADD this subsection)_
Date: 2025-08-14 23:10:43 UTC
Owner: Nick Goldman

**Year/Locale:** 1994, **Brightstar Daycare (Jackson, SC)** and roadside nearby.  
**POV:** strict in‑character; interleaved **Clara** and **Avery** legs.  
**Devices:** Clara—**MEDSTAT** only; unlocks **Notes** mid‑chapter via **PCMCIA Type II note‑card** (Newton‑compatible; no camera/internet). Avery—analog camera, paper custody, radio.  
**Canon locks:** Pin symbol = SYM‑001 (lore only). No FieldPad/TAPLINE in CH1.

**Clara Beats:** sign‑in → find card → insert → tour; overhear “the stars are right tonight” → light stealth/care → exit plan.  
**Avery Beats:** brief (deputy name **randomized per save**) → challenge → cuff → search → photo → bag/tag/log → locker handoff → debrief.

## **3.2 Chapter List**  _(Replace this entire subsection)_

- **PROLOGUES — Tutorials**  
  - **0A — Avery Jordan (1989, Quantico — Hogan’s Alley):** ROE, challenge→cuff→search, analog custody; range drill; dual‑wield + decoupled aim; no FieldPad.  
  - **0B — Clara Winston (1994, Betsy Lumbar’s Apt):** MEDSTAT vitals and caregiving; Reddy‑POV beat; Clara finds the Brightstar pin; no FieldPad/TAPLINE.

- **01 CHAPTER 1: “SIMPLE CURIOSITY”**  
- **02 CHAPTER 2: “PASSING INTEREST”**  
- **03 CHAPTER 3: “INNOCENT FASCINATION”**  
- **04 CHAPTER 4: “UNDYING OBSESSION”**  
- **05 CHAPTER 5: “RENEWED PURPOSE”**  
- **06 CHAPTER 6: “GLORIOUS QUEST”**

_Canon locks:_ Location/Name = **Brightstar Daycare, Jackson, SC**. Possession = **event‑driven**; day/night adjusts spawns only. POV = **strict in‑character**; Clara Prologue uses **Reddy‑POV** for face/knife beat.

# MANIFEST addendum — SEC-03 CH1 synopsis
Date: 2025-08-14 22:50:08 UTC

Section: SEC-03-NARRATIVE
Change:
- Add §3.5 “Chapter 1 — Simple Curiosity” using `Patches/SEC-03_3.5_CH1_SimpleCuriosity_ADD.md`.

Version bump:
- SEC-03 minor +1

Cross-refs:
- Trackers/CH1_Outline_SimpleCuriosity.md
- Trackers/CH1_Beat2Objective.md
- Trackers/AssetList_CH1_Brightstar.md
- Trackers/QATelemetry_CH1.md

# MANIFEST addendum — SEC-03 Prologues integration
Date: 2025-08-14T11:24Z

Section: SEC-03-NARRATIVE
Change:
- Replace §3.2 Chapter List with `Patches/SEC-03_3.2_Chapter_List_REPLACE.md`.
- Prepend §3.4 with `Patches/SEC-03_3.4_Synopsis_Prologues_ADD.md` (already in Patches).

Version bump:
- Previous: vX.Y  →  New: vX.(Y+1)  (minor bump)

Cross-refs:
- Trackers/NARR-TRACKER_Prologues_v0.3.md
- Trackers/NARR-TRACKER_Playbook-Outline_Sync_v0.1.md
- Trackers/Prop_SEC-04_Loops_Prologues.md
- Trackers/Prop_SEC-05_Systems_ProloguesFlags.md
- Trackers/Prop_TDD_Evidence_FieldPad_ProloguesHooks.md

QA/Telemetry:
- Ensure events in Trackers/QATelemetry_* are referenced in SEC-11/14.

# [SEC-03] Chapter 5 — Renewed Purpose (Narrative Paste)

> Source of truth: Narrative Playbook • Outline 2025. Period: 1994. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Ambient phrase only: “the stars are right tonight.”

## Scope
- Protagonists: Avery (primary), Clara (secondary thread).
- Setting: New York City and surrounding tri‑state travel hub. Avery’s car acts as a mobile base.
- Structure: Open‑world hub unlock + parallel Clara beat.

## Avery Beats
- Returns to NYC with Clara and Reddy; learns Fred Franklin has been murdered and is framed as a suspect.
- Chooses to operate off‑book while clearing his name. Contacts use landlines, pagers, fax. Evidence is walked to drop sites.
- World opens with **Federally Seized** variants of past locations. New enemy mixes appear only in seized sites.
- Day/Night cycle alters spawns and civilians:
  - Day: mind‑swapped civilians in public spaces; crowd‑control favored. Friendly hits fail states.
  - Night: ghosts and abominations increase; patrol density reduced.
- Vehicle loop: plan at trunk loadout, drive to site, park legally or risk tow, approach on foot. No GPS; rely on printed maps and signage.

## Clara Beats
- Tracks Betsy Lumbar and confirms allegiance to **Qin Xu Qi**.
- Boss branch:
  - If player found **Cultist Literature** in Prologue: Suzanne Cutlass intercepts; arrest sequence replaces fight.
  - Else: Betsy transforms into a **wendigo**; combat boss with environmental hazards.

## Systems Hooks
- FieldPad/MEDSTAT are cable‑synced or SENTINEL‑linked only; no internet.
- Spells: **Phrases equip L/R**, **Scrolls single‑use**, **Mana calm‑regen** (no combat regen spike).
- Deputy name must be randomized per session. Use placeholder `<DEPUTY_NAME>` in text.
- Only ambient phrase permitted globally: “the stars are right tonight.”

## Fail/State Rules
- City friendly/civilian hits = fail.
- Maintain 1994 authenticity in UI prompts, signage, and comms.
- Persist clues that set up Chapter 6 objectives without revealing SRS details.

## Deliverables in SEC‑03
- Replace CH5 narrative with this paste.
- Preserve anchors used by SEC‑05/06/07 cross‑refs.

# [SEC-03] Chapter 6 — Glorious Quest (Narrative Paste)

> Source of truth: Narrative Playbook • Outline 2025. Period: 1994. Ambient phrase only: “the stars are right tonight.”

## Scope
- Dual path operation against **Richard Tack** culminating at the **Savannah River Site (SRS)** with interlocks to **D‑LAMP (WV)**.
- Player alternates between locations via open‑world travel unlocked in CH5.
- New enemy type: **Mystical Heads**; spawn in distorted reactor chambers.

## Core Objective
Disable the **Transdimensional Complex Device** before Tack triggers cross‑dimensional brainwashing; overload leads to timed escape through collapsing, reality‑warped corridors.

## Path Structure
- **Clara — Stealth/Infiltration**
  - Goals: disable security systems, avoid detection by cultists and possessed security personnel.
  - Tools: ward jamming, valves, plant/detonate charges, photo/sample evidence.
- **Avery — Assault/Fireteam**
  - Goals: clear hostile forces, disable protective wards, cover Clara’s objectives.
  - Tools: cast/equip phrases, breaching, K‑9 reroute triggers, valve operations.

## Raid Rules (live in helpers)
- **CH6 = raid. Lethal authorized.** Neutralizations are **score‑neutral**.
- **Blue‑on‑Blue = hard fail (−10).** Exceptions:
  - **Shield‑absorbed** friendly hit.
  - A **single shotgun pellet** striking a friendly from **>10 m**.
- **Evidence cap in CH6 = 3 total.** HUD must show `Evidence 0/3` and `BlueOnBlue` flag.
- **Cameras only** in **Service Passage**. **No CCTV in Vault**.
- **Breaker ≈90 s** to cycle after trip. **K‑9 reroute** available via handler diversion or scent decoy.

## 1994 Constraints
- No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Navigation via printed maps, posted site diagrams, radio freqs.
- Comms over analog radios; logging on paper, Polaroids, and film camera; lab hand‑offs by courier.

## Spell/Item System
- **Phrases equip L/R**; **Scrolls single‑use**; **Mana calm‑regen**.
- Only ambient phrase in VO/text: “the stars are right tonight.”
- Deputy name randomized per session. Use `<DEPUTY_NAME>` placeholder where referenced.

## Evidence & Cameras
- Max three pieces of evidence total in CH6. Choice tension: tactical vs investigative.
- Photographic evidence is permitted in **Service Passage** where cameras exist.
- No photography in Vault due to zero CCTV and radiation protocols; rely on samples/logs.

## Deliverables in SEC‑03
- Replace CH6 narrative with this paste.
- Ensure cross‑refs to SEC‑05/06/07 remain intact.

# [SEC-03] Chapter 7 — Aftermath & Apparitions (Narrative Paste)

> Sources: Narrative Playbook • Outline 2025. Period: 1994. Ambient phrase only: “the stars are right tonight.”

## Scope
- Locale: New York City and nearby boroughs after SRS fallout.
- Frame on Avery for the Franklin murder is lifted; public trust remains low.
- Antagonist: **Krill** (Hauser’s successor). Modus: mind control, illusions, psychic bleed.
- Encounter arc: street-level investigations → mind-hazards → **Mindscape** confrontation hook.
- City evidence cap = **2**. Non‑lethal favored. Friendly/civilian hits = **fail**.

## Systems Constraints
- 1994 authenticity: landlines, pagers, fax, payphones, film, Polaroid. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS.
- FieldPad/MEDSTAT: cable sync or SENTINEL link only.
- Spells: **Phrases equip L/R**, **Scrolls single‑use**, **Mana calm‑regen**.
- Deputy identity randomized per session. Use `<DEPUTY_NAME>` token in text.
- Only ambient phrase allowed globally: “the stars are right tonight.”

## Avery Thread
- Goal: unwind remaining cover‑up, locate Krill’s control nodes, clear public narrative without breaking FBI rules.
- Play: surveillance on payphones and safehouses; interviews with mind‑swapped civilians; forensic drops at precincts.
- Mechanics:
  - **Non‑lethal priority**: tasers/batons; firearm discharge near civilians triggers fail.
  - **Evidence cap 2**: city HUD shows `Evidence 0/2` during Avery segments.
  - **Illusion checks**: compare FieldPad sensor drift vs. MEDSTAT samples to expose false cues.

## Clara Thread
- Goal: protect witnesses targeted by Krill’s proxies; gather ritual counter‑phrases; trace EM anomalies.
- Play: escort routes, decoy tactics, controlled reveals of **Reddy** to startle cult footmen.
- Mechanics:
  - **Calm‑regen** pacing; scroll scarcity; phrase loadout puzzle for **Mindscape** entry.
  - Cameras limited to public spaces; consent needed for photo evidence in private interiors.

## Mindscape Hook (Boss Setup)
- Trigger: complete both protagonists’ node objectives; locate Krill’s anchor object (artifact or sigil series).
- Environment: fractured NYC landmarks; visual glitches, doubled NPCs; sound desync.
- Boss: **Krill** deploys illusions that copy friendly silhouettes to bait Blue‑on‑Blue; city rules still apply.
- Outcome: defeat forces Krill to retreat; leaves a **Krill_Remnant** flag for Epilogue routing.

## Fail/State Rules
- Any friendly/civilian hit = immediate fail in city scenes.
- Evidence beyond 2 is denied with “Evidence full.”
- Public panic escalations persist into Epilogue scoring if siren thresholds are exceeded.

## Deliverables in SEC‑03
- Replace CH7 narrative section with this paste.
- Preserve anchors used by SEC‑06/07 for UI and world references.

# SEC-03 — Narrative CH5–CH6 Merge (Entry Point)
Repo dir: /Patches

Use this file as the **entry point** when opening the PR. It references the split paste blocks (kept separate for clarity).

## Paste order
1) Replace `## CH5` with the contents of:
   - `/Patches/ROOT_SEC-03_CH5_Narrative_Paste.md`
2) Replace `## CH6` with the contents of:
   - `/Patches/ROOT_SEC-03_CH6_Narrative_Paste.md`

## Post‑paste checks
- CH6 states the raid ROE, lethal authorized, **Blue‑on‑Blue = fail**.
- Evidence cap **3** is present.
- 1994 lock maintained; **MicroTAC/pagers/payphones/Polaroids/analog CCTV** only.
- Ambient phrase appears only as ambient text: “the stars are right tonight.”
- Deputy name randomized.

## Note
We keep CH5 and CH6 as two paste files to reduce conflicts and ease review. This entry file exists to satisfy the PR body pointer.

## CH2 — Avery: Inner Checkpoint

### Goal
Infiltrate the Jackson, SC compound. Pass the inner gate. Detain a leader. Secure evidence. Avoid civilian harm.

### Setting
Barn and backlot compound outside Jackson, South Carolina. Night.

### Cast
Avery Jordan. ASAC Franklin. SA Lewis Krill. Aiken Co. Deputy {DeputyName}. Gate guard. Deacon analogue. Civilians.

### 1994 kit
SIG P226 or S&W 13. Limited magazines. Paper maps. Polaroid. Payphone. Fax. Teletype. No weapon lights.

### Beats
1) Briefing. Passphrase issued: "the stars are right tonight." ROE emphasized.  
2) Recon. Guard rotations logged. Civilians identified. Inner gate protocol observed.  
3) Approach. Use cover or distraction. Optional payphone to SO for timing.  
4) Inner gate. Respond with exact passphrase. One Badge plus Warrant bluff retry. Second failure sets Alert High.  
5) Search. Outbuilding A cash ledger and rosters. Shed B generator. Office shack tapes and logbook.  
6) Detain. Non-lethal takedown of Deacon analogue. Secure .38.  
7) Chain of custody. Bag and tag. Complete FD-302. Fax to field office. Send teletype BOLOs. Coordinate bookings with {DeputyName}.  
8) Exfil. Save F_GromleyCleared=1. Hook to Clara via deputy remark about the trail.

### ROE note
If an NPC initiates lethal force then a player lethal response in that encounter is score neutral.

### Failure and branches
Wrong passphrase twice sets Alert High. Civilian endangered reduces score. Excessive force reduces score unless NPC initiated lethal force first.

### Prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

## CH2 — Clara: Kadath Survival

### Goal
Survive, feed Reddy, attempt escape, alert parents to collect children.

### Setting
Kadath forest beyond “Pine Break” portal behind Brightstar. Brightstar interior is liminal and scrambled except anchors.

### Cast
Clara Winston; Reddy; wardens; staff; distant children.

### 1994 Kit
Maglite, Polaroid, twine, chalk, matches, microcassette recorder, paper map, canteen, iodine, first-aid. MEDSTAT note-card (text only; intermittent SENTINEL).

### Beats
1) **Bivouac:** Learn portal at Pine Break. Forage. Set chalk mark.  
2) **Water run:** Culvert found. Boil or iodine → `WaterSafe`.  
3) **Loop demo:** Trails A–D loop. Chalk fades past 30 m from Brightstar.  
4) **Stash Reddy:** Use nearest Safe Nest (Bivouac/Bus/Locker). Carry = +noise, −stealth.  
5) **Infiltration I — Kitchen:** Food, can opener, canteen → `FoodSecured`.  
6) **Infiltration II — Nurse:** Iodine, gauze, D-cells; unlock Nurse Locker Safe Nest.  
7) **Office break-in:** Emergency Contact ledger + attendance log. Transcribe to MEDSTAT.  
8) **Parent calls:** Use landline. Call Intercept meter visible while connected; hang up to avoid intercept.  
9) **Brightstar Brawl (mandatory):** Multipurpose room fight. Non-lethal favored. Loot Master Keys, Admin map, Medkit → `F_BrawlWon=1`, `F_MasterKeys=1`.  
10) **Admin sweep:** Roster, delivery slips. Record vent whisper “the stars are right tonight.” Playback opens one warded cabinet.  
11) **Backtrack:** Return via portal. Feed Reddy. Manage meters.  
12) **Exit test:** Even with `FoodSecured & WaterSafe & ParentsConfirmed≥NMin`, outer trail collapses. Chapter wall holds.

### Failure/Branches
- Cry ping while carrying Reddy draws sweep.  
- Intercept at 100 cancels call and raises Alert.  
- Brawl defeat or Reddy harmed → soft reset to pre-call checkpoint; inventory kept; +Alert on retry.

### Evidence Log (text only)
Emergency ledger pages, attendance, roster, delivery slips, phrase notes, loop map, breaker/anchor notes.

### Scoring
See Patch file. Non-lethal and SafeCall bonuses prioritized.

### Prompts (≤14 chars)
Hush, Hide, Crouch, Throw, Listen, Use, Inspect, Pick Up, Forage, Gather, Boil, Purify, Eat, Drink, Rest, Soothe, Record, Play, Dial, Call Parent, Note, Map, Open, Unlock, Carry, Stash, Retrieve, Block, Dodge, Shove, Grapple, Swing, Spray, Trip, Sand, Lights, Wedge

# SEC-03 — CH3 Narrative Sections (Consolidated)

## CH3 — Clara & Reddy: “Innocent Fascination”
**Goal:** Survive Kadath, protect Reddy, repel scavengers without lethal force.  
**Setting:** Kadath forest near warped Brightstar (Jackson, SC). Time dilation persists.  
**Beats:**
1) Forage & trace a scavenger trail.  
2) Ambush springs; Clara shields Reddy.  
3) Swap to **Reddy Playable** telekinesis (infinite energy this chapter).  
4) Crowd control with non-lethal TK: pin, stack, block.  
5) Ethics check: wanton destruction reduces score.  
6) Clara collapses from concussion; Reddy powers down and returns to her side.  
7) Audio hook from Brightstar interior sets up convergence.

**Evidence:** Trail notes, delivery slips, ledger snapshots.  
**Phrase:** Ambient only: “the stars are right tonight.”  
**Failure/Retry:** Clara downed → Reddy rescue window; timer fail → soft reset; inventory persists.

## CH3 — Avery: “Suspension & Daycare Haunting”
**Goal:** Investigate condemned Brightstar while suspended; survive spectral threat; get forced into Kadath.  
**Setting:** Condemned Brightstar interior → Kadath threshold. Night.  
**Beats:**
1) Suspension notice from Franklin; fallout from Phillips.  
2) Solo return to condemned daycare.  
3) Spectral hunt; retrieve key evidence.  
4) Unwinnable fight; chase through threshold into Kadath.  
5) Rescue by Clara & Reddy; time-skew exchange.  
6) Save team-up flag for Chapter 4.

**Systems:** Spectral-Phased Muzzle Brake consumable enables limited damage; otherwise avoidance.  
**Evidence:** Condemnation copy, key ring, gate log fragment.  
**ROE:** Lethal allowed on spectral; civilian harm penalized.  
**Phrase:** Ambient only.

## Interlock & Continuity
- Jackson, SC continuity for Brightstar.  
- Time dilation acknowledged at rescue.  
- No dialogue use of the phrase in CH3.

# SEC-03 — CH4 Narrative (Revised)

## Title
Toward the Walled City

## Goal
Escape Kadath by reaching the Walled City; secure temporary refuge.

## Setting
Kadath forest near Brightstar’s Pine Break → hostile outskirts → South Gate of the Walled City (Kadath of Nyarlathotep inspiration). Night-dusk cycle.

## Cast
Clara Winston; Reddy; SA Avery Jordan; Outskirt Scavengers; Wall Wardens; slain Beast (on entry).

## Beats
1) **Pine Break kill:** Beast chases Avery. Reddy unleashes one telekinetic **Burst** and kills it.  
2) **Meet & align:** Clara, Reddy, Avery align. Clara confirms days of failed exit attempts via Brightstar and Pine Break.  
3) **Systems down:** Avery’s FieldPad and **TAPLINE** cannot connect to **SENTINEL**; devices run **offline** and store evidence locally only.  
4) **Recon ridge:** City spotted with binoculars. Decision to approach despite hostile outskirts.  
5) **Prep & pack:** Water safe, food packed, safe nest marked.  
6) **Traverse outskirts:** Stealth through hostile territory; optional barter. Whispered phrase present as ambient only.  
7) **Skirmish to ditch:** Brief chase; reach cover within bowshot of the South Gate.  
8) **Gate standoff:** Wardens watch; horn-call. No entry yet. Camp outside. Plan parley next.

## Failure/Branches
- Alert escalates during traverse → bigger skirmish and lower end score.  
- Injury without camp → fatigue penalties at start of next chapter.

## Evidence Log
Gate silhouettes, horn-call pattern, wall measurements, scavenger signs, SENTINEL/TAPLINE offline notes.

## Carryover Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-03 — CH5→CH6 Narrative Insert: Deep D‑LAMP & Iron Highway
Repo dir: /Patches

## CH5 Insert — Descent and Drive
- **WV River Island Shaft:** Avery locates the disguised elevator kiosk; descends ~1 mile to the abandoned D‑LAMP deep site.  
- **Abandoned Complex:** AEC→DOE exit paperwork, 1980s–1990s cult occupation, undead outbreaks.  
- **Mini‑Boss:** Star Vampire in Pump Cavern; victory grants Route Control Key.  
- **Rover Bay:** Acquire D‑LAMP utility rover; signage for **Iron Highway**.  
- **Iron Highway:** Drive the tunnel road toward **SRS Secret Annex**; zombies/night gaunts/cultists as encounters.  
- **Seal Gate:** Stop at Annex bulkhead. Flag handoff to CH6.

## CH6 Insert — SRS Secret Annex Entry
- **Ingress:** From Iron Highway pull‑off to man‑door; enter Core Galleries.  
- **Objective:** Reach Splinter Vault pre‑ritual and choose Contain/Sever/Black File path.  
- **Comms:** Rogue; Krill via pager/payphone only. Evidence capped.

## Continuity Notes
- 1994 constraints enforced (MicroTAC, Polaroid, paper logs).  
- Phrases equip L/R with Mana; scrolls single‑use.

# SEC-03 — CH5 Narrative Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Avery — D-LAMP Lead
1) **Franklin packet:** Faxed list points to D-LAMP vendor/site.  
2) **Recon + approach:** Night drive; perimeter sweep.  
3) **Inside or stakeout:** Front pretext/service tail vs camera-count + shipment log.  
4) **Findings:** Lab POs, occult-adjacent supplies, phone logs intersect Brightstar.  
5) **Hook:** Fold D-LAMP suppliers into SRS warrants. Flags: `F_DLampLocated`, `F_DLampEntered?`, `F_DLampLead`.

## Clara — Betsy Resolution
**Branch gate:** `BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)`

- **Raid bypass (if ineligible):** Multi-agency serve; quick clear; evidence sweep. Flags: `F_BetsyRaidBypass=1`, `F_BetsyHouseCleared=1`.  
- **Boss fight (if eligible):** **Wendigo Betsy** set piece at the house. Phases: Lunge/Grab → Wall-scramble shrieks → Frenzy. Use **Shield**, **Ward Jam**, furniture shove. Flags: `F_BetsyBossDefeated=1`, `F_BetsyHouseCleared=1`.

## Convergence
- **Motel rendezvous:** Clara + Reddy link with Avery. Packet sync. Set `F_ClaraFollowsAvery=1`.  
- **Forward:** Prepare CH6 warrants (SRS + D-LAMP) and UC brief.

## Evidence
- Raid: itemized seizure list, Polaroid refs.  
- Boss: recovered notes, floor-scratch glyph rubbings.

# SEC-03 — CH5 Narrative (Rework)
Repo dir: /Patches

## Title
NYFO: The Last Call

## Goals
Keep Avery out of custody; secure SRS undercover warrant; set Clara→Betsy guardianship path.

## Beats
1) **Hotel night:** Check-in near NYFO. POI status active.  
2) **NYFO debrief:** Interrogation on Kadath; FieldPad/TAPLINE queue evidence; uploads only at NYFO line.  
3) **Krill hallway:** Raises Avery’s clearance; “buckle up.” Confirms real magic exists beyond Kadath. `F_ClearanceRaised=1`, `F_KrillBriefed=1`.  
4) **Franklin killed (night):** Pager/news. `F_FranklinMurdered=1`.  
5) **Hotel morning raid:** Agents arrive to detain Avery. **Stealth exit** or **non-lethal takedown** path. `F_EscapeHotel=1`.  
6) **Warrant work (day):** Build **OpsOrder_SRS**, **Affidavit_EvidenceIndex**, **Warrant_Safehouse**; sign-offs: NYFO ASAC → USAO SDGA → magistrate. `F_WarrantSRS=1`.  
7) **Clara decision:** Clara travels to **Betsy** to address guardianship for Reddy. `F_ClaraToBetsy=1`, `F_GuardianshipPending=1`.  
8) **Close:** Avery slated for SRS UC brief; Clara departs NYC. Hooks to CH6/CH7.

## Evidence
Debrief summary, Krill memo, MicroTAC call logs, hotel register, warrant packet (ops order, affidavit, warrant), guardianship notes.

## Failure/Branches
- Flee or unreachable during POI window → harsher CH6 start.  
- Excessive force on agents → IA penalties that persist.

## Carryover
Spell phrases remain L/R equipped with Mana; scrolls remain single-use items.

# SEC-03 — CH6 Beat Sheet (Raid)
Repo dir: /Patches

## Scope
Sanctioned raid vs hostile combatants; lethal authorized; blue-on-blue fail. Evidence cap 3.

## Beats
1) **UC Pre-brief (Rogue):** Krill pager check, loadout set (phrases L/R, scrolls).  
2) **Safehouse Sting:** Buy/bust with {DeputyName}; seize ledgers/reagents/maps. `F_SafehouseSting=1`.  
3) **Ingress:** Iron Highway pull-off → SRS Secret Annex bulkhead. `F_SRSBreach=1`.  
4) **Service Passage:** K-9 arcs; analog cams; breaker shortcut.  
5) **Valve Row:** Tag A/B/C with Polaroid for Contain path.  
6) **Dead Piping:** Ritual prep tables; evidence (if cap allows). `F_CoreFound=1`.  
7) **Ritual Ignition:** Space fold; spawn waves. `F_RitualIgnited=1`.  
8) **Path A — Contain:** Jam Wards, cycle valves A→B→C, lock gimbal. `F_End_Contain=1`.  
9) **Path B — Sever:** Plant charges, interrupt chant, detonate, run. `F_End_Escape=1`.  
10) **Path C — Black File:** Photo, sample, bag+tag, exfil late. `F_End_BlackFile=1`.  
11) **Extraction:** Fence gap rendezvous with {DeputyName}; FD-302 queued.

## ROE Banner
- Lethal authorized. No score penalty for neutralizations.  
- Blue-on-blue = −10 and abort. No civilians expected.

## UI prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Crouch, Hide, Dodge, Breach, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

# SEC-03 — CH6 Epilogue
Repo dir: /Patches

## Overview
Final outcomes after the SRS raid. No civilians present. Phrase remains ambient: “the stars are right tonight.”

### Ending A — Contain (Seal)
- **Public face:** minor incident, localized blackout.  
- **Internal:** commendations in sealed annex; Krill message: “not over.”  
- **Hooks:** legal pressure on D‑LAMP vendors; Clara/Reddy low profile.  
- **Slides:** injured saved count; splinter stabilized.

### Ending B — Sever (Escape)
- **Public face:** unexplained anomalies near fence line; whispers.  
- **Internal:** reprimand avoided; Krill prioritizes damage control.  
- **Hooks:** rogue cells scatter; Iron Highway collapse risks.  
- **Slides:** team intact; area warped.

### Ending C — Black File (Evidence-first)
- **Public face:** nothing on record.  
- **Internal:** evidence maximum; reputation hit logged.  
- **Hooks:** secret indictments; Krill warns of fallout.  
- **Slides:** dossiers filled; trust eroded.

## Postcards (optional stingers)
- Clara & Reddy: roadside diner, 3 a.m., pager buzz.  
- Avery: MicroTAC rings from an unknown exchange.  
- Deputy {DeputyName}: radio silence, then a single horn-call on scan.

# SEC-03 §3.4 — Synopsis: Prologues (ADD)

> Scope: add concise prologue synopses under SEC‑03 §3.4. Period‑accurate to 1994 context, with Avery’s prologue set in 1989. Ambient phrase only: “the stars are right tonight.” Keep spoilers minimal; seed mechanics and motifs used later in CH5–CH7.

## Prologue — Avery Jordan (1989)
- **Premise:** Young federal agent observes early indicators of the Order during a routine investigation that escalates into an anomalous event.
- **Beats:**
  1) **Intake:** Bureau paperwork and phone trees establish 1989 workflow. Landlines, pagers, fax. Franklin appears as a respected contact who emphasizes chain‑of‑custody.
  2) **Anomaly:** Equipment behaves erratically near an industrial site; phrase fragments are recovered from suspects. First exposure to a warded space is documented in field notes rather than digital logs.
  3) **Outcome:** Case is closed administratively with unresolved anomalies. Avery keeps a redacted memo and a ritual fragment that later grounds CH6 rules (wards, breakers, cameras). Seeds distrust of convenient narratives.
- **Mechanics seeded:** Phrases equip **L/R**, Scrolls **single‑use**, Mana **calm‑regen**. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Evidence logged by fax and hand‑off.

## Prologue — Clara Winston (1994)
- **Premise:** Field medic‑researcher in a rural setting encounters the Order’s peripheral harm while using period‑accurate tools.
- **Beats:**
  1) **Triage:** MEDSTAT use is demonstrated with cable‑sync or SENTINEL link. FieldPad records analogue samples; consent for photos is documented.
  2) **Interference:** A protective ward complicates first aid; the ambient phrase is overheard from bystanders only as color. Early contact with an unusual childlike presence foreshadows later mind effects without revealing nature.
  3) **Outcome:** Clara extracts, preserves samples, and files a conservative incident note that aligns with 1994 procedures.
- **Mechanics seeded:** Consent/warrant language for photography in private interiors. Non‑lethal preference in populated areas. City evidence cap concept introduced for later (CH7 **2**).

## Cross‑refs
- See **SEC‑05** for snippet IDs introducing wards, breakers (≈90 s), cameras‑only zones, and K‑9 reroute.
- See **SEC‑06** for location rules later mirrored at SRS and in NYC.
- See **SEC‑07** for HUD language and prompt limits (≤14).

## Anchors (create if missing)
- `#synopsis-prologues-add`
- `#prologue-avery-1989`
- `#prologue-clara-1994`

## Integration notes
- Insert this section under SEC‑03 §3.4 with matching heading style.
- Avoid revealing later twists; maintain neutral clinical tone.

## **3.5 Chapter 1 — “Simple Curiosity”** _(ADD this subsection)_
Date: 2025-08-14 23:10:43 UTC
Owner: Nick Goldman

**Year/Locale:** 1994, **Brightstar Daycare (Jackson, SC)** and roadside nearby.  
**POV:** strict in‑character; interleaved **Clara** and **Avery** legs.  
**Devices:** Clara—**MEDSTAT** only; unlocks **Notes** mid‑chapter via **PCMCIA Type II note‑card** (Newton‑compatible; no camera/internet). Avery—analog camera, paper custody, radio.  
**Canon locks:** Pin symbol = SYM‑001 (lore only). No FieldPad/TAPLINE in CH1.

**Clara Beats:** sign‑in → find card → insert → tour; overhear “the stars are right tonight” → light stealth/care → exit plan.  
**Avery Beats:** brief (deputy name **randomized per save**) → challenge → cuff → search → photo → bag/tag/log → locker handoff → debrief.

## **3.2 Chapter List**  _(Replace this entire subsection)_

- **PROLOGUES — Tutorials**  
  - **0A — Avery Jordan (1989, Quantico — Hogan’s Alley):** ROE, challenge→cuff→search, analog custody; range drill; dual‑wield + decoupled aim; no FieldPad.  
  - **0B — Clara Winston (1994, Betsy Lumbar’s Apt):** MEDSTAT vitals and caregiving; Reddy‑POV beat; Clara finds the Brightstar pin; no FieldPad/TAPLINE.

- **01 CHAPTER 1: “SIMPLE CURIOSITY”**  
- **02 CHAPTER 2: “PASSING INTEREST”**  
- **03 CHAPTER 3: “INNOCENT FASCINATION”**  
- **04 CHAPTER 4: “UNDYING OBSESSION”**  
- **05 CHAPTER 5: “RENEWED PURPOSE”**  
- **06 CHAPTER 6: “GLORIOUS QUEST”**

_Canon locks:_ Location/Name = **Brightstar Daycare, Jackson, SC**. Possession = **event‑driven**; day/night adjusts spawns only. POV = **strict in‑character**; Clara Prologue uses **Reddy‑POV** for face/knife beat.

# MANIFEST addendum — SEC-03 CH1 synopsis
Date: 2025-08-14 22:50:08 UTC

Section: SEC-03-NARRATIVE
Change:
- Add §3.5 “Chapter 1 — Simple Curiosity” using `Patches/SEC-03_3.5_CH1_SimpleCuriosity_ADD.md`.

Version bump:
- SEC-03 minor +1

Cross-refs:
- Trackers/CH1_Outline_SimpleCuriosity.md
- Trackers/CH1_Beat2Objective.md
- Trackers/AssetList_CH1_Brightstar.md
- Trackers/QATelemetry_CH1.md

# MANIFEST addendum — SEC-03 Prologues integration
Date: 2025-08-14T11:24Z

Section: SEC-03-NARRATIVE
Change:
- Replace §3.2 Chapter List with `Patches/SEC-03_3.2_Chapter_List_REPLACE.md`.
- Prepend §3.4 with `Patches/SEC-03_3.4_Synopsis_Prologues_ADD.md` (already in Patches).

Version bump:
- Previous: vX.Y  →  New: vX.(Y+1)  (minor bump)

Cross-refs:
- Trackers/NARR-TRACKER_Prologues_v0.3.md
- Trackers/NARR-TRACKER_Playbook-Outline_Sync_v0.1.md
- Trackers/Prop_SEC-04_Loops_Prologues.md
- Trackers/Prop_SEC-05_Systems_ProloguesFlags.md
- Trackers/Prop_TDD_Evidence_FieldPad_ProloguesHooks.md

QA/Telemetry:
- Ensure events in Trackers/QATelemetry_* are referenced in SEC-11/14.

# [SEC-03] Chapter 5 — Renewed Purpose (Narrative Paste)

> Source of truth: Narrative Playbook • Outline 2025. Period: 1994. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Ambient phrase only: “the stars are right tonight.”

## Scope
- Protagonists: Avery (primary), Clara (secondary thread).
- Setting: New York City and surrounding tri‑state travel hub. Avery’s car acts as a mobile base.
- Structure: Open‑world hub unlock + parallel Clara beat.

## Avery Beats
- Returns to NYC with Clara and Reddy; learns Fred Franklin has been murdered and is framed as a suspect.
- Chooses to operate off‑book while clearing his name. Contacts use landlines, pagers, fax. Evidence is walked to drop sites.
- World opens with **Federally Seized** variants of past locations. New enemy mixes appear only in seized sites.
- Day/Night cycle alters spawns and civilians:
  - Day: mind‑swapped civilians in public spaces; crowd‑control favored. Friendly hits fail states.
  - Night: ghosts and abominations increase; patrol density reduced.
- Vehicle loop: plan at trunk loadout, drive to site, park legally or risk tow, approach on foot. No GPS; rely on printed maps and signage.

## Clara Beats
- Tracks Betsy Lumbar and confirms allegiance to **Qin Xu Qi**.
- Boss branch:
  - If player found **Cultist Literature** in Prologue: Suzanne Cutlass intercepts; arrest sequence replaces fight.
  - Else: Betsy transforms into a **wendigo**; combat boss with environmental hazards.

## Systems Hooks
- FieldPad/MEDSTAT are cable‑synced or SENTINEL‑linked only; no internet.
- Spells: **Phrases equip L/R**, **Scrolls single‑use**, **Mana calm‑regen** (no combat regen spike).
- Deputy name must be randomized per session. Use placeholder `<DEPUTY_NAME>` in text.
- Only ambient phrase permitted globally: “the stars are right tonight.”

## Fail/State Rules
- City friendly/civilian hits = fail.
- Maintain 1994 authenticity in UI prompts, signage, and comms.
- Persist clues that set up Chapter 6 objectives without revealing SRS details.

## Deliverables in SEC‑03
- Replace CH5 narrative with this paste.
- Preserve anchors used by SEC‑05/06/07 cross‑refs.

# [SEC-03] Chapter 6 — Glorious Quest (Narrative Paste)

> Source of truth: Narrative Playbook • Outline 2025. Period: 1994. Ambient phrase only: “the stars are right tonight.”

## Scope
- Dual path operation against **Richard Tack** culminating at the **Savannah River Site (SRS)** with interlocks to **D‑LAMP (WV)**.
- Player alternates between locations via open‑world travel unlocked in CH5.
- New enemy type: **Mystical Heads**; spawn in distorted reactor chambers.

## Core Objective
Disable the **Transdimensional Complex Device** before Tack triggers cross‑dimensional brainwashing; overload leads to timed escape through collapsing, reality‑warped corridors.

## Path Structure
- **Clara — Stealth/Infiltration**
  - Goals: disable security systems, avoid detection by cultists and possessed security personnel.
  - Tools: ward jamming, valves, plant/detonate charges, photo/sample evidence.
- **Avery — Assault/Fireteam**
  - Goals: clear hostile forces, disable protective wards, cover Clara’s objectives.
  - Tools: cast/equip phrases, breaching, K‑9 reroute triggers, valve operations.

## Raid Rules (live in helpers)
- **CH6 = raid. Lethal authorized.** Neutralizations are **score‑neutral**.
- **Blue‑on‑Blue = hard fail (−10).** Exceptions:
  - **Shield‑absorbed** friendly hit.
  - A **single shotgun pellet** striking a friendly from **>10 m**.
- **Evidence cap in CH6 = 3 total.** HUD must show `Evidence 0/3` and `BlueOnBlue` flag.
- **Cameras only** in **Service Passage**. **No CCTV in Vault**.
- **Breaker ≈90 s** to cycle after trip. **K‑9 reroute** available via handler diversion or scent decoy.

## 1994 Constraints
- No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Navigation via printed maps, posted site diagrams, radio freqs.
- Comms over analog radios; logging on paper, Polaroids, and film camera; lab hand‑offs by courier.

## Spell/Item System
- **Phrases equip L/R**; **Scrolls single‑use**; **Mana calm‑regen**.
- Only ambient phrase in VO/text: “the stars are right tonight.”
- Deputy name randomized per session. Use `<DEPUTY_NAME>` placeholder where referenced.

## Evidence & Cameras
- Max three pieces of evidence total in CH6. Choice tension: tactical vs investigative.
- Photographic evidence is permitted in **Service Passage** where cameras exist.
- No photography in Vault due to zero CCTV and radiation protocols; rely on samples/logs.

## Deliverables in SEC‑03
- Replace CH6 narrative with this paste.
- Ensure cross‑refs to SEC‑05/06/07 remain intact.

# [SEC-03] Chapter 7 — Aftermath & Apparitions (Narrative Paste)

> Sources: Narrative Playbook • Outline 2025. Period: 1994. Ambient phrase only: “the stars are right tonight.”

## Scope
- Locale: New York City and nearby boroughs after SRS fallout.
- Frame on Avery for the Franklin murder is lifted; public trust remains low.
- Antagonist: **Krill** (Hauser’s successor). Modus: mind control, illusions, psychic bleed.
- Encounter arc: street-level investigations → mind-hazards → **Mindscape** confrontation hook.
- City evidence cap = **2**. Non‑lethal favored. Friendly/civilian hits = **fail**.

## Systems Constraints
- 1994 authenticity: landlines, pagers, fax, payphones, film, Polaroid. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS.
- FieldPad/MEDSTAT: cable sync or SENTINEL link only.
- Spells: **Phrases equip L/R**, **Scrolls single‑use**, **Mana calm‑regen**.
- Deputy identity randomized per session. Use `<DEPUTY_NAME>` token in text.
- Only ambient phrase allowed globally: “the stars are right tonight.”

## Avery Thread
- Goal: unwind remaining cover‑up, locate Krill’s control nodes, clear public narrative without breaking FBI rules.
- Play: surveillance on payphones and safehouses; interviews with mind‑swapped civilians; forensic drops at precincts.
- Mechanics:
  - **Non‑lethal priority**: tasers/batons; firearm discharge near civilians triggers fail.
  - **Evidence cap 2**: city HUD shows `Evidence 0/2` during Avery segments.
  - **Illusion checks**: compare FieldPad sensor drift vs. MEDSTAT samples to expose false cues.

## Clara Thread
- Goal: protect witnesses targeted by Krill’s proxies; gather ritual counter‑phrases; trace EM anomalies.
- Play: escort routes, decoy tactics, controlled reveals of **Reddy** to startle cult footmen.
- Mechanics:
  - **Calm‑regen** pacing; scroll scarcity; phrase loadout puzzle for **Mindscape** entry.
  - Cameras limited to public spaces; consent needed for photo evidence in private interiors.

## Mindscape Hook (Boss Setup)
- Trigger: complete both protagonists’ node objectives; locate Krill’s anchor object (artifact or sigil series).
- Environment: fractured NYC landmarks; visual glitches, doubled NPCs; sound desync.
- Boss: **Krill** deploys illusions that copy friendly silhouettes to bait Blue‑on‑Blue; city rules still apply.
- Outcome: defeat forces Krill to retreat; leaves a **Krill_Remnant** flag for Epilogue routing.

## Fail/State Rules
- Any friendly/civilian hit = immediate fail in city scenes.
- Evidence beyond 2 is denied with “Evidence full.”
- Public panic escalations persist into Epilogue scoring if siren thresholds are exceeded.

## Deliverables in SEC‑03
- Replace CH7 narrative section with this paste.
- Preserve anchors used by SEC‑06/07 for UI and world references.

# SEC-03 — Narrative CH5–CH6 Merge (Entry Point)
Repo dir: /Patches

Use this file as the **entry point** when opening the PR. It references the split paste blocks (kept separate for clarity).

## Paste order
1) Replace `## CH5` with the contents of:
   - `/Patches/ROOT_SEC-03_CH5_Narrative_Paste.md`
2) Replace `## CH6` with the contents of:
   - `/Patches/ROOT_SEC-03_CH6_Narrative_Paste.md`

## Post‑paste checks
- CH6 states the raid ROE, lethal authorized, **Blue‑on‑Blue = fail**.
- Evidence cap **3** is present.
- 1994 lock maintained; **MicroTAC/pagers/payphones/Polaroids/analog CCTV** only.
- Ambient phrase appears only as ambient text: “the stars are right tonight.”
- Deputy name randomized.

## Note
We keep CH5 and CH6 as two paste files to reduce conflicts and ease review. This entry file exists to satisfy the PR body pointer.

## CH2 — Avery: Inner Checkpoint

### Goal
Infiltrate the Jackson, SC compound. Pass the inner gate. Detain a leader. Secure evidence. Avoid civilian harm.

### Setting
Barn and backlot compound outside Jackson, South Carolina. Night.

### Cast
Avery Jordan. ASAC Franklin. SA Lewis Krill. Aiken Co. Deputy {DeputyName}. Gate guard. Deacon analogue. Civilians.

### 1994 kit
SIG P226 or S&W 13. Limited magazines. Paper maps. Polaroid. Payphone. Fax. Teletype. No weapon lights.

### Beats
1) Briefing. Passphrase issued: "the stars are right tonight." ROE emphasized.  
2) Recon. Guard rotations logged. Civilians identified. Inner gate protocol observed.  
3) Approach. Use cover or distraction. Optional payphone to SO for timing.  
4) Inner gate. Respond with exact passphrase. One Badge plus Warrant bluff retry. Second failure sets Alert High.  
5) Search. Outbuilding A cash ledger and rosters. Shed B generator. Office shack tapes and logbook.  
6) Detain. Non-lethal takedown of Deacon analogue. Secure .38.  
7) Chain of custody. Bag and tag. Complete FD-302. Fax to field office. Send teletype BOLOs. Coordinate bookings with {DeputyName}.  
8) Exfil. Save F_GromleyCleared=1. Hook to Clara via deputy remark about the trail.

### ROE note
If an NPC initiates lethal force then a player lethal response in that encounter is score neutral.

### Failure and branches
Wrong passphrase twice sets Alert High. Civilian endangered reduces score. Excessive force reduces score unless NPC initiated lethal force first.

### Prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

## CH2 — Clara: Kadath Survival

### Goal
Survive, feed Reddy, attempt escape, alert parents to collect children.

### Setting
Kadath forest beyond “Pine Break” portal behind Brightstar. Brightstar interior is liminal and scrambled except anchors.

### Cast
Clara Winston; Reddy; wardens; staff; distant children.

### 1994 Kit
Maglite, Polaroid, twine, chalk, matches, microcassette recorder, paper map, canteen, iodine, first-aid. MEDSTAT note-card (text only; intermittent SENTINEL).

### Beats
1) **Bivouac:** Learn portal at Pine Break. Forage. Set chalk mark.  
2) **Water run:** Culvert found. Boil or iodine → `WaterSafe`.  
3) **Loop demo:** Trails A–D loop. Chalk fades past 30 m from Brightstar.  
4) **Stash Reddy:** Use nearest Safe Nest (Bivouac/Bus/Locker). Carry = +noise, −stealth.  
5) **Infiltration I — Kitchen:** Food, can opener, canteen → `FoodSecured`.  
6) **Infiltration II — Nurse:** Iodine, gauze, D-cells; unlock Nurse Locker Safe Nest.  
7) **Office break-in:** Emergency Contact ledger + attendance log. Transcribe to MEDSTAT.  
8) **Parent calls:** Use landline. Call Intercept meter visible while connected; hang up to avoid intercept.  
9) **Brightstar Brawl (mandatory):** Multipurpose room fight. Non-lethal favored. Loot Master Keys, Admin map, Medkit → `F_BrawlWon=1`, `F_MasterKeys=1`.  
10) **Admin sweep:** Roster, delivery slips. Record vent whisper “the stars are right tonight.” Playback opens one warded cabinet.  
11) **Backtrack:** Return via portal. Feed Reddy. Manage meters.  
12) **Exit test:** Even with `FoodSecured & WaterSafe & ParentsConfirmed≥NMin`, outer trail collapses. Chapter wall holds.

### Failure/Branches
- Cry ping while carrying Reddy draws sweep.  
- Intercept at 100 cancels call and raises Alert.  
- Brawl defeat or Reddy harmed → soft reset to pre-call checkpoint; inventory kept; +Alert on retry.

### Evidence Log (text only)
Emergency ledger pages, attendance, roster, delivery slips, phrase notes, loop map, breaker/anchor notes.

### Scoring
See Patch file. Non-lethal and SafeCall bonuses prioritized.

### Prompts (≤14 chars)
Hush, Hide, Crouch, Throw, Listen, Use, Inspect, Pick Up, Forage, Gather, Boil, Purify, Eat, Drink, Rest, Soothe, Record, Play, Dial, Call Parent, Note, Map, Open, Unlock, Carry, Stash, Retrieve, Block, Dodge, Shove, Grapple, Swing, Spray, Trip, Sand, Lights, Wedge

# SEC-03 — CH3 Narrative Sections (Consolidated)

## CH3 — Clara & Reddy: “Innocent Fascination”
**Goal:** Survive Kadath, protect Reddy, repel scavengers without lethal force.  
**Setting:** Kadath forest near warped Brightstar (Jackson, SC). Time dilation persists.  
**Beats:**
1) Forage & trace a scavenger trail.  
2) Ambush springs; Clara shields Reddy.  
3) Swap to **Reddy Playable** telekinesis (infinite energy this chapter).  
4) Crowd control with non-lethal TK: pin, stack, block.  
5) Ethics check: wanton destruction reduces score.  
6) Clara collapses from concussion; Reddy powers down and returns to her side.  
7) Audio hook from Brightstar interior sets up convergence.

**Evidence:** Trail notes, delivery slips, ledger snapshots.  
**Phrase:** Ambient only: “the stars are right tonight.”  
**Failure/Retry:** Clara downed → Reddy rescue window; timer fail → soft reset; inventory persists.

## CH3 — Avery: “Suspension & Daycare Haunting”
**Goal:** Investigate condemned Brightstar while suspended; survive spectral threat; get forced into Kadath.  
**Setting:** Condemned Brightstar interior → Kadath threshold. Night.  
**Beats:**
1) Suspension notice from Franklin; fallout from Phillips.  
2) Solo return to condemned daycare.  
3) Spectral hunt; retrieve key evidence.  
4) Unwinnable fight; chase through threshold into Kadath.  
5) Rescue by Clara & Reddy; time-skew exchange.  
6) Save team-up flag for Chapter 4.

**Systems:** Spectral-Phased Muzzle Brake consumable enables limited damage; otherwise avoidance.  
**Evidence:** Condemnation copy, key ring, gate log fragment.  
**ROE:** Lethal allowed on spectral; civilian harm penalized.  
**Phrase:** Ambient only.

## Interlock & Continuity
- Jackson, SC continuity for Brightstar.  
- Time dilation acknowledged at rescue.  
- No dialogue use of the phrase in CH3.

# SEC-03 — CH4 Narrative (Revised)

## Title
Toward the Walled City

## Goal
Escape Kadath by reaching the Walled City; secure temporary refuge.

## Setting
Kadath forest near Brightstar’s Pine Break → hostile outskirts → South Gate of the Walled City (Kadath of Nyarlathotep inspiration). Night-dusk cycle.

## Cast
Clara Winston; Reddy; SA Avery Jordan; Outskirt Scavengers; Wall Wardens; slain Beast (on entry).

## Beats
1) **Pine Break kill:** Beast chases Avery. Reddy unleashes one telekinetic **Burst** and kills it.  
2) **Meet & align:** Clara, Reddy, Avery align. Clara confirms days of failed exit attempts via Brightstar and Pine Break.  
3) **Systems down:** Avery’s FieldPad and **TAPLINE** cannot connect to **SENTINEL**; devices run **offline** and store evidence locally only.  
4) **Recon ridge:** City spotted with binoculars. Decision to approach despite hostile outskirts.  
5) **Prep & pack:** Water safe, food packed, safe nest marked.  
6) **Traverse outskirts:** Stealth through hostile territory; optional barter. Whispered phrase present as ambient only.  
7) **Skirmish to ditch:** Brief chase; reach cover within bowshot of the South Gate.  
8) **Gate standoff:** Wardens watch; horn-call. No entry yet. Camp outside. Plan parley next.

## Failure/Branches
- Alert escalates during traverse → bigger skirmish and lower end score.  
- Injury without camp → fatigue penalties at start of next chapter.

## Evidence Log
Gate silhouettes, horn-call pattern, wall measurements, scavenger signs, SENTINEL/TAPLINE offline notes.

## Carryover Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-03 — CH5→CH6 Narrative Insert: Deep D‑LAMP & Iron Highway
Repo dir: /Patches

## CH5 Insert — Descent and Drive
- **WV River Island Shaft:** Avery locates the disguised elevator kiosk; descends ~1 mile to the abandoned D‑LAMP deep site.  
- **Abandoned Complex:** AEC→DOE exit paperwork, 1980s–1990s cult occupation, undead outbreaks.  
- **Mini‑Boss:** Star Vampire in Pump Cavern; victory grants Route Control Key.  
- **Rover Bay:** Acquire D‑LAMP utility rover; signage for **Iron Highway**.  
- **Iron Highway:** Drive the tunnel road toward **SRS Secret Annex**; zombies/night gaunts/cultists as encounters.  
- **Seal Gate:** Stop at Annex bulkhead. Flag handoff to CH6.

## CH6 Insert — SRS Secret Annex Entry
- **Ingress:** From Iron Highway pull‑off to man‑door; enter Core Galleries.  
- **Objective:** Reach Splinter Vault pre‑ritual and choose Contain/Sever/Black File path.  
- **Comms:** Rogue; Krill via pager/payphone only. Evidence capped.

## Continuity Notes
- 1994 constraints enforced (MicroTAC, Polaroid, paper logs).  
- Phrases equip L/R with Mana; scrolls single‑use.

# SEC-03 — CH5 Narrative Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Avery — D-LAMP Lead
1) **Franklin packet:** Faxed list points to D-LAMP vendor/site.  
2) **Recon + approach:** Night drive; perimeter sweep.  
3) **Inside or stakeout:** Front pretext/service tail vs camera-count + shipment log.  
4) **Findings:** Lab POs, occult-adjacent supplies, phone logs intersect Brightstar.  
5) **Hook:** Fold D-LAMP suppliers into SRS warrants. Flags: `F_DLampLocated`, `F_DLampEntered?`, `F_DLampLead`.

## Clara — Betsy Resolution
**Branch gate:** `BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)`

- **Raid bypass (if ineligible):** Multi-agency serve; quick clear; evidence sweep. Flags: `F_BetsyRaidBypass=1`, `F_BetsyHouseCleared=1`.  
- **Boss fight (if eligible):** **Wendigo Betsy** set piece at the house. Phases: Lunge/Grab → Wall-scramble shrieks → Frenzy. Use **Shield**, **Ward Jam**, furniture shove. Flags: `F_BetsyBossDefeated=1`, `F_BetsyHouseCleared=1`.

## Convergence
- **Motel rendezvous:** Clara + Reddy link with Avery. Packet sync. Set `F_ClaraFollowsAvery=1`.  
- **Forward:** Prepare CH6 warrants (SRS + D-LAMP) and UC brief.

## Evidence
- Raid: itemized seizure list, Polaroid refs.  
- Boss: recovered notes, floor-scratch glyph rubbings.

# SEC-03 — CH5 Narrative (Rework)
Repo dir: /Patches

## Title
NYFO: The Last Call

## Goals
Keep Avery out of custody; secure SRS undercover warrant; set Clara→Betsy guardianship path.

## Beats
1) **Hotel night:** Check-in near NYFO. POI status active.  
2) **NYFO debrief:** Interrogation on Kadath; FieldPad/TAPLINE queue evidence; uploads only at NYFO line.  
3) **Krill hallway:** Raises Avery’s clearance; “buckle up.” Confirms real magic exists beyond Kadath. `F_ClearanceRaised=1`, `F_KrillBriefed=1`.  
4) **Franklin killed (night):** Pager/news. `F_FranklinMurdered=1`.  
5) **Hotel morning raid:** Agents arrive to detain Avery. **Stealth exit** or **non-lethal takedown** path. `F_EscapeHotel=1`.  
6) **Warrant work (day):** Build **OpsOrder_SRS**, **Affidavit_EvidenceIndex**, **Warrant_Safehouse**; sign-offs: NYFO ASAC → USAO SDGA → magistrate. `F_WarrantSRS=1`.  
7) **Clara decision:** Clara travels to **Betsy** to address guardianship for Reddy. `F_ClaraToBetsy=1`, `F_GuardianshipPending=1`.  
8) **Close:** Avery slated for SRS UC brief; Clara departs NYC. Hooks to CH6/CH7.

## Evidence
Debrief summary, Krill memo, MicroTAC call logs, hotel register, warrant packet (ops order, affidavit, warrant), guardianship notes.

## Failure/Branches
- Flee or unreachable during POI window → harsher CH6 start.  
- Excessive force on agents → IA penalties that persist.

## Carryover
Spell phrases remain L/R equipped with Mana; scrolls remain single-use items.

# SEC-03 — CH6 Beat Sheet (Raid)
Repo dir: /Patches

## Scope
Sanctioned raid vs hostile combatants; lethal authorized; blue-on-blue fail. Evidence cap 3.

## Beats
1) **UC Pre-brief (Rogue):** Krill pager check, loadout set (phrases L/R, scrolls).  
2) **Safehouse Sting:** Buy/bust with {DeputyName}; seize ledgers/reagents/maps. `F_SafehouseSting=1`.  
3) **Ingress:** Iron Highway pull-off → SRS Secret Annex bulkhead. `F_SRSBreach=1`.  
4) **Service Passage:** K-9 arcs; analog cams; breaker shortcut.  
5) **Valve Row:** Tag A/B/C with Polaroid for Contain path.  
6) **Dead Piping:** Ritual prep tables; evidence (if cap allows). `F_CoreFound=1`.  
7) **Ritual Ignition:** Space fold; spawn waves. `F_RitualIgnited=1`.  
8) **Path A — Contain:** Jam Wards, cycle valves A→B→C, lock gimbal. `F_End_Contain=1`.  
9) **Path B — Sever:** Plant charges, interrupt chant, detonate, run. `F_End_Escape=1`.  
10) **Path C — Black File:** Photo, sample, bag+tag, exfil late. `F_End_BlackFile=1`.  
11) **Extraction:** Fence gap rendezvous with {DeputyName}; FD-302 queued.

## ROE Banner
- Lethal authorized. No score penalty for neutralizations.  
- Blue-on-blue = −10 and abort. No civilians expected.

## UI prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Crouch, Hide, Dodge, Breach, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

# SEC-03 — CH6 Epilogue
Repo dir: /Patches

## Overview
Final outcomes after the SRS raid. No civilians present. Phrase remains ambient: “the stars are right tonight.”

### Ending A — Contain (Seal)
- **Public face:** minor incident, localized blackout.  
- **Internal:** commendations in sealed annex; Krill message: “not over.”  
- **Hooks:** legal pressure on D‑LAMP vendors; Clara/Reddy low profile.  
- **Slides:** injured saved count; splinter stabilized.

### Ending B — Sever (Escape)
- **Public face:** unexplained anomalies near fence line; whispers.  
- **Internal:** reprimand avoided; Krill prioritizes damage control.  
- **Hooks:** rogue cells scatter; Iron Highway collapse risks.  
- **Slides:** team intact; area warped.

### Ending C — Black File (Evidence-first)
- **Public face:** nothing on record.  
- **Internal:** evidence maximum; reputation hit logged.  
- **Hooks:** secret indictments; Krill warns of fallout.  
- **Slides:** dossiers filled; trust eroded.

## Postcards (optional stingers)
- Clara & Reddy: roadside diner, 3 a.m., pager buzz.  
- Avery: MicroTAC rings from an unknown exchange.  
- Deputy {DeputyName}: radio silence, then a single horn-call on scan.

# SEC-03 §3.4 — Synopsis: Prologues (ADD)

> Scope: add concise prologue synopses under SEC‑03 §3.4. Period‑accurate to 1994 context, with Avery’s prologue set in 1989. Ambient phrase only: “the stars are right tonight.” Keep spoilers minimal; seed mechanics and motifs used later in CH5–CH7.

## Prologue — Avery Jordan (1989)
- **Premise:** Young federal agent observes early indicators of the Order during a routine investigation that escalates into an anomalous event.
- **Beats:**
  1) **Intake:** Bureau paperwork and phone trees establish 1989 workflow. Landlines, pagers, fax. Franklin appears as a respected contact who emphasizes chain‑of‑custody.
  2) **Anomaly:** Equipment behaves erratically near an industrial site; phrase fragments are recovered from suspects. First exposure to a warded space is documented in field notes rather than digital logs.
  3) **Outcome:** Case is closed administratively with unresolved anomalies. Avery keeps a redacted memo and a ritual fragment that later grounds CH6 rules (wards, breakers, cameras). Seeds distrust of convenient narratives.
- **Mechanics seeded:** Phrases equip **L/R**, Scrolls **single‑use**, Mana **calm‑regen**. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS. Evidence logged by fax and hand‑off.

## Prologue — Clara Winston (1994)
- **Premise:** Field medic‑researcher in a rural setting encounters the Order’s peripheral harm while using period‑accurate tools.
- **Beats:**
  1) **Triage:** MEDSTAT use is demonstrated with cable‑sync or SENTINEL link. FieldPad records analogue samples; consent for photos is documented.
  2) **Interference:** A protective ward complicates first aid; the ambient phrase is overheard from bystanders only as color. Early contact with an unusual childlike presence foreshadows later mind effects without revealing nature.
  3) **Outcome:** Clara extracts, preserves samples, and files a conservative incident note that aligns with 1994 procedures.
- **Mechanics seeded:** Consent/warrant language for photography in private interiors. Non‑lethal preference in populated areas. City evidence cap concept introduced for later (CH7 **2**).

## Cross‑refs
- See **SEC‑05** for snippet IDs introducing wards, breakers (≈90 s), cameras‑only zones, and K‑9 reroute.
- See **SEC‑06** for location rules later mirrored at SRS and in NYC.
- See **SEC‑07** for HUD language and prompt limits (≤14).

## Anchors (create if missing)
- `#synopsis-prologues-add`
- `#prologue-avery-1989`
- `#prologue-clara-1994`

## Integration notes
- Insert this section under SEC‑03 §3.4 with matching heading style.
- Avoid revealing later twists; maintain neutral clinical tone.

## **3.5 Chapter 1 — “Simple Curiosity”** _(ADD this subsection)_
Date: 2025-08-14 23:10:43 UTC
Owner: Nick Goldman

**Year/Locale:** 1994, **Brightstar Daycare (Jackson, SC)** and roadside nearby.  
**POV:** strict in‑character; interleaved **Clara** and **Avery** legs.  
**Devices:** Clara—**MEDSTAT** only; unlocks **Notes** mid‑chapter via **PCMCIA Type II note‑card** (Newton‑compatible; no camera/internet). Avery—analog camera, paper custody, radio.  
**Canon locks:** Pin symbol = SYM‑001 (lore only). No FieldPad/TAPLINE in CH1.

**Clara Beats:** sign‑in → find card → insert → tour; overhear “the stars are right tonight” → light stealth/care → exit plan.  
**Avery Beats:** brief (deputy name **randomized per save**) → challenge → cuff → search → photo → bag/tag/log → locker handoff → debrief.

## **3.2 Chapter List**  _(Replace this entire subsection)_

- **PROLOGUES — Tutorials**  
  - **0A — Avery Jordan (1989, Quantico — Hogan’s Alley):** ROE, challenge→cuff→search, analog custody; range drill; dual‑wield + decoupled aim; no FieldPad.  
  - **0B — Clara Winston (1994, Betsy Lumbar’s Apt):** MEDSTAT vitals and caregiving; Reddy‑POV beat; Clara finds the Brightstar pin; no FieldPad/TAPLINE.

- **01 CHAPTER 1: “SIMPLE CURIOSITY”**  
- **02 CHAPTER 2: “PASSING INTEREST”**  
- **03 CHAPTER 3: “INNOCENT FASCINATION”**  
- **04 CHAPTER 4: “UNDYING OBSESSION”**  
- **05 CHAPTER 5: “RENEWED PURPOSE”**  
- **06 CHAPTER 6: “GLORIOUS QUEST”**

_Canon locks:_ Location/Name = **Brightstar Daycare, Jackson, SC**. Possession = **event‑driven**; day/night adjusts spawns only. POV = **strict in‑character**; Clara Prologue uses **Reddy‑POV** for face/knife beat.

## **3.2 Chapter List**  _(Replace this entire subsection)_

- **PROLOGUES — Tutorials**  
  - **0A — Avery Jordan (1989, Quantico — Hogan’s Alley):** ROE, challenge→cuff→search, analog custody; range drill; dual‑wield + decoupled aim; no FieldPad.  
  - **0B — Clara Winston (1994, Betsy Lumbar’s Apt):** MEDSTAT vitals and caregiving; Reddy‑POV beat; Clara finds the Brightstar pin; no FieldPad/TAPLINE.

- **01 CHAPTER 1: “SIMPLE CURIOSITY”**  
- **02 CHAPTER 2: “PASSING INTEREST”**  
- **03 CHAPTER 3: “INNOCENT FASCINATION”**  
- **04 CHAPTER 4: “UNDYING OBSESSION”**  
- **05 CHAPTER 5: “RENEWED PURPOSE”**  
- **06 CHAPTER 6: “GLORIOUS QUEST”**

_Canon locks:_ Location/Name = **Brightstar Daycare, Jackson, SC**. Possession = **event‑driven**; day/night adjusts spawns only. POV = **strict in‑character**; Clara Prologue uses **Reddy‑POV** for face/knife beat.

# [SEC-04-LOOPS] Core Gameplay Loops
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-01-FRONT` — Front Matter & Executive Summary
- `SEC-03-NARRATIVE` — Narrative
- `SEC-05-SYSTEMS` — Systems & Mechanics
- `SEC-06-WORLD` — World, Levels, & Content

## **4.1 Overview**

Loops connect investigation, stealth/combat, and narrative progression. Avery \= procedural agency within ROE. Clara \= survival agency under scarcity. Both feed the shared world state and ending matrix.

## **4.2 Moment‑to‑Moment Loop**

Primary verbs: observe, collect, infer, act, record, move.

[Observe] → [Collect Evidence] → [Evaluate Risk] → [Act (Stealth/Combat/Dialogue)]

         ↘                                          ↗

           [Record in FieldPad] ← [Update World/AI State] ← [Relocate]

**Guardrails**

* Evidence first. Action without intel raises risk and cost.

* Devices are the UI. Non‑diegetic assists stay minimal.

**Success Criteria**

* Player logs evidence in ≥80% of missions before major actions.

## **4.3 Mission Loop (POV‑specific)**

**Avery (FBI)**

[Brief/Case Intake] → [Legal Prep (warrant/ROE)] → [Travel/Loadout]

      → [Recon] → {Branch: Infiltrate | Knock/Breach} → [Secure/Arrest]

      → [Scene Processing] → [Debrief/Casefile]

**Clara (Survival)**

[Immediate Need (Protect Reddy)] → [Scavenge/Route Plan] → [Infiltrate/Bypass]

      → [Avoid/Disable Threat] → [Extract] → [Recuperate/Journal]

**Checkpoints**

* Autosave at **Brief**, **Branch**, **Outcome**. Manual save outside combat.

## **4.4 Meta‑Progression**

* **Caseboard (shared):** pins, threads, suspects; reflects cross‑POV state.

* **Devices:** apps unlock by story beats; upgrades change verbs (ex: TAPLINE → passive scan → targeted decode).

* **Skills:** separate tracks; no shared XP. Avery favors procedure/tactics. Clara favors stealth/improvisation.

* **Reputation/Heat:** systemic response to arrests, kills, noise.

## **4.5 Evidence System**

* **Tiers:** A (forensic), B (eyewitness/analysis), C (circumstantial).

* **Quality score:** affects dialog gates, warrant success, and combat modifiers.

* **Chain of custody (Avery):** must bag, tag, and log. Breaks invalidate A‑tier gates.

* **Reddy care (Clara):** stress and noise modify encounter density.

* Outcomes write to the **Consequences Matrix** used by Epilogue.

## **4.6 Stealth & Combat Loops**

**Stealth**

[Shadow/Noise Mgmt] → [Intel Peek] → [Path/Create Distraction] → [Bypass/Isolate]

        ↖——————————————————————[Break LOS]/[Hide]———————————————————————↗

**Avery Combat**: cover, decoupled aiming, arrests \> lethal. Suppression and team calls supported by MEDSTAT.  
 **Clara Combat**: last resort. Limited firearms, improvised traps, sprint windows. Fewer bullets, more routes.

## **4.7 Failure & Recovery**

* **Soft fail:** blown stealth raises heat and spawns reinforcements; fallback to escape routes.

* **Hard fail:** incapacitation → checkpoint reload; injury debuffs persist until treated in MEDSTAT.

* **Case fail‑forward:** poor evidence locks some branches but preserves continuity; alternate endings remain reachable.

## **4.8 Difficulty & Pacing**

* **Dynamic pressure:** AI alertness and patrol density scale with noise/heat.

* **Assist options:** aim assist, slower clue timers, enhanced device hints.

* **Encounter budgets:** readable silhouettes, limited simultaneous threats.

## **4.9 UI Touchpoints (Devices)**

* **FieldPad:** capture photos, tag, annotate, chain‑of‑custody, caseboard.

* **TAPLINE:** scan bands, log intercepts, decode, triangulate.

* **MEDSTAT:** health states, status effects, team telemetry, triage.

## **4.10 Telemetry Targets (for tuning)**

* Evidence logged before breach ≥70%.

* Arrest:kill ratio for Avery ≥2:1 in mid‑game.

* Clara stealth resolution rate ≥60%.

* Average mission length 25–40 min on Standard.

## **4.11 Content Hooks (Templates)**

* **Recon → Infiltrate → Extract**

* **Stakeout → Warrant → Breach**

* **Escort/Protect (Reddy) → Diversion → Evade**

## **4.12 Accessibility Notes**

* Color‑blind safe palettes in device UIs.

* Subtitles by default.

* Remappable inputs.

* Toggle for reduced camera shake and flashing.

## **4.13 Deliverables**

* Loop diagrams (final art).

* Caseboard schema and save‑state spec.

* KPI dashboard definitions.

## **4.14 Approvals**

On approval: archive to MASTER as `[SEC-04-LOOPS] v0.1` and update manifest. Next section: **SEC‑05 Systems & Mechanics**.

# **Patch Instructions for Existing MASTER — SEC-05**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-05-SYSTEMS |` and replace the entire line with:

`| SEC-05-SYSTEMS | Systems and mechanics | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# [SEC-05-SYSTEMS] Systems & Mechanics
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-03-NARRATIVE` — Narrative
- `SEC-04-LOOPS` — Core Gameplay Loops
- `SEC-06-WORLD` — World, Levels, & Content
- `SEC-07-UI` — UI/UX (Devices, HUD, Menus)

## **5.1 Systems Overview**

This section defines player-facing mechanics, underlying rules, tunables, and AI behaviors. It connects to SEC‑04 Loops, SEC‑07 UI, and SEC‑03 Narrative.

**POV deltas**

* **Avery (FBI):** procedure‑gated access, arrests preferred, team telemetry via **MEDSTAT**, legal gates via **FieldPad** casework and **TAPLINE** warrants.

* **Clara (Civilian):** scarcity, improvisation, escort care for Reddy, analog friction, stealth bias.

## **5.2 Player State Model**

| Track | Range | Notes |
| ----- | ----- | ----- |
| Health (HP) | 0–100 | Global. Below 25 triggers **Critical**. |
| Blood Loss | 0–3 | Per‑limb; stacks cause **Bleeding** DoT until bandaged. |
| Pain | 0–100 | Affects aim sway and sprint duration. |
| Stress | 0–100 | Increases under threat; raises noise and tunnel vision. |
| Fatigue | 0–100 | Gated sprint, climb, hold breath. |
| Contamination | 0–100 | Eldritch exposure; unlocks narrative effects. |

**Status Effects (MEDSTAT)**  
 `Stable, Wounded, Critical, In Shock, Unconscious, Infected, Contaminated`

## **5.3 Movement & Interaction**

* Walk, crouch, prone, vault, mantle, lean, ladder, ledge shimmy.

* Contextual interactions: door types (latched, chained, keypad), physical locks (picks, bolt cutters), electrical panels (fuses, breakers).

* Encumbrance tiers from **Load %** thresholds (0–25–50–75–100) modify sprint and noise.

## **5.4 Stealth System**

**Detection** \= f(Visibility, Noise, Proximity, Angle, Light, Time).

* Visibility: silhouette contrast vs background; crouch/prone reduce profile.

* Noise budget per action (dB‑like unit): walk 5, crouch 2, sprint 12, vault 10, firearm unsuppressed 90\.

* Light: player‑held light cones expose; ambient darkness grants threshold reductions.

* Cover quality: `High / Partial / None`.

* Distractions: throwables, TAPLINE audio spoof (Avery), analog timers (Clara).  
   **Fail states:** escalation to search → pursuit → breach; escape reduces heat over time.

## **5.5 Combat & Weapons**

**Avery**

* Stance shooting with **decoupled aiming**; suppression and verbal compliance prompts.

* Non‑lethal: baton, taser, pepper spray, beanbag shotgun; arrest animations and cuff time.

* Lethal: era‑appropriate sidearms and long guns.  
   **Clara**

* Last‑resort lethals, improvised traps (tripwire, glass, chemical irritants), thrown objects.

**Ballistics**

* Penetration tiers: Light (wood/drywall), Medium (doors), Heavy (brick/steel ‑ no pen).

* Recoil pattern by weapon class; aim sway raised by Pain and Fatigue.

* Hit model: head/torso/limb with armor zones (Avery armor vests).

**Damage Types**: kinetic, blunt, laceration, burn, shock, psychic.

## **5.6 Arrest & ROE (Avery)**

* **ROE Gate:** Lethal force only when threat presents deadly force.

* **Compliance Loop:** `Aim → Challenge → Countdown → Restrain`. NPC morale, numbers, and witness presence modify surrender probability.

* **Evidence Integrity:** discharges, injuries, and property damage log to casefile.

## **5.7 Evidence & Casework**

**Tiers**: `A = forensic`, `B = analytical/eyewitness`, `C = circumstantial`.  
 **Quality Score (0–100)** drives access gates and outcomes.

**Quality Formula (baseline)**  
 `Q = BaseTier + ChainBonus − ContamPenalty − TimeDecay + CrosslinkBonus`

* BaseTier: A=50, B=30, C=15.

* ChainBonus: +0–20 if bag→tag→log completed in **FieldPad**.

* ContamPenalty: −0–25 for mishandling or broken seals.

* TimeDecay: −0–10 if perishable and delayed.

* CrosslinkBonus: +0–15 if connected to ≥2 corroborating items.

**Chain of Custody (Avery)**

1. Photograph in place → 2) Collect with gloves → 3) Bag & seal → 4) Tag ID → 5) Log in FieldPad → 6) Transfer receipt.  
    Breaks invalidate A‑tier gates until remedied by supervisor sign‑off.

## **5.8 TAPLINE (Signals) — Mechanics**

* Bands: VHF/UHF, cordless phones, pagers, analog trunked radio.

* Modes: **Scan**, **Record**, **Triangulate**, **Spoof** (Avery only), **Decode** (DTMF/FSK).

* Minigame: lock to frequency, maintain signal quality; terrain occlusion affects SNR.

* Warrants: evidence threshold `Q ≥ 60` unlocks lawful intercept; otherwise limited to exigent use with risk.

## **5.9 FieldPad (Casework) — Mechanics**

* Apps: Camera, Evidence, Caseboard, Warrant Builder, Map, Contacts.

* Warrant Builder: template + probable cause fields; auto‑pulls linked evidence; judge approval simulated via score.

* Caseboard: nodes and threads; inference suggestions with uncertainty badges.

## **5.10 MEDSTAT (Vitals) — Mechanics**

* Tracks HP, Pain, Blood Loss, Stress, Fatigue.

* Triage actions: bandage, tourniquet, analgesic, stimulant, sedative.

* Team telemetry: Avery can issue commands when teammates are within range; Clara uses self‑care only.

## **5.11 Inventory, Crafting, Economy**

* **Slots + Weight** hybrid. Quick slots: 4\. Backpack tiers affect capacity.

* **Crafting (Clara‑focused):** simple traps, lock tools, noise devices using found parts.

* **Economy:** no global money; favors barter and requisition (Avery through casefile approvals).

## **5.12 Progression**

* **Skills:** separate trees; no shared XP.

  * Avery: Procedure, Firearms, Tactics, Signals.

  * Clara: Stealth, Improvisation, Athletics, Care.

* **Unlock cadence:** per chapter beats; prevents grinding.

## **5.13 AI Behavior**

**Senses:** hearing, sight cone, light sensitivity.  
 **States:** idle → suspicious → search → engage → pursue → fallback.  
 **Group Tactics (Avery arcs):** bounding, flank, breach; morale checks drive surrenders.  
 **Investigation:** NPCs log last known position, inspect distractions, call for backup on radios.  
 **Evidence Reaction:** guards may move or destroy exposed C‑tier items; A‑tier is secured.

## **5.14 Heat & Reputation**

* Heat rises with noise, bodies found, property damage; decays over time when hidden.

* Reputation tracks arrests vs kills for Avery; affects community cooperation and support.

## **5.15 Accessibility & Options**

* Sliders: camera shake, motion blur, aim assist, input remap.

* Toggles: simplified evidence prompts, slower TAPLINE minigames, high‑contrast device themes.

## **5.16 Telemetry & Tuning Targets**

* Pre‑action evidence logged rate ≥70%.

* Avery arrest:kill ≥2:1.

* Clara lethal usage ≤20% of resolved encounters.

* Average stealth breach detection time 6–12 s at Standard.

## **5.17 Data Contracts (Save/Load)**

* Caseboard graph, Evidence items with chain state, Heat/Reputation, AI world state snapshot, device app unlock flags.

## **5.18 Deliverables**

* System spec JSON (attributes, thresholds).

* AI behavior trees and perception tunables.

* Device app flows and wireframes (link to SEC‑07).

* Test plans for ROE, chain‑of‑custody, TAPLINE legality cases.

## **5.19 Approvals**

On approval: archive to MASTER as `[SEC-05-SYSTEMS] v0.1` and update manifest. Next section: **SEC‑06 World, Levels, & Content**.


### **5.x TAPLINE Legal Gates (1994)**
- **Pen register / trap‑and‑trace**: logs dialed numbers only; lower standard order. UI must label as **No content capture**.
- **Content interception (Title III)**: required for audio/content; block capture without active order; show **Title III order required** messaging.
- Full audit trail: judge, order id, start/stop timestamps.

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

# SEC-05 — CH6: Splinter Vault Mechanics
Repo dir: /Patches

## Overview
Final arena inside the **Splinter of Azathoth** vault. Raid ROE. No civilians. Phrase remains ambient: “the stars are right tonight.”

## Layout
- **Antechamber:** breaker, valve test rig, first-aid.  
- **Vault Ring:** rotating catwalk segments (manual).  
- **Core Dais:** Splinter obelisk on gimbal. Ritual pylons ×3.

## Shared Rules
- **Mana:** regen only during 3s calm windows.  
- **Light:** flashlight cones stagger Night Gaunts; Headlights not present.  
- **Damage:** lethal allowed; blue-on-blue = fail.

## Ending A — Seal (Contain)
Goal: stabilize the gimbal and choke flows.
1) **Tag valves** A→B→C with Polaroid (once).  
2) **Cycle order** under **Shield** windows.  
3) **Jam pylon wards** (Ward Jam) for 5s each to allow valve turns.  
4) **Manual lock** on gimbal set to “STABLE”.  
Success: breach sealed. Set `F_End_Contain=1`.

Failure: wrong order → surge. Spawn +2 Cultists; retry after 10s.

## Ending B — Sever (Escape)
Goal: break couplings and run.
1) Plant charges at two couplings.  
2) **Counter-chant** window opens; interrupt with TK Push or gunfire.  
3) Detonate; sprint route opens to Service Stair.  
Success: link severed; anomalies spike outside. Set `F_End_Escape=1`.

Failure: mis-timed det → partial break; path still opens but Fear spike.

## Ending C — Black File (Evidence-first)
Goal: catalog apparatus and samples then extract.
1) Photo each pylon control and gimbal plate (Polaroid).  
2) Collect one reagent and one shard sample.  
3) Bag+tag and exfil.  
Success: evidence maxed; rep penalty. Set `F_End_BlackFile=1`.

Failure: over-encumbered → sprint penalty on exit.

## Spawns (Vault)
- **Waves:** small Cultist squads + Night Gaunt swoops every 20–30s.  
- **Trigger:** each objective step may spawn a wave.  
- **Balance:** ammo caches at antechamber; tonics rare.

## UI prompts (≤14 chars)
Valve A, Valve B, Valve C, Jam Ward, Shield, Plant, Detonate, Photo, Sample, Bag, Tag, Map, Note

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

# SEC-05 — CH6: Splinter Vault Mechanics
Repo dir: /Patches

## Overview
Final arena inside the **Splinter of Azathoth** vault. Raid ROE. No civilians. Phrase remains ambient: “the stars are right tonight.”

## Layout
- **Antechamber:** breaker, valve test rig, first-aid.  
- **Vault Ring:** rotating catwalk segments (manual).  
- **Core Dais:** Splinter obelisk on gimbal. Ritual pylons ×3.

## Shared Rules
- **Mana:** regen only during 3s calm windows.  
- **Light:** flashlight cones stagger Night Gaunts; Headlights not present.  
- **Damage:** lethal allowed; blue-on-blue = fail.

## Ending A — Seal (Contain)
Goal: stabilize the gimbal and choke flows.
1) **Tag valves** A→B→C with Polaroid (once).  
2) **Cycle order** under **Shield** windows.  
3) **Jam pylon wards** (Ward Jam) for 5s each to allow valve turns.  
4) **Manual lock** on gimbal set to “STABLE”.  
Success: breach sealed. Set `F_End_Contain=1`.

Failure: wrong order → surge. Spawn +2 Cultists; retry after 10s.

## Ending B — Sever (Escape)
Goal: break couplings and run.
1) Plant charges at two couplings.  
2) **Counter-chant** window opens; interrupt with TK Push or gunfire.  
3) Detonate; sprint route opens to Service Stair.  
Success: link severed; anomalies spike outside. Set `F_End_Escape=1`.

Failure: mis-timed det → partial break; path still opens but Fear spike.

## Ending C — Black File (Evidence-first)
Goal: catalog apparatus and samples then extract.
1) Photo each pylon control and gimbal plate (Polaroid).  
2) Collect one reagent and one shard sample.  
3) Bag+tag and exfil.  
Success: evidence maxed; rep penalty. Set `F_End_BlackFile=1`.

Failure: over-encumbered → sprint penalty on exit.

## Spawns (Vault)
- **Waves:** small Cultist squads + Night Gaunt swoops every 20–30s.  
- **Trigger:** each objective step may spawn a wave.  
- **Balance:** ammo caches at antechamber; tonics rare.

## UI prompts (≤14 chars)
Valve A, Valve B, Valve C, Jam Ward, Shield, Plant, Detonate, Photo, Sample, Bag, Tag, Map, Note

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

# SEC-05 — CH6: Splinter Vault Mechanics
Repo dir: /Patches

## Overview
Final arena inside the **Splinter of Azathoth** vault. Raid ROE. No civilians. Phrase remains ambient: “the stars are right tonight.”

## Layout
- **Antechamber:** breaker, valve test rig, first-aid.  
- **Vault Ring:** rotating catwalk segments (manual).  
- **Core Dais:** Splinter obelisk on gimbal. Ritual pylons ×3.

## Shared Rules
- **Mana:** regen only during 3s calm windows.  
- **Light:** flashlight cones stagger Night Gaunts; Headlights not present.  
- **Damage:** lethal allowed; blue-on-blue = fail.

## Ending A — Seal (Contain)
Goal: stabilize the gimbal and choke flows.
1) **Tag valves** A→B→C with Polaroid (once).  
2) **Cycle order** under **Shield** windows.  
3) **Jam pylon wards** (Ward Jam) for 5s each to allow valve turns.  
4) **Manual lock** on gimbal set to “STABLE”.  
Success: breach sealed. Set `F_End_Contain=1`.

Failure: wrong order → surge. Spawn +2 Cultists; retry after 10s.

## Ending B — Sever (Escape)
Goal: break couplings and run.
1) Plant charges at two couplings.  
2) **Counter-chant** window opens; interrupt with TK Push or gunfire.  
3) Detonate; sprint route opens to Service Stair.  
Success: link severed; anomalies spike outside. Set `F_End_Escape=1`.

Failure: mis-timed det → partial break; path still opens but Fear spike.

## Ending C — Black File (Evidence-first)
Goal: catalog apparatus and samples then extract.
1) Photo each pylon control and gimbal plate (Polaroid).  
2) Collect one reagent and one shard sample.  
3) Bag+tag and exfil.  
Success: evidence maxed; rep penalty. Set `F_End_BlackFile=1`.

Failure: over-encumbered → sprint penalty on exit.

## Spawns (Vault)
- **Waves:** small Cultist squads + Night Gaunt swoops every 20–30s.  
- **Trigger:** each objective step may spawn a wave.  
- **Balance:** ammo caches at antechamber; tonics rare.

## UI prompts (≤14 chars)
Valve A, Valve B, Valve C, Jam Ward, Shield, Plant, Detonate, Photo, Sample, Bag, Tag, Map, Note

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# [SEC-06-WORLD] World, Levels, & Content
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-04-LOOPS` — Core Gameplay Loops
- `SEC-05-SYSTEMS` — Systems & Mechanics
- `SEC-07-UI` — UI/UX (Devices, HUD, Menus)
- `SEC-08-ARTAUDIO` — Art Direction & Audio

## **6.1 World Overview**

Grounded 1994 U.S. setting warped by the **Splinter**. Two vectors:

* Avery Jordan: operates within federal jurisdictions, warrants, ROE.

* Clara Winston: traverses civilian spaces under scarcity while protecting Reddy.

Reality fractures into **New Kadath** (adjacent, navigable) and **Unknown Kadath** (hostile, non-Euclidean). Some sites exist in both with altered geometry.

## **6.2 Factions & Organizations**

| Faction | Mandate | Notes |
| ----- | ----- | ----- |
| FBI / Task Group | Investigate disappearances and comms anomalies | Avery’s org; politics constrain |
| Brightstar / Kids Kamp Front | Childcare cover for experiments | Clara’s entry; rural network |
| The Splinter Circle | Cult-adjacent operators enabling incursions | Antagonists Qin Xu Qi, Paul Kent, Richard Tack |
| Local Law & Services | Sheriffs, EMTs, utilities | Variable cooperation; rep-gated |
| Federal Shadow Counsel | Legal pressure channel | Pushes latitude after Level X clearance |

## **6.3 Key Locations & Hubs**

| ID | Location | Layer(s) | Role |
| ----- | ----- | ----- | ----- |
| L-01 | Brightstar Daycare / Kids Kamp | Real / New Kadath | Prologue, Clara escape, later Avery return |
| L-02 | Jackson, South Carolina | Real | Avery early fieldwork |
| L-03 | Backwoods & Service Roads | Real / New Kadath | Clara traversal; route choice, scavenging |
| L-04 | Utility Substations & Switchyards | Real | TAPLINE triangulation; stealth puzzles |
| L-05 | NYC Field Office & Safehouse | Real | Mid-game Avery hub |
| L-06 | Transit/Steam Tunnels (NYC) | Real / New Kadath | Cross-POV infiltration |
| L-07 | Transdimensional Complex | Unknown Kadath | Late-game ascent, escape |

## **6.4 Level Design Tenets**

* Readable austerity: PS1-era silhouettes + modern lighting.

* Two-pass geometry: Clara stealth first, Avery breach second.

* Multiple resolutions: investigate → bypass → arrest/neutralize → extract.

* Diegetic signage, period-accurate props.

* Vertical micro-loops: ledges, vents, catwalks.

## **6.5 Mission Archetypes**

| Template | Clara | Avery |
| ----- | ----- | ----- |
| Recon → Infiltrate → Extract | Scout, disable, escort Reddy | Brief, warrant, breach/knock |
| Stakeout → Warrant → Breach | N/A | Casework, judge score, entry |
| Escort/Protect (Reddy) | Core | MEDSTAT support |
| Evidence Sweep | Scavenge under pressure | Chain-of-custody |
| Disruption | Improvised traps | Targeted arrests, comms seizure |

## **6.6 Encounter Taxonomy**

* Human: guards, cultists, contractors.

* Paranormal: echo forms, geometry shears, contamination zones.

* Environmental: power, locks, alarms, dogs, fog volumes.

## **6.7 NPC Cast (Primary)**

Clara Winston, Avery Jordan, Reddy, Qin Xu Qi, Paul Kent, Richard Tack, Betsy Lumbar, Langston Gromley.

## **6.8 Cross-POV World State**

* Shared caseboard reflects arrests, deaths, assets.

* Spaces re-enterable with altered states.

* Evidence/reputation affects cooperation and patrol density.

## **6.9 Content Matrix (v0 scope)**

| Chapter | Locale(s) | Missions | Notes |
| ----- | ----- | ----- | ----- |
| Prologue | Brightstar / New Kadath | 1 | Clara intro |
| Ch1 | Kids Kamp, Jackson SC | 2–3 | Clara escape; Avery check |
| Ch2 | Backwoods, Substations | 2 | Route choice; TAPLINE |
| Ch3 | Brightstar return, Unknown Kadath | 2 | Convergence, time dilation |
| Ch4 | NYC Tunnels + surreal | 2 | Swap cadence tighter |
| Ch5 | NYC hub + prior sites | 2–3 | Rogue Avery, open returns |
| Ch6 | Transdimensional Complex | 2 | Ascent, escape |
| Epilogue | Variable | 1 | Endings matrix |
| Total missions: 13–16. |  |  |  |

## **6.10 Props & Interactables**

Locks, fuses, breakers, time clocks, payphones, tape recorders, pagers, radios, filing cabinets, CRTs, turnstiles, steam valves, vents, evidence bags, cameras.

## **6.11 Art & Audio Hooks**

Art: low-poly kits, fog, signage packs. Audio: period SFX, Kadath distortions.

## **6.12 Accessibility**

High-contrast signage, readable fonts, optional repeats, reduced-horror toggle.

## **6.13 Performance & Budget**

Per level: draw call targets, enemy caps, fog tuned, heavy FX for Kadath.

## **6.14 Deliverables**

Greybox plans, prop lists, re-entry specs, audio maps, optimization checklist.

## **6.15 Approvals**

On approval: archive to MASTER as [SEC-06-WORLD] v0.1 and update manifest. Next: SEC-07 UI/UX.

# **Patch Instructions for Existing MASTER — SEC-07**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-07-UI |` and replace the entire line with:

`| SEC-07-UI | UI/UX | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**


> **Era barks:** Prefer payphone and pager language; avoid smartphones, texting, USB, Wi‑Fi, and GPS turn‑by‑turn references.

# ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md
> Append to SEC-06 (World) and SEC-07 (UI). CH6 = raid; lethal authorized; neutralizations score-neutral.

## SEC-06 — World Merge
- Service Passage: only CCTV zone; allow Photo and Sample interactions.
- Vault: no CCTV; photography disabled; rely on Sample and logs.
- K-9 Reroute: scent decoy nodes + handler diversion radio event.
- Breaker: ≈90 s recycle; lights and cameras restore in stages (30/60/90 s).
- Signage: 1994 OSHA/DOE style; map boards near valves A/B/C.
- Evidence: cap = 3 total across site.

## SEC-06 — Interactables
- Valves: A, B, C. Each with Equip/Valve prompts; audible pressure shift.
- Breach points: charge Plant → Detonate loop; jammer affects wards.
- Service cameras: breaker trip blanks feeds, restores per cooldown.

## SEC-07 — UI Merge
- HUD: `Evidence 0/3`, `BlueOnBlue`, health/mana, cast/equip L/R.
- Prompt set must include: Ward Jam, Cast L, Cast R, Equip L, Equip R, Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample.
- Failure states: show “BlueOnBlue” banner on friendly hit outside exceptions.
- City rules (CH5): friendly/civilian hits fail; non-lethal favored.

## Notes
- Keep all text period-accurate to 1994. No modern tech terms.

# ROOT_SEC-06-07_World_UI_CH7_Merge.md
> Append to SEC-06 (World) and SEC-07 (UI). Period: 1994. City evidence cap **2**. Non-lethal favored. Friendly/civilian hits = fail.

## SEC-06 — City World Merge
- Public spaces allow Photo/Sample with consent. Private interiors require consent or warrant text; avoid unlawful evidence.
- Evidence cap **2** across city segments; deny third pickup with “Evidence full.”
- Nodes: Payphone taps, safehouse stakeouts, precinct handoffs, artifact/sigil anchor search.
- Illusions: doubled NPC silhouettes, desynced audio, false signage. FieldPad vs MEDSTAT comparisons reveal fakes.
- Mindscape access: locate **anchor** object; entry via ritual phrase set; exit by **Wake** or **Ground** interaction.
- Civilians: erratic paths; panic escalates patrol density and affects Epilogue scoring.

## SEC-06 — Interactables
- Payphone: Dial, Hang Up, Trace (scripted).
- Pager: Page, Read.
- Fax: Fax Send (use in precincts).
- Escort routes: start/stop nodes; crowd control without lethal force.
- Anchor/Sigil: Inspect, Anchor, Counter.

## SEC-07 — UI Merge
- HUD: `Evidence 0/2` during investigation. Hide counter elsewhere.
- Failure: any friendly/civilian hit = immediate fail in city scenes.
- Illusion tells: brief **Reveal** banner when contradictions detected.
- Keep prompts ≤14 and 1994-authentic.

## World — CH2 Avery: Inner Checkpoint (SEC-06 addendum)

### Nodes
- Outer Fence: low light, chain-link, single patroller.
- Inner Gate (Checkpoint): challenge/response node; passphrase gate.
- Outbuilding A: cash ledger + rosters.
- Shed B: generator; optional power cut branch.
- Office Shack: microcassettes + gate logbook; fax/teletype access for later use (secure line at SO).

### Patrols (1994 lighting)
- Two-guard loop on 90s arcs. Flashlight cones only. No NVGs.
- Civilian path near Office Shack; avoid collateral.

### Evidence Placement
- Ledger in lockbox (simple pin tumbler).
- Rosters on clipboard.
- Tapes in desk drawer.
- .38 on Deacon analogue.

### Exit
- Exfil via Outer Fence rendezvous with {DeputyName}. Booking at Aiken Co. SO.

## World — CH3 Addendum (SEC-06)

### Clara & Reddy Nodes
- **Kadath Sectors A–D:** Looping pine scrub; Forage/Water nodes; bivouac sites.
- **Pine Break Portal:** Two-way portal behind Brightstar; returns from building to forest only.
- **Brightstar Anchors:** Service Corridor, Office, Multipurpose Room; non-anchors scramble per entry.
- **Scavenger Ambush Site:** Clearing with wagon debris; cover objects for TK play.

### Avery Nodes
- **Condemned Brightstar:** Caution tape, plywood panels, dim interior; spectral patrol path.
- **Spectral Spawn Points:** Cold spots that trigger phase-only vulnerability windows.
- **Threshold Chase Route:** Forced path from Office → Service Corridor → Portal yard.

### Hazards & Interactables (1994)
- No weapon lights. Flashlight cones, payphone stubs, paper notices. Fire extinguishers, sand tables, mop buckets usable.

# SEC-06 — CH4 World Addendum: Kadath City
Repo dir: /Patches

## Nodes
- **South Gate & Ditch:** Entry, horn-call signals, watch rotations.
- **Elder Hall:** Parley chamber; safe zone after entry.
- **Sanctum Spire:** Boss arena; two levels; warded pillars; bells; braziers.
- **Alleys & Markets:** Stealth approach routes; hostile outskirts beyond walls.
- **Car Return Point:** Real-world anchor for Fast Travel (Avery’s car).

## Patrol & Signals
- **Wardens:** Bow and spear; horn patterns = patrol shifts.  
- **Civilians:** Unarmed; flee on gunfire; collateral penalties apply.

## Interactables (1994)
- Braziers, bells, wooden doors, rope pulleys, paper writs. No modern tech.  
- Payphone analogs absent; city uses horns and runners.

## Artifacts
- Ward sigils, charter scraps, loop anchor glyphs, spellbook folios.

## Map Notes
- Mark parapet lines, sanctum entrances, fallback ladders, and Fast Travel return line to Car Return Point.

# SEC-06 — CH5→CH6 Callsigns & Nodes
Repo dir: /Patches

## Callsigns (radio/pager codes)
- **LEAD:** Avery  
- **SAGE:** Clara  
- **DRIFT:** Reddy  
- **ANCHOR:** {DeputyName}  
- **HAND:** Krill (pager only)

## Sites (codenames)
- **DEEP-GLASS:** D‑LAMP deep site  
- **IRON-MILE:** Iron Highway  
- **ANNEX-GATE:** SRS bulkhead layby  
- **VALVE-ROW:** valve corridor  
- **VAULT-RING:** Splinter catwalk ring

## Quick-use UI prompts (≤14)
LEAD, SAGE, DRIFT, ANCHOR, HAND (labels only)

# SEC-06 — Iron Highway Routebook (CH5→CH6)
Repo dir: /Patches

## Start
D‑LAMP Vehicle Bay → pick up **D‑LAMP Utility Rover**.

## Legs (textual map)
1) **Ramp A**: descend; keep right at split; loose gravel.
2) **Pump Cavern**: Star Vampire cleared; cross catwalk; exit north portal.
3) **Switchback 1–3**: slow turns; cave‑in on left; detour marker.
4) **Marker “IH‑12”**: night gaunt swoops reported; lights recommended.
5) **Spur JCT**: avoid left spur “FAN‑2”; zombies cluster.
6) **Vault Hall**: low O2 tone possible; idle near fan to recover.
7) **Annex Sign**: “SRS SECRET ANNEX →”; brake for switchback.
8) **Bulkhead Layby**: park rover; handbrake; lights off; proceed on foot.

## Hazards
- Cave‑ins, low O2, undead pockets, cultist patrols.
- Fuel is finite; no refuel outside Vehicle Bay.

## Evidence (cap mindful)
- Route card, dock log page, PO photo opportunities.

## UI prompts (≤14)
Drive, Brake, Lights, Horn, Enter, Exit, Map, Note

# SEC-06 — World: D‑LAMP Deep Site & Iron Highway (CH5→CH6)
Repo dir: /Patches

## Access
- **WV River Island:** Concealed elevator kiosk disguised as a maintenance shed.  
- **Deep Elevator:** Industrial cage; manual brake and call box; ~1 mile descent.

## D‑LAMP Deep Site (Abandoned)
- **Nodes:** Entry Gallery, Admin Archive, Pump Cavern (Star Vampire arena), Vehicle Bay, Route Control.  
- **Readables:** AEC→DOE exit notes; Splintered God rota; 1980s purchase orders; Iron Highway route cards.  
- **Hazards:** Collapsed shafts, low O2 alarms (tone cue only), undead pockets.

## Iron Highway
- **Description:** Braced utility road for D‑LAMP rovers; signage to **SRS Secret Annex**.  
- **Encounters:** Zombie clusters at cross‑tunnels; night gaunt swoops in tall vaults; scattered cultists.  
- **Traversal:** Driveable segments with occasional on‑foot detours; switchbacks; cave‑in bypasses.

## SRS Secret Annex (Exterior)
- **Bulkhead Gate:** Mechanical seals; DOE placards; cult graffiti.  
- **Staging:** Safe pull‑off for rover; service man‑door; leads to CH6 “Core Galleries.”

## Enemy Roster (these locales)
- **Zombie:** slow, headshot bias.  
- **Night Gaunt:** dive attack, stagger on light.  
- **Star Vampire:** mini‑boss (see SEC‑05).  
- **Cultist:** rites/sidearms; interruptible chants.

## Interactables (1994)
- Polaroid markers, paper maps, clipboards; handbrake rovers; crank lights; analog call boxes.

# SEC-06 — CH5 World Addendum
Repo dir: /Patches

## Nodes
### NYFO / Hotel
- **NYFO Interview Rooms:** Interrogation, Hallway (Krill brief), Evidence Drop.  
- **Hotel:** Lobby, Service Corridor, Stairwell, Room, Alley exit.

### D-LAMP Campus
- **Reception**, **Shipping Dock**, **Records Closet**, **Night Dock Loop**.

### Betsy House
- **Living Room**, **Kitchen Cut**, **Hallway**, **Back Porch**, **Street**.

## Civilians & Patrols (1994)
- NYFO Agents: suits, pagers, radios; non-lethal expected.  
- D-LAMP Guards: flashlights, clipboards; no NVGs.  
- Betsy Block: neighbors indoors; collateral penalties if harmed.

## Interactables (1994)
- Phones: MicroTAC, payphones, fax at NYFO only.  
- Evidence: paper logs, Polaroids, purchase orders, writs.  
- Doors: key cylinders, chain locks; no electronic maglocks.

## Map Notes
- Hotel camera angles in stairwell.  
- D-LAMP shipment lanes and badge doors.  
- Betsy house egress routes and porch sightlines.

# SEC-06-CH6_Ascii_Map.md
> SRS operation layout for Chapter 6. Cameras only in Service Passage. Vault has **no CCTV**.\n
```
                       NORTH
        ┌──────────────────────────────────────────┐
        │   DELIVERY YARD                         │
        │   [Parking][Trunk][Radio]               │
        └───────┬───────────────────────┬─────────┘
                │                       │
        ┌───────▼───────────┐   ┌───────▼───────────┐
        │  SERVICE PASSAGE  │   │     ADMIN WING    │
        │  [CCTV ZONE]      │   │  Offices, Breakr │
        │  [Photo/Sample]   │   │  Breaker Panel ◻ │
        │  K‑9 Route ⇄      │   │                   │
        └───┬─────────┬─────┘   └─────────┬────────┘
            │         │                   │
            │   ┌─────▼─────┐       ┌────▼─────┐
            │   │ REACTOR A │       │ REACTOR B│
            │   │ Valve A ● │       │ Valve B ●│
            │   │ Ward ◇    │       │ Ward ◇   │
            │   └─────┬─────┘       └────┬─────┘
            │         │                   │
        ┌───▼─────────▼──────┐      ┌────▼───────────┐
        │  CONNECTOR TUNNEL  │      │  REACTOR C     │
        │  Breach ✚  Jammer  │      │  Valve C ●     │
        └───┬────────────────┘      │  Ward ◇        │
            │                       └────┬───────────┘
            │                            │
        ┌───▼────────────────────────────▼───┐
        │               VAULT                 │
        │   [NO CCTV]   Core ◯   Device ▣    │
        │   Photo: ✖    Sample: ✔            │
        │   Escape Route ⇒ Collapsing Corr.  │
        └────────────────────────────────────┘

Legend:
● Valve A/B/C      ◻ Breaker (≈90 s)    ◇ Ward Node
✚ Breach Point     ▣ Device             ◯ Core
✔ Allowed          ✖ Not allowed        ⇄ K‑9 reroute path
```

## Notes
- Cameras exist only in **Service Passage**. Photography restricted there.
- Breaker recycle ≈ **90 s**. Staged restore at 30/60/90 s.
- K‑9 reroute via handler diversion or scent decoy along marked path.
- Vault enforces **no photography**; rely on samples/logs.

# SEC-06 — CH6 Route + Encounter Tables
Repo dir: /Patches

## Route
1) Bulkhead Gate → Man-Door → Service Passage  
2) Valve Row → Dead Piping → Service Stair  
3) Core Gallery → Splinter Vault

## Encounter Table (d10 per segment)
- 1–2: **Zombie pack** (3–5). Headshot bias.  
- 3–4: **Cultists** (2–3) chanting “the stars are right tonight.”  
- 5: **Beast** charge (1). Telegraph sound cue.  
- 6–7: **Night Gaunt** swoop (1). Stagger on light.  
- 8: **Mixed** (2 Cultists + 2 Zombies).  
- 9: **Quiet** (loot cache).  
- 10: **Alarm** (next segment auto-spawn +1 step).

## Scaling
- If Alert High: add +1 to all rolls.  
- If ammo <25%: suppress one spawn per two segments.

## Loot Table (d6 on Quiet)
1–2: Ammo cache.  
3: Tonic (Mana).  
4: First-aid.  
5: Map scrap (evidence cap permitting).  
6: Spare fuse (breaker shortcut).

# SEC-06 — CH6 World: SRS Secret Annex
Repo dir: /Patches

## Nodes
- **Bulkhead Gate:** DOE placards, cult graffiti, manual seal wheels.
- **Man-Door:** Keyed cylinder; entry to Service Passage.
- **Service Passage:** Low light; analog cameras; K-9 patrol routes.
- **Valve Row:** Numbered valves A/B/C; Polaroid tags for “Seal” path.
- **Dead Piping:** Decommissioned lines; ritual prep tables.
- **Service Stair:** Vertical link to Core Gallery.
- **Core Gallery:** Main arena for ritual ignition; geometry shifts.
- **Splinter Vault:** Sealed chamber for the **Splinter of Azathoth**.
- **Egress Run:** Marked to fence gap rendezvous with {DeputyName}.

## Encounters
Zombies (headshot bias), Night Gaunts (light-stagger), Cultists (chant: “the stars are right tonight”), Beasts (charge tells).

## Interactables (1994)
Padlocks, keyed doors, paper logs, Polaroids, analog cams, radios. No network terminals.

## Lighting
Flashlight cones only; breaker boxes gate limited areas.

# SEC-06 — CH6 Stealth: Breakers & Camera Loops
Repo dir: /Patches

## Analog cameras (1994)
- Fixed arcs in **Service Passage** only. Tape‑deck recording; no network.  
- **Blind spots:** at arc seams and breaker outages.

## Breaker boxes
- **Fuse pull** creates a **90 s** camera outage in connected zone.  
- **Cooldown:** 60 s before fuse reinsert allowed.  
- **K‑9 reroute:** patrol shifts to lantern sweep during outage.  
- **Risk:** pulling during Alert High spawns +1 Cultist on response.

## Loop design
- Player can chain two boxes to walk Valve Row unseen.  
- Breakers do **not** affect Vault cameras (none installed).

## UI prompts (≤14 chars)
Fuse, Pull Fuse, Insert Fuse, Breach, Hide, Crouch, Map, Note

## QA
- Verify 90 s outage timing.  
- Verify K‑9 route swap.  
- Verify no Vault cameras.

# SEC-06 — CH1 World Layouts ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑06 World (new CH1 subsection).

## Brightstar Daycare (Interior, day→dusk)
- Zones & blockout: foyer 8×6, classroom 10×8, infirmary 5×4, storage hall 12×2.2, exit 4×3.
- Navigation: Staffer patrol loop foyer→hall→storage→foyer (45–60 s); cones 50°/9 m.
- Interactables: visitor ledger, supply drawer (MEDSTAT note‑card), MEDSTAT card slot, care station.
- Perf spots: PS‑B1 foyer desk; PS‑B2 storage hall mid; PS‑B3 exit vestibule.
- Signage/dressing: “Visitors Sign In,” evacuation map, period health posters, toys pre‑1994.

## Roadside Stop (Exterior)
- Blockout: road 120×10 with 2×3 m shoulder; S‑curve; stop 15 m after apex.
- Props: patrol car, cones, folding table, mobile locker case.
- Triggers: suspect stand 5 m from bumper; locker trigger 1.5 m box; photo hotspot on table.
- Perf spots: PS‑R1 OTS to suspect; PS‑R2 locker table; PS‑R3 road curve wide.

# ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md
> Append to SEC-06 (World) and SEC-07 (UI). CH6 = raid; lethal authorized; neutralizations score-neutral.

## SEC-06 — World Merge
- Service Passage: only CCTV zone; allow Photo and Sample interactions.
- Vault: no CCTV; photography disabled; rely on Sample and logs.
- K-9 Reroute: scent decoy nodes + handler diversion radio event.
- Breaker: ≈90 s recycle; lights and cameras restore in stages (30/60/90 s).
- Signage: 1994 OSHA/DOE style; map boards near valves A/B/C.
- Evidence: cap = 3 total across site.

## SEC-06 — Interactables
- Valves: A, B, C. Each with Equip/Valve prompts; audible pressure shift.
- Breach points: charge Plant → Detonate loop; jammer affects wards.
- Service cameras: breaker trip blanks feeds, restores per cooldown.

## SEC-07 — UI Merge
- HUD: `Evidence 0/3`, `BlueOnBlue`, health/mana, cast/equip L/R.
- Prompt set must include: Ward Jam, Cast L, Cast R, Equip L, Equip R, Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample.
- Failure states: show “BlueOnBlue” banner on friendly hit outside exceptions.
- City rules (CH5): friendly/civilian hits fail; non-lethal favored.

## Notes
- Keep all text period-accurate to 1994. No modern tech terms.

# ROOT_SEC-06-07_World_UI_CH7_Merge.md
> Append to SEC-06 (World) and SEC-07 (UI). Period: 1994. City evidence cap **2**. Non-lethal favored. Friendly/civilian hits = fail.

## SEC-06 — City World Merge
- Public spaces allow Photo/Sample with consent. Private interiors require consent or warrant text; avoid unlawful evidence.
- Evidence cap **2** across city segments; deny third pickup with “Evidence full.”
- Nodes: Payphone taps, safehouse stakeouts, precinct handoffs, artifact/sigil anchor search.
- Illusions: doubled NPC silhouettes, desynced audio, false signage. FieldPad vs MEDSTAT comparisons reveal fakes.
- Mindscape access: locate **anchor** object; entry via ritual phrase set; exit by **Wake** or **Ground** interaction.
- Civilians: erratic paths; panic escalates patrol density and affects Epilogue scoring.

## SEC-06 — Interactables
- Payphone: Dial, Hang Up, Trace (scripted).
- Pager: Page, Read.
- Fax: Fax Send (use in precincts).
- Escort routes: start/stop nodes; crowd control without lethal force.
- Anchor/Sigil: Inspect, Anchor, Counter.

## SEC-07 — UI Merge
- HUD: `Evidence 0/2` during investigation. Hide counter elsewhere.
- Failure: any friendly/civilian hit = immediate fail in city scenes.
- Illusion tells: brief **Reveal** banner when contradictions detected.
- Keep prompts ≤14 and 1994-authentic.

## World — CH2 Avery: Inner Checkpoint (SEC-06 addendum)

### Nodes
- Outer Fence: low light, chain-link, single patroller.
- Inner Gate (Checkpoint): challenge/response node; passphrase gate.
- Outbuilding A: cash ledger + rosters.
- Shed B: generator; optional power cut branch.
- Office Shack: microcassettes + gate logbook; fax/teletype access for later use (secure line at SO).

### Patrols (1994 lighting)
- Two-guard loop on 90s arcs. Flashlight cones only. No NVGs.
- Civilian path near Office Shack; avoid collateral.

### Evidence Placement
- Ledger in lockbox (simple pin tumbler).
- Rosters on clipboard.
- Tapes in desk drawer.
- .38 on Deacon analogue.

### Exit
- Exfil via Outer Fence rendezvous with {DeputyName}. Booking at Aiken Co. SO.

## World — CH3 Addendum (SEC-06)

### Clara & Reddy Nodes
- **Kadath Sectors A–D:** Looping pine scrub; Forage/Water nodes; bivouac sites.
- **Pine Break Portal:** Two-way portal behind Brightstar; returns from building to forest only.
- **Brightstar Anchors:** Service Corridor, Office, Multipurpose Room; non-anchors scramble per entry.
- **Scavenger Ambush Site:** Clearing with wagon debris; cover objects for TK play.

### Avery Nodes
- **Condemned Brightstar:** Caution tape, plywood panels, dim interior; spectral patrol path.
- **Spectral Spawn Points:** Cold spots that trigger phase-only vulnerability windows.
- **Threshold Chase Route:** Forced path from Office → Service Corridor → Portal yard.

### Hazards & Interactables (1994)
- No weapon lights. Flashlight cones, payphone stubs, paper notices. Fire extinguishers, sand tables, mop buckets usable.

# SEC-06 — CH4 World Addendum: Kadath City
Repo dir: /Patches

## Nodes
- **South Gate & Ditch:** Entry, horn-call signals, watch rotations.
- **Elder Hall:** Parley chamber; safe zone after entry.
- **Sanctum Spire:** Boss arena; two levels; warded pillars; bells; braziers.
- **Alleys & Markets:** Stealth approach routes; hostile outskirts beyond walls.
- **Car Return Point:** Real-world anchor for Fast Travel (Avery’s car).

## Patrol & Signals
- **Wardens:** Bow and spear; horn patterns = patrol shifts.  
- **Civilians:** Unarmed; flee on gunfire; collateral penalties apply.

## Interactables (1994)
- Braziers, bells, wooden doors, rope pulleys, paper writs. No modern tech.  
- Payphone analogs absent; city uses horns and runners.

## Artifacts
- Ward sigils, charter scraps, loop anchor glyphs, spellbook folios.

## Map Notes
- Mark parapet lines, sanctum entrances, fallback ladders, and Fast Travel return line to Car Return Point.

# SEC-06 — CH5→CH6 Callsigns & Nodes
Repo dir: /Patches

## Callsigns (radio/pager codes)
- **LEAD:** Avery  
- **SAGE:** Clara  
- **DRIFT:** Reddy  
- **ANCHOR:** {DeputyName}  
- **HAND:** Krill (pager only)

## Sites (codenames)
- **DEEP-GLASS:** D‑LAMP deep site  
- **IRON-MILE:** Iron Highway  
- **ANNEX-GATE:** SRS bulkhead layby  
- **VALVE-ROW:** valve corridor  
- **VAULT-RING:** Splinter catwalk ring

## Quick-use UI prompts (≤14)
LEAD, SAGE, DRIFT, ANCHOR, HAND (labels only)

# SEC-06 — Iron Highway Routebook (CH5→CH6)
Repo dir: /Patches

## Start
D‑LAMP Vehicle Bay → pick up **D‑LAMP Utility Rover**.

## Legs (textual map)
1) **Ramp A**: descend; keep right at split; loose gravel.
2) **Pump Cavern**: Star Vampire cleared; cross catwalk; exit north portal.
3) **Switchback 1–3**: slow turns; cave‑in on left; detour marker.
4) **Marker “IH‑12”**: night gaunt swoops reported; lights recommended.
5) **Spur JCT**: avoid left spur “FAN‑2”; zombies cluster.
6) **Vault Hall**: low O2 tone possible; idle near fan to recover.
7) **Annex Sign**: “SRS SECRET ANNEX →”; brake for switchback.
8) **Bulkhead Layby**: park rover; handbrake; lights off; proceed on foot.

## Hazards
- Cave‑ins, low O2, undead pockets, cultist patrols.
- Fuel is finite; no refuel outside Vehicle Bay.

## Evidence (cap mindful)
- Route card, dock log page, PO photo opportunities.

## UI prompts (≤14)
Drive, Brake, Lights, Horn, Enter, Exit, Map, Note

# SEC-06 — World: D‑LAMP Deep Site & Iron Highway (CH5→CH6)
Repo dir: /Patches

## Access
- **WV River Island:** Concealed elevator kiosk disguised as a maintenance shed.  
- **Deep Elevator:** Industrial cage; manual brake and call box; ~1 mile descent.

## D‑LAMP Deep Site (Abandoned)
- **Nodes:** Entry Gallery, Admin Archive, Pump Cavern (Star Vampire arena), Vehicle Bay, Route Control.  
- **Readables:** AEC→DOE exit notes; Splintered God rota; 1980s purchase orders; Iron Highway route cards.  
- **Hazards:** Collapsed shafts, low O2 alarms (tone cue only), undead pockets.

## Iron Highway
- **Description:** Braced utility road for D‑LAMP rovers; signage to **SRS Secret Annex**.  
- **Encounters:** Zombie clusters at cross‑tunnels; night gaunt swoops in tall vaults; scattered cultists.  
- **Traversal:** Driveable segments with occasional on‑foot detours; switchbacks; cave‑in bypasses.

## SRS Secret Annex (Exterior)
- **Bulkhead Gate:** Mechanical seals; DOE placards; cult graffiti.  
- **Staging:** Safe pull‑off for rover; service man‑door; leads to CH6 “Core Galleries.”

## Enemy Roster (these locales)
- **Zombie:** slow, headshot bias.  
- **Night Gaunt:** dive attack, stagger on light.  
- **Star Vampire:** mini‑boss (see SEC‑05).  
- **Cultist:** rites/sidearms; interruptible chants.

## Interactables (1994)
- Polaroid markers, paper maps, clipboards; handbrake rovers; crank lights; analog call boxes.

# SEC-06 — CH5 World Addendum
Repo dir: /Patches

## Nodes
### NYFO / Hotel
- **NYFO Interview Rooms:** Interrogation, Hallway (Krill brief), Evidence Drop.  
- **Hotel:** Lobby, Service Corridor, Stairwell, Room, Alley exit.

### D-LAMP Campus
- **Reception**, **Shipping Dock**, **Records Closet**, **Night Dock Loop**.

### Betsy House
- **Living Room**, **Kitchen Cut**, **Hallway**, **Back Porch**, **Street**.

## Civilians & Patrols (1994)
- NYFO Agents: suits, pagers, radios; non-lethal expected.  
- D-LAMP Guards: flashlights, clipboards; no NVGs.  
- Betsy Block: neighbors indoors; collateral penalties if harmed.

## Interactables (1994)
- Phones: MicroTAC, payphones, fax at NYFO only.  
- Evidence: paper logs, Polaroids, purchase orders, writs.  
- Doors: key cylinders, chain locks; no electronic maglocks.

## Map Notes
- Hotel camera angles in stairwell.  
- D-LAMP shipment lanes and badge doors.  
- Betsy house egress routes and porch sightlines.

# SEC-06-CH6_Ascii_Map.md
> SRS operation layout for Chapter 6. Cameras only in Service Passage. Vault has **no CCTV**.\n
```
                       NORTH
        ┌──────────────────────────────────────────┐
        │   DELIVERY YARD                         │
        │   [Parking][Trunk][Radio]               │
        └───────┬───────────────────────┬─────────┘
                │                       │
        ┌───────▼───────────┐   ┌───────▼───────────┐
        │  SERVICE PASSAGE  │   │     ADMIN WING    │
        │  [CCTV ZONE]      │   │  Offices, Breakr │
        │  [Photo/Sample]   │   │  Breaker Panel ◻ │
        │  K‑9 Route ⇄      │   │                   │
        └───┬─────────┬─────┘   └─────────┬────────┘
            │         │                   │
            │   ┌─────▼─────┐       ┌────▼─────┐
            │   │ REACTOR A │       │ REACTOR B│
            │   │ Valve A ● │       │ Valve B ●│
            │   │ Ward ◇    │       │ Ward ◇   │
            │   └─────┬─────┘       └────┬─────┘
            │         │                   │
        ┌───▼─────────▼──────┐      ┌────▼───────────┐
        │  CONNECTOR TUNNEL  │      │  REACTOR C     │
        │  Breach ✚  Jammer  │      │  Valve C ●     │
        └───┬────────────────┘      │  Ward ◇        │
            │                       └────┬───────────┘
            │                            │
        ┌───▼────────────────────────────▼───┐
        │               VAULT                 │
        │   [NO CCTV]   Core ◯   Device ▣    │
        │   Photo: ✖    Sample: ✔            │
        │   Escape Route ⇒ Collapsing Corr.  │
        └────────────────────────────────────┘

Legend:
● Valve A/B/C      ◻ Breaker (≈90 s)    ◇ Ward Node
✚ Breach Point     ▣ Device             ◯ Core
✔ Allowed          ✖ Not allowed        ⇄ K‑9 reroute path
```

## Notes
- Cameras exist only in **Service Passage**. Photography restricted there.
- Breaker recycle ≈ **90 s**. Staged restore at 30/60/90 s.
- K‑9 reroute via handler diversion or scent decoy along marked path.
- Vault enforces **no photography**; rely on samples/logs.

# SEC-06 — CH6 Route + Encounter Tables
Repo dir: /Patches

## Route
1) Bulkhead Gate → Man-Door → Service Passage  
2) Valve Row → Dead Piping → Service Stair  
3) Core Gallery → Splinter Vault

## Encounter Table (d10 per segment)
- 1–2: **Zombie pack** (3–5). Headshot bias.  
- 3–4: **Cultists** (2–3) chanting “the stars are right tonight.”  
- 5: **Beast** charge (1). Telegraph sound cue.  
- 6–7: **Night Gaunt** swoop (1). Stagger on light.  
- 8: **Mixed** (2 Cultists + 2 Zombies).  
- 9: **Quiet** (loot cache).  
- 10: **Alarm** (next segment auto-spawn +1 step).

## Scaling
- If Alert High: add +1 to all rolls.  
- If ammo <25%: suppress one spawn per two segments.

## Loot Table (d6 on Quiet)
1–2: Ammo cache.  
3: Tonic (Mana).  
4: First-aid.  
5: Map scrap (evidence cap permitting).  
6: Spare fuse (breaker shortcut).

# SEC-06 — CH6 World: SRS Secret Annex
Repo dir: /Patches

## Nodes
- **Bulkhead Gate:** DOE placards, cult graffiti, manual seal wheels.
- **Man-Door:** Keyed cylinder; entry to Service Passage.
- **Service Passage:** Low light; analog cameras; K-9 patrol routes.
- **Valve Row:** Numbered valves A/B/C; Polaroid tags for “Seal” path.
- **Dead Piping:** Decommissioned lines; ritual prep tables.
- **Service Stair:** Vertical link to Core Gallery.
- **Core Gallery:** Main arena for ritual ignition; geometry shifts.
- **Splinter Vault:** Sealed chamber for the **Splinter of Azathoth**.
- **Egress Run:** Marked to fence gap rendezvous with {DeputyName}.

## Encounters
Zombies (headshot bias), Night Gaunts (light-stagger), Cultists (chant: “the stars are right tonight”), Beasts (charge tells).

## Interactables (1994)
Padlocks, keyed doors, paper logs, Polaroids, analog cams, radios. No network terminals.

## Lighting
Flashlight cones only; breaker boxes gate limited areas.

# SEC-06 — CH6 Stealth: Breakers & Camera Loops
Repo dir: /Patches

## Analog cameras (1994)
- Fixed arcs in **Service Passage** only. Tape‑deck recording; no network.  
- **Blind spots:** at arc seams and breaker outages.

## Breaker boxes
- **Fuse pull** creates a **90 s** camera outage in connected zone.  
- **Cooldown:** 60 s before fuse reinsert allowed.  
- **K‑9 reroute:** patrol shifts to lantern sweep during outage.  
- **Risk:** pulling during Alert High spawns +1 Cultist on response.

## Loop design
- Player can chain two boxes to walk Valve Row unseen.  
- Breakers do **not** affect Vault cameras (none installed).

## UI prompts (≤14 chars)
Fuse, Pull Fuse, Insert Fuse, Breach, Hide, Crouch, Map, Note

## QA
- Verify 90 s outage timing.  
- Verify K‑9 route swap.  
- Verify no Vault cameras.

# SEC-06 — CH1 World Layouts ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑06 World (new CH1 subsection).

## Brightstar Daycare (Interior, day→dusk)
- Zones & blockout: foyer 8×6, classroom 10×8, infirmary 5×4, storage hall 12×2.2, exit 4×3.
- Navigation: Staffer patrol loop foyer→hall→storage→foyer (45–60 s); cones 50°/9 m.
- Interactables: visitor ledger, supply drawer (MEDSTAT note‑card), MEDSTAT card slot, care station.
- Perf spots: PS‑B1 foyer desk; PS‑B2 storage hall mid; PS‑B3 exit vestibule.
- Signage/dressing: “Visitors Sign In,” evacuation map, period health posters, toys pre‑1994.

## Roadside Stop (Exterior)
- Blockout: road 120×10 with 2×3 m shoulder; S‑curve; stop 15 m after apex.
- Props: patrol car, cones, folding table, mobile locker case.
- Triggers: suspect stand 5 m from bumper; locker trigger 1.5 m box; photo hotspot on table.
- Perf spots: PS‑R1 OTS to suspect; PS‑R2 locker table; PS‑R3 road curve wide.

# ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md
> Append to SEC-06 (World) and SEC-07 (UI). CH6 = raid; lethal authorized; neutralizations score-neutral.

## SEC-06 — World Merge
- Service Passage: only CCTV zone; allow Photo and Sample interactions.
- Vault: no CCTV; photography disabled; rely on Sample and logs.
- K-9 Reroute: scent decoy nodes + handler diversion radio event.
- Breaker: ≈90 s recycle; lights and cameras restore in stages (30/60/90 s).
- Signage: 1994 OSHA/DOE style; map boards near valves A/B/C.
- Evidence: cap = 3 total across site.

## SEC-06 — Interactables
- Valves: A, B, C. Each with Equip/Valve prompts; audible pressure shift.
- Breach points: charge Plant → Detonate loop; jammer affects wards.
- Service cameras: breaker trip blanks feeds, restores per cooldown.

## SEC-07 — UI Merge
- HUD: `Evidence 0/3`, `BlueOnBlue`, health/mana, cast/equip L/R.
- Prompt set must include: Ward Jam, Cast L, Cast R, Equip L, Equip R, Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample.
- Failure states: show “BlueOnBlue” banner on friendly hit outside exceptions.
- City rules (CH5): friendly/civilian hits fail; non-lethal favored.

## Notes
- Keep all text period-accurate to 1994. No modern tech terms.

## CH6 Raid ROE and Safety

- CH6 = raid. Lethal authorized. Neutralizations are score-neutral.  
- **Blue-on-Blue = hard fail (−10).** Exceptions: (1) Shield-absorbed friendly hits do not count. (2) A **single** shotgun pellet striking a friendly **>10 m** away does not count.  
- Cameras only in Service Passage; **No CCTV in Vault**. Breaker cut ≈90 s. **K-9 reroute** available.  
- **Evidence cap = 3** in CH6. HUD must show `Evidence 0/3` and a `BlueOnBlue` indicator.

## CH6 Raid ROE and Safety

- CH6 = raid. Lethal authorized. Neutralizations are score-neutral.
- Blue-on-Blue = hard fail (-10). Exceptions:
  (1) Shield-absorbed friendly hits do not count.
  (2) A single shotgun pellet striking a friendly >10 m away does not count.
- Cameras only in Service Passage; No CCTV in Vault. Breaker cut approx 90 s. K-9 reroute available.
- Evidence cap = 3 in CH6. HUD must show "Evidence 0/3" and a "BlueOnBlue" indicator.

# ROOT_SEC-06-07_World_UI_CH7_Merge.md
> Append to SEC-06 (World) and SEC-07 (UI). Period: 1994. City evidence cap **2**. Non-lethal favored. Friendly/civilian hits = fail.

## SEC-06 — City World Merge
- Public spaces allow Photo/Sample with consent. Private interiors require consent or warrant text; avoid unlawful evidence.
- Evidence cap **2** across city segments; deny third pickup with “Evidence full.”
- Nodes: Payphone taps, safehouse stakeouts, precinct handoffs, artifact/sigil anchor search.
- Illusions: doubled NPC silhouettes, desynced audio, false signage. FieldPad vs MEDSTAT comparisons reveal fakes.
- Mindscape access: locate **anchor** object; entry via ritual phrase set; exit by **Wake** or **Ground** interaction.
- Civilians: erratic paths; panic escalates patrol density and affects Epilogue scoring.

## SEC-06 — Interactables
- Payphone: Dial, Hang Up, Trace (scripted).
- Pager: Page, Read.
- Fax: Fax Send (use in precincts).
- Escort routes: start/stop nodes; crowd control without lethal force.
- Anchor/Sigil: Inspect, Anchor, Counter.

## SEC-07 — UI Merge
- HUD: `Evidence 0/2` during investigation. Hide counter elsewhere.
- Failure: any friendly/civilian hit = immediate fail in city scenes.
- Illusion tells: brief **Reveal** banner when contradictions detected.
- Keep prompts ≤14 and 1994-authentic.

## World — CH2 Avery: Inner Checkpoint (SEC-06 addendum)

### Nodes
- Outer Fence: low light, chain-link, single patroller.
- Inner Gate (Checkpoint): challenge/response node; passphrase gate.
- Outbuilding A: cash ledger + rosters.
- Shed B: generator; optional power cut branch.
- Office Shack: microcassettes + gate logbook; fax/teletype access for later use (secure line at SO).

### Patrols (1994 lighting)
- Two-guard loop on 90s arcs. Flashlight cones only. No NVGs.
- Civilian path near Office Shack; avoid collateral.

### Evidence Placement
- Ledger in lockbox (simple pin tumbler).
- Rosters on clipboard.
- Tapes in desk drawer.
- .38 on Deacon analogue.

### Exit
- Exfil via Outer Fence rendezvous with {DeputyName}. Booking at Aiken Co. SO.

## World — CH3 Addendum (SEC-06)

### Clara & Reddy Nodes
- **Kadath Sectors A–D:** Looping pine scrub; Forage/Water nodes; bivouac sites.
- **Pine Break Portal:** Two-way portal behind Brightstar; returns from building to forest only.
- **Brightstar Anchors:** Service Corridor, Office, Multipurpose Room; non-anchors scramble per entry.
- **Scavenger Ambush Site:** Clearing with wagon debris; cover objects for TK play.

### Avery Nodes
- **Condemned Brightstar:** Caution tape, plywood panels, dim interior; spectral patrol path.
- **Spectral Spawn Points:** Cold spots that trigger phase-only vulnerability windows.
- **Threshold Chase Route:** Forced path from Office → Service Corridor → Portal yard.

### Hazards & Interactables (1994)
- No weapon lights. Flashlight cones, payphone stubs, paper notices. Fire extinguishers, sand tables, mop buckets usable.

# SEC-06 — CH4 World Addendum: Kadath City
Repo dir: /Patches

## Nodes
- **South Gate & Ditch:** Entry, horn-call signals, watch rotations.
- **Elder Hall:** Parley chamber; safe zone after entry.
- **Sanctum Spire:** Boss arena; two levels; warded pillars; bells; braziers.
- **Alleys & Markets:** Stealth approach routes; hostile outskirts beyond walls.
- **Car Return Point:** Real-world anchor for Fast Travel (Avery’s car).

## Patrol & Signals
- **Wardens:** Bow and spear; horn patterns = patrol shifts.  
- **Civilians:** Unarmed; flee on gunfire; collateral penalties apply.

## Interactables (1994)
- Braziers, bells, wooden doors, rope pulleys, paper writs. No modern tech.  
- Payphone analogs absent; city uses horns and runners.

## Artifacts
- Ward sigils, charter scraps, loop anchor glyphs, spellbook folios.

## Map Notes
- Mark parapet lines, sanctum entrances, fallback ladders, and Fast Travel return line to Car Return Point.

# SEC-06 — CH5→CH6 Callsigns & Nodes
Repo dir: /Patches

## Callsigns (radio/pager codes)
- **LEAD:** Avery  
- **SAGE:** Clara  
- **DRIFT:** Reddy  
- **ANCHOR:** {DeputyName}  
- **HAND:** Krill (pager only)

## Sites (codenames)
- **DEEP-GLASS:** D‑LAMP deep site  
- **IRON-MILE:** Iron Highway  
- **ANNEX-GATE:** SRS bulkhead layby  
- **VALVE-ROW:** valve corridor  
- **VAULT-RING:** Splinter catwalk ring

## Quick-use UI prompts (≤14)
LEAD, SAGE, DRIFT, ANCHOR, HAND (labels only)

# SEC-06 — Iron Highway Routebook (CH5→CH6)
Repo dir: /Patches

## Start
D‑LAMP Vehicle Bay → pick up **D‑LAMP Utility Rover**.

## Legs (textual map)
1) **Ramp A**: descend; keep right at split; loose gravel.
2) **Pump Cavern**: Star Vampire cleared; cross catwalk; exit north portal.
3) **Switchback 1–3**: slow turns; cave‑in on left; detour marker.
4) **Marker “IH‑12”**: night gaunt swoops reported; lights recommended.
5) **Spur JCT**: avoid left spur “FAN‑2”; zombies cluster.
6) **Vault Hall**: low O2 tone possible; idle near fan to recover.
7) **Annex Sign**: “SRS SECRET ANNEX →”; brake for switchback.
8) **Bulkhead Layby**: park rover; handbrake; lights off; proceed on foot.

## Hazards
- Cave‑ins, low O2, undead pockets, cultist patrols.
- Fuel is finite; no refuel outside Vehicle Bay.

## Evidence (cap mindful)
- Route card, dock log page, PO photo opportunities.

## UI prompts (≤14)
Drive, Brake, Lights, Horn, Enter, Exit, Map, Note

# SEC-06 — World: D‑LAMP Deep Site & Iron Highway (CH5→CH6)
Repo dir: /Patches

## Access
- **WV River Island:** Concealed elevator kiosk disguised as a maintenance shed.  
- **Deep Elevator:** Industrial cage; manual brake and call box; ~1 mile descent.

## D‑LAMP Deep Site (Abandoned)
- **Nodes:** Entry Gallery, Admin Archive, Pump Cavern (Star Vampire arena), Vehicle Bay, Route Control.  
- **Readables:** AEC→DOE exit notes; Splintered God rota; 1980s purchase orders; Iron Highway route cards.  
- **Hazards:** Collapsed shafts, low O2 alarms (tone cue only), undead pockets.

## Iron Highway
- **Description:** Braced utility road for D‑LAMP rovers; signage to **SRS Secret Annex**.  
- **Encounters:** Zombie clusters at cross‑tunnels; night gaunt swoops in tall vaults; scattered cultists.  
- **Traversal:** Driveable segments with occasional on‑foot detours; switchbacks; cave‑in bypasses.

## SRS Secret Annex (Exterior)
- **Bulkhead Gate:** Mechanical seals; DOE placards; cult graffiti.  
- **Staging:** Safe pull‑off for rover; service man‑door; leads to CH6 “Core Galleries.”

## Enemy Roster (these locales)
- **Zombie:** slow, headshot bias.  
- **Night Gaunt:** dive attack, stagger on light.  
- **Star Vampire:** mini‑boss (see SEC‑05).  
- **Cultist:** rites/sidearms; interruptible chants.

## Interactables (1994)
- Polaroid markers, paper maps, clipboards; handbrake rovers; crank lights; analog call boxes.

# SEC-06 — CH5 World Addendum
Repo dir: /Patches

## Nodes
### NYFO / Hotel
- **NYFO Interview Rooms:** Interrogation, Hallway (Krill brief), Evidence Drop.  
- **Hotel:** Lobby, Service Corridor, Stairwell, Room, Alley exit.

### D-LAMP Campus
- **Reception**, **Shipping Dock**, **Records Closet**, **Night Dock Loop**.

### Betsy House
- **Living Room**, **Kitchen Cut**, **Hallway**, **Back Porch**, **Street**.

## Civilians & Patrols (1994)
- NYFO Agents: suits, pagers, radios; non-lethal expected.  
- D-LAMP Guards: flashlights, clipboards; no NVGs.  
- Betsy Block: neighbors indoors; collateral penalties if harmed.

## Interactables (1994)
- Phones: MicroTAC, payphones, fax at NYFO only.  
- Evidence: paper logs, Polaroids, purchase orders, writs.  
- Doors: key cylinders, chain locks; no electronic maglocks.

## Map Notes
- Hotel camera angles in stairwell.  
- D-LAMP shipment lanes and badge doors.  
- Betsy house egress routes and porch sightlines.

# SEC-06-CH6_Ascii_Map.md
> SRS operation layout for Chapter 6. Cameras only in Service Passage. Vault has **no CCTV**.\n
```
                       NORTH
        ┌──────────────────────────────────────────┐
        │   DELIVERY YARD                         │
        │   [Parking][Trunk][Radio]               │
        └───────┬───────────────────────┬─────────┘
                │                       │
        ┌───────▼───────────┐   ┌───────▼───────────┐
        │  SERVICE PASSAGE  │   │     ADMIN WING    │
        │  [CCTV ZONE]      │   │  Offices, Breakr │
        │  [Photo/Sample]   │   │  Breaker Panel ◻ │
        │  K‑9 Route ⇄      │   │                   │
        └───┬─────────┬─────┘   └─────────┬────────┘
            │         │                   │
            │   ┌─────▼─────┐       ┌────▼─────┐
            │   │ REACTOR A │       │ REACTOR B│
            │   │ Valve A ● │       │ Valve B ●│
            │   │ Ward ◇    │       │ Ward ◇   │
            │   └─────┬─────┘       └────┬─────┘
            │         │                   │
        ┌───▼─────────▼──────┐      ┌────▼───────────┐
        │  CONNECTOR TUNNEL  │      │  REACTOR C     │
        │  Breach ✚  Jammer  │      │  Valve C ●     │
        └───┬────────────────┘      │  Ward ◇        │
            │                       └────┬───────────┘
            │                            │
        ┌───▼────────────────────────────▼───┐
        │               VAULT                 │
        │   [NO CCTV]   Core ◯   Device ▣    │
        │   Photo: ✖    Sample: ✔            │
        │   Escape Route ⇒ Collapsing Corr.  │
        └────────────────────────────────────┘

Legend:
● Valve A/B/C      ◻ Breaker (≈90 s)    ◇ Ward Node
✚ Breach Point     ▣ Device             ◯ Core
✔ Allowed          ✖ Not allowed        ⇄ K‑9 reroute path
```

## Notes
- Cameras exist only in **Service Passage**. Photography restricted there.
- Breaker recycle ≈ **90 s**. Staged restore at 30/60/90 s.
- K‑9 reroute via handler diversion or scent decoy along marked path.
- Vault enforces **no photography**; rely on samples/logs.

# SEC-06 — CH6 Route + Encounter Tables
Repo dir: /Patches

## Route
1) Bulkhead Gate → Man-Door → Service Passage  
2) Valve Row → Dead Piping → Service Stair  
3) Core Gallery → Splinter Vault

## Encounter Table (d10 per segment)
- 1–2: **Zombie pack** (3–5). Headshot bias.  
- 3–4: **Cultists** (2–3) chanting “the stars are right tonight.”  
- 5: **Beast** charge (1). Telegraph sound cue.  
- 6–7: **Night Gaunt** swoop (1). Stagger on light.  
- 8: **Mixed** (2 Cultists + 2 Zombies).  
- 9: **Quiet** (loot cache).  
- 10: **Alarm** (next segment auto-spawn +1 step).

## Scaling
- If Alert High: add +1 to all rolls.  
- If ammo <25%: suppress one spawn per two segments.

## Loot Table (d6 on Quiet)
1–2: Ammo cache.  
3: Tonic (Mana).  
4: First-aid.  
5: Map scrap (evidence cap permitting).  
6: Spare fuse (breaker shortcut).

# SEC-06 — CH6 World: SRS Secret Annex
Repo dir: /Patches

## Nodes
- **Bulkhead Gate:** DOE placards, cult graffiti, manual seal wheels.
- **Man-Door:** Keyed cylinder; entry to Service Passage.
- **Service Passage:** Low light; analog cameras; K-9 patrol routes.
- **Valve Row:** Numbered valves A/B/C; Polaroid tags for “Seal” path.
- **Dead Piping:** Decommissioned lines; ritual prep tables.
- **Service Stair:** Vertical link to Core Gallery.
- **Core Gallery:** Main arena for ritual ignition; geometry shifts.
- **Splinter Vault:** Sealed chamber for the **Splinter of Azathoth**.
- **Egress Run:** Marked to fence gap rendezvous with {DeputyName}.

## Encounters
Zombies (headshot bias), Night Gaunts (light-stagger), Cultists (chant: “the stars are right tonight”), Beasts (charge tells).

## Interactables (1994)
Padlocks, keyed doors, paper logs, Polaroids, analog cams, radios. No network terminals.

## Lighting
Flashlight cones only; breaker boxes gate limited areas.

# SEC-06 — CH6 Stealth: Breakers & Camera Loops
Repo dir: /Patches

## Analog cameras (1994)
- Fixed arcs in **Service Passage** only. Tape‑deck recording; no network.  
- **Blind spots:** at arc seams and breaker outages.

## Breaker boxes
- **Fuse pull** creates a **90 s** camera outage in connected zone.  
- **Cooldown:** 60 s before fuse reinsert allowed.  
- **K‑9 reroute:** patrol shifts to lantern sweep during outage.  
- **Risk:** pulling during Alert High spawns +1 Cultist on response.

## Loop design
- Player can chain two boxes to walk Valve Row unseen.  
- Breakers do **not** affect Vault cameras (none installed).

## UI prompts (≤14 chars)
Fuse, Pull Fuse, Insert Fuse, Breach, Hide, Crouch, Map, Note

## QA
- Verify 90 s outage timing.  
- Verify K‑9 route swap.  
- Verify no Vault cameras.

# SEC-06 — CH1 World Layouts ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑06 World (new CH1 subsection).

## Brightstar Daycare (Interior, day→dusk)
- Zones & blockout: foyer 8×6, classroom 10×8, infirmary 5×4, storage hall 12×2.2, exit 4×3.
- Navigation: Staffer patrol loop foyer→hall→storage→foyer (45–60 s); cones 50°/9 m.
- Interactables: visitor ledger, supply drawer (MEDSTAT note‑card), MEDSTAT card slot, care station.
- Perf spots: PS‑B1 foyer desk; PS‑B2 storage hall mid; PS‑B3 exit vestibule.
- Signage/dressing: “Visitors Sign In,” evacuation map, period health posters, toys pre‑1994.

## Roadside Stop (Exterior)
- Blockout: road 120×10 with 2×3 m shoulder; S‑curve; stop 15 m after apex.
- Props: patrol car, cones, folding table, mobile locker case.
- Triggers: suspect stand 5 m from bumper; locker trigger 1.5 m box; photo hotspot on table.
- Perf spots: PS‑R1 OTS to suspect; PS‑R2 locker table; PS‑R3 road curve wide.

# [SEC-07-UI] UI/UX (Devices, HUD, Menus)
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-05-SYSTEMS` — Systems & Mechanics
- `SEC-06-WORLD` — World, Levels, & Content
- `SEC-08-ARTAUDIO` — Art Direction & Audio
- `SEC-09-TECH` — Technology & Performance Targets

## **7.1 Goals & Principles**

* Diegetic first. Devices (FieldPad, TAPLINE, MEDSTAT) are primary UI.

* 1994 constraints. Limited color, latency, coarse hit targets, period affordances.

* Readability over spectacle. PS1‑era silhouettes + modern clarity.

* Minimal HUD. Surface only actionable state.

* Accessibility from day one.

## **7.2 Visual Language**

**Palette.** HUD: 1 accent + neutrals. Devices: two‑tone skins (Green, Amber, Gray).  
 **Type.** Bitmap sans for devices; clean sans for HUD. Minimum 12 px at 1080p equivalent.  
 **Grid.** Virtual 320×240 device canvas, 8 px base unit; HUD uses 12‑pt safe margins.  
 **Iconography.** Stroke icons, 1 px weight at 1080p, scale by step 1.25×.

## **7.3 Global HUD (contextual, minimal)**

* **Top‑left:** Objective stub + sub‑task dot list.

* **Bottom‑left:** Health bar + vitals pill. Clara shows **Stress**; Avery shows **Armor**.

* **Bottom‑right:** Ammo/weapon or tool readout.

* **Center‑low:** Interaction prompt with verb + hold meter where needed.

* **Stealth:** eye glyph (visibility), waveform glyph (noise).

* **Heat/Reputation:** small indicator in map/caseboard, not moment‑to‑moment.

Example HUD overlay (schematic):

[OBJ] Kids Kamp: Extract Reddy

  • Unlock north gate  ◻

  • Avoid patrols       ■

ꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏ (screen)

[HP ████▌]  [VIS ◐][NOISE ≈≈]                             [9× .38 | ■■■■]

      Clara: Stress ▒▒▒▒                                 Prompt: Hold E — Pick Lock ▓▓▓▒▒

## **7.4 Devices — Shared Conventions**

* **Nav**: Soft‑keys `◀ BACK` `OK ▶`, D‑pad/arrow focus, `Tab` cycles panes.

* **Latency**: app open/close 150–250 ms; scrolling steps 80 ms.

* **Status bar**: battery ▮▮▮▯, signal ▂▃▅, storage ■■■□, time 24h.

* **File ops**: save states are explicit; confirm destructive actions.

* **Skins**: Green (Avery default), Amber (Clara), Gray (accessibility high‑contrast).

### **7.4.1 FieldPad — Casework & Evidence**

**Purpose.** Capture, tag, link, and warrant‑build.  
 **Apps.** Home, Camera, Evidence, Caseboard, Warrant, Map, Contacts.  
 **Flows.** Photo → Tag → Chain steps → Link to case → Warrant score.

FieldPad — HOME

┌──────────────── FIELD•PAD ────────────────┐   ▂▃▅  ■■■□  ▮▮▮▯  14:32

│ [Camera] [Evidence] [Caseboard]           │

│ [Warrant] [Map]      [Contacts]           │

│                                            │

│ Tips: Complete bag→tag→log for A‑tier     │

└◀ BACK                            OK ▶──────┘

FieldPad — EVIDENCE (item view)

┌───────────── EVIDENCE: BAG #A‑014 ─────────┐   ▂▃▅  ■■■■  ▮▮▮▮  14:41

│ Photo: IMG\_0142  [View]                    │

│ Type: Fiber (A‑tier)                       │  Q: 78

│ Chain: Photo → Collect → Bag → Tag → Log   │  Seal: ▣ Intact

│ Links: Case #82 • Victim #2 • Locker 3     │

│ Notes:                                     │

│  − Found under vent panel                  │

└◀ BACK                   [LINK]   OK ▶──────┘

FieldPad — WARRANT BUILDER

┌────────────── WARRANT BUILDER ─────────────┐   ▂▃▅  ■■□□  ▮▮▮▯  15:06

│ Case: #82  Judge: S. Hartford              │  Score: 62 (PASS)

│ Probable Cause:                            │

│  [ ] Evidence A‑014 (fiber)                │

│  [ ] Intercepts TPL‑07                     │

│  [ ] Statement W‑03                        │

│ Affidavit Text:                            │

│  \> Suspect used south entrance…            │

└◀ BACK                 [SUBMIT]   OK ▶──────┘

### **7.4.2 TAPLINE — Signals**

**Purpose.** Scan, record, triangulate, spoof, and decode era radios/phones.  
 **Modes.** Scan • Record • Triangulate • Decode • Spoof (Avery only).

TAPLINE — SCAN

┌──────────────── TAPLINE: SCAN ─────────────┐   ▂▃▅  ■■□□  ▮▮▮▯  22:18

│ Band: UHF  |  Freq: 462.6125 MHz           │  SNR: ▓▓▓▒▒

│ [◀] 462.6000 ◁▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▷ 462.6500 [▶]

│ Hold to lock: ████▒▒                       │

│ Hits:  19:32  "Gate open"                   │

│        19:35  DTMF: 4 1 2                  │

└◀ BACK                 [RECORD]   OK ▶──────┘

TAPLINE — TRIANGULATE

┌───────────── TAPLINE: TRIANGULATE ─────────┐   ▂▃▅  ■■□□  ▮▮▮▯  22:26

│ Node A  ▣  Node B  ▢  Node C  ▢             │  Fix: 48%

│ Bearings: A 062° • B 239° • C  —           │

│ Map:  [A───────╳────────B]                  │

│        Clara route  [ ]  Avery route [x]    │

└◀ BACK                  [PING]    OK ▶──────┘

### **7.4.3 MEDSTAT — Vitals & Team**

**Purpose.** Health, status effects, triage, and telemetry.  
 **States.** Stable • Wounded • Critical • In Shock • Infected • Contaminated.

MEDSTAT — VITALS

┌──────────────── MED•STAT ──────────────────┐   ▂▃▅  ■■■■  ▮▮▮▯  02:14

│ Patient: AVERY     Armor: ▣▣▢               │

│ HP █████░  Pain ▓▓  Stress ▓                 │

│ Blood Loss: Arm ▪▪  Leg ▪  Torso ▪▪         │

│ Status: Wounded (Bleeding)                  │

│ Actions: [Bandage] [Tourniquet] [Analgesic] │

└◀ BACK                 [APPLY]    OK ▶──────┘

## **7.5 Menus & Screens**

* **Pause.** Resume, Save, Load, Options, Accessibility, Quit.

* **Inventory.** Slots + Weight hybrid; quick slots ×4.

* **Caseboard.** Graph of nodes and links; filter by time, tier, POV.

* **Map.** Layered (Real, New Kadath, Unknown); TAPLINE nodes and search areas.

Inventory (schematic)

┌──────────────── INVENTORY ────────────────┐

│ Weight: 62%   Quick: [1][2][3][4]         │

│ Backpack: MED                              │

│ Items:                                     │

│  ▣ Lockpicks (x3)  ▣ Glass Shards (x6)    │

│  ▣ .38 Rounds (9)  ▣ Tourniquet (1)       │

│  ▣ Evidence A‑014  ▣ Tape Recorder        │

└◀ BACK                 [ASSIGN]   OK ▶─────┘

Caseboard (schematic)

[Case #82]

  (Victim #2)───(Fiber A‑014)───(Vent South)

        │              │               \\

     (W‑03)         (TPL‑07)          (Locker 3)

## **7.6 Input & Controls**

* **KB/M:** WASD, `Q/E` lean, `C` crouch, `Z` prone, `F` interact, `R` reload, `1–4` quick slots, `Tab` device pane, `M` map, `Esc` pause.

* **Gamepad:** LS move, RS look, `LB/RB` cycle, `LT` aim, `RT` fire/apply, `Y` device swap, `X` interact, `A` confirm, `B` back.

* **Avery‑only:** `HOLD T` to Challenge (ROE), `G` to cuff when compliant.

* **Clara‑only:** `HOLD G` place trap, `V` whistle (distraction).

## **7.7 Feedback & Error States**

* **Prompts:** verb‑first, concise. Hold meters show discrete ticks.

* **Errors:** inline banners on devices (“Seal broken: A‑tier invalid”).

* **Saves:** autos at Brief/Branch/Outcome; manual outside combat.

## **7.8 Accessibility**

* High‑contrast device skin, scalable UI, color‑blind safe glyphs.

* Subtitles on, speaker tags, SFX ducking during dialogue.

* Input remap for all actions; toggle hold‑to‑press.

* Reduce camera shake/flash; simplify minigames.

## **7.9 Localization**

* All device text uses resource keys.

* String budget: device labels ≤14 chars; body lines wrap at 24–28 chars.

* Avoid cultural idioms in core prompts.

## **7.10 Telemetry Targets**

* Device app time‑to‑task ≤ 6 s for common flows.

* Prompt mis‑use rate \< 5% by beta.

* Evidence linked per mission ≥ 3 on average.

## **7.11 Deliverables**

* Wireframes for FieldPad/TAPLINE/MEDSTAT and HUD.

* Icon set (SVG/bitmap) with states.

* Device skins (Green/Amber/Gray).

* Interaction prompt library.

## **7.12 Approvals**

On approval: archive to MASTER as `[SEC-07-UI] v0.1` and update manifest. Next section: **SEC‑08 Art Direction & Audio**.

# **Patch Instructions for Existing MASTER — SEC-08**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-08-ARTAUDIO |` and replace the entire line with:

`| SEC-08-ARTAUDIO | Art direction and audio | v0.2 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**


> **Telephony note (1994):** Caller ID availability varies by carrier/market. Do not rely on it for puzzles; provide alternate clues.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# [SEC-08-ARTAUDIO] Art Direction & Audio
Version: v0.2  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-06-WORLD` — World, Levels, & Content
- `SEC-07-UI` — UI/UX (Devices, HUD, Menus)
- `SEC-09-TECH` — Technology & Performance Targets
- `SEC-10-PRODUCTION` — Production Plan & Milestones

## **8.1 Visual Pillars**

* PS1‑era austerity + modern clarity (fog, lights, post).

* Readable silhouettes first. Texture thrift.

* 1994 authenticity for props, signage, and UI.

## **8.2 Reference Package (deliver to Art Dir.)**

* Mood boards: **Real / New Kadath / Unknown Kadath**.

* Prop sheets: 1994 utilities, payphones, radios, lockers.

* Typeface refs: bitmap device sans, highway/OSHA signage fonts.

* Material library: plastic, painted metal, concrete, paper, glass.

* Lighting refs: sodium vapor, fluorescent, halogen, flashlight cones.

## **8.3 Color Palettes (master)**

**World Core (neutral, low‑sat):**

* **Splinter Black** `#0B0B0E`

* **Fog Gray** `#8D9199`

* **Concrete** `#5E666F`

* **Steel Blue** `#3B5368`

* **Sodium Amber** `#C48A1B`

* **Emergency Red** `#B21E2B`

**Device Skins (SEC‑07 parity):**

* **FieldPad Green** `#1C6B3C`

* **TAPLINE Amber** `#D09A2A`

* **MEDSTAT Gray** `#C7C9CC`

* **CRT Phosphor** `#00C853`

ASCII swatches:

████ Splinter Black #0B0B0E   ████ Fog Gray #8D9199   ████ Concrete #5E666F

████ Steel Blue    #3B5368   ████ Sodium Amber #C48A1B ████ Emergency Red #B21E2B

████ FieldPad Green #1C6B3C  ████ TAPLINE Amber #D09A2A ████ MEDSTAT Gray #C7C9CC

### **8.3.1 Locale Palettes**

| Locale | Primary | Accents | Notes |
| ----- | ----- | ----- | ----- |
| **Real‑Day** | Concrete `#5E666F`, Fog Gray `#8D9199` | Steel Blue `#3B5368`, Sodium Amber `#C48A1B` | Utility, signage pops |
| **Real‑Night** | Splinter Black `#0B0B0E`, Steel Blue `#3B5368` | Emergency Red `#B21E2B`, Sodium Amber `#C48A1B` | Patrol readability |
| **New Kadath** | Steel Blue `#3B5368`, Concrete `#5E666F` | CRT Phosphor `#00C853` | Subtle surreal shift |
| **Unknown Kadath** | Splinter Black `#0B0B0E` | Phosphor `#00C853`, Emergency Red `#B21E2B` | High contrast cues |
| **Industrial/Utilities** | Concrete `#5E666F` | TAPLINE Amber `#D09A2A` | Devices, wiring, meters |

### **8.3.2 Contrast Guidance (WCAG)**

* Target **≥4.5:1** for body, **≥3:1** for large text/icons.

* Approved pairs (AA pass):

  * `#FFFFFF` on `#1C6B3C` (FieldPad),

  * `#0B0B0E` on `#D09A2A` (TAPLINE),

  * `#FFFFFF` on `#3B5368`,

  * `#FFFFFF` on `#5E666F` (large text).

* Do not put `#FFFFFF` on `#C7C9CC` except for large text with stroke.

## **8.4 Modeling & LOD**

* Triangle budgets (target): hero chars **6–10k**, majors **4–6k**, grunts **2–4k**; hero props **1–3k**.

* LODs: LOD0/1/2 at **1.0/0.6/0.35** screen fractions; drop small geo first.

* Prioritize silhouette and normal hints over micro‑detail.

## **8.5 Materials & Shading**

* Few master materials; instance for tint/wear.

* Dithered gradients for 8–16‑bit look; limited roughness range.

* Decals for grime, leaks, signage; avoid high‑freq tiling.

## **8.6 Lighting & Fog**

* Mixed: baked GI where stable, dynamic keys for patrols and flickers.

* Temperature: sodium streets **2000–2200K**, fluorescents **4000–4500K**, halogen **3000K**.

* Volumetrics as gameplay: stealth cover vs readability.

* Kadath layers warp: slight non‑Euclidean offsets, color bleeding, shadow bend.

## **8.7 Post‑Processing**

* Film grain subtle; 90s chroma bleed minimal; CRT scanline option toggle.

* Chromatic aberration off by default.

* Camera shake configurable per Accessibility.

## **8.8 VFX**

* Splinter anomalies: refraction cones, audio‑reactive shimmer, particulate falloff.

* Environmental: steam, fluorescent buzz flicker, dust motes.

* Combat: modest muzzle flash, decal‑light footprints, low‑gore blood with pooling caps.

## **8.9 Animation Style**

* 24 fps keyframed look; occasional pose hold to evoke era.

* Clara cautious weight; Avery authoritative stance.

* Minimal facial rigs; rely on posture and camera.

## **8.10 UI Tie‑ins (from SEC‑07)**

* Two‑tone devices, bitmap type, 320×240 virtual grid.

* HUD minimal; visibility/noise glyphs; hold meters with ticks.

---

## **8.11 Audio Pillars**

* Dread via implication.

* 1994 soundscape: pagers, trunked radios, CRTs, HVAC.

* POV contrast: Avery comms; Clara breath/handling/space.

## **8.12 SFX Taxonomy**

* Movement, devices, world, human, paranormal, weapons.

* Ensure material sets by surface: concrete, dirt, grass, metal, wood, water.

## **8.13 Music Direction**

* Analog synths, tape wow/flutter, bowed metals, sparse piano; low‑drone strings for Splinter.

* Motifs: **Avery** procedural ostinato; **Clara** fragile two‑note rise; **Splinter** inharmonic cluster.

* Stems for **Stealth / Investigate / Combat / Aftermath**.

* Diegetic sources: radios, TVs, PA systems; mild LPF for occlusion.

## **8.14 Implementation (Audio Tech)**

* Middleware: **Wwise** (fallback: UE Audio).

* Mix bus: Master → Music / SFX / VO / UI → sub‑buses.

* RTPCs: Heat, Visibility, Stress, Health, LocationLayer.

* Ducking: Dialogue over SFX by **−6 dB**; UI under VO.

* Reverb zones: tunnels, rooms, Kadath diffuse.

* Loudness: true‑peak ≤ **−1 dBTP**; dialogue ≈ **−18 LUFS** short‑term.

## **8.15 VO & Dialogue — Pipeline**

* **Casting specs:** restrained natural reads; minimal melodrama.

* **Mic chain:** LDC with pop filter → clean preamp → 48 kHz/24‑bit WAV.

* **Session:** one actor per folder; one line per file; 1 s room tone head/tail per scene.

* **File naming:** `vo_<char>_<scene>_<lineID>_take##.wav`.

* **Slate:** soft clap + verbal slate at start of each scene.

* **Processing:** light HPF only; no FX baked.

## **8.16 Audio Deliverables — Spec**

* **Format:** WAV PCM **48 kHz / 24‑bit**.

* **Channels:** SFX mono unless spatial, Music stereo stems, VO mono.

* **Headroom:** peaks ≤ **−3 dBFS**; tails faded.

* **Loops:** seamless, zero‑cross boundaries, 10–50 ms ramps.

* **Naming:**

  * SFX `sfx_<cat>_<object>_<action>_v##.wav`

  * Music `mx_<state>_<cue>_<stem>.wav`

  * UI `ui_<device>_<app>_<action>.wav`

## **8.17 Music Stems Map & Cue Sheet Template**

**Stems per state:**

* *Stealth:* pad, pulse, texture.

* *Investigate:* pad, ticks, motif.

* *Combat:* drums, bass, lead, hits.

* *Aftermath:* drone, piano, noise bed.

Cue Sheet (example):

CUE: M\_CH3\_Tunnels\_Stealth  BPM: 84  Key: Em

Stems: pad, pulse, texture   Loop: 0:45

Enter: Visibility\<0.3 AND Heat\<0.2

Exit: Alert==true OR Combat==true

## **8.18 VFX Performance Caps & LOD**

* **Per‑frame particles (CPU):** ≤ **512** visible.

* **GPU sprites:** ≤ **20k** total; overdraw heatmap checked per milestone.

* **Fog volumes:** ≤ **3** large per level; avg overdraw \< **1.5×**.

* **Niagara LOD:** tick rate scales by distance; collisions off for small sprites.

* **Budget gates:** VFX time ≤ **2 ms** on min‑spec at target res.

## **8.19 UE5 Material/Post Stack Presets**

* **AA:** TSR default; TAAU fallback.

* **Post chain:** Exposure (manual), minimal Bloom, Film Grain low, Vignette low; **Chromatic Aberration OFF**.

* **Master materials:** `M_Master_Surface`, `M_Master_Emissive`, `M_Master_Glass`, `M_Master_Decal`.

* **Instances only** in levels; no per‑asset unique shaders.

* **Don’t:** full‑screen color‑grade swaps per room; do localized volumes.

## **8.20 Fonts, Licenses, Fallbacks**

* **Device UI (bitmap):** *VT323* (SIL OFL).

* **HUD/UI Sans:** *Inter* (SIL OFL).

* **Headings/Labels:** *IBM Plex Sans* (SIL OFL).

* **Monospace (debug):** *JetBrains Mono* (Apache 2.0).

* **Fallback stacks:**

  * Sans: `Inter, IBM Plex Sans, -apple-system, Segoe UI, Roboto, Arial, sans-serif`

  * Mono: `JetBrains Mono, Courier New, monospace`.

* If using commercial fonts, acquire licenses and update this section.

## **8.21 Asset Naming & Folders (UE5‑ready)**

**Folders** (`/Content/Diplomagic/...`):

* `Art/Characters`, `Art/Props`, `Art/Environments`, `Art/Materials`, `UI`, `VFX`, `Audio/SFX`, `Audio/Music`, `Audio/VO`, `Design/Blueprints`.

**Prefixes**: `SM_` StaticMesh, `SK_` SkeletalMesh, `T_` Texture, `M_` Material, `MI_` MaterialInstance, `NI_` Niagara, `BP_` Blueprint, `AN_` Anim, `S_` Sound, `CUE_` SoundCue, `UMG_` Widget.  
 **Examples**: `SM_Tunnel_Vent_Cap_A`, `T_UI_Device_Amber_01`, `S_UI_FieldPad_Click_A`, `CUE_Mx_Stealth_Pad_A`.

## **8.22 Budgets by Level Type (starting targets)**

| Level Type | Visible Tris/frame | Draw Calls | Texture Streaming Budget |
| ----- | ----- | ----- | ----- |
| Interior/Corridor | ≤ 0.8 M | ≤ 1,200 | ≤ 1.5 GB |
| Hub | ≤ 1.0 M | ≤ 1,500 | ≤ 2.0 GB |
| Exterior | ≤ 1.5 M | ≤ 1,800 | ≤ 2.5 GB |

Notes: tune with profiling; reserve headroom for VFX and AI.

## **8.23 Concept Art Package Checklist (per location)**

* Key art (wide, hero).

* Callouts: materials, signage, props.

* Palette swatches with hex.

* Turnarounds for hero props.

* Lighting moods: day/night/Kadath.

* Blockout plan overlay with routes.

* VFX and audio notes.

## **8.24 Deliverables (Art & Audio)**

* Mood boards and palette sheet.

* Kitbash packs per locale.

* VFX bible for Splinter.

* Audio style guide + cue sheet template.

* Wwise project skeleton and routing.

* Accessibility checklist.

## **8.25 Approvals**

On approval: archive to MASTER as `[SEC-08-ARTAUDIO] v0.2` and update manifest. Next: **SEC‑09 Technology & Performance**.

# **Patch Instructions for Existing MASTER — SEC-09**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-09-TECH |` and replace the entire line with:

`| SEC-09-TECH | Tech spec | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# SEC-08 — CH5–CH6 Audio & Soundscape
Repo dir: /Patches

## Pillars (no music bias)
- **1994 texture:** tape hiss, CRT hum, analog radio.  
- **Kadath motif:** distant horn-calls; low choral beds.  
- **Raid clarity:** readable tells for charges, valves, chant.

## Key cues
- **Phrase motif:** whisper layers of “the stars are right tonight” only in cult chant beds; never spoken by party/NPCs.  
- **Zombies:** wet shuffle, jaw clack; aggro swell at 2 kHz.  
- **Night Gaunt:** ceiling skitter, air split before dive.  
- **Cultist rite:** pulse drone + syllabic mutter; build to bell.  
- **Beast:** hoof scrape + bellow; rising whoosh on charge.  
- **Warden Shade:** glassy ring; null when Ward Jam active.  
- **Star Vampire:** phase shimmer; reveal snap with Lights/flare.  
- **Valve turn:** dry metal groan; in-order triad confirms A→B→C.  
- **Charge plant/det:** canvas rip + sticky whump; 2 s fuse tick.  
- **Blue-on-blue:** single staccato beep + hard fail sting.

## Spaces
- **Deep D-LAMP:** moist reverb, slow drips, fan thrum, O2 low tone.  
- **Iron Highway:** tire grit, tunnel slap, engine knock.  
- **Annex:** concrete slapback, distant K‑9 bark, breaker pop.  
- **Vault:** rotating catwalk clack, pylon hum, gimbal groan.

## Mix rules
- Prioritize tells over bed during combat.  
- Side-chain chants under gunfire by −6 dB.  
- Keep UI tones short, dry, mono. No modern whooshes.

## Implementation notes
- Loop stems ≤ 60 s; randomize heads/tails.  
- One-shot library tagged by enemy/event.  
- Memory budget conservative; reuse stems across CH5→CH6.

# SEC-08 — CH5–CH6 Audio & Soundscape
Repo dir: /Patches

## Pillars (no music bias)
- **1994 texture:** tape hiss, CRT hum, analog radio.  
- **Kadath motif:** distant horn-calls; low choral beds.  
- **Raid clarity:** readable tells for charges, valves, chant.

## Key cues
- **Phrase motif:** whisper layers of “the stars are right tonight” only in cult chant beds; never spoken by party/NPCs.  
- **Zombies:** wet shuffle, jaw clack; aggro swell at 2 kHz.  
- **Night Gaunt:** ceiling skitter, air split before dive.  
- **Cultist rite:** pulse drone + syllabic mutter; build to bell.  
- **Beast:** hoof scrape + bellow; rising whoosh on charge.  
- **Warden Shade:** glassy ring; null when Ward Jam active.  
- **Star Vampire:** phase shimmer; reveal snap with Lights/flare.  
- **Valve turn:** dry metal groan; in-order triad confirms A→B→C.  
- **Charge plant/det:** canvas rip + sticky whump; 2 s fuse tick.  
- **Blue-on-blue:** single staccato beep + hard fail sting.

## Spaces
- **Deep D-LAMP:** moist reverb, slow drips, fan thrum, O2 low tone.  
- **Iron Highway:** tire grit, tunnel slap, engine knock.  
- **Annex:** concrete slapback, distant K‑9 bark, breaker pop.  
- **Vault:** rotating catwalk clack, pylon hum, gimbal groan.

## Mix rules
- Prioritize tells over bed during combat.  
- Side-chain chants under gunfire by −6 dB.  
- Keep UI tones short, dry, mono. No modern whooshes.

## Implementation notes
- Loop stems ≤ 60 s; randomize heads/tails.  
- One-shot library tagged by enemy/event.  
- Memory budget conservative; reuse stems across CH5→CH6.

# SEC-08 — CH5–CH6 Audio & Soundscape
Repo dir: /Patches

## Pillars (no music bias)
- **1994 texture:** tape hiss, CRT hum, analog radio.  
- **Kadath motif:** distant horn-calls; low choral beds.  
- **Raid clarity:** readable tells for charges, valves, chant.

## Key cues
- **Phrase motif:** whisper layers of “the stars are right tonight” only in cult chant beds; never spoken by party/NPCs.  
- **Zombies:** wet shuffle, jaw clack; aggro swell at 2 kHz.  
- **Night Gaunt:** ceiling skitter, air split before dive.  
- **Cultist rite:** pulse drone + syllabic mutter; build to bell.  
- **Beast:** hoof scrape + bellow; rising whoosh on charge.  
- **Warden Shade:** glassy ring; null when Ward Jam active.  
- **Star Vampire:** phase shimmer; reveal snap with Lights/flare.  
- **Valve turn:** dry metal groan; in-order triad confirms A→B→C.  
- **Charge plant/det:** canvas rip + sticky whump; 2 s fuse tick.  
- **Blue-on-blue:** single staccato beep + hard fail sting.

## Spaces
- **Deep D-LAMP:** moist reverb, slow drips, fan thrum, O2 low tone.  
- **Iron Highway:** tire grit, tunnel slap, engine knock.  
- **Annex:** concrete slapback, distant K‑9 bark, breaker pop.  
- **Vault:** rotating catwalk clack, pylon hum, gimbal groan.

## Mix rules
- Prioritize tells over bed during combat.  
- Side-chain chants under gunfire by −6 dB.  
- Keep UI tones short, dry, mono. No modern whooshes.

## Implementation notes
- Loop stems ≤ 60 s; randomize heads/tails.  
- One-shot library tagged by enemy/event.  
- Memory budget conservative; reuse stems across CH5→CH6.

# [SEC-09-TECH] Technology & Performance Targets
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-07-UI` — UI/UX (Devices, HUD, Menus)
- `SEC-08-ARTAUDIO` — Art Direction & Audio
- `SEC-10-PRODUCTION` — Production Plan & Milestones
- `SEC-11-QA` — QA, Localization, Accessibility

## **9.1 Tech Stack**

* Engine: **Unreal Engine 5.6**.

* RHI: **DX12** on Windows; **Vulkan** optional.

* Middleware: **Wwise** (audio), Niagara (VFX).

* UI: UMG + Slate; bitmap device fonts per SEC‑07.

* Source control: **Perforce** recommended for binary assets; Git acceptable for code/tools if isolated.

* Build automation: Unreal Automation Tool (UAT) + CI runner (local or hosted).

* Scripting: Blueprints for gameplay glue; C++ for systems.

## **9.2 Platforms & Performance Targets**

| Platform | Resolution | FPS Target | Notes |
| ----- | ----- | ----- | ----- |
| PC min‑spec | 1080p | **60** | Low/Medium preset, baked GI, limited volumetrics |
| PC rec‑spec | 1440p | **60** | Medium/High, selective volumetrics |
| PC high‑end | 2160p | **60** | High, optional CRT filter |
| Consoles (post‑launch) | 1080p/1440p | **60** | Parity with PC Medium/High; dynamic res allowed |

## **9.3 Hardware Targets (PC)**

* **Minimum**: 4‑core CPU @3.2 GHz, 16 GB RAM, GPU \~ GTX 1060 / RX 580 (6–8 GB), SSD.

* **Recommended**: 6‑core CPU @3.6+ GHz, 32 GB RAM, GPU \~ RTX 3060 / RX 6700 XT (8–12 GB), SSD.

## **9.4 Rendering Pipeline**

* GI/Lighting: baked where stable; limited dynamic keys for patrols and flicker.

* Shadows: stationary for key lights; virtual shadow maps off on min‑spec.

* Lumen: **off**; Nanite: **off by default** (enable only for hero props if perf allows).

* Post: minimal bloom, low grain, vignette low; chromatic aberration **off**.

* AA: **TSR** default; TAAU fallback for upscaling.

* Fog/Volumetrics: budgeted per SEC‑08.

## **9.5 Performance Budgets (frame)**

* GPU time: **≤ 14 ms** @ 1080p min‑spec.

* CPU game + render: **≤ 16 ms** total @ 1080p.

* Draw calls: **≤ 1,200** interior, **≤ 1,800** exterior.

* Visible triangles: **≤ 0.8 M** interior, **≤ 1.5 M** exterior.

* Shadowed lights: **≤ 2** dynamic key, **≤ 6** stationary total.

* Skeletal meshes active: **≤ 20** interior, **≤ 35** exterior.

* Particles: see SEC‑08 caps (≤512 CPU, ≤20k GPU).

* Audio voices: **≤ 48** concurrent.

## **9.6 Memory & Streaming**

* System RAM: **≤ 8 GB** working set min‑spec.

* VRAM: **≤ 5 GB** min‑spec; **≤ 7 GB** rec.

* Texture streaming pool: **1.5 GB** interior, **2.5 GB** exterior.

* Async loading screens for large layer swaps (Kadath transitions).

* Pak chunking by chapter; shared core pak for devices/UI.

## **9.7 Scalability Presets**

* **Low**: baked GI only, no volumetrics, low post, 0.75 res scale allowed.

* **Medium**: limited volumetrics, medium shadows, SSR off.

* **High**: volumetrics on budget, higher shadow resolution, SSR low.

* **Accessibility**: high‑contrast UI skin, reduced flash, lower camera shake.

## **9.8 Save/Load & Data**

* Format: compressed JSON + binary blobs for maps; slots: **3 manual + autos**.

* Contents: caseboard graph, evidence chain states, heat/reputation, device unlock flags, AI snapshot.

* Integrity: checksum per slot; versioned schema.

## **9.9 Telemetry & QA**

* Telemetry events: evidence logged, arrest/kill outcomes, stealth resolution rate, mission duration, crashes.

* Storage: local JSON logs with opt‑in upload; anonymized session ID.

* Crash handling: UE Crash Reporter; symbols preserved per build.

* KPI gates mirror SEC‑04 and SEC‑05 targets.

## **9.10 Localization & Fonts**

* UE Localization Dashboard; cultures: en‑US base, configurable expansions.

* Device text uses resource keys; font fallbacks per SEC‑08.

* All strings ≤14 chars for device labels; wrap at 24–28 chars.

## **9.11 Accessibility Hooks**

* Global toggles: subtitles on, color‑blind safe palettes, reduced camera shake, reduced flashing, input remap, hold‑to‑press toggle.

* Device skins: Green/Amber/Gray with WCAG pairs per SEC‑08.

## **9.12 Networking & Online**

* Core game is offline.

* Optional telemetry upload and crash reports; no account system.

## **9.13 Mod Support (post‑EA)**

* Expose data tables, device skins, audio cue routing, and simple blueprint actors.

* Load loose content or external pak folder `Mods/`.

* Basic in‑menu mod list with enable/disable; no code plugins.

## **9.14 Source Control & Branching**

* **Perforce** depot layout: `//DIPLOMAGIC/Dev`, `//DIPLOMAGIC/Release`, `//DIPLOMAGIC/ArtDrop`.

* Branch model: main → release branches per milestone; cherry‑pick hotfixes.

* LFS/Git allowed only for tooling docs outside `.uproject`.

## **9.15 Build & Release**

* CI: per‑commit cooks for Windows Dev build; nightly cooked Editorless.

* Milestone builds signed and versioned: `v{MAJOR.MINOR.PATCH}_{YYYY-MM-DD}`.

* Art/audio validation step: reference scanner for textures, triangle budgets, loudness.

## **9.16 Compliance & Legal**

* Ratings targets: ESRB M / PEGI 18 (see SEC‑02).

* Licensing: verify font and SFX licenses per SEC‑08.

* Privacy: plain‑language prompt for telemetry; no PII.

## **9.17 Risks & Mitigations**

* **Perf regressions**: lock budgets; perf CI gate; capture baselines per level.

* **Shader compile hitches**: precompile PSO cache; share DDC.

* **Asset bloat**: enforce naming, LODs, streaming budgets; weekly report.

## **9.18 Deliverables**

* Perf budget worksheet per level.

* CI scripts and UAT configs.

* PSO cache and DDC sharing guide.

* Telemetry schema and dashboard spec.

* Localization glossary and test plan.

## **9.19 Approvals**

On approval: archive to MASTER as `[SEC-09-TECH] v0.1` and update manifest. Next: **SEC‑10 Production Plan & Milestones**.

# **Patch Instructions for Existing MASTER — SEC-10**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-10-PRODUCTION |` and replace the entire line with:

`| SEC-10-PRODUCTION | Production plan | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

### **9.x Device I/O & Storage (1994 constraints)**
- FieldPad storage via **PCMCIA Type‑II ATA/SRAM** or **CF Type‑I** using **CF→PC Card** adapter.
- Practical throughput ≤ 1–2 MB/s; photo write/read operations are slow.
- Photo caps aligned with TDD: ≤ 60 per mission, ~200 KB each.
- Connectors: **RJ‑11** for modem cards, **RJ‑45** for 10Base‑T NICs, optional **RS‑232 DE‑9** on device/dock.

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# [SEC-10-PRODUCTION] Production Plan & Milestones
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-08-ARTAUDIO` — Art Direction & Audio
- `SEC-09-TECH` — Technology & Performance Targets
- `SEC-11-QA` — QA, Localization, Accessibility
- `SEC-12-RISKS` — Risks, Legal, Ratings

## **10.1 Scope & Assumptions**

* Solo developer with targeted contractors.

* Tech per SEC‑09; art/audio per SEC‑08; systems per SEC‑05; loops per SEC‑04.

* Release track: **Demo Halloween 2025 → Early Access Q2 2026 → Full Release Q1 2027**.

* Platforms: PC at full release; consoles post‑launch.

## **10.2 Team & Vendors (baseline)**

| Role | Mode | Notes |
| ----- | ----- | ----- |
| Creative/Tech Director (Nick) | FT | Design, code, integration, PM |
| 3D Artist (environments/props) | Contract | 15–25 hrs/wk Nov’25–Oct’26 |
| Character Artist/Rigger | Contract | 8–12 wks across slice→beta |
| Animator | Contract | 10–15 hrs/wk Jan’26–Nov’26 |
| UI/UX Designer | Contract | 6–10 wks across SEC‑07 deliverables |
| Technical Artist (Shaders/VFX) | Contract | 6–8 wks for Splinter VFX + perf |
| Sound Designer | Contract | 12–16 wks spread; Wwise impl |
| Composer | Contract | 10–14 wks, stems system |
| QA Lead (external) | Vendor | 2× passes: EA and pre‑gold |
| Localization Vendor | Vendor | Strings, LQA pre‑gold |

## **10.3 High‑Level Schedule**

| Phase | Window | Goals |
| ----- | ----- | ----- |
| **P0 Pre‑Pro Refresh** | Aug–Sep 2025 | Lock GDD v1.0, pipelines, perf budgets |
| **P1 Vertical Slice** | Sep–Nov 2025 | 1 polished mission (Clara), core devices, HUD; **Demo Oct 31, 2025** |
| **P2 EA Core** | Dec 2025–May 2026 | Ship Ch1–3, core loops complete, tuning; **Early Access by Jun 2026** |
| **P3 Content Build‑out** | Jun–Oct 2026 | Add Ch4–5, NYC hub, re‑entry states; perf parity |
| **P4 Beta** | Nov–Dec 2026 | Feature‑complete, content‑complete; only bug/perf |
| **P5 Gold** | Jan–Mar 2027 | Cert‑ready PC build, marketing assets, launch ops |

## **10.4 Milestones — Entry/Exit & Deliverables**

### **M1: Vertical Slice (due Nov 15, 2025)**

**Entry:** SEC‑04/05 baseline implemented; device UI MVP; perf captures at target map.  
 **Exit:** One Clara mission shippable; TAPLINE scan+triangulate; FieldPad photo→tag→warrant; MEDSTAT triage; HUD minimal; controller parity; demo branch tagged.  
 **Deliverables:** Steam demo build, trailer cut, press kit v0.

### **M2: Early Access (due Jun 15, 2026)**

**Entry:** Ch1–3 playable end‑to‑end; caseboard saves; ROE loop stable.  
 **Exit:** Telemetry online (opt‑in), difficulty presets, accessibility baseline, crash‑free P90 ≥99.0%.  
 **Content:** \~7–9 missions; NYC tunnels preview; devices feature‑complete V1.  
 **Deliverables:** EA build, roadmap, patch plan, community guidelines.

### **M3: Content Expansion (Oct 31, 2026)**

**Entry:** Stable EA; art perf budget holding.  
 **Exit:** Add Ch4–5, hub re‑use loops, antagonist arcs Qi/Kent; arrest systems tuned; VO pass 1\.  
 **Deliverables:** Major content update, marketing beats, LQA plan.

### **M4: Beta (Dec 15, 2026)**

**Entry:** Feature‑complete; all chapters implemented.  
 **Exit:** Content‑complete; bug backlog triaged; crash‑free P90 ≥99.5%; perf budgets met; accessibility check pass.  
 **Deliverables:** Beta candidate builds, test plan, known issues.

### **M5: Gold (Mar 15, 2027)**

**Entry:** All Blocker/Critical fixed; audio mix final; balance locked.  
 **Exit:** Gold master signed; store assets delivered; mod tools beta post‑EA finalized.  
 **Deliverables:** Release build, soundtrack stems pack, press kit v1.0.

## **10.5 Content Quotas (targets)**

| Asset | Slice | EA | Beta/Gold |
| ----- | ----- | ----- | ----- |
| Missions (playable) | 1 | 7–9 | 13–16 |
| Unique locales | 1 | 4–5 | 7 |
| Devices apps | 3 | 6 | 6 + polish |
| Enemy archetypes | 2 | 4 | 6 |
| Weapons/tools | 3 | 6 | 8 |
| VO lines (approx) | 50 | 400 | 800 |

## **10.6 Budget Ranges (rough order)**

* Art external: $35–60k.

* Audio external (SFX+Music): $20–40k.

* QA+LQA vendor passes: $10–25k.

* Misc (licenses, marketing, services): $5–15k.

* Total external range: **$70–140k** over 18–20 months.

* Internal time: tracked via timesheets; opportunity cost not priced here.

## **10.7 Pipelines & PM**

* **Source control:** Perforce with streams; weekly checkpoint tags mirror GDD checkpoints.

* **Branches:** `Dev`, `Release/*`, `ArtDrop`.

* **Builds:** CI nightlies; slice/EA/beta/gold branches locked.

* **Tasking:** 2‑week sprints; Definition of Done includes perf + accessibility checks.

* **Reviews:** Milestone gates require KPI dashboard and perf captures.

## **10.8 QA Strategy**

* Unit smoke tests on devices and evidence chain.

* Checklists per SEC‑07/08/09.

* Telemetry review weekly during EA.

* External test passes: pre‑EA, pre‑beta, pre‑gold.

* Bug policy: Blocker/Critical stop the line; High within 72h; Medium within sprint; Low as capacity allows.

## **10.9 Localization**

* Scope: UI, menus, HUD, device text, subtitles.

* String freeze at Beta; LQA pass before Gold.

* Languages beyond en‑US determined by demand.

## **10.10 Marketing & Community**

* Demo + EA beats, devlogs, controlled roadmap.

* Clear mod policy; community standards.

## **10.11 Risks & Mitigations**

* **Contractor availability:** pre‑book, backups, reduce critical path coupling.

* **Perf misses:** enforce budgets, cut set‑dress, prioritize silhouettes.

* **Scope creep:** milestone gates with quota tables; defer to post‑launch.

## **10.12 Deliverables**

* Timeline Gantt (simple), resource plan, cost tracker, risk register, publisher one‑pager.

## **10.13 Approvals**

On approval: archive to MASTER as `[SEC-10-PRODUCTION] v0.1` and update manifest. Next: **SEC‑11 QA, Localization, Accessibility**.

# **Patch Instructions for Existing MASTER — SEC-11**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-11-QA |` and replace the entire line with:

`| SEC-11-QA | QA, loc, accessibility | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# [SEC-11-QA] QA, Localization, Accessibility
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-09-TECH` — Technology & Performance Targets
- `SEC-10-PRODUCTION` — Production Plan & Milestones
- `SEC-12-RISKS` — Risks, Legal, Ratings
- `SEC-13-APPENDICES` — Appendices

## **11.1 QA Strategy**

**Goals.** Ship a stable, readable, fair game that meets perf budgets and accessibility baselines.  
 **Approach.** Risk‑based testing on core loops (SEC‑04), systems (SEC‑05), UI (SEC‑07), art/audio (SEC‑08), and tech (SEC‑09).

**Test types**

* **Smoke** (per build): boot, load, start mission, exit.

* **Functional**: devices, evidence chain, ROE, stealth, combat, save/load, caseboard.

* **Systems**: AI perception, heat, reputation, telemetry events.

* **Performance**: FPS, frametime, draw calls, VRAM, CPU/GPU budgets.

* **Stability**: long‑session soak (2–3 h), repeated save/load, memory growth.

* **Regression**: checklist per feature after fixes.

* **Compatibility**: min/rec PC configs, gamepad parity.

**Entry/Exit gates**

* **Slice/EA/Beta** builds require: crash‑free P90 ≥ target, KPI deltas reported, no Blockers/Criticals open.

## **11.2 Bug Policy**

| Severity | Definition | SLA |
| ----- | ----- | ----- |
| **Blocker** | Crash/data loss, progress stop | Fix/rollback same day |
| **Critical** | Major system broken, mission cannot complete | 48–72 h |
| **High** | Significant feature defect or perf miss | Within sprint |
| **Medium** | Noticeable defect, workaround exists | As capacity allows |
| **Low** | Cosmetic, minor text, non‑blocking | Backlog |

Status flow: **New → Triaged → In‑Progress → Fixed → Verified → Closed**.  
 Repro format: build, map, steps, expected/actual, logs, attachments.

## **11.3 Test Matrices (core)**

**Devices**

* FieldPad: Photo→Tag→Chain, Links, Warrant score, Judge pass/fail.

* TAPLINE: Scan/Record/Triangulate/Decode/Spoof; warrant gating.

* MEDSTAT: status effects, triage actions, team telemetry (Avery), self‑care (Clara).

**Loops**

* Investigate→Act→Record; evidence used before action ≥70%.

* Clara stealth resolution ≥60%; Avery arrest:kill ≥2:1.

* Save/Load persists caseboard, evidence chain, heat/reputation, device unlocks.

**Performance**

* Interior: ≤ 0.8 M tris, ≤ 1,200 draws, GPU ≤ 14 ms @1080p min‑spec.

* Exterior: ≤ 1.5 M tris, ≤ 1,800 draws, GPU ≤ 14 ms @1080p.

* Audio voices ≤ 48; VFX caps per SEC‑08.

## **11.4 Telemetry & Crash**

* Events: evidence logged, warrant pass/fail, arrest/kill, stealth resolves, mission time, deaths, crashes.

* Local JSON logs; opt‑in upload; anonymized session ID.

* Crash Reporter enabled; symbols stored per build.

## **11.5 Accessibility (Checklist)**

**Global**

* Subtitles on by default with speaker tags.

* UI scale slider; minimum body size ≥ 12 px @1080p.

* Color‑blind safe glyphs; high‑contrast device skin (Gray).

* Toggle hold‑to‑press; remap all inputs.

* Reduce camera shake/flash options.

* Content warnings pre‑scene; skip with summary.

**Devices/UI**

* Tap targets ≥ 32×32 px @1080p; focus ring visible.

* WCAG AA text contrast per SEC‑08 pairs.

* Latency modeled but input buffered for accessibility mode.

**Audio**

* Dynamic range presets (Night/TV/Cinema).

* SFX ducking under dialogue; subtitle timing aligned.

**Difficulty**

* Aim assist, clue timers, device hinting, stealth forgiveness toggles.

* No forced QTEs without remap/hold options.

**QA acceptance**

* Accessibility smoke on every milestone build; defects tracked like functional bugs.

## **11.6 Localization Plan**

* **Scope:** UI, HUD, device text, tutorials, subtitles, store copy.

* **Pipeline:** UE Localization Dashboard → string tables; resource keys for device labels.

* **Length constraints:** device labels ≤ 14 chars; wrap at 24–28 chars.

* **Languages:** start en‑US → add by demand (e.g., de, fr, es‑LA, ja, zh‑CN).

* **Schedule:** string freeze at **Beta**; LQA before **Gold**.

**Deliverables**

* Master string table (CSV/PO).

* Glossary + style guide.

* Font fallback sets per SEC‑08.

* LQA test cases: device flows, HUD truncation, right‑to‑left audit if added.

## **11.7 Compliance & Ratings**

* ESRB M / PEGI 18 content guidance in SEC‑02.

* Privacy: clear telemetry consent; no PII logged.

* Licenses: fonts and SFX licenses tracked in SEC‑08.

## **11.8 Milestone QA Passes**

* **Pre‑EA:** full functional + perf + accessibility baseline.

* **Pre‑Beta:** regression, content‑complete sweep, LQA round 1\.

* **Pre‑Gold:** stability soak, perf locks, LQA final, accessibility sign‑off.

## **11.9 Approvals**

On approval: archive to MASTER as `[SEC-11-QA] v0.1` and update manifest. Next: **SEC‑12 Risks, Legal, Ratings**.

# **Patch Instructions for Existing MASTER — SEC-12**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-12-RISKS |` and replace the entire line with:

`| SEC-12-RISKS | Risks, legal, ratings | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# [SEC-12-RISKS] Risks, Legal, Ratings
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-10-PRODUCTION` — Production Plan & Milestones
- `SEC-11-QA` — QA, Localization, Accessibility
- `SEC-13-APPENDICES` — Appendices
- `SEC-14-QA` — Quality Assurance Test Plan

## **12.1 Key Risks Register**

| ID | Risk | Cat. | Prob. | Impact | Owner | Triggers | Mitigations |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| R‑01 | Scope creep across dual‑POV + devices | Prod | M | H | Nick | New features added post‑slice | Lock pillars; change‑control; defer to post‑launch |
| R‑02 | Performance misses on fog/VFX | Tech | M | H | Tech Art | GPU spikes; overdraw heatmaps | SEC‑08 caps; VFX budget gate; perf CI |
| R‑03 | Device UI overload/confusion | UX | M | M | UI | Playtest misuse \>5% | Progressive disclosure; tutorials via cases; accessibility mode |
| R‑04 | Procedural realism frustrates | Design | M | M | Design | Negative playtest verbatims | Optional briefs; hint tiers; difficulty sliders |
| R‑05 | Dual‑protagonist content debt | Prod | M | H | Nick | Slip on shared spaces re‑use | Shared locations; modular objectives; reuse kits |
| R‑06 | Legal/ratings issue (minors in peril) | Legal | L | H | Legal | Platform flag; ratings query | No on‑screen harm to minors; implied peril only; content warnings |
| R‑07 | Audio/Font licensing gaps | Legal | M | H | Audio/UI | Missing license docs | Use OFL/Apache fonts per SEC‑08; track SFX/music licenses; audit before beta |
| R‑08 | Contractor availability | Prod | M | M | PM | Missed sprint deliverables | Pre‑book alternates; flexible scope; buffer time |
| R‑09 | Save corruption/state bugs | Tech | L | H | Eng | Crash on load; bad schema | Versioned schema; autosave validation; load tests |
| R‑10 | Mod misuse (post‑EA) | Comm | L | M | PM | Offensive content shared | In‑menu warnings; disable online sharing; policy + moderation |
| R‑11 | Libel/brand infringement | Legal | L | H | Legal | Real brand slips in | Fictional brands; art review checklist; legal pass |
| R‑12 | Story/imagery controversy | PR | L | M | PM | Social media flare‑ups | Clear themes doc; content toggles; press kit Q\&A |

## **12.2 Legal & Compliance Checklist**

**IP & Contracts**

* Wordmark **DIPLOMAGIC**: run clearance search; consider TM file (Nice Class 9, 41).

* Work‑for‑hire + IP assignment for all contractors; NDAs as needed.

* Model/voice releases for VO.

* Avoid real organizations/brands; use fictional names (e.g., Brightstar).

**Licenses**

* Fonts: VT323, Inter, IBM Plex Sans, JetBrains Mono (open licenses) — see SEC‑08. Store license files in `/Docs/Licenses/`.

* SFX/Music: track sources and rights; prefer custom or CC‑BY/royalty‑free with commercial allowance. No viral copyleft for shipped audio.

* Software: comply with UE5/Marketplace EULAs; track any OSS (MIT/BSD/Apache) with NOTICE file.

**Privacy & Telemetry**

* Opt‑in only. No PII. Random session IDs. Retention ≤ 180 days. Plain‑language consent screen.

* Crash reports scrubbed of usernames/paths where possible.

**Accessibility & Claims**

* Do not state compliance beyond tested features. Publish an accessibility features list matching SEC‑07/11.

**Export/Regulatory**

* Standard US export compliance. No encryption beyond engine defaults.

**Platforms (PC)**

* Steam/Epic checklists: save path, controller prompts, crash reporter, quit to desktop, high‑DPI icon, privacy text.

## **12.3 Ratings Strategy (Targets)**

**ESRB:** **Mature 17+** expected. Likely content descriptors: *Violence*, *Blood*, *Strong Language*, *Intense Violence (select scenes)*.  
 **PEGI:** **18** likely for violence/horror intensity.

**Design guardrails**

* No sexual content. No torture‑porn.

* **Minors:** no graphic harm on‑screen; peril implied or off‑screen only; fade/abstraction when needed.

* Reduced‑gore toggle and content warnings (scene‑specific).

* Language filtered to maintain target rating.

**Submission kit**

* Unedited gameplay video of representative scenes (stealth, arrest, combat, Kadath).

* Written content questionnaire aligned to above guardrails.

## **12.4 Sensitive Content & Ethics**

* Law enforcement portrayal: procedural focus without endorsing brutality; ROE enforced; arrests preferred.

* Cult imagery: fictional symbols; avoid real‑world groups.

* Real places/people: fictionalized locales; no real persons implied.

## **12.5 Paperwork & Templates**

* Contractor MSA + SOW templates.

* VO agreement and rate card.

* Music commission agreement with deliverables (stems, looping).

* Asset ingestion checklist (naming, LODs, loudness, licenses).

* OSS NOTICE and third‑party attributions file.

## **12.6 External Reviews (Pre‑Gold)**

* Legal read‑through of narrative and UI text.

* License audit for fonts/SFX/music.

* Ratings pre‑submission check.

* Accessibility review against published features list.

## **12.7 Deliverables**

* Risk register spreadsheet (live).

* Legal/licenses binder.

* Ratings submission pack.

* Accessibility features list for store pages.

* Press kit Q\&A on themes and guardrails.

## **12.8 Approvals**

On approval: archive to MASTER as `[SEC-12-RISKS] v0.1` and update manifest. Next: **SEC‑13 Appendices**.

# **Patch Instructions for Existing MASTER — SEC-13**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-13-APPENDICES |` and replace the entire line with:

`| SEC-13-APPENDICES | Appendices | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# [SEC-13-APPENDICES] Appendices
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-11-QA` — QA, Localization, Accessibility
- `SEC-12-RISKS` — Risks, Legal, Ratings
- `SEC-14-QA` — Quality Assurance Test Plan
- `TDD-EVIDENCE+FIELDPAD` — Technical Design Document

## **13.1 Glossary**

* **Caseboard**: Graph of evidence, persons, locations, threads.

* **Chain‑of‑custody**: Steps that keep A‑tier evidence valid.

* **Heat**: Systemic alert level from player actions.

* **Kadath (New/Unknown)**: Liminal layers affecting space, rules.

* **MEDSTAT / FieldPad / TAPLINE**: Devices for vitals, casework, signals.

## **13.2 Acronyms**

| Term | Meaning |
| ----- | ----- |
| AA | Anti‑Aliasing |
| DDC | Derived Data Cache |
| EA | Early Access |
| GI | Global Illumination |
| KPI | Key Performance Indicator |
| LOD | Level of Detail |
| LUFS | Loudness Units Full Scale |
| POI | Point of Interest |
| PSO | Pipeline State Object |
| ROE | Rules of Engagement |
| RTPC | Real‑Time Parameter Control |

## **13.3 Data Schemas (authoritative keys)**

**Evidence Item (save/telemetry)**

{

  "id": "A-014",

  "tier": "A|B|C",

  "quality": 78,

  "chain": {"photo": true, "collect": true, "bag": true, "tag": true, "log": true, "sealIntact": true},

  "links": ["case:82", "victim:2", "loc:locker3"],

  "contam": 0,

  "time": "1994-10-31T14:41:00Z"

}

**Caseboard Node/Edge**

{

  "nodes": [{"id": "victim:2", "type": "person"}, {"id": "evidence:A-014", "type": "evidence"}],

  "edges": [{"from": "victim:2", "to": "evidence:A-014", "rel": "linked"}]

}

**Telemetry Event (subset)**

[

  {"evt": "evidence\_logged", "id": "A-014", "mission": "CH1\_KidsKamp"},

  {"evt": "arrest", "npc": "guard\_03", "nonlethal": true},

  {"evt": "stealth\_resolve", "mode": "bypass"}

]

## **13.4 Checklists**

**Level Readability**

* Silhouettes readable at min spec.

* Patrol lines and cover affordances obvious.

* Fog volumes tuned; no glare hotspots.

**Device UX**

* Nav path discoverable within 6 s.

* Tap targets ≥32×32 px @1080p.

* Error states readable; destructive ops confirmed.

**Performance Pass**

* Tris/DC within SEC‑08/09 caps.

* GPU ≤14 ms @1080p min spec.

* Audio voices ≤48; particle caps met.

**Accessibility**

* Subtitles on; UI scale works.

* High‑contrast skin verified.

* Camera shake/flash reduction toggles.

## **13.5 Tuning Tables (defaults)**

| Parameter | Default | Notes |
| ----- | ----- | ----- |
| Detection base | 0.35 | Stealth visibility curve start |
| Noise budget walk/crouch/sprint | 5 / 2 / 12 | dB‑like units |
| Arrest surrender base | 0.25 | Avery compliance check |
| Evidence BaseTier A/B/C | 50 / 30 / 15 | See SEC‑05 |

## **13.6 Input Reference**

**Keyboard/Mouse**: WASD move, Q/E lean, C crouch, Z prone, F interact, R reload, 1–4 quick slots, Tab device pane, M map, Esc pause.  
 **Gamepad**: LS move, RS look, LB/RB cycle, LT aim, RT fire/apply, Y device swap, X interact, A confirm, B back.  
 **Avery**: Hold T challenge, G cuff.  
 **Clara**: Hold G place trap, V whistle.

## **13.7 Versioning & Build IDs**

* Scheme: `vMAJOR.MINOR.PATCH_YYYY‑MM‑DD` (e.g., `v1.0.0_2025‑10‑31`).

* Branch map: Dev → Release/* → hotfix tags.

* Changelogs per section using IDs `[SEC‑NN‑TAG]`.

## **13.8 Repository & Paths (UE5)**

/Content/Diplomagic/

  Art/{Characters,Props,Environments,Materials}

  UI/

  VFX/

  Audio/{SFX,Music,VO}

  Design/Blueprints/

/Docs/{GDD, Licenses, Style, Build}

## **13.9 Store Page Content Warnings (template)**

Contains intense violence, blood, strong language, and horror themes. No on‑screen harm to minors. Options include reduced‑gore and content warnings.

## **13.10 Contractor Handoff Pack**

* Current GDD sections.

* References (SEC‑08).

* Naming + folder rules.

* Budgets and KPIs.

* Sample assets and target captures.

## **13.11 Third‑Party & OSS Attributions**

* Fonts: VT323 (SIL OFL), Inter (SIL OFL), IBM Plex Sans (SIL OFL), JetBrains Mono (Apache 2.0).

* Engine and Marketplace items per their EULAs.

* Maintain `/Docs/Licenses/NOTICE.md`.

## **13.12 UI String Keys**

* Pattern: `ui.<area>.<screen>.<element>`

* Example: `ui.fieldpad.evidence.link_button`

## **13.13 Milestone Manifest & Changelog**

| Section | Version | Date | Summary |
| ----- | ----- | ----- | ----- |
| SEC‑01‑FRONT | v0.2 | 2025‑08‑11 | Exec summary finalized |
| SEC‑02‑PILLARS | v0.1 | 2025‑08‑11 | Pillars/audience |
| … | … | … | … |

## **13.14 Contacts**

* Owner: Nick Goldman — design, tech, approvals.

* External: to be filled per contract.

## **13.15 Figures & Diagrams**

* **UML**: `Diplomagic_UML.drawio`, `Statlines_and_Environmental_Systems.drawio` → export **PNG/PDF** for inclusion.

* Loop diagrams (SEC‑04), device flows (SEC‑07).

## **13.16 Templates (files to create)**

* `Docs/Templates/bug_report.md`

* `Docs/Templates/art_hand-off.md`

* `Docs/Templates/audio_cue_sheet.csv`

* `Docs/Templates/changelog.md`

## **13.17 Approvals**

On approval: archive to MASTER as `[SEC-13-APPENDICES] v0.1` and update manifest.

# [SEC-14-QA] Quality Assurance Test Plan
Version: v0.1  
Date: 2025-08-12  
Owner: Nick Goldman

### Related sections
- `SEC-12-RISKS` — Risks, Legal, Ratings
- `SEC-13-APPENDICES` — Appendices
- `TDD-EVIDENCE+FIELDPAD` — Technical Design Document

Scope: end‑to‑end QA for PC builds. Aligns with SEC‑06/07/08/09/11/13 and PKG‑BUILD‑SOP.

## **14.0 Objectives**

* Find and prevent regressions that block play, performance, or accessibility.

* Keep shipping confidence high through automated and manual coverage.

* Produce repeatable evidence for compliance and marketing capture.

## **14.1 Definitions**

* **P1/P2/P3** severity; **Blocker/Major/Minor**.

* **Golden Path**: curated story progression per level for perf capture.

* **Perf Spot**: fixed coordinates/angles for comparable captures.

## **14.2 Test Types**

* **Automation:** boot, menu flows, devices (FieldPad/TAPLINE/MEDSTAT), save/load, controller hot‑swap.

* **Functional:** mission flows, evidence chain steps, warrants, TAPLINE, MEDSTAT.

* **Compatibility:** min/mid/high PC configs; windowed/fullscreen; input devices.

* **Performance:** frame time med/95p at perf spots; streaming boundaries.

* **Stability:** long‑run soak; save/load loops.

* **Localization/LQA:** layout, truncation, glyph coverage.

* **Accessibility:** AX‑matrix from SEC‑11; subtitles, UI scale, reduced‑horror, color‑independent cues.

* **Compliance:** CM‑matrix from SEC‑11.

## **14.3 Environments**

* **OS:** Windows 10/11.

* **Hardware tiers:**

  * **Min:** GTX 970 / RX 570, 8 GB RAM, HDD/SSD SATA.

  * **Mid:** GTX 1660 / RX 6600, 16 GB RAM, SATA SSD.

  * **High:** RTX 3060+ / RX 6700+, 16–32 GB, NVMe.

* **Displays:** 1080p required; check 1440p/4K scaling.

* **Input:** KBM, Xbox/PS controller; hot‑plug tests.

## **14.4 Tools & Data**

* UE automation framework; replay recorder; stat dumps; CSV exporters.

* Crash reporter with symbols; minidumps stored.

* Telemetry staging endpoint for canary events (SEC‑13).

* Screenshot script for shotlist (press kit).

## **14.5 Bug Workflow**

* Tracker states: **New → Triaged → In‑Progress → Ready‑for‑QA → Verified/Failed → Closed**.

* Required fields: build ID, map, steps, expected, actual, severity, repro rate, attachments.

* SLA targets: P1 fix attempt ≤ 48h; P2 within next sprint; P3 on backlog.

## **14.6 Entry/Exit Criteria**

* **Sprint Entry:** latest dev build boots; smoke tests pass.

* **Sprint Exit:** P1=0, P2≤10, perf within budgets on mid tier, CM/AX reds=0.

* **Milestone Exit:** all sprint exits + capture pack updated + SEC‑11 evidence archived.

## **14.7 Test Suites (high level)**

* **TS‑BOOT:** cold boot to menu; crash reporter check; save path permissions.

* **TS‑UI:** HUD prompts, menus, options, remap, glyph swap.

* **TS‑DEV‑FIELD:** FieldPad camera→Tag→Bag→Log; Caseboard; Warrant Builder WS.

* **TS‑DEV‑TAPLINE:** ping→triangulate→seize; icon state changes; toasts.

* **TS‑DEV‑MEDSTAT:** self‑care, Reddy check, stabilize.

* **TS‑MISSIONS:** per‑level objective flow, stealth/breach alt paths, re‑entry states.

* **TS‑SAVE:** slot create/load/delete; atomic write; backup restore.

* **TS‑PERF:** perf spots captures; heatmap boundaries.

* **TS‑AX:** subtitles, UI scale, high‑contrast skin, reduced‑horror, color‑independent cues.

* **TS‑LOC:** pseudoloc, truncation, font fallback.

* **TS‑COMPLIANCE:** CM matrix runs.

## **14.8 Perf Spots (initial)**

| ID | Map | Coords | Notes |
| ----- | ----- | ----- | ----- |
| PS‑L01‑LOT | L‑01 Kids Kamp lot | (x,y,z) TBD | Exterior cones/fog check |
| PS‑L03‑RD | Backwoods road bend | (x,y,z) TBD | Streaming boundary |
| PS‑L06‑TUN | NYC steam tunnel hub | (x,y,z) TBD | Dynamic lights |
| PS‑L07‑ASC | Transdimensional complex | (x,y,z) TBD | Kadath VFX |

## **14.9 Accessibility Tests (AX)**

* **AX‑001:** Subtitles default ON; size slider works; speaker tags visible.

* **AX‑002:** UI scale 0.85–1.50; no clipping at extremes.

* **AX‑003:** High‑contrast device skin selectable; persists.

* **AX‑004:** Status uses shapes/icons not color alone.

* **AX‑005:** Reduced‑horror swaps audio/visual spikes; summary page on skip.

* **AX‑006:** Hold→Press/Toggle available and functional.

* Evidence: screenshots + short videos archived to `/Compliance/AX/`.

## **14.10 Compliance Tests (CM)**

* Follow SEC‑11 CM‑001..010; evidence archived to `/Compliance/CM/` with build ID and date.

## **14.11 Localization & LQA**

* Pseudoloc pass before LQA.

* LQA smoke on Beta: layout, truncation, context tags, cultural flags logged.

## **14.12 Soak & Stability**

* 2‑hour idle and traversal; memory growth monitored; save/load loop every 10 min.

## **14.13 Regression Strategy**

* Tag failing tests; auto‑replay affected missions; compare perf spot CSVs.

* Diff localization assets after string changes.

## **14.14 Reporting**

* Daily: open bugs by severity, crash rate, perf med/95p deltas.

* Weekly: CM/AX status, risk list, burn‑down chart.

## **14.15 Deliverables**

* Test plan DOCX, suites checklist CSV, perf capture CSV templates, evidence folder tree.

* On approval: export DOCX (full + subsections) and ZIP with templates.

# **Patch Instructions — Support Doc: TDD‑EVIDENCE+FIELDPAD**

## **1) Archive as standalone support doc**

Create/Update the **Support Docs** index and add this row:  
 `| TDD-EVIDENCE+FIELDPAD | Technical Design — Evidence & FieldPad | v0.1 | 2025-08-11 | approved | archived |`

## **2) Append the approved content (add a `` before it)**
