# DIPLOMAGIC — Combined GDD Export
Generated: 2025-08-14 06:48:34 UTC

---

## Table of Contents
- [SEC-01-FRONT — Front Matter & Executive Summary](#sec-01-front)- [SEC-02-PILLARS — Pillars & Audience](#sec-02-pillars)- [SEC-03-NARRATIVE — Narrative](#sec-03-narrative)- [SEC-04-LOOPS — Core Gameplay Loops](#sec-04-loops)- [SEC-05-SYSTEMS — Systems & Mechanics](#sec-05-systems)- [SEC-06-WORLD — World, Levels, & Content](#sec-06-world)- [SEC-07-UI — UI/UX (Devices, HUD, Menus)](#sec-07-ui)- [SEC-08-ARTAUDIO — Art Direction & Audio](#sec-08-artaudio)- [SEC-09-TECH — Technology & Performance Targets](#sec-09-tech)- [SEC-10-PRODUCTION — Production Plan & Milestones](#sec-10-production)- [SEC-11-QA — QA, Localization, Accessibility](#sec-11-qa)- [SEC-12-RISKS — Risks, Legal, Ratings](#sec-12-risks)- [SEC-13-APPENDICES — Appendices](#sec-13-appendices)- [SEC-14-QA — Quality Assurance Test Plan](#sec-14-qa)
---

<a id="sec-01-front"></a>
# [SEC-01-FRONT] Front Matter & Executive Summary
Version: v0.2  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-02-PILLARS — Pillars & Audience`
- `SEC-03-NARRATIVE — Narrative`
- `SEC-04-LOOPS — Core Gameplay Loops`

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

---

<a id="sec-02-pillars"></a>
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

---

<a id="sec-03-narrative"></a>
# [SEC-03-NARRATIVE] Narrative
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-02-PILLARS — Pillars & Audience`
- `SEC-04-LOOPS — Core Gameplay Loops`
- `SEC-05-SYSTEMS — Systems & Mechanics`

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

---

<a id="sec-04-loops"></a>
# [SEC-04-LOOPS] Core Gameplay Loops
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-03-NARRATIVE — Narrative`
- `SEC-05-SYSTEMS — Systems & Mechanics`
- `SEC-06-WORLD — World, Levels, & Content`

## **4.1 Overview**

Loops connect investigation, stealth/combat, and narrative progression. Avery \= procedural agency within ROE. Clara \= survival agency under scarcity. Both feed the shared world state and ending matrix.

## **4.2 Moment‑to‑Moment Loop**

Primary verbs: observe, collect, infer, act, record, move.

\[Observe\] → \[Collect Evidence\] → \[Evaluate Risk\] → \[Act (Stealth/Combat/Dialogue)\]

         ↘                                          ↗

           \[Record in FieldPad\] ← \[Update World/AI State\] ← \[Relocate\]

**Guardrails**

* Evidence first. Action without intel raises risk and cost.

* Devices are the UI. Non‑diegetic assists stay minimal.

**Success Criteria**

* Player logs evidence in ≥80% of missions before major actions.

## **4.3 Mission Loop (POV‑specific)**

**Avery (FBI)**

\[Brief/Case Intake\] → \[Legal Prep (warrant/ROE)\] → \[Travel/Loadout\]

      → \[Recon\] → {Branch: Infiltrate | Knock/Breach} → \[Secure/Arrest\]

      → \[Scene Processing\] → \[Debrief/Casefile\]

**Clara (Survival)**

\[Immediate Need (Protect Reddy)\] → \[Scavenge/Route Plan\] → \[Infiltrate/Bypass\]

      → \[Avoid/Disable Threat\] → \[Extract\] → \[Recuperate/Journal\]

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

\[Shadow/Noise Mgmt\] → \[Intel Peek\] → \[Path/Create Distraction\] → \[Bypass/Isolate\]

        ↖——————————————————————\[Break LOS\]/\[Hide\]———————————————————————↗

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

---

<a id="sec-05-systems"></a>
# [SEC-05-SYSTEMS] Systems & Mechanics
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-04-LOOPS — Core Gameplay Loops`
- `SEC-06-WORLD — World, Levels, & Content`
- `SEC-07-UI — UI/UX (Devices, HUD, Menus)`

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

* ChainBonus: \+0–20 if bag→tag→log completed in **FieldPad**.

* ContamPenalty: −0–25 for mishandling or broken seals.

* TimeDecay: −0–10 if perishable and delayed.

* CrosslinkBonus: \+0–15 if connected to ≥2 corroborating items.

**Chain of Custody (Avery)**

1. Photograph in place → 2\) Collect with gloves → 3\) Bag & seal → 4\) Tag ID → 5\) Log in FieldPad → 6\) Transfer receipt.  
    Breaks invalidate A‑tier gates until remedied by supervisor sign‑off.

## **5.8 TAPLINE (Signals) — Mechanics**

* Bands: VHF/UHF, cordless phones, pagers, analog trunked radio.

* Modes: **Scan**, **Record**, **Triangulate**, **Spoof** (Avery only), **Decode** (DTMF/FSK).

* Minigame: lock to frequency, maintain signal quality; terrain occlusion affects SNR.

* Warrants: evidence threshold `Q ≥ 60` unlocks lawful intercept; otherwise limited to exigent use with risk.

## **5.9 FieldPad (Casework) — Mechanics**

* Apps: Camera, Evidence, Caseboard, Warrant Builder, Map, Contacts.

* Warrant Builder: template \+ probable cause fields; auto‑pulls linked evidence; judge approval simulated via score.

* Caseboard: nodes and threads; inference suggestions with uncertainty badges.

## **5.10 MEDSTAT (Vitals) — Mechanics**

* Tracks HP, Pain, Blood Loss, Stress, Fatigue.

* Triage actions: bandage, tourniquet, analgesic, stimulant, sedative.

* Team telemetry: Avery can issue commands when teammates are within range; Clara uses self‑care only.

## **5.11 Inventory, Crafting, Economy**

* **Slots \+ Weight** hybrid. Quick slots: 4\. Backpack tiers affect capacity.

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

---

