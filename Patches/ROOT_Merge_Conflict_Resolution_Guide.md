# Root Merge Conflict Resolution — CH5–CH6
Repo dir: /Patches

## Typical conflicts
- Anchors moved or extra chapter inserted between CH5 and CH6.
- Older ROE text (“non‑lethal preferred”) lingering in systems.
- Duplicate UI prompt tables.

## Resolve strategy
1) **Narrative:** Keep *this* patch as source of truth. Remove obsolete CH5/CH6 prose blocks wholesale.
2) **Systems:** Prefer raid ROE, BlueOnBlue fail, and phrase/scroll model. Delete legacy IA penalty lines.
3) **World/UI:** Merge nodes; dedupe prompt lists. Keep ≤14‑char enforcement and Annex tasks.
4) **Scoring:** Ensure CH6 evidence cap = 3 and lethal neutralizations = 0 points.
5) **1994:** Replace any StarTAC mentions with MicroTAC; remove digital camera notes.

## Sanity checks
- Search repo for “non‑lethal preferred” → none.
- Search repo for “StarTAC” → none.
- Search repo for prompts longer than 14 → none.

## Post‑merge
Run `/Trackers/CH5-6_Build_Verification.md`.
