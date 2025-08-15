# CH6 — Blue‑on‑Blue Test Plan
Repo dir: /Trackers

## Goals
Validate friendly-fire fail logic and exceptions.

### Cases
- B1: Pistol body shot on Clara → FAIL, log event
- B2: Shield absorbs shotgun blast on Reddy → No fail, log absorb
- B3: Shotgun single pellet at >10 m on Deputy → No fail
- B4: Rifle graze at 2 m on Deputy → FAIL
- B5: TK push knocks ally into hazard → FAIL (counts as friendly hit)
- B6: Simultaneous AoE near ally with Shield → No fail

### Steps
1) Load CH6 test arena.
2) Trigger each case once. Record in `CH6_Ending_Scorecard.md`.
3) Confirm fail screen where expected; icon flash on set.
4) Confirm exceptions behave as specified in systems doc.

Notes: Neutralizations remain score‑neutral. Evidence cap unaffected.
