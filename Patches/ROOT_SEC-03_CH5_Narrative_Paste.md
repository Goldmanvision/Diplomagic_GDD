# ROOT — SEC-03 CH5 Narrative (Paste Block)
Repo dir: /Patches

> Paste into `SEC-03-NARRATIVE - Narrative.md` replacing the CH5 section.

## CH5 — NYFO Hotel → Deep D‑LAMP → Iron Highway
**State:** `F_Rogue=1` (Avery off‑book). Krill is sole handler (`F_KrillHandler=1`). SENTINEL only at NYFO. Phrases equip L/R with Mana; scrolls single‑use. Ambient phrase only: “the stars are right tonight.”

**Beats**
1) Hotel near NYFO. POI window. Avery debrief.  
2) Krill hallway: raises clearance. “Buckle up.” (`F_ClearanceRaised=1`)  
3) Night: Franklin murdered (`F_FranklinMurdered=1`).  
4) Morning: agents attempt detention; stealth escape or non‑lethal takedowns (`F_EscapeHotel=1`).  
5) Rogue pivot: FBI access limited; pager/payphone cadence.  
6) WV river island: concealed elevator kiosk. Descend ~1 mile (`F_WV_IslandFound`, `F_ElevatorDown`, `F_DLampUnderground`).  
7) Abandoned D‑LAMP: 1980s–90s cult occupation evidence; undead pockets.  
8) Mini‑boss: **Star Vampire** in Pump Cavern (`F_StarVampireDefeated`, route key loot).  
9) Vehicle bay: acquire D‑LAMP utility rover (`F_DLampRover=1`).  
10) **Iron Highway** drive toward **SRS Secret Annex**; zombie/gaunt/cultist encounters (`F_IronHighwayEntered=1`).  
11) Bulkhead layby reached (`F_SRS_SecretAnnexSeen=1`). Chapter handoff to CH6.

**Clara/Betsy branch**
- If `F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS`: FBI raid bypass (`F_BetsyRaidBypass=1`).  
- Else boss fight: **Wendigo Betsy** (`F_BetsyBossDefeated=1`).  
Outcome: Clara + Reddy reunite and follow Avery (`F_ClaraFollowsAvery=1`).

**Evidence (cap aware)** Manifest/route card (+2 cap 1), occupation proofs (rota, PO copies), phone slips intersecting Brightstar.

**UI prompts ≤14** Answer, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pager, Payphone, Elevator, Descend, Drive, Brake, Lights, Enter, Exit
