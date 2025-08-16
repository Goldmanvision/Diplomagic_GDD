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