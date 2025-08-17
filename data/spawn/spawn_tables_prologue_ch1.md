---
Title: Prologue & Chapter 1 — Spawn Tables
Department: Adversary & NPC Systems
Codename: Taxonomist
Owner: Taxonomist
Reviewer: Storymaster; Postmaster
Date: 2025-08-17
Type: Spawn Tables
Status: Active
---

## Revision — 2025-08-17
Added `scene_id` column and applied SG-20250817.

### Rules — SG-20250817
- Flicker allowed when clue_threshold >= 1 and low-light present.
- Full manifestation allowed only when clue_threshold >= 2 AND darkness condition is met.
- Cap: <= 1 full manifestation per chapter.

### Prologue (scene_id binding)
| scene_id | location | d6    | result                             | adv_ids                | cap | notes                |
|----------|----------|-------|------------------------------------|------------------------|-----|----------------------|
| PRO-01   | street   | 1     | 2x occult cultists                 | ADV-0001               | 1   | light intro          |
| PRO-01   | street   | 2     | 1x new-kadathi-cultist             | ADV-0003               | 1   | ranged harass        |
| PRO-02   | street   | 3     | 1x mind-swapped-civilian           | ADV-0002               | 1   | non-lethal branch    |
| PRO-02   | street   | 4     | spectral flicker                   | ADV-0004               | 1   | tease only           |
| PRO-02   | basement | 1-2   | 2x occult cultists                 | ADV-0001               | 1   | closed space         |
| PRO-02   | basement | 5     | 1x mind-swapped-civilian           | ADV-0002               | 1   | interruption         |
| PRO-02   | basement | 6     | spectral full                      | ADV-0004               | 1   | requires darkness    |

**Prologue caps:** <= 2 total combats; >= 1 non-lethal engagement.

### Chapter 1 (scene_id binding)
| scene_id | location  | d6  | result                              | adv_ids                | cap | notes                 |
|----------|-----------|-----|-------------------------------------|------------------------|-----|-----------------------|
| CH1-01   | alley     | 1   | 2x occult cultists                  | ADV-0001               | 1   | light                 |
| CH1-01   | alley     | 2   | 1x cultist + 1x new-kadathi         | ADV-0001, ADV-0003     | 1   | mixed                 |
| CH1-02   | alley     | 3   | 1x mind-swapped-civilian            | ADV-0002               | 1   | conversation beat     |
| CH1-02   | alley     | 4   | spectral flicker                    | ADV-0004               | 1   | tease only            |
| CH1-03   | warehouse | 1   | 2x cultists + 1x new-kadathi        | ADV-0001, ADV-0003     | 1   | medium                |
| CH1-03   | warehouse | 2   | spectral full                       | ADV-0004               | 1   | boss-like moment      |
| CH1-03   | warehouse | 3   | 1x mind-swapped-civilian            | ADV-0002               | 1   | quiet tension         |

**Chapter 1 caps:** <= 3 total combats; spectral full <= 1.

### Validation
- IDs resolve to `data/statblocks/` files: ADV-0001, ADV-0002, ADV-0003, ADV-0004.
- Period-correct equipment only (see research checks).
- Ties to `/narrative_scene_ids_prologue_ch1.md` (to be moved to `/narrative/scenes/scene_ids_prologue_ch1.md`).

### Sign-off
Owner (Taxonomist): ___  Date: ___  
Storymaster: ___  Date: ___  
Postmaster: ___  Date: ___