<a id="sec-06-world"></a>
# [SEC-06-WORLD] World, Levels, & Content
Version: v0.1 • 2025-08-11  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-04-LOOPS — Core Gameplay Loops`
- `SEC-05-SYSTEMS — Systems & Mechanics`
- `SEC-07-UI — UI/UX (Devices, HUD, Menus)`
- `SEC-08-ARTAUDIO — Art Direction & Audio`
- `SEC-09-TECH — Technology & Performance Targets`

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

* Readable austerity: PS1-era silhouettes \+ modern lighting.

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
| Ch4 | NYC Tunnels \+ surreal | 2 | Swap cadence tighter |
| Ch5 | NYC hub \+ prior sites | 2–3 | Rogue Avery, open returns |
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

On approval: archive to MASTER as \[SEC-06-WORLD\] v0.1 and update manifest. Next: SEC-07 UI/UX.

# **Patch Instructions for Existing MASTER — SEC-07**

## **1\) Replace this single manifest row**

Find the row that begins with `| SEC-07-UI |` and replace the entire line with:

`| SEC-07-UI | UI/UX | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2\) Append this section to the end of MASTER (add a `
` before it)**

\[\[PAGEBREAK\]\]

---

<a id="sec-07-ui"></a>
# [SEC-07-UI] UI/UX (Devices, HUD, Menus)
Version: v0.1 • 2025-08-11  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-05-SYSTEMS — Systems & Mechanics`
- `SEC-06-WORLD — World, Levels, & Content`
- `SEC-08-ARTAUDIO — Art Direction & Audio`
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`

## **7.1 Goals & Principles**

* Diegetic first. Devices (FieldPad, TAPLINE, MEDSTAT) are primary UI.

* 1994 constraints. Limited color, latency, coarse hit targets, period affordances.

* Readability over spectacle. PS1‑era silhouettes \+ modern clarity.

* Minimal HUD. Surface only actionable state.

* Accessibility from day one.

## **7.2 Visual Language**

**Palette.** HUD: 1 accent \+ neutrals. Devices: two‑tone skins (Green, Amber, Gray).
 **Type.** Bitmap sans for devices; clean sans for HUD. Minimum 12 px at 1080p equivalent.
 **Grid.** Virtual 320×240 device canvas, 8 px base unit; HUD uses 12‑pt safe margins.
 **Iconography.** Stroke icons, 1 px weight at 1080p, scale by step 1.25×.

## **7.3 Global HUD (contextual, minimal)**

* **Top‑left:** Objective stub \+ sub‑task dot list.

* **Bottom‑left:** Health bar \+ vitals pill. Clara shows **Stress**; Avery shows **Armor**.

* **Bottom‑right:** Ammo/weapon or tool readout.

* **Center‑low:** Interaction prompt with verb \+ hold meter where needed.

* **Stealth:** eye glyph (visibility), waveform glyph (noise).

* **Heat/Reputation:** small indicator in map/caseboard, not moment‑to‑moment.

Example HUD overlay (schematic):

\[OBJ\] Kids Kamp: Extract Reddy

  • Unlock north gate  ◻

  • Avoid patrols       ■

ꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏ (screen)

\[HP ████▌\]  \[VIS ◐\]\[NOISE ≈≈\]                             \[9× .38 | ■■■■\]

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

│ \[Camera\] \[Evidence\] \[Caseboard\]           │

│ \[Warrant\] \[Map\]      \[Contacts\]           │

│                                            │

│ Tips: Complete bag→tag→log for A‑tier     │

└◀ BACK                            OK ▶──────┘

FieldPad — EVIDENCE (item view)

┌───────────── EVIDENCE: BAG \#A‑014 ─────────┐   ▂▃▅  ■■■■  ▮▮▮▮  14:41

│ Photo: IMG\_0142  \[View\]                    │

│ Type: Fiber (A‑tier)                       │  Q: 78

│ Chain: Photo → Collect → Bag → Tag → Log   │  Seal: ▣ Intact

│ Links: Case \#82 • Victim \#2 • Locker 3     │

│ Notes:                                     │

│  − Found under vent panel                  │

└◀ BACK                   \[LINK\]   OK ▶──────┘

FieldPad — WARRANT BUILDER

┌────────────── WARRANT BUILDER ─────────────┐   ▂▃▅  ■■□□  ▮▮▮▯  15:06

│ Case: \#82  Judge: S. Hartford              │  Score: 62 (PASS)

│ Probable Cause:                            │

│  \[ \] Evidence A‑014 (fiber)                │

│  \[ \] Intercepts TPL‑07                     │

│  \[ \] Statement W‑03                        │

│ Affidavit Text:                            │

│  \> Suspect used south entrance…            │

└◀ BACK                 \[SUBMIT\]   OK ▶──────┘

### **7.4.2 TAPLINE — Signals**

**Purpose.** Scan, record, triangulate, spoof, and decode era radios/phones.
 **Modes.** Scan • Record • Triangulate • Decode • Spoof (Avery only).

TAPLINE — SCAN

┌──────────────── TAPLINE: SCAN ─────────────┐   ▂▃▅  ■■□□  ▮▮▮▯  22:18

│ Band: UHF  |  Freq: 462.6125 MHz           │  SNR: ▓▓▓▒▒

│ \[◀\] 462.6000 ◁▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▷ 462.6500 \[▶\]

│ Hold to lock: ████▒▒                       │

│ Hits:  19:32  "Gate open"                   │

│        19:35  DTMF: 4 1 2                  │

└◀ BACK                 \[RECORD\]   OK ▶──────┘

TAPLINE — TRIANGULATE

┌───────────── TAPLINE: TRIANGULATE ─────────┐   ▂▃▅  ■■□□  ▮▮▮▯  22:26

│ Node A  ▣  Node B  ▢  Node C  ▢             │  Fix: 48%

│ Bearings: A 062° • B 239° • C  —           │

│ Map:  \[A───────╳────────B\]                  │

│        Clara route  \[ \]  Avery route \[x\]    │

└◀ BACK                  \[PING\]    OK ▶──────┘

### **7.4.3 MEDSTAT — Vitals & Team**

**Purpose.** Health, status effects, triage, and telemetry.
 **States.** Stable • Wounded • Critical • In Shock • Infected • Contaminated.

MEDSTAT — VITALS

┌──────────────── MED•STAT ──────────────────┐   ▂▃▅  ■■■■  ▮▮▮▯  02:14

│ Patient: AVERY     Armor: ▣▣▢               │

│ HP █████░  Pain ▓▓  Stress ▓                 │

│ Blood Loss: Arm ▪▪  Leg ▪  Torso ▪▪         │

│ Status: Wounded (Bleeding)                  │

│ Actions: \[Bandage\] \[Tourniquet\] \[Analgesic\] │

