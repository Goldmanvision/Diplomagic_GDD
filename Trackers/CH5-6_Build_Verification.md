# CH5-6_Build_Verification.md

Scope: Post-merge functional sweep for CH5–CH6. Period 1994. Prompts ≤14. Ambient phrase only: “the stars are right tonight.”

## Test environment
- Branch: `feat/ch5-6-root-merge` (game content) with helpers on `main`.
- Platform: Windows build (target). Debug HUD enabled.
- Fresh profile to validate Deputy randomization per session.

## Preflight
- [ ] Helpers present on `main` under `/Patches` and trackers under `/Trackers`.
- [ ] README/ToC updated and anchors intact.
- [ ] Load game with CH5 unlocked and CH6 reachable.

## CH5 — City rules
- [ ] Friendly/civilian hits cause fail in city encounters.
- [ ] Non-lethal options available and favored by scoring/hints.
- [ ] Contacts use landlines/pagers/fax; FieldPad/MEDSTAT cable/SENTINEL only.

## CH6 — Raid criticals
- [ ] **CH6 = raid**; lethal authorized; neutralizations score-neutral.
- [ ] **Blue-on-Blue** hard fail (−10) except:
  - [ ] Shield-absorbed friendly hit does not fail.
  - [ ] Single shotgun pellet at >10 m does not fail.
- [ ] **Evidence cap** = 3. Fourth pickup denied with “Evidence full” prompt.
- [ ] **HUD** shows `Evidence 0/3` and `BlueOnBlue` flag.
- [ ] **Cameras only** in **Service Passage**; **no CCTV** in Vault.
- [ ] **Breaker** recycle ≈ **90 s** (staged restore at ~30/60/90 s).
- [ ] **K‑9 reroute** works via handler diversion or scent decoy; success opens ~90 s window.

## Interactables
- [ ] Valves A/B/C operate with audible pressure change.
- [ ] Ward Jam disables ward nodes for intended duration.
- [ ] Breach points support Plant → Detonate loop; jammer affects wards.
- [ ] Photo allowed only in Service Passage; Vault blocks photography.

## Spells & Items
- [ ] Phrases equip **L/R**; Scrolls **single-use**; Mana **calm-regen** (no combat spike).
- [ ] Deputy name randomized; `<DEPUTY_NAME>` placeholder absent in player-facing text.

## UI/Prompt limits
- [ ] Prompt set present: Ward Jam, Cast L/R, Equip L/R, Valve A/B/C, Plant, Detonate, Photo, Sample.
- [ ] No prompt exceeds 14 characters anywhere in HUD or hints.

## Period authenticity
- [ ] No smartphone/Wi‑Fi/Bluetooth/GPS/SMS references.
- [ ] Navigation via printed maps, signage, analog radio frequencies.

## Logs to capture (attach to Results Summary)
- Screenshot: HUD with `Evidence 0/3` and `BlueOnBlue`.
- Screenshot: Service Passage photo allowed; Vault photo denied.
- Video/GIF: breaker trip and staged restore timing.
- Video/GIF: K‑9 reroute success window.
- Screenshot: shotgun pellet >10 m exception working.

## Quick grep suite (optional)
See `/Patches/ROOT_Validation_Grep_Patterns.md`. Record outputs in Results Summary.

## Acceptance
- [ ] All checks PASS or have documented waivers.
- [ ] PR labeled, milestone set, Results Summary updated.
- [ ] Reviewer sign-off recorded.
