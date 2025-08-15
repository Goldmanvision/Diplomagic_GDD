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
