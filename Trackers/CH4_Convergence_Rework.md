# Patch: CH4 — “Toward the Walled City” (Convergence Rework)
Version: v0.2 • 2025-08-15
Owner: Nick Goldman

## Summary
Rewrites CH4 to match new directives: Reddy kills the pursuing beast at the Pine Break with a single telekinetic burst; Clara, Reddy, and Avery team up; SENTINEL is unreachable so FieldPad/TAPLINE run offline; escape via Brightstar or Pine Break remains impossible; party scouts a distant **walled city** within Kadath (inspired by Lovecraft’s Kadath of Nyarlathotep) and decides to approach despite hostile outskirts.

## Canonical changes
- **Beast kill on entry:** Reddy’s TK Burst instantly neutralizes the beast. No score penalty. Flag `F_BeastNeutralized=1`.
- **Team formed:** Clara introduces Reddy to Avery; trust established.
- **Futility of exits:** Clara confirms repeated failed exits via Brightstar and Pine Break; loop persists.
- **Comms dark:** FieldPad and TAPLINE cannot reach **SENTINEL**. Evidence stores to local device memory only. No internet or radio backhaul.
- **New objective:** Reach the **Walled City of Kadath**. Clara reports hostile natives in the outskirts; Avery argues walls imply safer order within.

## Beats
1) **Threshold Impact:** Avery bursts through Pine Break pursued by a beast. Reddy fires **TK Burst** → kill. Set `F_BeastNeutralized`.
2) **Contact:** Introductions. Clara briefs failed exits and survival constraints. Avery syncs offline FieldPad notes with Clara’s MEDSTAT text.
3) **High-Ground Recon:** Binocular scan reveals a distant walled city: smoke columns, lamplight grids, patrol silhouettes. Set `F_SawCity=1`.
4) **Debate & Decision:** Clara warns of hostile outskirts. Avery argues for refuge within walls. Decision: approach city at dusk.
5) **Prep:** Water safe, food packed, nest marked. SENTINEL status shown **Offline**. Set `F_SentinelOffline=1`, `F_TaplineOffline=1`.
6) **Outskirts Traverse:** Stealth and avoidance. Optional trade or bribe with scavengers. Ambient whisper of “the stars are right tonight.”
7) **Skirmish Window:** Short chase set piece to reach sightline of the **South Gate**. Non-lethal preferred on humanoids; monstrous threats are neutral if lethal.
8) **Gate Standoff:** Wardens on parapet observe; horn signal ends pursuit. Entry not yet granted. Save `F_GateSeen=1`.
9) **Camp at Ditch:** Party camps outside the walls. Plan for parley next chapter.

## Evidence
- Avery: offline FieldPad entries; photos via Polaroid (for reference only); paper sketches of the wall layout.  
- Clara: MEDSTAT text notes.  
- Shared: tally of hostile encounters, gate silhouettes, horn-call pattern.

## 1994 Lock
Paper maps, Polaroid, Maglite, SIG P226 or S&W 13 for Avery. No weapon lights. No network.

## Scoring
- **Neutral:** Reddy’s beast kill and other **non-human** monstrous lethals.  
- **Positive:** Non-lethal disables on humanoids; evidence pages; camp established without alert.  
- **Negative:** Civilian harm; Alert High end-state.

## UI prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags/Vars
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen
