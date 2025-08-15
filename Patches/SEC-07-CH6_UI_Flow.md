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
