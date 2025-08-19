## Correction — 2025-08-17
Applied Gate Map and SG-20250817 clarifications.

### Prologue adjustments
- Removed **spectral full** from Prologue (rule: none allowed). Converted PRO-02 basement `d6=6` to **spectral flicker**.
- Kept Chapter 1 limit **spectral full ≤ 1**.

### Prologue (scene_id binding — corrected)
| scene_id | location | d6    | result                             | adv_ids                | cap | notes                     |
|----------|----------|-------|------------------------------------|------------------------|-----|---------------------------|
| PRO-01   | street   | 1     | 2x occult cultists                 | ADV-0001               | 1   | light intro               |
| PRO-01   | street   | 2     | 1x new-kadathi-cultist             | ADV-0003               | 1   | ranged harass             |
| PRO-02   | street   | 3     | 1x mind-swapped-civilian           | ADV-0002               | 1   | non-lethal branch         |
| PRO-02   | street   | 4     | spectral flicker                   | ADV-0004               | 1   | tease only                |
| PRO-02   | basement | 1-2   | 2x occult cultists                 | ADV-0001               | 1   | closed space              |
| PRO-02   | basement | 5     | 1x mind-swapped-civilian           | ADV-0002               | 1   | interruption              |
| PRO-02   | basement | 6     | spectral flicker                   | ADV-0004               | 1   | **was full → flicker**    |

**Prologue caps:** ≤ 2 total combats; ≥ 1 non‑lethal; **no spectral‑full**.

### SG compliance notes
- PRO‑01: no spectral events → OK.
- PRO‑02: flickers only; no full → OK.
- CH1‑01/02/03: exactly one spectral‑full across chapter → OK.

### Branch coverage (Prologue & Ch1)
| scene_id | branches covered            | missing branches | notes |
|----------|-----------------------------|------------------|-------|
| PRO-01   | mainline, cautious          | none             |       |
| PRO-02   | mainline, stealth, failure  | none             |       |
| CH1-01   | mainline, stealth           | fail‑state       | add encounter skip consequence |
| CH1-02   | mainline, talk‑down         | none             |       |
| CH1-03   | mainline, alarm‑trigger     | stealth‑success  | add loot variant |

### Failstates
| scene_id | fail trigger                 | consequence                                 | recovery                    |
|----------|------------------------------|---------------------------------------------|-----------------------------|
| PRO-01   | player downed                | reload recent checkpoint                     | checkpoint before ambush    |
| PRO-02   | alarmed cultists cluster     | extra patrol waves                           | evasion path opens          |
| CH1-01   | flee without clue            | clue deficit +1                              | find backup clue in CH1‑02  |
| CH1-03   | spectral countermeasures missing | retreat forced, branch to side‑quest     | side‑quest grants counter   |