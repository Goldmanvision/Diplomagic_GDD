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
