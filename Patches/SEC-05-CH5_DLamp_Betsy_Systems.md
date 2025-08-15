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
