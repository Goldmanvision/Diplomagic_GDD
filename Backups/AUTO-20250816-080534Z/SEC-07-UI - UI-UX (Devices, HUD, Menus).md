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