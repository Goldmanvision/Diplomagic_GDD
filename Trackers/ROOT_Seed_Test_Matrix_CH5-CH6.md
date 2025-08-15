# Tracker — Seed Test Matrix (DeputyName & Outcomes)
Repo dir: /Trackers
Date: 2025-08-15

## Purpose
Verify deterministic DeputyName selection and stable endings/score across seeds.

| Save Seed | DeputyName | Path | Evidence (0–3) | BlueOnBlue | Ending | FinalScoreDelta | Notes |
|---:|---|---|---:|---|---|---|---|
| 1001 |  | Contain | 2 | 0 | Contain |  |  |
| 1002 |  | Sever | 1 | 0 | Sever |  |  |
| 1003 |  | Black File | 3 | 0 | Black File |  | Rep −5 |
| 1004 |  | Contain | 0 | 1 | — | FAIL | Friendly hit |
| 1005 |  | Sever | 3 | 0 | Sever |  | Ammo tight |

Rules: Name chosen once per save from pool, seeded deterministically. Surname may elide for UI width. Constraints: 1994 lock; prompts ≤14; ambient phrase only: “the stars are right tonight.”
