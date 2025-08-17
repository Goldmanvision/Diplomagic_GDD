---
Department: QA & UX
Codename: Exterminator
Type: Template
Status: Active
Date: 2025-08-17
---

# Severity & Priority Matrix

## Definitions
Severity (impact on player):
- **S0** Crash/data loss, progression block, save corruption.
- **S1** Major feature broken, frequent soft lock, widespread missing content.
- **S2** Noticeable defect, inconsistent behavior, minor progression friction.
- **S3** Cosmetic or trivial issue.

Priority (when to fix):
- **P0** Must fix before release branch cut.
- **P1** Fix for upcoming milestone.
- **P2** Backlog; fix if time.
- **P3** Track; unlikely to fix.

## Matrix
|        | P0 | P1 | P2 | P3 |
|--------|----|----|----|----|
| **S0** | ✔  |    |    |    |
| **S1** | ✔  | ✔  |    |    |
| **S2** |    | ✔  | ✔  |    |
| **S3** |    |    | ✔  | ✔  |

## Triage rules
- S0/P0 routed immediately to engineering lead. QA verifies hotfix.
- Narrative issues reference `scene_id` when applicable.
- Attach logs, repro rate, and hardware profile for S0–S1.
- Label format: `area/feature`, `severity/S#`, `priority/P#`.

## Sign‑off
- Owner (QA):
- Postmaster:
- Blockers: none | list
