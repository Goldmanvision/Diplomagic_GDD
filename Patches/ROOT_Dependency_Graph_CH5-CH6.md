# ROOT — Dependency Graph (CH5–CH6 Flags)
Repo dir: /Patches

## Adjacency (→ requires/feeds)
- `F_ClearanceRaised` → enables rogue pivot narrative beats.  
- `F_EscapeHotel` → `F_Rogue`, `F_KrillHandler`.  
- `F_WV_IslandFound` → `F_ElevatorDown` → `F_DLampUnderground`.  
- `F_StarVampireDefeated` → `F_DLampRover` → `F_IronHighwayEntered` → `F_SRS_SecretAnnexSeen`.  
- `F_SRSBreach` → `F_CoreFound` → `F_RitualIgnited` → (`F_End_Contain` | `F_End_Escape` | `F_End_BlackFile`).  
- Any friendly hit → `BlueOnBlue=1` → Chapter fail.  
- `EvidenceCount` ≤ 3 enforced; attempts >3 blocked from scoring.

## Preconditions
- `SpellsKnown` includes Fast Travel from CH4 spellbook.  
- DeputyName seeded on save start; fixed thereafter.

## Outputs
- Ending flag set exactly one of: Contain / Escape / BlackFile.  
- Score delta computed per `/Trackers/CH6_Ending_Scorecard.md`.

Constraints: 1994 lock; prompts ≤14; ambient phrase only.
