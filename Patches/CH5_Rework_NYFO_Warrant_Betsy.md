# Patch: CH5 — “NYFO: The Last Call” (Rework)
Version: v0.2 • 2025-08-15
Owner: Nick Goldman
Repo dir: /Patches

## Summary
Refactors CH5 per latest directive: Avery debriefs at NYFO, Krill raises his clearance and confirms real-world magic threats, Fred Franklin is killed the following night, and agents attempt to detain Avery the next morning at the hotel. Player escapes stealth or via non-lethal takedowns. Avery assembles an **undercover** operations order and supporting **warrant** for a Savannah River Site (SRS) adjacent cult safehouse. Clara departs NYC to **Betsy** to address Reddy’s guardianship. 1994 tech is enforced throughout.

## Key Changes
- **Krill hallway brief:** “buckle up” line; `F_ClearanceRaised=1`, `F_KrillBriefed=1`.
- **Franklin murder timing:** night after debrief; `F_FranklinMurdered=1`.
- **Hotel escape:** stealth or non-lethal; `F_EscapeHotel=1`.
- **SRS warrant & UC:** `F_WarrantSRS=1`; packet objects created (Ops Order, Affidavit, Warrant).
- **Clara→Betsy:** guardianship path active; `F_ClaraToBetsy=1`, `F_GuardianshipPending=1`.
- **Spell model:** phrases stay equipped L/R with Mana; scrolls are single-use.

## Continuity & Tech (1994)
- Phones: **Motorola MicroTAC**.  
- FieldPad/TAPLINE: local storage; uploads only from NYFO secure line.  
- SENTINEL: available at NYFO only; no hotel access.

## UI prompts (≤14 chars)
Answer, Cooperate, Lawyer Up, Inspect, Bag, Tag, Note, Map, Pursue, Back Off, Cuff, Disarm, Door-Jam, Equip L, Equip R, Cast L, Cast R