└◀ BACK                 \[APPLY\]    OK ▶──────┘

## **7.5 Menus & Screens**

* **Pause.** Resume, Save, Load, Options, Accessibility, Quit.

* **Inventory.** Slots \+ Weight hybrid; quick slots ×4.

* **Caseboard.** Graph of nodes and links; filter by time, tier, POV.

* **Map.** Layered (Real, New Kadath, Unknown); TAPLINE nodes and search areas.

Inventory (schematic)

┌──────────────── INVENTORY ────────────────┐

│ Weight: 62%   Quick: \[1\]\[2\]\[3\]\[4\]         │

│ Backpack: MED                              │

│ Items:                                     │

│  ▣ Lockpicks (x3)  ▣ Glass Shards (x6)    │

│  ▣ .38 Rounds (9)  ▣ Tourniquet (1)       │

│  ▣ Evidence A‑014  ▣ Tape Recorder        │

└◀ BACK                 \[ASSIGN\]   OK ▶─────┘

Caseboard (schematic)

\[Case \#82\]

  (Victim \#2)───(Fiber A‑014)───(Vent South)

        │              │               \\

     (W‑03)         (TPL‑07)          (Locker 3\)

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

## **1\) Replace this single manifest row**

Find the row that begins with `| SEC-08-ARTAUDIO |` and replace the entire line with:

`| SEC-08-ARTAUDIO | Art direction and audio | v0.2 | 2025-08-11 | approved | archived to Master |`

## **2\) Append this section to the end of MASTER (add a `
` before it)**

\[\[PAGEBREAK\]\]

---

<a id="sec-08-artaudio"></a>
# [SEC-08-ARTAUDIO] Art Direction & Audio
Version: v0.2  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-06-WORLD — World, Levels, & Content`
- `SEC-07-UI — UI/UX (Devices, HUD, Menus)`
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`



## **8.1 Visual Pillars**

* PS1‑era austerity \+ modern clarity (fog, lights, post).

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

████ Splinter Black \#0B0B0E   ████ Fog Gray \#8D9199   ████ Concrete \#5E666F

████ Steel Blue    \#3B5368   ████ Sodium Amber \#C48A1B ████ Emergency Red \#B21E2B

████ FieldPad Green \#1C6B3C  ████ TAPLINE Amber \#D09A2A ████ MEDSTAT Gray \#C7C9CC

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

* **Slate:** soft clap \+ verbal slate at start of each scene.

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

* Audio style guide \+ cue sheet template.

* Wwise project skeleton and routing.

* Accessibility checklist.

## **8.25 Approvals**

On approval: archive to MASTER as `[SEC-08-ARTAUDIO] v0.2` and update manifest. Next: **SEC‑09 Technology & Performance**.

---

<a id="sec-09-tech"></a>
# [SEC-09-TECH] Technology & Performance Targets
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-07-UI — UI/UX (Devices, HUD, Menus)`
- `SEC-08-ARTAUDIO — Art Direction & Audio`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-12-RISKS — Risks, Legal, Ratings`

## **9.1 Tech Stack**

* Engine: **Unreal Engine 5.6**.

* RHI: **DX12** on Windows; **Vulkan** optional.

* Middleware: **Wwise** (audio), Niagara (VFX).

* UI: UMG \+ Slate; bitmap device fonts per SEC‑07.

* Source control: **Perforce** recommended for binary assets; Git acceptable for code/tools if isolated.

* Build automation: Unreal Automation Tool (UAT) \+ CI runner (local or hosted).

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

* CPU game \+ render: **≤ 16 ms** total @ 1080p.

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

* Format: compressed JSON \+ binary blobs for maps; slots: **3 manual \+ autos**.

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

---

<a id="sec-10-production"></a>
# [SEC-10-PRODUCTION] Production Plan & Milestones
Version: v0.1 • 2025-08-11  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-08-ARTAUDIO — Art Direction & Audio`
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-13-APPENDICES — Appendices`

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
| Technical Artist (Shaders/VFX) | Contract | 6–8 wks for Splinter VFX \+ perf |
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

### **M1: Vertical Slice (due Nov 15, 2025\)**

**Entry:** SEC‑04/05 baseline implemented; device UI MVP; perf captures at target map.
 **Exit:** One Clara mission shippable; TAPLINE scan+triangulate; FieldPad photo→tag→warrant; MEDSTAT triage; HUD minimal; controller parity; demo branch tagged.
 **Deliverables:** Steam demo build, trailer cut, press kit v0.

### **M2: Early Access (due Jun 15, 2026\)**

**Entry:** Ch1–3 playable end‑to‑end; caseboard saves; ROE loop stable.
 **Exit:** Telemetry online (opt‑in), difficulty presets, accessibility baseline, crash‑free P90 ≥99.0%.
 **Content:** \~7–9 missions; NYC tunnels preview; devices feature‑complete V1.
 **Deliverables:** EA build, roadmap, patch plan, community guidelines.

### **M3: Content Expansion (Oct 31, 2026\)**

**Entry:** Stable EA; art perf budget holding.
 **Exit:** Add Ch4–5, hub re‑use loops, antagonist arcs Qi/Kent; arrest systems tuned; VO pass 1\.
 **Deliverables:** Major content update, marketing beats, LQA plan.

### **M4: Beta (Dec 15, 2026\)**

**Entry:** Feature‑complete; all chapters implemented.
 **Exit:** Content‑complete; bug backlog triaged; crash‑free P90 ≥99.5%; perf budgets met; accessibility check pass.
 **Deliverables:** Beta candidate builds, test plan, known issues.

### **M5: Gold (Mar 15, 2027\)**

**Entry:** All Blocker/Critical fixed; audio mix final; balance locked.
 **Exit:** Gold master signed; store assets delivered; mod tools beta post‑EA finalized.
 **Deliverables:** Release build, soundtrack stems pack, press kit v1.0.

## **10.5 Content Quotas (targets)**

| Asset | Slice | EA | Beta/Gold |
| ----- | ----- | ----- | ----- |
| Missions (playable) | 1 | 7–9 | 13–16 |
| Unique locales | 1 | 4–5 | 7 |
| Devices apps | 3 | 6 | 6 \+ polish |
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

* **Tasking:** 2‑week sprints; Definition of Done includes perf \+ accessibility checks.

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

* Demo \+ EA beats, devlogs, controlled roadmap.

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

## **1\) Replace this single manifest row**

Find the row that begins with `| SEC-11-QA |` and replace the entire line with:

`| SEC-11-QA | QA, loc, accessibility | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2\) Append this section to the end of MASTER (add a `
` before it)**

\[\[PAGEBREAK\]\]

---

<a id="sec-11-qa"></a>
# [SEC-11-QA] QA, Localization, Accessibility
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-13-APPENDICES — Appendices`
- `SEC-08-ARTAUDIO — Art Direction & Audio`

## **11.1 QA Strategy**

### Goals
Ship a stable, readable, fair game that meets perf budgets and accessibility baselines.

### Approach
Risk‑based testing on core loops (SEC‑04), systems (SEC‑05), UI (SEC‑07), art/audio (SEC‑08), and tech (SEC‑09).

### Test types
- **Smoke (per build):** boot, load, start mission, exit.
- **Functional:** devices, evidence chain, ROE, stealth, combat, save/load, caseboard.
- **Systems:** AI perception, heat, reputation, telemetry events.
- **Performance:** FPS, frametime, draw calls, VRAM, CPU/GPU budgets.
- **Stability:** long‑session soak (2–3 h), repeated save/load, memory growth.
- **Regression:** checklist per feature after fixes.
- **Compatibility:** min/rec PC configs, gamepad parity.

### Entry/Exit gates
Slice/EA/Beta builds require: crash‑free P90 ≥ target, KPI deltas reported, no Blockers/Criticals open.

## **11.2 Bug Policy**

### Severity & SLAs

| Severity | Definition | SLA |
|---|---|---|
| **Blocker** | Crash/data loss, progress stop | Fix/rollback same day |
| **Critical** | Major system broken, mission cannot complete | 48–72 h |
| **High** | Significant feature defect or perf miss | Within sprint |
| **Medium** | Noticeable defect, workaround exists | As capacity allows |
| **Low** | Cosmetic, minor text, non‑blocking | Backlog |

### Status flow
New → Triaged → In‑Progress → Fixed → Verified → Closed.

### Repro format
Build, map, steps, expected/actual, logs, attachments.

## **11.3 Test Matrices (core)**

### Devices
- **FieldPad:** Photo → Tag → Chain, links, warrant score, judge pass/fail.
- **TAPLINE:** Scan/Record/Triangulate/Decode/Spoof; warrant gating.
- **MEDSTAT:** status effects, triage actions, team telemetry (Avery), self‑care (Clara).

### Loops
- Investigate → Act → Record; evidence used before action ≥70%.
- Clara stealth resolution ≥60%; Avery arrest:kill ≥ 2:1.
- Save/Load persists caseboard, evidence chain, heat/reputation, device unlocks.

### Performance
- Interior: ≤ 0.8 M tris, ≤ 1,200 draws, GPU ≤ 14 ms @1080p min‑spec.
- Exterior: ≤ 1.5 M tris, ≤ 1,800 draws, GPU ≤ 14 ms @1080p.
- Audio voices ≤ 48; VFX caps per SEC‑08.

## **11.4 Telemetry & Crash**

### Events
Evidence logged, warrant pass/fail, arrest/kill, stealth resolves, mission time, deaths, crashes.

### Storage
Local JSON logs; opt‑in upload; anonymized session ID.

### Crash reporter
Enabled; symbols stored per build.

## **11.5 Accessibility (Checklist)**

### Global
- Subtitles on by default with speaker tags.
- UI scale slider; minimum body size ≥ 12 px @1080p.
- Color‑blind safe glyphs; high‑contrast device skin (Gray).
- Toggle hold‑to‑press; remap all inputs.
- Reduce camera shake/flash options.
- Content warnings pre‑scene; skip with summary.

### Devices/UI
- Tap targets ≥ 32×32 px @1080p; focus ring visible.
- WCAG AA text contrast per SEC‑08 pairs.
- Latency modeled but input buffered for accessibility mode.

### Audio
- Dynamic range presets (Night/TV/Cinema).
- SFX ducking under dialogue; subtitle timing aligned.

### Difficulty
- Aim assist, clue timers, device hinting, stealth forgiveness toggles.
- No forced QTEs without remap/hold options.

### QA acceptance
Accessibility smoke on every milestone build; defects tracked like functional bugs.

## **11.6 Localization Plan**

### Scope
UI, HUD, device text, tutorials, subtitles, store copy.

### Pipeline
UE Localization Dashboard → string tables; resource keys for device labels.

### Length constraints
Device labels ≤ 14 chars; wrap at 24–28 chars.

### Languages
Start en‑US → add by demand (e.g., de, fr, es‑LA, ja, zh‑CN).

### Schedule
String freeze at Beta; LQA before Gold.

### Deliverables
- Master string table (CSV/PO).
- Glossary + style guide.
- Font fallback sets per SEC‑08.
- LQA test cases: device flows, HUD truncation, right‑to‑left audit if added.

## **11.7 Compliance & Ratings**
- ESRB M / PEGI 18 content guidance in SEC‑02.
- Privacy: clear telemetry consent; no PII logged.
- Licenses: fonts and SFX licenses tracked in SEC‑08.

## **11.8 Milestone QA Passes**
- **Pre‑EA:** full functional + perf + accessibility baseline.
- **Pre‑Beta:** regression, content‑complete sweep, LQA round 1.
- **Pre‑Gold:** stability soak, perf locks, LQA final, accessibility sign‑off.

## **11.9 Approvals**
On approval: archive to MASTER as `[SEC-11-QA] v0.1` and update manifest. Next: **SEC‑12 Risks, Legal, Ratings**.

---

<a id="sec-12-risks"></a>
# [SEC-12-RISKS] Risks, Legal, Ratings
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-13-APPENDICES — Appendices`
- `SEC-14-QA — Quality Assurance Test Plan`

## **12.1 Key Risks Register**

| ID | Risk | Cat. | Prob. | Impact | Owner | Triggers | Mitigations |
|---|---|---|---|---|---|---|---|
| R‑01 | Scope creep across dual‑POV + devices | Prod | M | H | Nick | New features added post‑slice | Lock pillars; change‑control; defer to post‑launch |
| R‑02 | Performance misses on fog/VFX | Tech | M | H | Tech Art | GPU spikes; overdraw heatmaps | SEC‑08 caps; VFX budget gate; perf CI |
| R‑03 | Device UI overload/confusion | UX | M | M | UI | Playtest misuse >5% | Progressive disclosure; tutorials via cases; accessibility mode |
| R‑04 | Procedural realism frustrates | Design | M | M | Design | Negative playtest verbatims | Optional briefs; hint tiers; difficulty sliders |
| R‑05 | Dual‑protagonist content debt | Prod | M | H | Nick | Slip on shared spaces re‑use | Shared locations; modular objectives; reuse kits |
| R‑06 | Legal/ratings issue (minors in peril) | Legal | L | H | Legal | Platform flag; ratings query | No on‑screen harm to minors; implied peril only; content warnings |
| R‑07 | Audio/Font licensing gaps | Legal | M | H | Audio/UI | Missing license docs | Use OFL/Apache fonts per SEC‑08; track SFX/music licenses; audit before beta |
| R‑08 | Contractor availability | Prod | M | M | PM | Missed sprint deliverables | Pre‑book alternates; flexible scope; buffer time |
| R‑09 | Save corruption/state bugs | Tech | L | H | Eng | Crash on load; bad schema | Versioned schema; autosave validation; load tests |
| R‑10 | Mod misuse (post‑EA) | Comm | L | M | PM | Offensive content shared | In‑menu warnings; disable online sharing; policy + moderation |
| R‑11 | Libel/brand infringement | Legal | L | H | Legal | Real brand slips in | Fictional brands; art review checklist; legal pass |
| R‑12 | Story/imagery controversy | PR | L | M | PM | Social media flare‑ups | Clear themes doc; content toggles; press kit Q&A |

## **12.2 Legal & Compliance Checklist**

### IP & Contracts
- Wordmark **DIPLOMAGIC**: run clearance search; consider TM file (Nice Class 9, 41).
- Work‑for‑hire + IP assignment for all contractors; NDAs as needed.
- Model/voice releases for VO.
- Avoid real organizations/brands; use fictional names (e.g., Brightstar).

### Licenses
- **Fonts:** VT323, Inter, IBM Plex Sans, JetBrains Mono (open licenses) — see SEC‑08. Store license files in `/Docs/Licenses/`.
- **SFX/Music:** track sources and rights; prefer custom or CC‑BY/royalty‑free with commercial allowance. No viral copyleft for shipped audio.
- **Software:** comply with UE5/Marketplace EULAs; track any OSS (MIT/BSD/Apache) with NOTICE file.

### Privacy & Telemetry
- Opt‑in only. No PII. Random session IDs. Retention ≤ 180 days. Plain‑language consent screen.
- Crash reports scrubbed of usernames/paths where possible.

### Accessibility & Claims
- Do not state compliance beyond tested features. Publish an accessibility features list matching SEC‑07/11.

### Export/Regulatory
- Standard US export compliance. No encryption beyond engine defaults.

### Platforms (PC)
- Steam/Epic checklists: save path, controller prompts, crash reporter, quit to desktop, high‑DPI icon, privacy text.

## **12.3 Ratings Strategy (Targets)**

- **ESRB:** Mature 17+ expected. Likely content descriptors: Violence, Blood, Strong Language, Intense Violence (select scenes).
- **PEGI:** 18 likely for violence/horror intensity.

### Design guardrails
- No sexual content. No torture‑porn.
- **Minors:** no graphic harm on‑screen; peril implied or off‑screen only; fade/abstraction when needed.
- Reduced‑gore toggle and content warnings (scene‑specific).
- Language filtered to maintain target rating.

### Submission kit
- Unedited gameplay video of representative scenes (stealth, arrest, combat, Kadath).
- Written content questionnaire aligned to above guardrails.

## **12.4 Sensitive Content & Ethics**
- Law enforcement portrayal: procedural focus without endorsing brutality; ROE enforced; arrests preferred.
- Cult imagery: fictional symbols; avoid real‑world groups.
- Real places/people: fictionalized locales; no real persons implied.

## **12.5 Paperwork & Templates**
- Contractor MSA + SOW templates.
- VO agreement and rate card.
- Music commission agreement with deliverables (stems, looping).
- Asset ingestion checklist (naming, LODs, loudness, licenses).
- OSS NOTICE and third‑party attributions file.

## **12.6 External Reviews (Pre‑Gold)**
- Legal read‑through of narrative and UI text.
- License audit for fonts/SFX/music.
- Ratings pre‑submission check.
- Accessibility review against published features list.

## **12.7 Deliverables**
- Risk register spreadsheet (live).
- Legal/licenses binder.
- Ratings submission pack.
- Accessibility features list for store pages.
- Press kit Q&A on themes and guardrails.

## **12.8 Approvals**
On approval: archive to MASTER as `[SEC-12-RISKS] v0.1` and update manifest. Next: **SEC‑13 Appendices**.

---

<a id="sec-13-appendices"></a>
# [SEC-13-APPENDICES] Appendices
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-14-QA — Quality Assurance Test Plan`
- `TDD-EVIDENCE+FIELDPAD — Technical Design Document`

## **13.1 Glossary**

* **Caseboard**: Graph of evidence, persons, locations, threads.
* **Chain‑of‑custody**: Steps that keep A‑tier evidence valid.
* **Heat**: Systemic alert level from player actions.
* **Kadath (New/Unknown)**: Liminal layers affecting space, rules.
* **MEDSTAT / FieldPad / TAPLINE**: Devices for vitals, casework, signals.

## **13.2 Acronyms**

| Term | Meaning |
|---|---|
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

```json
{
  "id": "A-014",
  "tier": "A|B|C",
  "quality": 78,
  "chain": {
    "photo": true,
    "collect": true,
    "bag": true,
    "tag": true,
    "log": true,
    "sealIntact": true
  },
  "links": ["case:82", "victim:2", "loc:locker3"],
  "contam": 0,
  "time": "1994-10-31T14:41:00Z"
}
```

**Caseboard Node/Edge**

```json
{
  "nodes": [
    {"id": "victim:2", "type": "person"},
    {"id": "evidence:A-014", "type": "evidence"}
  ],
  "edges": [
    {"from": "victim:2", "to": "evidence:A-014", "rel": "linked"}
  ]
}
```

**Telemetry Event (subset)**

```json
[
  {"evt": "evidence_logged", "id": "A-014", "mission": "CH1_KidsKamp"},
  {"evt": "arrest", "npc": "guard_03", "nonlethal": true},
  {"evt": "stealth_resolve", "mode": "bypass"}
]
```

## **13.4 Checklists**

**Level Readability**

* Silhouettes readable at min spec.
* Patrol lines and cover affordances obvious.
* Fog volumes tuned; no glare hotspots.

**Device UX**

* Nav path discoverable within 6 s.
* Tap targets ≥ 32×32 px @1080p.
* Error states readable; destructive ops confirmed.

**Performance Pass**

* Tris/DC within SEC‑08/09 caps.
* GPU ≤ 14 ms @1080p min spec.
* Audio voices ≤ 48; particle caps met.

**Accessibility**

* Subtitles on; UI scale works.
* High‑contrast skin verified.
* Camera shake/flash reduction toggles.

## **13.5 Tuning Tables (defaults)**

| Parameter | Default | Notes |
|---|---|---|
| Detection base | 0.35 | Stealth visibility curve start |
| Noise budget walk/crouch/sprint | 5 / 2 / 12 | dB‑like units |
| Arrest surrender base | 0.25 | Avery compliance check |
| Evidence BaseTier A/B/C | 50 / 30 / 15 | See SEC‑05 |

## **13.6 Input Reference**

* **Keyboard/Mouse**: WASD move, Q/E lean, C crouch, Z prone, F interact, R reload, 1–4 quick slots, Tab device pane, M map, Esc pause.
* **Gamepad**: LS move, RS look, LB/RB cycle, LT aim, RT fire/apply, Y device swap, X interact, A confirm, B back.
* **Avery**: Hold T challenge, G cuff.
* **Clara**: Hold G place trap, V whistle.

## **13.7 Versioning & Build IDs**

* Scheme: `vMAJOR.MINOR.PATCH_YYYY‑MM‑DD` (e.g., `v1.0.0_2025‑10‑31`).
* Branch map: `Dev → Release/* → hotfix` tags.
* Changelogs per section using IDs `[SEC‑NN‑TAG]`.

## **13.8 Repository & Paths (UE5)**

```
/Content/Diplomagic/
  Art/{Characters,Props,Environments,Materials}
  UI/
  VFX/
  Audio/{SFX,Music,VO}
  Design/Blueprints/
/Docs/{GDD, Licenses, Style, Build}
```

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
|---|---|---|---|
| SEC‑01‑FRONT | v0.2 | 2025‑08‑11 | Exec summary finalized |
| SEC‑02‑PILLARS | v0.1 | 2025‑08‑11 | Pillars/audience |
| … | … | … | … |

## **13.14 Contacts**

* **Owner**: Nick Goldman — design, tech, approvals.
* **External**: to be filled per contract.

## **13.15 Figures & Diagrams**

* UML: `Diplomagic_UML.drawio`, `Statlines_and_Environmental_Systems.drawio` → export PNG/PDF for inclusion.
* Loop diagrams (SEC‑04), device flows (SEC‑07).

## **13.16 Templates (files to create)**

* `Docs/Templates/bug_report.md`
* `Docs/Templates/art_hand-off.md`
* `Docs/Templates/audio_cue_sheet.csv`
* `Docs/Templates/changelog.md`

## **13.17 Approvals**

On approval: archive to MASTER as `[SEC-13-APPENDICES] v0.1` and update manifest.

---

<a id="sec-14-qa"></a>
# [SEC-14-QA] Quality Assurance Test Plan
Version: v0.1  
Date: 2025-08-12  
Owner: Nick Goldman

### Related sections
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-13-APPENDICES — Appendices`

## **Scope**
End‑to‑end QA for PC builds. Aligns with SEC‑06/07/08/09/11/13 and PKG‑BUILD‑SOP.

## **14.0 Objectives**

* Find and prevent regressions that block play, performance, or accessibility.
* Keep shipping confidence high through automated and manual coverage.
* Produce repeatable evidence for compliance and marketing capture.

## **14.1 Definitions**

* **P1/P2/P3** severity; **Blocker/Major/Minor**.
* **Golden Path**: curated story progression per level for perf capture.
* **Perf Spot**: fixed coordinates/angles for comparable captures.

## **14.2 Test Types**

* **Automation**: boot, menu flows, devices (FieldPad/TAPLINE/MEDSTAT), save/load, controller hot‑swap.
* **Functional**: mission flows, evidence chain steps, warrants, TAPLINE, MEDSTAT.
* **Compatibility**: min/mid/high PC configs; windowed/fullscreen; input devices.
* **Performance**: frame time median/95p at perf spots; streaming boundaries.
* **Stability**: long‑run soak; save/load loops.
* **Localization/LQA**: layout, truncation, glyph coverage.
* **Accessibility**: AX‑matrix from SEC‑11; subtitles, UI scale, reduced‑horror, color‑independent cues.
* **Compliance**: CM‑matrix from SEC‑11.

## **14.3 Environments**

* **OS**: Windows 10/11.
* **Hardware tiers**:
  * **Min**: GTX 970 / RX 570, 8 GB RAM, HDD/SSD SATA.
  * **Mid**: GTX 1660 / RX 6600, 16 GB RAM, SATA SSD.
  * **High**: RTX 3060+ / RX 6700+, 16–32 GB, NVMe.
* **Displays**: 1080p required; check 1440p/4K scaling.
* **Input**: KBM, Xbox/PS controller; hot‑plug tests.

## **14.4 Tools & Data**

* UE automation framework; replay recorder; stat dumps; CSV exporters.
* Crash reporter with symbols; minidumps stored.
* Telemetry staging endpoint for canary events (SEC‑13).
* Screenshot script for shotlist (press kit).

## **14.5 Bug Workflow**

* **Tracker states**: New → Triaged → In‑Progress → Ready‑for‑QA → Verified/Failed → Closed.
* **Required fields**: build ID, map, steps, expected, actual, severity, repro rate, attachments.
* **SLA targets**: P1 fix attempt ≤ 48h; P2 within next sprint; P3 on backlog.

## **14.6 Entry/Exit Criteria**

* **Sprint Entry**: latest dev build boots; smoke tests pass.
* **Sprint Exit**: P1=0, P2≤10, perf within budgets on mid tier, CM/AX reds=0.
* **Milestone Exit**: all sprint exits + capture pack updated + SEC‑11 evidence archived.

## **14.7 Test Suites (high level)**

* **TS‑BOOT**: cold boot to menu; crash reporter check; save path permissions.
* **TS‑UI**: HUD prompts, menus, options, remap, glyph swap.
* **TS‑DEV‑FIELD**: FieldPad camera→Tag→Bag→Log; Caseboard; Warrant Builder WS.
* **TS‑DEV‑TAPLINE**: ping→triangulate→seize; icon state changes; toasts.
* **TS‑DEV‑MEDSTAT**: self‑care, Reddy check, stabilize.
* **TS‑MISSIONS**: per‑level objective flow, stealth/breach alt paths, re‑entry states.
* **TS‑SAVE**: slot create/load/delete; atomic write; backup restore.
* **TS‑PERF**: perf spots captures; heatmap boundaries.
* **TS‑AX**: subtitles, UI scale, high‑contrast skin, reduced‑horror, color‑independent cues.
* **TS‑LOC**: pseudoloc, truncation, font fallback.
* **TS‑COMPLIANCE**: CM matrix runs.

## **14.8 Perf Spots (initial)**

| ID | Map | Coords | Notes |
|---|---|---|---|
| PS‑L01‑LOT | L‑01 Kids Kamp lot | (x,y,z) TBD | Exterior cones/fog check |
| PS‑L03‑RD | Backwoods road bend | (x,y,z) TBD | Streaming boundary |
| PS‑L06‑TUN | NYC steam tunnel hub | (x,y,z) TBD | Dynamic lights |
| PS‑L07‑ASC | Transdimensional complex | (x,y,z) TBD | Kadath VFX |

## **14.9 Accessibility Tests (AX)**

* **AX‑001**: Subtitles default ON; size slider works; speaker tags visible.
* **AX‑002**: UI scale 0.85–1.50; no clipping at extremes.
* **AX‑003**: High‑contrast device skin selectable; persists.
* **AX‑004**: Status uses shapes/icons not color alone.
* **AX‑005**: Reduced‑horror swaps audio/visual spikes; summary page on skip.
* **AX‑006**: Hold→Press/Toggle available and functional.
* **Evidence**: screenshots + short videos archived to `/Compliance/AX/`.

## **14.10 Compliance Tests (CM)**
Follow SEC‑11 CM‑001..010; evidence archived to `/Compliance/CM/` with build ID and date.

## **14.11 Localization & LQA**

* Pseudoloc pass before LQA.
* LQA smoke on Beta: layout, truncation, context tags, cultural flags logged.

## **14.12 Soak & Stability**

* 2‑hour idle and traversal; memory growth monitored; save/load loop every 10 min.

## **14.13 Regression Strategy**

* Tag failing tests; auto‑replay affected missions; compare perf spot CSVs.
* Diff localization assets after string changes.

## **14.14 Reporting**

* **Daily**: open bugs by severity, crash rate, perf median/95p deltas.
* **Weekly**: CM/AX status, risk list, burn‑down chart.

## **14.15 Deliverables**

* Test plan DOCX, suites checklist CSV, perf capture CSV templates, evidence folder tree.

## **Approvals**
On approval: export DOCX (full + subsections) and ZIP with templates.

---

<a id="tdd-evidence-fieldpad"></a>
# [TDD-EVIDENCE+FIELDPAD] Technical Design Document
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-05-SYSTEMS — Systems & Mechanics`
- `SEC-06-WORLD — World, Levels, & Content`
- `SEC-07-UI — UI/UX (Devices, HUD, Menus)`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-13-APPENDICES — Appendices`

## **Scope**
Evidence system and the FieldPad device apps (Camera, Evidence, Caseboard, Warrant, Map, Contacts). Integrates with SEC‑05 (Systems), SEC‑07 (UI), SEC‑06 (World). Targets slice→gold.

## **1) Goals, Non‑Goals, Dependencies**

### Goals
- Make evidence meaningful, not collectible spam.
- Enforce simplified chain‑of‑custody (bag→tag→log) with clear feedback.
- Gate warrants and scene actions by evidence quality (Q) and legality.
- Keep 1994 friction while preserving play flow.

### Non‑Goals
- No lab minigames. No DNA/AFIS sims. No networked case sharing.

### Dependencies
- SEC‑05 §5.7 (Evidence & Casework), §5.9 (FieldPad), §5.6 (ROE).
- SEC‑07 §7.4.1 (FieldPad UI) and global HUD.
- SEC‑13 §13.D (Telemetry), §13.E (Save), §13.I (Localization).

## **2) Core Concepts**
- **Evidence Item**: world pickup or documentable object bound to a Case.
- **Chain of Custody (CoC)**: ordered steps; breaks invalidate A‑tier for warrants until supervisor sign‑off.
- **Quality Score (Q 0–100)**: formula determines gate strength.
- **Warrant Score (WS 0–100)**: function of linked evidence and affidavit quality.

## **3) State Machines**

### 3.1 Evidence Item Lifecycle
Discovered → Photographed → Collected → Bagged → Tagged → Logged → Stored/Transferred → Analyzed (narrative) → Released

**Guards**
- Photographed required before Collected for A/B tiers.
- Bagged requires available bag item; Tagged requires label printer or pre‑printed tags.
- Logged requires FieldPad online state (device storage OK, sync later).
- Stored/Transferred occurs at evidence locker/NPC handoff.

### 3.2 Seal State
Intact → Broken → Resealed

- If **Broken** before **Logged**, apply `ContamPenalty` and downgrade tier usage for warrants.

### 3.3 CoC Validity
Valid ↔ Invalid (break) ↔ Remediated (supervisor sign‑off)

- Remediation halves `ContamPenalty` and restores warrant eligibility for **B‑tier** only.

## **4) Data Model (Save‑Ready)**

### 4.1 EvidenceItem JSON
```json
{
  "id": "A-014",
  "case_id": 82,
  "tier": "A",
  "category": "fiber",
  "subtype": "carpet_fiber",
  "world_ref": "L-01_S-04_floor_vent",
  "photos": ["IMG_0142"],
  "chain": {
    "photographed": true,
    "collected": true,
    "bagged": true,
    "tagged": true,
    "logged": true,
    "stored": true,
    "seal_state": "Intact",
    "break_log": []
  },
  "handlers": ["Clara","Avery"],
  "locker_id": "LKR-3",
  "q_components": {
    "base_tier": 50,
    "chain_bonus": 18,
    "contam_penalty": 0,
    "time_decay": 4,
    "crosslink_bonus": 14
  },
  "Q": 78,
  "links": ["TPL-07","W-03"],
  "notes": "Found under vent panel"
}
```

### 4.2 Casefile
```json
{
  "case_id": 82,
  "title": "Brightstar Site",
  "items": ["A-014","B-021","C-005"],
  "suspects": ["Langston_Gromley"],
  "warrants": ["WRT-82-01"],
  "graph": { "nodes":[], "links":[] }
}
```

### 4.3 Warrant
```json
{
  "warrant_id": "WRT-82-01",
  "case_id": 82,
  "judge": "S_Hartford",
  "affidavit_text": "...",
  "linked_items": ["A-014","TPL-07"],
  "WS": 62,
  "status": "Submitted|Approved|Denied"
}
```

**Constraints**
- `id` is unique within `case_id`.
- `tier ∈ {A,B,C}`.
- Photos stored as compressed PNG/JPEG with EXIF‑like header.

## **5) Formulas & Scoring**

**Evidence Quality (SEC‑05 baseline)**

`Q = BaseTier + ChainBonus − ContamPenalty − TimeDecay + CrosslinkBonus`

- BaseTier: A=50, B=30, C=15.
- ChainBonus: +0…20 if bag→tag→log completed.
- ContamPenalty: −0…25 for breaks or missing steps.
- TimeDecay: −0…10 for perishable/late log.
- CrosslinkBonus: +0…15 for ≥2 corroborations.

**Warrant Score (WS)**

`WS = clamp( Σ(Q_linked) × K_evidence + K_affidavit − Penalties , 0, 100 )`

- `K_evidence = 0.35` (sum of Q capped at 200 pre‑scale).
- `K_affidavit = 0…30` from template completeness and length.
- Penalties: CoC invalid items ignored; exigent use applies −15 risk note.
- Gate: WS ≥ 60 → Approved; 45–59 → Judge Questions; <45 → Denied.

## **6) FieldPad Apps — UX Flows (SEC‑07 parity)**
Latency target per action ≤ 250 ms. All destructive ops require confirm.

### 6.1 Camera
- Open → focus reticle → **CAPTURE** → store `IMG_####` with timestamp and location.
- Auto‑suggest **Tag** if object outline detected (simple bounding box, no hard ML).

### 6.2 Evidence (List + Detail)
- **List**: filter by tier, CoC state, linked/unlinked, locker.
- **Detail actions**: PHOTO VIEW, CHAIN STEP, LINK, LOCKER, NOTES.

**CHAIN STEP modal**
- Shows checklist: Photo ✓ → Collect ✓ → Bag □ → Tag □ → Log □.
- Selecting a step records timestamp + handler.
- If Seal broken, banner: “Seal broken: A‑tier invalid until sign‑off.”

### 6.3 Caseboard
- Node graph for items, suspects, locations.
- Actions: ADD LINK, REMOVE LINK, PIN NOTE, FILTER by time/tier/POV.

### 6.4 Warrant Builder
- Template fields: Location, PC summary, Linked Items, Requested Actions.
- Live WS readout; reasons for failure listed.
- **SUBMIT** → status Submitted; mock judge delay 10–30 s; result Approved/Denied with rationale.

### 6.5 Map
- Shows lockers, TAPLINE nodes, last photo locations.
- Breadcrumbs for Clara path if enabled by difficulty.

### 6.6 Contacts
- Judges, supervisors, dispatch.
- Actions: request sign‑off for CoC remediation; log responses.

## **7) Items, Props, and World Hooks**
- Evidence Bag pickup increases bag capacity.
- Label Printer prop enables tagging without pre‑prints.
- Evidence Locker actor with slots; enforces `stored=true` and transfers handler to system.

## **8) Error Handling & Edge Cases**
- Duplicate ID: auto‑increment suffix `_B`; toast + edit option.
- Photo lost/corrupt: item remains usable but `ChainBonus −5` and banner shown.
- Seal broken after log: apply `ContamPenalty −10` and set `resealed=true` if resealed.
- Offline logging: cache ops; show **SYNC PENDING**; retries on next session.
- Bag shortage: allow **Collected** but not **Bagged/Tagged**; Q max capped at 55.

## **9) Performance & Storage**
- Max photos per mission: 60; image size target ≤ 200 KB each (JPEG Q80).
- Evidence items per mission target: 20–30 total; A‑tier ≤ 6.
- FieldPad memory bar shows storage; archive oldest photos first after confirm.

## **10) Accessibility & Localization**
- Device skins: Green/Amber/Gray; contrast pairs per SEC‑08.
- Minimum device font size equivalent ≥ 12 px @1080p; scalable.
- Avoid jargon; all UI strings in table with ≤14 char labels; provide short/long forms.

## **11) Telemetry (SEC‑13 parity)**

### Events
- `evidence_logged(case_id,item_id,tier,Q,time)`
- `warrant_submit(case_id,WS,pass_bool)`
- `chain_break(case_id,item_id,when)`
- `link_add/remove(case_id,src,dst)`
- `affidavit_edit(case_id,len,sections_filled)`

### KPIs
- Pre‑action evidence logged ≥70% (Avery arcs).
- Avg WS on first submit ≥55 by EA, ≥65 by Beta.
- Prompt misuse <5%.

## **12) Save/Load Contracts**
- **Slots**: 3 manual + autos.
- **Persist**: EvidenceItem structs, Casefile, Warrant, map breadcrumbs, locker state, pending sync queue.
- **Integrity**: checksum; schema version `evidence_schema_ver`.

## **13) Testing — Acceptance**
- **Functional**: complete CoC, link items, build warrant with WS≥60, approve/deny branches.
- **Negative**: break seal before log; attempt warrant with Q<60; offline log then quit; duplicate IDs.
- **Perf**: capture list open with 30 items < 150 ms; photo capture to view < 300 ms.
- **Localization**: truncation audit for 7–14 char labels.

## **14) Risks & Mitigations**
- **UI overload** → progressive disclosure; tutorial tips; limit on‑screen text.
- **Grind/Spam** → cap A‑tier, boost crosslink value, make optional C‑tier low friction.
- **Legal confusion** → simple WS meter and clear reasons; tie outcomes to narrative, not fail states.

## **15) Deliverables**
JSON schemas, BP/C++ API stubs, widget wireframes (SEC‑07), test plan, tuning table for Q/WS weights, data contract docs.

## **16) Approvals**
On approval: archive as `[TDD‑EVIDENCE+FIELDPAD] v0.1`, export DOCX (full + subsections), link from SEC‑05 §5.7/5.9 and SEC‑07 §7.4.1.

---
