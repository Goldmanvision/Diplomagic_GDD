# PR_Validation_Tasklist_CH7.md

Scope: Validate CH7 pack integration. City evidence cap = 2. Non-lethal favored. Friendly/civilian hits fail. Period 1994. Prompts ≤14.

## Pre-checks
- [ ] PR targets `main` from `feat/ch7-pack`.
- [ ] Labels: period-1994, prompt-≤14, evidence-cap-2, non-lethal.
- [ ] Milestone set: v0.7-ch7-pack.

## Content checks
- [ ] SEC-03: CH7 replaced with helper paste.
- [ ] SEC-06/07: city world/UI appended.
- [ ] SEC-07: CH7 prompt extensions added; all ≤14.
- [ ] README/ToC updated with CH7 bullets.
- [ ] Epilogue seeds file referenced where needed.

## Rules present
- [ ] City evidence cap = 2; HUD shows `Evidence 0/2`.
- [ ] Non-lethal favored in city; friendly/civilian hits fail.
- [ ] Krill illusions and Mindscape anchor noted.
- [ ] Consent/warrant rules for photography in private interiors.
- [ ] 1994 constraints carried (no smartphone/Wi‑Fi/Bluetooth/GPS/SMS).
- [ ] Spells: Phrases equip L/R; Scrolls single-use; Mana calm-regen.

## Grep suite
Use prior grep file: `/Patches/ROOT_Validation_Grep_Patterns.md` plus these:
- `"Evidence 0/2"`
- `"friendly/civilian hits fail"`
- `"Krill"`
- `"Mindscape"`
- `"consent"`
- `"warrant"`

## Prompt length sweep
Confirm each in `ROOT_SEC-07_UI_Prompts_CH7_Extensions.md` ≤14.

## Smoke checks
- [ ] ToC anchors resolve.
- [ ] Evidence counter hides outside investigation.
- [ ] Illusion reveal banner appears.
- [ ] No modern tech terms.

## Sign-off
- [ ] Owner sign-off
- [ ] Reviewer sign-off
