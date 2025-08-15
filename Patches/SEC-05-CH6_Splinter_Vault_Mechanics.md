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
