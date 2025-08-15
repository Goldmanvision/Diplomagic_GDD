# ROOT — SEC-03 CH6 Narrative (Paste Block)
Repo dir: /Patches

> Paste into `SEC-03-NARRATIVE - Narrative.md` replacing the CH6 section.

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
