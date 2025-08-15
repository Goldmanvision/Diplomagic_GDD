# ROOT MERGE — SEC-03 Narrative (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-03-NARRATIVE - Narrative.md`, replacing the CH5 and CH6 sections.

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

---

## CH6 — SRS Secret Annex: Raid and Splinter Vault
**Mode:** **Raid** vs hostile combatants (Sov. Nation of New Kadath / Order of the Splintered God). **Lethal authorized.** Neutralizations are score‑neutral. **Blue‑on‑blue** is a hard fail (−10, abort). **Evidence cap: 3.**

**Route**
Bulkhead Gate → Man‑Door → Service Passage → Valve Row → Dead Piping → Service Stair → Core Gallery (Ignition) → Splinter Vault → Egress Run.

**Core systems**
- Spell phrases equip L/R; Mana regen only in calm windows; scrolls single‑use.  
- Camera loops via breakers in Service Passage; K‑9 route swap. No Vault cameras.  
- Enemy roster: Zombie (headshot bias), Night Gaunt (light stagger), Cultist (chant interrupts), Beast (charge tells), Warden Shade (Ward Jam vulnerability).

**Vault mechanics**
- **Contain (Seal):** Jam wards, cycle valves A→B→C, lock gimbal (`F_End_Contain`).  
- **Sever (Escape):** Plant two charges, interrupt chant, detonate, sprint (`F_End_Escape`).  
- **Black File:** Photo + sample + exfil; evidence max, rep penalty (`F_End_BlackFile`).

**Scoring**
- Contain +5, Sever +3, Black File +5 evidence/−5 rep.  
- +2 per evidence item (cap 3).  
- Blue‑on‑blue −10 and fail.

**UI prompts ≤14** Aim, Fire, Reload, Suppress, Frag, Crouch, Hide, Dodge, Breach, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag, Map, Note
