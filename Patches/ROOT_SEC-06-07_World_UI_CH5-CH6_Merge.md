# ROOT — SEC-06 & SEC-07 Merge Additions (CH5–CH6)
Repo dir: /Patches

> Paste these blocks into the root docs.

---
## SEC-06 — World, Levels, & Content

### Deep D‑LAMP (WV Shaft → Pump Cavern → Vehicle Bay)
- **Access:** Concealed kiosk on a WV river island; 1‑mile descent via elevator.
- **Spaces:** Control Lobby, Pump Cavern (Star Vampire), Vehicle Bay, Maintenance Corridors.
- **Loot:** Rover route card, fuel chits, Polaroids of occupation.
- **Encounters:** Undead pockets, Night Gaunts in dark ceilings.
- **Exit:** Iron Highway ramp.

### Iron Highway (D‑LAMP to SRS Layby)
- **Route:** Utility roadway; checkpoints listed on route card.
- **Events:** Ambushes, barrier clears, rover diagnostics.
- **End:** **SRS bulkhead layby** with man‑door ingress.

### SRS Secret Annex (Raid Route)
Bulkhead Gate → Man‑Door → Service Passage (cams/breakers) → Valve Row (A‑B‑C) → Dead Piping → Service Stair → Core Gallery (Ignition) → Splinter Vault → Egress fence gap.

**Cameras:** Service Passage only; breaker pull ≈90 s loop; K‑9 reroute.  
**Vault:** No cameras. Ending paths: **Contain**, **Sever**, **Black File**.

---
## SEC-07 — UI-UX (Devices, HUD, Menus)

### HUD
Health | Stamina | Mana | Ammo | Evidence **0/3** | **BlueOnBlue**

### Prompts (≤14 chars)
Answer, Breach, Bag, Brake, Call Back, Cast L, Cast R, Crouch, Detonate, Drive, Dodge, Elevator, Enter, Equip L, Equip R, Fire, Frag, Headlights, Hide, Holster, Inspect, **Ward Jam**, Lawyer Up, Lights, Map, Note, Pager, Payphone, Photo, Plant, Reload, Sample, Shield, Shove, Suppress, Tag, Valve A, Valve B, Valve C, Exit, Descend, Aim

### Context Loops
- **Valve Loop (Contain):** Valve A → Valve B → Valve C → set gimbal **STABLE**.
- **Charge Loop (Sever):** Plant×2 → interrupt chant → **Detonate** → sprint to egress.
- **Evidence Loop (Black File):** **Photo**×2 + **Sample**×1; counter enforces cap 3.

### Comms (Rogue)
Pager → Payphone. Timed call ≤90 s.

### Alerts
Cap Reached, BlueOnBlue, STABLE.

Constraints: 1994 period; deputy name randomized; ambient phrase only — “the stars are right tonight.”
