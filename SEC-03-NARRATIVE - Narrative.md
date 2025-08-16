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
