# CH6 — Raid Summary & File Index
Version: v0.1 • 2025-08-15
Repo dir: /Patches

## Snapshot
- **Mode:** Sanctioned **raid** vs hostile combatants (Sovereign Nation of New Kadath / Order of the Splintered God).  
- **ROE:** Lethal authorized; **no** Final Score penalty. **Blue‑on‑blue** = hard fail (−10 + abort).  
- **Evidence cap:** 3 items total.  
- **Phrase:** ambient only — “the stars are right tonight.”  
- **1994 lock:** MicroTAC, Polaroids, paper logs, flashlights; no network on-site.

## Route
Bulkhead Gate → Man‑Door → Service Passage → Valve Row → Dead Piping → Service Stair → Core Gallery → Splinter Vault → Egress Run.

## Endings
- **Contain (Seal):** valves A→B→C + Ward Jam + Shield → STABLE gimbal.  
- **Sever (Escape):** plant 2 charges, interrupt chant, detonate, sprint out.  
- **Black File:** photo + sample + exfil; evidence max, rep penalty.

## CH6 File Map (this repo)
- Mechanics: `SEC-05-CH6_Systems.md`, `SEC-05-CH6_Splinter_Vault_Mechanics.md`  
- World: `SEC-06-CH6_SRS_Secret_Annex_World.md`, `SEC-06-CH6_Route_Encounter_Tables.md`  
- UI: `SEC-07-CH6_Raid_UI_Prompts.md`, `SEC-07-CH6_UI_Flow.md`  
- Tuning/QA: `SEC-05-CH6_Combat_Tuning_Params.md`, `/Trackers/CH6_QA_Test_Cases.md`, `/Trackers/CH6_Scoring_Raid.md`  
- Narrative addenda: `SEC-03-CH6_BeatSheet_Raid.md`, `SEC-03-CH6_Raid_Addendum.md`

## Dependencies
- From CH5: Iron Highway ingress, deep D‑LAMP, Star Vampire mini‑boss cleared, `F_IronHighwayEntered=1` leads to Annex.

## Flags (top level)
F_SRSBreach, F_CoreFound, F_RitualIgnited, F_End_Contain/F_End_Escape/F_End_BlackFile, EvidenceCount≤3, BlueOnBlue=0
