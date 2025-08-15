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
