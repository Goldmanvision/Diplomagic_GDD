# [SEC-07-UI] UI/UX (Devices, HUD, Menus)
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-05-SYSTEMS` — Systems & Mechanics
- `SEC-06-WORLD` — World, Levels, & Content
- `SEC-08-ARTAUDIO` — Art Direction & Audio
- `SEC-09-TECH` — Technology & Performance Targets

## **7.1 Goals & Principles**

* Diegetic first. Devices (FieldPad, TAPLINE, MEDSTAT) are primary UI.

* 1994 constraints. Limited color, latency, coarse hit targets, period affordances.

* Readability over spectacle. PS1‑era silhouettes + modern clarity.

* Minimal HUD. Surface only actionable state.

* Accessibility from day one.

## **7.2 Visual Language**

**Palette.** HUD: 1 accent + neutrals. Devices: two‑tone skins (Green, Amber, Gray).  
 **Type.** Bitmap sans for devices; clean sans for HUD. Minimum 12 px at 1080p equivalent.  
 **Grid.** Virtual 320×240 device canvas, 8 px base unit; HUD uses 12‑pt safe margins.  
 **Iconography.** Stroke icons, 1 px weight at 1080p, scale by step 1.25×.

## **7.3 Global HUD (contextual, minimal)**

* **Top‑left:** Objective stub + sub‑task dot list.

* **Bottom‑left:** Health bar + vitals pill. Clara shows **Stress**; Avery shows **Armor**.

* **Bottom‑right:** Ammo/weapon or tool readout.

* **Center‑low:** Interaction prompt with verb + hold meter where needed.

* **Stealth:** eye glyph (visibility), waveform glyph (noise).

* **Heat/Reputation:** small indicator in map/caseboard, not moment‑to‑moment.

Example HUD overlay (schematic):

[OBJ] Kids Kamp: Extract Reddy

  • Unlock north gate  ◻

  • Avoid patrols       ■

ꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏ (screen)

[HP ████▌]  [VIS ◐][NOISE ≈≈]                             [9× .38 | ■■■■]

      Clara: Stress ▒▒▒▒                                 Prompt: Hold E — Pick Lock ▓▓▓▒▒

## **7.4 Devices — Shared Conventions**

* **Nav**: Soft‑keys `◀ BACK` `OK ▶`, D‑pad/arrow focus, `Tab` cycles panes.

* **Latency**: app open/close 150–250 ms; scrolling steps 80 ms.

* **Status bar**: battery ▮▮▮▯, signal ▂▃▅, storage ■■■□, time 24h.

* **File ops**: save states are explicit; confirm destructive actions.

* **Skins**: Green (Avery default), Amber (Clara), Gray (accessibility high‑contrast).

### **7.4.1 FieldPad — Casework & Evidence**

**Purpose.** Capture, tag, link, and warrant‑build.  
 **Apps.** Home, Camera, Evidence, Caseboard, Warrant, Map, Contacts.  
 **Flows.** Photo → Tag → Chain steps → Link to case → Warrant score.

FieldPad — HOME

┌──────────────── FIELD•PAD ────────────────┐   ▂▃▅  ■■■□  ▮▮▮▯  14:32

│ [Camera] [Evidence] [Caseboard]           │

│ [Warrant] [Map]      [Contacts]           │

│                                            │

│ Tips: Complete bag→tag→log for A‑tier     │

└◀ BACK                            OK ▶──────┘

FieldPad — EVIDENCE (item view)

┌───────────── EVIDENCE: BAG #A‑014 ─────────┐   ▂▃▅  ■■■■  ▮▮▮▮  14:41

│ Photo: IMG\_0142  [View]                    │

│ Type: Fiber (A‑tier)                       │  Q: 78

│ Chain: Photo → Collect → Bag → Tag → Log   │  Seal: ▣ Intact

│ Links: Case #82 • Victim #2 • Locker 3     │

│ Notes:                                     │

│  − Found under vent panel                  │

└◀ BACK                   [LINK]   OK ▶──────┘

FieldPad — WARRANT BUILDER

┌────────────── WARRANT BUILDER ─────────────┐   ▂▃▅  ■■□□  ▮▮▮▯  15:06

│ Case: #82  Judge: S. Hartford              │  Score: 62 (PASS)

│ Probable Cause:                            │

│  [ ] Evidence A‑014 (fiber)                │

│  [ ] Intercepts TPL‑07                     │

│  [ ] Statement W‑03                        │

│ Affidavit Text:                            │

│  \> Suspect used south entrance…            │

└◀ BACK                 [SUBMIT]   OK ▶──────┘

### **7.4.2 TAPLINE — Signals**

**Purpose.** Scan, record, triangulate, spoof, and decode era radios/phones.  
 **Modes.** Scan • Record • Triangulate • Decode • Spoof (Avery only).

TAPLINE — SCAN

┌──────────────── TAPLINE: SCAN ─────────────┐   ▂▃▅  ■■□□  ▮▮▮▯  22:18

│ Band: UHF  |  Freq: 462.6125 MHz           │  SNR: ▓▓▓▒▒

│ [◀] 462.6000 ◁▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▷ 462.6500 [▶]

│ Hold to lock: ████▒▒                       │

│ Hits:  19:32  "Gate open"                   │

│        19:35  DTMF: 4 1 2                  │

└◀ BACK                 [RECORD]   OK ▶──────┘

TAPLINE — TRIANGULATE

┌───────────── TAPLINE: TRIANGULATE ─────────┐   ▂▃▅  ■■□□  ▮▮▮▯  22:26

│ Node A  ▣  Node B  ▢  Node C  ▢             │  Fix: 48%

│ Bearings: A 062° • B 239° • C  —           │

│ Map:  [A───────╳────────B]                  │

│        Clara route  [ ]  Avery route [x]    │

└◀ BACK                  [PING]    OK ▶──────┘

### **7.4.3 MEDSTAT — Vitals & Team**

**Purpose.** Health, status effects, triage, and telemetry.  
 **States.** Stable • Wounded • Critical • In Shock • Infected • Contaminated.

MEDSTAT — VITALS

┌──────────────── MED•STAT ──────────────────┐   ▂▃▅  ■■■■  ▮▮▮▯  02:14

│ Patient: AVERY     Armor: ▣▣▢               │

│ HP █████░  Pain ▓▓  Stress ▓                 │

│ Blood Loss: Arm ▪▪  Leg ▪  Torso ▪▪         │

│ Status: Wounded (Bleeding)                  │

│ Actions: [Bandage] [Tourniquet] [Analgesic] │

└◀ BACK                 [APPLY]    OK ▶──────┘

## **7.5 Menus & Screens**

* **Pause.** Resume, Save, Load, Options, Accessibility, Quit.

* **Inventory.** Slots + Weight hybrid; quick slots ×4.

* **Caseboard.** Graph of nodes and links; filter by time, tier, POV.

* **Map.** Layered (Real, New Kadath, Unknown); TAPLINE nodes and search areas.

Inventory (schematic)

┌──────────────── INVENTORY ────────────────┐

│ Weight: 62%   Quick: [1][2][3][4]         │

│ Backpack: MED                              │

│ Items:                                     │

│  ▣ Lockpicks (x3)  ▣ Glass Shards (x6)    │

│  ▣ .38 Rounds (9)  ▣ Tourniquet (1)       │

│  ▣ Evidence A‑014  ▣ Tape Recorder        │

└◀ BACK                 [ASSIGN]   OK ▶─────┘

Caseboard (schematic)

[Case #82]

  (Victim #2)───(Fiber A‑014)───(Vent South)

        │              │               \\

     (W‑03)         (TPL‑07)          (Locker 3)

## **7.6 Input & Controls**

* **KB/M:** WASD, `Q/E` lean, `C` crouch, `Z` prone, `F` interact, `R` reload, `1–4` quick slots, `Tab` device pane, `M` map, `Esc` pause.

* **Gamepad:** LS move, RS look, `LB/RB` cycle, `LT` aim, `RT` fire/apply, `Y` device swap, `X` interact, `A` confirm, `B` back.

* **Avery‑only:** `HOLD T` to Challenge (ROE), `G` to cuff when compliant.

* **Clara‑only:** `HOLD G` place trap, `V` whistle (distraction).

## **7.7 Feedback & Error States**

* **Prompts:** verb‑first, concise. Hold meters show discrete ticks.

* **Errors:** inline banners on devices (“Seal broken: A‑tier invalid”).

* **Saves:** autos at Brief/Branch/Outcome; manual outside combat.

## **7.8 Accessibility**

* High‑contrast device skin, scalable UI, color‑blind safe glyphs.

* Subtitles on, speaker tags, SFX ducking during dialogue.

* Input remap for all actions; toggle hold‑to‑press.

* Reduce camera shake/flash; simplify minigames.

## **7.9 Localization**

* All device text uses resource keys.

* String budget: device labels ≤14 chars; body lines wrap at 24–28 chars.

* Avoid cultural idioms in core prompts.

## **7.10 Telemetry Targets**

* Device app time‑to‑task ≤ 6 s for common flows.

* Prompt mis‑use rate \< 5% by beta.

* Evidence linked per mission ≥ 3 on average.

## **7.11 Deliverables**

* Wireframes for FieldPad/TAPLINE/MEDSTAT and HUD.

* Icon set (SVG/bitmap) with states.

* Device skins (Green/Amber/Gray).

* Interaction prompt library.

## **7.12 Approvals**

On approval: archive to MASTER as `[SEC-07-UI] v0.1` and update manifest. Next section: **SEC‑08 Art Direction & Audio**.

# **Patch Instructions for Existing MASTER — SEC-08**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-08-ARTAUDIO |` and replace the entire line with:

