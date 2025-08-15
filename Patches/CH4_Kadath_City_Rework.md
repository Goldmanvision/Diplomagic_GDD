# Patch: CH4 — “Kadath City: Elder’s Charge”
Version: v0.4 • 2025-08-15
Owner: Nick Goldman
Repo dir: /Patches

## Summary
Party enters Kadath’s walled city. Elder leader reveals the closed-topology loop is anchored by an **American Cult Boss** inside the city—a wizard wielding eldritch magic and contraband firearms. Avery is tasked to **kill** him, not arrest. Defeat yields an ancient spellbook. **Multi‑use spell phrases** are stored in FieldPad/MEDSTAT and **equipped like weapons** (single or dual wield) and consume **Mana**. **Single‑use scrolls** go to Inventory. **Fast Travel** becomes a learned phrase with a high Mana cost and cooldown to return the party to **Avery’s car**. Avery then phones ASAC Fred Franklin via **Motorola MicroTAC**: “boy have I got some crazy shit to debrief.”

## 1994 corrections
- Use **Motorola MicroTAC**-class cellular phone (1994-correct). SENTINEL remains unreachable in Kadath; FieldPad/TAPLINE store locally.

## Beats
1) **South Gate Entry:** Parley succeeds. Elder receives the trio.  
2) **Elder’s Charge:** Elder identifies the American cult wizard as the loop’s source. Offers safe conduct to an inner sanctum.  
3) **Loadout & ROE:** Lethal authorized against the Boss. Civilians protected. Phrase “the stars are right tonight” heard in cult liturgy only.  
4) **Approach:** Alley stealth to the **Sanctum Spire**. Optional evidence rooms.  
5) **Boss Battle:** Multi‑phase arena with wards and summoned hazards.  
6) **Victory:** Loop wards collapse. **Spellbook** obtained.  
7) **Spells:** Learn phrases. Equip via FieldPad/MEDSTAT loadout (single/dual). Mana governs casting. Scrolls are single‑use items.  
8) **Escape:** Cast **Fast Travel** (phrase) → return to **Avery’s car**. Cooldown prevents re‑cast in CH4.  
9) **Call Out:** Avery uses MicroTAC to call Franklin.  
10) **Hook to CH5:** Drive to NYC hotel near NYFO. Franklin murdered; FBI calls Avery.

## Evidence
City charter scraps, ward sigils, boss folios, firearm serials, elder’s writ.

## Flags
F_ElderMet, F_BossRevealed, F_BossDefeated, F_Spellbook, F_Spell_FastTravel, F_EscapeKadath, F_AveryCalledFranklin, F_CH5_HookReady

## UI prompts (≤14 chars)
Parley, Sneak, Scout, **Equip L**, **Equip R**, **Cast L**, **Cast R**, Swap, FastTravel, Shield, Counter, Dodge, Aim, Fire, Reload, TK Push, TK Shield, Map, Note
