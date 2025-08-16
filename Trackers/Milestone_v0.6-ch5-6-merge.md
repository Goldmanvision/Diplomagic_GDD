# Milestone: v0.6-ch5-6-merge

Date created: 2025-08-16 ET
Owner: <your name>

Goal
- Merge CH5-CH6 into root docs and enforce CH6 rules. Validate and lock.

Scope
- Root edits: SEC-03/05/06/07, README/ToC.
- CH6: Blue-on-Blue hard fail (+ exceptions), evidence cap 3, HUD flags.
- Validations: grep suite and smoke checks.
- CI helpers: PR commenter and daily digest active.

Out of scope
- CH7 root edits and epilogue endings.
- New mechanics beyond enforcement items.

Deliverables
- Updated: SEC-03.md, SEC-05.md, SEC-06.md, SEC-07.md, README.md.
- Trackers updated to PASS: PR_Status_Board_CH5-CH6.md, PR_Validation_Results_Summary_CH5-CH6.md.
- Grep clean; smoke checks complete.

Acceptance criteria
- Strings present: "Evidence 0/3", "BlueOnBlue", "CH6 = raid", "Blue-on-Blue = hard fail", "No CCTV in Vault", "K-9 reroute".
- Systems snippet shows evidence cap 3 and Blue-on-Blue exceptions.
- All UI prompts <=14 chars.
- Period sweep: 0 hits for smartphone/Wi-Fi/Bluetooth/GPS/SMS.
- PR #1 merged to main. Main protected by branch rule.

Risks
- Helper drift vs root edits.
- Missed grep terms.
- Branch protection blocks merges (approvals).

Mitigations
- Run grep suite on PR open and hotfix if needed.
- Use PR commenter output for PASS/FAIL.
- Keep "Require approvals" off while solo.

Timeline
- Start: <YYYY-MM-DD>
- Code freeze: <YYYY-MM-DD>
- Merge: <YYYY-MM-DD>
- Post-merge validation: <YYYY-MM-DD>

Issue checklist
- [ ] Apply SEC-03 CH5-CH6 from helpers
- [ ] Insert SEC-05 systems snippets
- [ ] Append SEC-06/07 world+UI
- [ ] Replace SEC-07 prompts (<=14)
- [ ] README/ToC bullets
- [ ] Grep sweep + smoke checks
- [ ] Final validation summary update
- [ ] Merge PR and mark milestone complete

Tracker links
- Trackers/PR_Status_Board_CH5-CH6.md
- Trackers/PR_Validation_Results_Summary_CH5-CH6.md
- Trackers/ROOT_Merge_Smoke_Checks.md
- Patches/ROOT_Validation_Grep_Patterns.md