`| SEC-08-ARTAUDIO | Art direction and audio | v0.2 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**


> **Telephony note (1994):** Caller ID availability varies by carrier/market. Do not rely on it for puzzles; provide alternate clues.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.

# ROOT_SEC-07_UI_Prompts_CH7_Extensions.md
> Add to the prompts master. All ≤14 chars.

## City
- Restrain
- Tase
- Escort
- Payphone
- Dial
- Hang Up
- Page
- Fax Send
- Consent
- Warrant
- Decoy
- Subdue

## Mindscape
- Anchor
- Counter
- Dispel
- Reveal
- Focus
- Ground
- Wake
- Retreat

# ROOT_SEC-07_UI_Prompts_Master.md
> All prompts ≤14 characters. Keep 1994 tone. No emoji.

# Core
- Ward Jam
- Cast L
- Cast R
- Equip L
- Equip R
- Valve A
- Valve B
- Valve C
- Plant
- Detonate
- Photo
- Sample

# Combat
- Aim
- Fire
- Reload
- Swap Mag
- Melee
- Sprint
- Crouch
- Peek
- Dodge

# Interact
- Interact
- Inspect
- Open
- Close
- Lockpick
- Pry
- Breach
- Climb
- Jump

# Tools
- Radio
- Pager
- Map
- Notes
- FieldPad
- MEDSTAT
- Trunk

# Vehicle
- Start
- Park
- Exit

## UI — CH2 Avery Prompts (SEC-07 addendum)

Prompts must be ≤14 characters.

- Badge
- Warrant
- Say Phrase
- Cuff
- Arrest
- Reload
- Holster
- Search
- Bag
- Tag
- Evidence
- Radio
- Map
- Fax 302
- Teletype

## UI — CH3 Prompts (SEC-07 addendum)

### Clara/Reddy (≤14 chars)
Grab, Throw, Drop, Pin, Stack, Block, Shield, Swap, Soothe, Rest, Use, Inspect, Map, Note

### Avery (≤14 chars)
Holster, Reload, Sprint, Duck, Vault, Search, Bag, Tag, Radio, Map, Aim, Fire, Phase, Swap

# SEC-07 — CH4 UI: Spell Equip & Casting
Repo dir: /Patches

## Loadout UI
- **Phrases Tab** in FieldPad/MEDSTAT lists learned multi‑use spells.  
- Player assigns to **Left** or **Right** slot: **Equip L** / **Equip R**.  
- Show **Mana** bar and **Cooldown** icons for equipped phrases.

## Casting UI
- HUD shows **Cast L** and **Cast R** prompts when slots are filled.  
- If Mana insufficient, show “No Mana” flash; no color mandate.

## Inventory UI
- **Scrolls** appear under Inventory. “Use” consumes the scroll; not equip‑slot based.

## Prompts (≤14 chars)
Equip L, Equip R, Cast L, Cast R, Swap, FastTravel, Shield, Ward Jam, Use, No Mana

## Accessibility
- Keep prompts ≤14 chars. No modern UI tropes beyond simple meters and icons.

# SEC-07 — CH5–CH6 UI Prompts (Consolidated)
Repo dir: /Patches
All prompts ≤14 chars.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Rogue Ops / Comms
Pager, Payphone

## Combat / Stealth
Aim, Fire, Reload, Holster, Crouch, Hide, Dodge, Shove, Cuff, Arrest

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, FastTravel

## Deep D-LAMP
Elevator, Descend, Pry Door, Lights, Headlights, Horn, Drive, Brake, Enter, Exit

## Iron Highway / SRS
Breach, Pretext, Stakeout, Valve A, Valve B, Valve C

# SEC-07 — CH5 UI Prompts
Repo dir: /Patches

Prompts must be ≤14 characters.

## Core
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map

## Hotel Escape
Pursue, Back Off, Cuff, Disarm, Door-Jam

## D-LAMP
Badge, Pretext, Stakeout, Search

## Betsy
Knock, Warrant, Breach, Hide, Dodge, Shove

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

# SEC-07 — CH6 Prompts Verification
Repo dir: /Patches

All entries ≤14 characters.

| Prompt | Len | Check |
|---|---:|:---:|
| Aim | 3 | OK |
| Answer | 6 | OK |
| Bag | 3 | OK |
| Brake | 5 | OK |
| Breach | 6 | OK |
| Call Back | 9 | OK |
| Cast L | 6 | OK |
| Cast R | 6 | OK |
| Crouch | 6 | OK |
| Descend | 7 | OK |
| Detonate | 8 | OK |
| Dodge | 5 | OK |
| Drive | 5 | OK |
| Elevator | 8 | OK |
| Enter | 5 | OK |
| Equip L | 7 | OK |
| Equip R | 7 | OK |
| Exit | 4 | OK |
| Fire | 4 | OK |
| Frag | 4 | OK |
| Headlights | 10 | OK |
| Hide | 4 | OK |
| Holster | 7 | OK |
| Inspect | 7 | OK |
| Lawyer Up | 9 | OK |
| Lights | 6 | OK |
| Map | 3 | OK |
| Note | 4 | OK |
| Pager | 5 | OK |
| Payphone | 8 | OK |
| Photo | 5 | OK |
| Plant | 5 | OK |
| Reload | 6 | OK |
| Sample | 6 | OK |
| Shield | 6 | OK |
| Shove | 5 | OK |
| Suppress | 8 | OK |
| Tag | 3 | OK |
| Valve A | 7 | OK |
| Valve B | 7 | OK |
| Valve C | 7 | OK |
| Ward Jam | 8 | OK |

How to use
1) Paste this table under Prompts in the root UI doc.
2) Search root for any longer variants. Replace using `/Patches/ROOT_Prompts_Conflict_Map.md`.
3) Keep ambient phrase out of prompts. Ambient only: “the stars are right tonight.”

# SEC-07 — CH6 Raid UI Prompts
Repo dir: /Patches

All prompts ≤14 chars.

## Core Combat
Aim, Fire, Reload, Holster, Suppress, Frag

## Movement / Stealth
Crouch, Hide, Dodge, Shove, Breach

## Spells
Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam

## Ops / Map
Map, Note

## Annex Tasks
Valve A, Valve B, Valve C

# SEC-07 — CH6 UI Flow (Raid)
Repo dir: /Patches

All prompts ≤14 chars.

## HUD
- Health, Stamina, Mana bars (simple meters).  
- Ammo readout.  
- BlueOnBlue indicator (off unless triggered).  
- Evidence cap counter: 0/3.

## Context prompts
- Combat: Aim, Fire, Reload, Suppress, Frag.  
- Spells: Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam.  
- Annex tasks: Valve A, Valve B, Valve C, Plant, Detonate, Photo, Sample, Bag, Tag.

## Valve mini-loop (Contain)
1) Player tags each valve (Polaroid).  
2) When near the correct valve in order A→B→C, show **Valve A/B/C**.  
3) On turn, brief cast window for **Shield**/**Ward Jam**.

## Charges mini-loop (Sever)
1) At coupling, show **Plant**.  
2) After both planted, show **Detonate** with 2 s fuse.  
3) Fear spike; sprint route markers appear.

## Evidence loop (Black File)
- Show **Photo**, **Sample**, **Bag**, **Tag** when near apparatus.  
- Counter enforces 3-item cap; fourth attempt shows “Cap Reached”.

## Blue-on-Blue
- On friendly hit: flash indicator; fail state triggers on confirm.

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Card/Hardware spec
- PCMCIA Type II linear flash; Newton‑compatible; no camera or internet.
- SENTINEL satellite hop links to other MEDSTATs only.
