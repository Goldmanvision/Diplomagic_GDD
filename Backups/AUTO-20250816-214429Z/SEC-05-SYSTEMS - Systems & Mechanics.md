# [SEC-05-SYSTEMS] Systems & Mechanics
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-03-NARRATIVE` — Narrative
- `SEC-04-LOOPS` — Core Gameplay Loops
- `SEC-06-WORLD` — World, Levels, & Content
- `SEC-07-UI` — UI/UX (Devices, HUD, Menus)

## **5.1 Systems Overview**

This section defines player-facing mechanics, underlying rules, tunables, and AI behaviors. It connects to SEC‑04 Loops, SEC‑07 UI, and SEC‑03 Narrative.

**POV deltas**

* **Avery (FBI):** procedure‑gated access, arrests preferred, team telemetry via **MEDSTAT**, legal gates via **FieldPad** casework and **TAPLINE** warrants.

* **Clara (Civilian):** scarcity, improvisation, escort care for Reddy, analog friction, stealth bias.

## **5.2 Player State Model**

| Track | Range | Notes |
| ----- | ----- | ----- |
| Health (HP) | 0–100 | Global. Below 25 triggers **Critical**. |
| Blood Loss | 0–3 | Per‑limb; stacks cause **Bleeding** DoT until bandaged. |
| Pain | 0–100 | Affects aim sway and sprint duration. |
| Stress | 0–100 | Increases under threat; raises noise and tunnel vision. |
| Fatigue | 0–100 | Gated sprint, climb, hold breath. |
| Contamination | 0–100 | Eldritch exposure; unlocks narrative effects. |

**Status Effects (MEDSTAT)**  
 `Stable, Wounded, Critical, In Shock, Unconscious, Infected, Contaminated`

## **5.3 Movement & Interaction**

* Walk, crouch, prone, vault, mantle, lean, ladder, ledge shimmy.

* Contextual interactions: door types (latched, chained, keypad), physical locks (picks, bolt cutters), electrical panels (fuses, breakers).

* Encumbrance tiers from **Load %** thresholds (0–25–50–75–100) modify sprint and noise.

## **5.4 Stealth System**

**Detection** \= f(Visibility, Noise, Proximity, Angle, Light, Time).

* Visibility: silhouette contrast vs background; crouch/prone reduce profile.

* Noise budget per action (dB‑like unit): walk 5, crouch 2, sprint 12, vault 10, firearm unsuppressed 90\.

* Light: player‑held light cones expose; ambient darkness grants threshold reductions.

* Cover quality: `High / Partial / None`.

* Distractions: throwables, TAPLINE audio spoof (Avery), analog timers (Clara).  
   **Fail states:** escalation to search → pursuit → breach; escape reduces heat over time.

## **5.5 Combat & Weapons**

**Avery**

* Stance shooting with **decoupled aiming**; suppression and verbal compliance prompts.

* Non‑lethal: baton, taser, pepper spray, beanbag shotgun; arrest animations and cuff time.

* Lethal: era‑appropriate sidearms and long guns.  
   **Clara**

* Last‑resort lethals, improvised traps (tripwire, glass, chemical irritants), thrown objects.

**Ballistics**

* Penetration tiers: Light (wood/drywall), Medium (doors), Heavy (brick/steel ‑ no pen).

* Recoil pattern by weapon class; aim sway raised by Pain and Fatigue.

* Hit model: head/torso/limb with armor zones (Avery armor vests).

**Damage Types**: kinetic, blunt, laceration, burn, shock, psychic.

## **5.6 Arrest & ROE (Avery)**

* **ROE Gate:** Lethal force only when threat presents deadly force.

* **Compliance Loop:** `Aim → Challenge → Countdown → Restrain`. NPC morale, numbers, and witness presence modify surrender probability.

* **Evidence Integrity:** discharges, injuries, and property damage log to casefile.

## **5.7 Evidence & Casework**

**Tiers**: `A = forensic`, `B = analytical/eyewitness`, `C = circumstantial`.  
 **Quality Score (0–100)** drives access gates and outcomes.

**Quality Formula (baseline)**  
 `Q = BaseTier + ChainBonus − ContamPenalty − TimeDecay + CrosslinkBonus`

* BaseTier: A=50, B=30, C=15.

* ChainBonus: +0–20 if bag→tag→log completed in **FieldPad**.

* ContamPenalty: −0–25 for mishandling or broken seals.

* TimeDecay: −0–10 if perishable and delayed.

* CrosslinkBonus: +0–15 if connected to ≥2 corroborating items.

**Chain of Custody (Avery)**

1. Photograph in place → 2) Collect with gloves → 3) Bag & seal → 4) Tag ID → 5) Log in FieldPad → 6) Transfer receipt.  
    Breaks invalidate A‑tier gates until remedied by supervisor sign‑off.

## **5.8 TAPLINE (Signals) — Mechanics**

* Bands: VHF/UHF, cordless phones, pagers, analog trunked radio.

* Modes: **Scan**, **Record**, **Triangulate**, **Spoof** (Avery only), **Decode** (DTMF/FSK).

* Minigame: lock to frequency, maintain signal quality; terrain occlusion affects SNR.

* Warrants: evidence threshold `Q ≥ 60` unlocks lawful intercept; otherwise limited to exigent use with risk.

## **5.9 FieldPad (Casework) — Mechanics**

* Apps: Camera, Evidence, Caseboard, Warrant Builder, Map, Contacts.

* Warrant Builder: template + probable cause fields; auto‑pulls linked evidence; judge approval simulated via score.

* Caseboard: nodes and threads; inference suggestions with uncertainty badges.

## **5.10 MEDSTAT (Vitals) — Mechanics**

* Tracks HP, Pain, Blood Loss, Stress, Fatigue.

* Triage actions: bandage, tourniquet, analgesic, stimulant, sedative.

* Team telemetry: Avery can issue commands when teammates are within range; Clara uses self‑care only.

## **5.11 Inventory, Crafting, Economy**

* **Slots + Weight** hybrid. Quick slots: 4\. Backpack tiers affect capacity.

* **Crafting (Clara‑focused):** simple traps, lock tools, noise devices using found parts.

* **Economy:** no global money; favors barter and requisition (Avery through casefile approvals).

## **5.12 Progression**

* **Skills:** separate trees; no shared XP.

  * Avery: Procedure, Firearms, Tactics, Signals.

  * Clara: Stealth, Improvisation, Athletics, Care.

* **Unlock cadence:** per chapter beats; prevents grinding.

## **5.13 AI Behavior**

**Senses:** hearing, sight cone, light sensitivity.  
 **States:** idle → suspicious → search → engage → pursue → fallback.  
 **Group Tactics (Avery arcs):** bounding, flank, breach; morale checks drive surrenders.  
 **Investigation:** NPCs log last known position, inspect distractions, call for backup on radios.  
 **Evidence Reaction:** guards may move or destroy exposed C‑tier items; A‑tier is secured.

## **5.14 Heat & Reputation**

* Heat rises with noise, bodies found, property damage; decays over time when hidden.

* Reputation tracks arrests vs kills for Avery; affects community cooperation and support.

## **5.15 Accessibility & Options**

* Sliders: camera shake, motion blur, aim assist, input remap.

* Toggles: simplified evidence prompts, slower TAPLINE minigames, high‑contrast device themes.

## **5.16 Telemetry & Tuning Targets**

* Pre‑action evidence logged rate ≥70%.

* Avery arrest:kill ≥2:1.

* Clara lethal usage ≤20% of resolved encounters.

* Average stealth breach detection time 6–12 s at Standard.

## **5.17 Data Contracts (Save/Load)**

* Caseboard graph, Evidence items with chain state, Heat/Reputation, AI world state snapshot, device app unlock flags.

## **5.18 Deliverables**

* System spec JSON (attributes, thresholds).

* AI behavior trees and perception tunables.

* Device app flows and wireframes (link to SEC‑07).

* Test plans for ROE, chain‑of‑custody, TAPLINE legality cases.

## **5.19 Approvals**

On approval: archive to MASTER as `[SEC-05-SYSTEMS] v0.1` and update manifest. Next section: **SEC‑06 World, Levels, & Content**.


### **5.x TAPLINE Legal Gates (1994)**
- **Pen register / trap‑and‑trace**: logs dialed numbers only; lower standard order. UI must label as **No content capture**.
- **Content interception (Title III)**: required for audio/content; block capture without active order; show **Title III order required** messaging.
- Full audit trail: judge, order id, start/stop timestamps.

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-05 — Systems Insert Points (Root Merge)
Repo dir: /Patches

> Use these headings to locate paste points in `SEC-05-SYSTEMS - Systems & Mechanics.md`.

## Insert after:
### "Spellcasting Overview"
- Add **Phrases & Scrolls** equip model (L/R, Mana calm-regen, scrolls single-use).

### "Field Devices"
- Add **FieldPad/MEDSTAT storage** note for phrases.

### "Combat Rules"
- Add **Raid ROE (CH6)**: lethal authorized, Blue-on-Blue fail, no civilians, score-neutral neutralizations.

### "Stealth & Surveillance"
- Add **Analog Cameras** and **Breaker Loop** (Service Passage only, 90s outage, K-9 reroute).

### "Boss & Mini-boss"
- Add **Star Vampire (CH5 pump cavern)** summary + reveal via lights/flare.

### "Endings & Outcomes"
- Add **Splinter Vault**: Contain/Sever/Black File mechanics + scoring.

### "Tuning & Balancing"
- Add initial DMG/HP targets, wave pacing, ammo economy.

### "Failure States"
- Add Blue-on-Blue detection logic and exceptions (Shield absorb, >10m pellet one-hit ignore).

Constraints reminder: prompts ≤14 chars; ambient phrase only “the stars are right tonight.”

# ROOT MERGE — SEC-05 Systems & Mechanics (CH5–CH6)
Repo dir: /Patches

> Paste into `SEC-05-SYSTEMS - Systems & Mechanics.md`. Append or replace matching subsections.

## Spell phrases & scrolls
- **Phrases:** multi‑use, stored in FieldPad/MEDSTAT, equip **Left/Right**. Triggers **Cast L/R**.  
- **Mana:** shared pool; regen only in calm windows.  
- **Scrolls:** single‑use items in Inventory.  
- Examples unlocked: Fast Travel (CH4), Shield, Ward Jam.

## Rogue Ops (CH5)
- `F_Rogue=1`: Krill‑only handler via pager/payphone windows (:00/:20/:40 ±5).  
- Evidence loop throttled; 1994 comms only.

## Deep D‑LAMP & Iron Highway (CH5→CH6)
- One‑mile descent on WV island elevator; abandoned D‑LAMP complex; **Star Vampire** mini‑boss in Pump Cavern; acquire rover; drive Iron Highway to SRS layby.

## CH6 Raid ROE
- Hostiles are combatants (SN New Kadath / Order). **Lethal authorized.** Neutralizations score‑neutral. **Blue‑on‑blue** triggers fail (−10). No civilians in AO.

## Cameras & breakers (1994)
- Analog cams in Service Passage only; fuse pull = 90 s outage; K‑9 route swap; no Vault cameras.

## Splinter Vault endings
- **Contain:** Jam wards → Valves A→B→C → gimbal STABLE.  
- **Sever:** Plant×2 → interrupt → detonate → sprint.  
- **Black File:** Photo+Sample+exfil, rep penalty.

## AI behavior (raid focus)
- Zombies: Idle→Shamble→Lunge→Recover→Search; staggers on headshot/Shove.  
- Night Gaunts: Perch→Track→Dive→Grounded→FleePerch; light stagger 1.5s.  
- Cultists: Patrol→Rite→Fire→Flinch→Retreat; chants interrupt on Suppress/TK Push.  
- Beast: Stalk→Charge→Stun→Reacquire; wall hit stun.  
- Warden Shade: Drift→Swipe→Phase→Disperse; Ward Jam removes DR.

## Combat tuning (initial targets)
- Sidearm 30 body/100 head (zombie). Shotgun slug 80/120.  
- Ammo economy: pistol 60 start; shotgun 12; rifle 90. Caches spaced.  
- Vault waves every 35–45 s; Alert High −10 s, +1 cultist.

## Blue‑on‑Blue detection
- Any friendly hit (Avery/Clara/Reddy/Deputy) sets `BlueOnBlue=1` and fails chapter; Shield‑absorbed hits ignored; >10 m pellet single‑pellet exception.

## Scoring
- CH5: Convoy stop +3, Manifest +2 (cap 1), Star Vampire +3.  
- CH6: Contain +5, Sever +3, Black File +5 evidence/−5 rep; evidence +2 each (cap 3).

## Constraints
- 1994 tech only. Prompts ≤14 chars. Ambient phrase only.

### Inner checkpoint passphrase
Challenge requires exact match: "the stars are right tonight."  
Logic: if input equals phrase then Clearance else Alert increments. One retry via Badge plus Warrant bluff. Failure sets Alert High.

### Rules of engagement
Non-lethal arrests score higher. Lethal or unjustified force applies penalties. Exception: if an NPC initiates lethal force then any player lethal response in that encounter is score neutral.

### Evidence chain
Bag and tag items. Complete FD-302. Fax to field office. Teletype BOLOs.  
Vars: EvidenceCount, FD302Filed, TeletypeSent.

### Scoring
+5 Arrest. +3 Evidence Bagged. +2 FD-302. +2 Teletype.  
-5 Lethal. -3 Civilian Endangered. -2 Alert High end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

### Shared alert hook
If Avery CH2 ends Alert High then Clara CH2 Call Intercept base window shortens.

### UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

## SEC‑05 Additions — CH3 Systems

### Reddy Telekinesis (CH3)
- **Energy:** Infinite for CH3 set piece.  
- **Targets:** Physics objects and living enemies.  
- **Verbs:** Grab, Hold, Throw, Drop, Pin, Stack, Block.  
- **Damage Rules:** Launch into hard surface = lethal; into soft surface = non‑lethal knock‑out.  
- **Scoring Hooks:** +Non‑lethal disables; +Protective blocks; −Chain explosions or environmental carnage.

### Fear Meter (Clara/Avery)
- Applies endurance debuff when spiking; recovers with light, distance, or safe nest. Unlocks in CH3.

### Spectral‑Phased Muzzle Brake (Avery)
- Temporary attachment consumable that phases muzzle output to damage spectral entities. Time‑limited charge.  
- **UI:** “Phase” prompt appears when equipped.  
- **Balance:** Scarce ammo; encourages avoidance until necessary.

### Time Dilation & Convergence
- **Rule:** Kadath time moves faster. Clara years ≈ Avery weeks.  
- **Flag:** F_TimeSkewExplained set during rescue.  
- **Outcome:** Enables Chapter 4 team‑up without retcon.

### Phrase Handling
- “the stars are right tonight” present as ambient audio only; no dialogue input in CH3.

# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

# SEC-05 — CH4 Systems (Revised)

## Reddy TK in CH4
- **Burst (1x):** Consumed at chapter start to kill the Beast. No score penalty.  
- **Shield (1x):** One-time damage mitigation during traverse or skirmish.  
- **Jam Ward (0–1x):** Single-use interference with a warded device or symbol if encountered (optional).

## FieldPad / TAPLINE / SENTINEL
- **Status:** `Offline`. No network or satellite link.  
- **Storage:** Evidence stored to local device memory with timestamps.  
- **Sync:** Disabled. No external comms or internet.

## Walled City Perimeter
- **AI:** Outskirt hostiles operate in small packs; avoid direct firefights.  
- **Gate Logic:** Wardens respond to noise and approach posture. Entry deferred to next chapter’s parley.  
- **Signals:** Horn-call escalations mark patrol changes.

## Scoring Hooks
+3 evidence page; +2 camp without alert; +3 non-lethal disable on humanoids; −3 civilian harm; −2 Alert High end.  
**Neutral:** lethal against **non-human** monstrous threats (e.g., the entry Beast).

## UI / Prompts (≤14 chars)
Scout, Binoculars, Move Out, Camp, Boil, Pack, Parley, Trade, Bribe, Sneak, Sprint, Shield, Jam Ward, Signal, Map, Note

## Flags
F_BeastNeutralized, F_SentinelOffline, F_TaplineOffline, F_SawCity, F_ApproachCity, F_GateSeen

# SEC-05 — Enemies & Mini‑Boss: Star Vampire (CH5→CH6)
Repo dir: /Patches

## Zombies
- **Behavior:** Shamble, lunge when close.  
- **Weakness:** Headshots; light stagger.  
- **Counter:** Dodge, Shove, Shield.  
- **Scoring:** No bonus; avoid civilian harm.

## Night Gaunts
- **Behavior:** Ceiling traverse; dive grab.  
- **Weakness:** Light; **Ward Jam** opens cast window.  
- **Counter:** Dodge, TK Push, firearm when grounded.

## Cultists
- **Behavior:** Patrol, chant (“the stars are right tonight”); sidearms.  
- **Weakness:** Interrupt chants; non‑lethal takedowns score.

## Mini‑Boss — Star Vampire
- **Arena:** Pump Cavern (catwalks + cistern).  
- **Phases:**  
  1) **Haze** — partial invisibility; reveal with **Headlights** or flare.  
  2) **Siphon** — beam drains stamina; block with **Shield** or pillar.  
  3) **Rend** — close swipes; stagger with **TK Push** or shotgun‑class hit if available.  
- **Win:** Deplete health after reveal; drops **Route Control Key** for Vehicle Bay.  
- **Scoring:** +3 mini‑boss clear; neutral lethal vs non‑human.  

## Vehicle — D‑LAMP Utility Rover
- **Controls:** Drive, Brake, Headlights, Horn.  
- **Hazards:** Cave‑ins; fuel limits (metered).  
- **UI Prompts (≤14):** Drive, Brake, Lights, Horn, Exit, Enter.

## Flags/Vars
F_StarVampireDefeated, F_RouteKey, F_DLampRover, Fuel, O2LowCue

# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

# SEC-05 — CH5 Systems Addendum: D-LAMP & Betsy
Repo dir: /Patches

## Branch Logic
```
BetsyBossEligible = !(F_HauserPistolLogged && F_BetsyPinSigilsLogged && F_WarrantSRS)
```
- If **false** → Raid bypass.  
- If **true** → Boss fight enabled.

## Wendigo Betsy — Boss
- **Arena:** Living Room ↔ Kitchen Cut ↔ Back Porch.  
- **Phases:**  
  1) **Lunge/Grab** — counter with **Dodge** or furniture **Shove**.  
  2) **Wall-scramble** — shriek; **Ward Jam** creates cast window.  
  3) **Frenzy** — break LOS to drop Fear; **Cast L/R** windows open.  
- **Win:** Non-lethal preferred; lethal allowed if forced. Civilians protected.  
- **Scoring:** +5 non-lethal disable, −3 civilian harm. Phrase stays ambient only.

## D-LAMP Recon/Inside
- **Recon:** camera counts, guard rotations, shipment logs.  
- **Inside:** front pretext or tail-in at service; capture POs and call logs.  
- **Scoring:** +2 recon packet; +3 inside packet.

## UI Prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

# SEC-05 — CH5 Systems (Rework)
Repo dir: /Patches

## POI Window
- Player must remain reachable until `F_EscapeHotel=1`.  
- Missed calls escalate scrutiny and reduce CH6 access.

## Hotel Escape Mini-Loop
- **Stealth:** Service corridors, stairwells, cameras, keycard doors.  
- **Apprehension (non-lethal):** Cuff, Disarm, Door-Jam. IA penalties track if excessive.  
- Flags: `F_EscapeHotel`, `IA_PenaltyLevel`.

## Warrant Assembly
- **Inputs:** Evidence index, probable cause narrative, target location near **Savannah River Site**.  
- **Outputs (objects):** `OpsOrder_SRS`, `Affidavit_EvidenceIndex`, `Warrant_Safehouse`.  
- **Approvals:** NYFO ASAC → USAO SDGA → magistrate.  
- **Scoring:** +3 complete packet; −2 missing affidavit element.

## SENTINEL / TAPLINE (1994)
- SENTINEL: limited to NYFO secure terminals.  
- TAPLINE: upload queue; transmit only at NYFO.  
- FieldPad/MEDSTAT **Phrases**: equip **L/R**; **Mana** regen slow in real world (Rest or tonic). **Scrolls**: single-use.

## Scoring
+3 timeline completeness, +2 stealth escape, +2 warrant packet approved, −3 lie caught, −2 unreachable during POI window.

## Prompts (≤14 chars)
Answer, Call Back, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R

# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

# SEC-05 — CH6 After-Action Report (1994)
Repo dir: /Patches

## Documents
- **FD-302:** raid narrative, times, locations, personnel, use of force (raid ROE).  
- **Seizure Forms:** evidence numbers, chain of custody.  
- **Teletype (BOLO/INFO):** minimal facts to field offices.  
- **Debrief Notes:** Krill pager references, payphone logs.

## Process
1) Draft FD-302 from FieldPad notes (offline).  
2) Queue teletype and scans; upload only from NYFO.  
3) File seizure forms with Aiken Co. SO copy if joint.  
4) Evidence cap reminder: 3 items scored; extra may exist but do not alter score.

## Scoring Hook
- +2 each scored evidence (cap 3).  
- Endings bonuses per `CH6_Scoring_Raid.md`.  
- Blue-on-Blue = mission fail regardless of paperwork.

## UI prompts (≤14 chars)
Fax 302, Teletype, File, Bag, Tag, Note, Map

# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

# SEC-05 — CH6 Enemy: Resist & Interrupt Table
Repo dir: /Patches

| Enemy | Resistances | Vulnerabilities | Interrupts (≤14) | Notes |
|---|---|---|---|---|
| Zombie | Body shots weak | Headshots; Shove | Dodge, Shove, Frag | Noise attracts more |
| Night Gaunt | Firearms while airborne | Light stagger; TK Push | Lights, TK Push | Dive-grab telegraph |
| Cultist | Suppressive fire | Interrupt chants | Suppress, Aim | Chant: “the stars are right tonight” |
| Beast | Small arms at range | Dodge window on charge | Dodge, Frag | Bleeds out on kite |
| Warden Shade | Ballistic glaze | Ward Jam, Cast L/R | Ward Jam | Short-lived |
| Star Vampire | Partial invis. | Headlights/flare reveal | Lights, Cast | Mini-boss (CH5 pump cavern) |

**Casting model:** phrases equip L/R; scrolls single-use; Mana regen in calm windows only.

# SEC-05 — CH6 Loadout Guide (1994)
Repo dir: /Patches

## Avery
- **Primary:** SIG P226 (9mm) or S&W 13 (.38).  
- **Backup:** 2 speedloaders / 2 mags.  
- **Grenades:** 2 frags if issued.  
- **Phrases (L/R):** Shield, Ward Jam.  
- **Scrolls:** 1× Plant (if available), 1× Sample (optional).  
- **Tools:** Polaroid, tape, valve tags, flashlight.

## Clara
- **Primary:** shotgun (slug) or carbine if available.  
- **Phrases (L/R):** Shield or Quiet Step.  
- **Scrolls:** 1× Photo, 1× Sample (Black File path).

## Reddy
- **Phrases:** TK Push, Shield.  
- **Limiters:** Mana only in calm windows.  
- **Role:** Stagger gaunts, cover valve/charge windows.

## Shared
- **Tonics:** 1–2 total.  
- **Med:** 2 first‑aid.  
- **Ammo:** respect CH6 tuning table.  
- **Evidence cap:** 3 items max.

# SEC-05 — CH6 Raid ROE One-Pager
Repo dir: /Patches

## Authorization
- Target: Hostile combatants of the Sovereign Nation of New Kadath / Order of the Splintered God.
- Lethal force authorized. No Final Score penalty for lethal.

## Restrictions
- Blue-on-blue / friendly-fire: hard fail (−10 and abort).  
- No civilians in AO. If encountered by design change, disengage and mark.

## Evidence
- Bonus +2 per item, **cap 3** for CH6 total.

## Comms
- Rogue posture. Krill via pager/payphone only.

## UI
Aim, Fire, Reload, Suppress, Frag, Equip L, Equip R, Cast L, Cast R, Shield, Ward Jam, Map, Note

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

# SEC-05 — CH6 Systems
Repo dir: /Patches

## UC Operation
- **Cover:** forged paper badge + pretext; fallback stealth path.  

## Raid ROE
- **Authorization:** All CH6 hostiles are combatants (Sovereign Nation of New Kadath / Order of the Splintered God). **Lethal force authorized.**  
- **Penalties:** No Final Score penalty for lethal against hostiles. **Blue-on-blue or friendly-fire** is a hard fail (−10 and mission abort).
- **Evidence Flow:** evidence bonuses limited; FD‑302 and teletype queued post‑op.
- **AI:** K‑9 patrols, flashlight arcs, analog cameras.  
- **Access:** chain‑link, padlocks, keyed doors, paper sign‑ins.

## Ritual Event
- **Trigger:** when `F_CoreFound=1` and timer expires, set `F_RitualIgnited=1`.  
- **Effects:** looped corridors, geometry shifts, hostile anomalies.  
- **Reddy Utilities:** **Shield** (party‑wide soak), **Ward Jam** (open windows), phrases consume **Mana**; scrolls single‑use.

## Finale Branching
- **Seal:** stabilize via valve sequence + phrase **Shield** windows; casualties minimized; evidence partial. Set `F_End_Contain`.  
- **Sever:** blast couplings + sprint to egress; high anomalies; evidence mixed. Set `F_End_Escape`.  
- **Black File:** prioritize bag+tag over rescue; reputation hit; evidence maximal. Set `F_End_BlackFile`.

## Scoring
| Action | Points |
|---|---:|
| Seal breach | +5 |
| Sever link | +3 |
| Black file | +5 evidence / −5 rep |
| Evidence item (cap 3) | +2 each |
| Blue-on-Blue | −10 and mission fail |

## Prompts (≤14 chars)
Aim, Fire, Reload, Suppress, Frag, Shield, Ward Jam, Equip L, Equip R, Cast L, Cast R, Map, Note

# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH
