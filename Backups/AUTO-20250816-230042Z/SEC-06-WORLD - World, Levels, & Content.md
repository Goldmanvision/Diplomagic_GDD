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
