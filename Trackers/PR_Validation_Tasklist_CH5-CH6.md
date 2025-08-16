# PR_Validation_Tasklist_CH5-CH6.md

Scope: Validate CH5–CH6 root merge. Keep period 1994. Enforce prompts ≤14. Enforce raid rules.

## Pre-checks
- [ ] Open PR exists and targets `main` from `feat/ch5-6-root-merge`.
- [ ] Labels applied: period-1994, prompt-≤14, roe-raid, blue-on-blue, evidence-cap-3.
- [ ] Milestone set: v0.6-ch5-6-merge.

## Content checks
- [ ] SEC-03: CH5 and CH6 replaced with helper pastes.
- [ ] SEC-05: systems snippets inserted at correct anchors.
- [ ] SEC-06/07: world+UI appended.
- [ ] SEC-07: prompts replaced with master; all ≤14 chars.
- [ ] README/ToC updated with bullets.
- [ ] ASCII map linked inside SEC-06.

## Rules present
- [ ] CH6 = raid; lethal authorized; neutralizations score-neutral.
- [ ] Blue-on-Blue = hard fail (−10). Exceptions: Shield-absorbed; single shotgun pellet >10 m.
- [ ] Cameras only in Service Passage; **no CCTV in Vault**.
- [ ] Breaker ≈90 s cooldown present.
- [ ] K‑9 reroute mention present.
- [ ] Evidence cap in CH6 = 3; HUD shows `Evidence 0/3` and `BlueOnBlue`.

## Grep suite
Run patterns from `/Patches/ROOT_Validation_Grep_Patterns.md`.
Record findings in the Results Summary.

## Prompt length sweep
Confirm every prompt in `ROOT_SEC-07_UI_Prompts_Master.md` is ≤14.

## Period sweep
Confirm no modern terms: smartphone, Wi‑Fi, Bluetooth, GPS, SMS.

## Smoke checks
- [ ] Navigation anchors intact (no broken ToC links).
- [ ] Unique snippet IDs in SEC-05.
- [ ] Service Passage is the only CCTV zone.
- [ ] Vault forbids photography.
- [ ] No prompt over 14 chars displayed in HUD or hints.

## Sign-off
- [ ] Owner sign-off
- [ ] Reviewer sign-off
