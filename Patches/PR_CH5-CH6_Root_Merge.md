# CH5–CH6 root merge

Integrate Chapter 5 and Chapter 6 narrative, systems, and world/UI into the root docs.

## Summary
- Replace SEC‑03 CH5 and CH6 with helper pastes.
- Insert systems snippets in SEC‑05.
- Append world + UI merges in SEC‑06/07.
- Replace UI prompts with the SEC‑07 master.
- Update README/ToC entries.
- Link ASCII map in SEC‑06.

## Constraints
- Period: **1994**. No smartphone/Wi‑Fi/Bluetooth/GPS/SMS.
- Prompts ≤14 characters.
- Ambient phrase only: “the stars are right tonight.”
- Spells: **Phrases equip L/R**, **Scrolls single‑use**, **Mana calm‑regen**.

## CH6 Raid Rules (must appear in helpers and HUD)
- CH6 = raid. Lethal authorized. Neutralizations score‑neutral.
- Blue‑on‑Blue = hard fail (−10). Exceptions: Shield‑absorbed; >10 m single shotgun pellet.
- Cameras only in Service Passage; **No CCTV in Vault**; breaker ≈90 s; **K‑9 reroute**.
- Evidence cap in CH6 = **3**. HUD shows `Evidence 0/3` and `BlueOnBlue`.

## Validation
Run:
- `/Trackers/PR_Validation_Tasklist_CH5-CH6.md`
- Record results in `/Trackers/PR_Validation_Results_Summary_CH5-CH6.md`
- Grep per `/Patches/ROOT_Validation_Grep_Patterns.md`
- Smoke per `/Trackers/ROOT_Merge_Smoke_Checks.md`

## Labels & Milestone
Labels: `period-1994`, `prompt-≤14`, `roe-raid`, `blue-on-blue`, `evidence-cap-3`  
Milestone: `v0.6-ch5-6-merge`

## Attachments
- Narrative pastes: `ROOT_SEC-03_CH5_Narrative_Paste.md`, `ROOT_SEC-03_CH6_Narrative_Paste.md`
- To follow in next commits (kept ≤3 files per export): UI prompts master, systems snippets, world/UI merge, ASCII map, README/ToC bullets, PR attachments.
