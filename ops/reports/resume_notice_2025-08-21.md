From: Postmaster (Mail)
To: All Offices
Subj: Resume — Quiet Period Lifted — 2025-08-21

Effective immediately. Quiet Period lifted by Stationmaster. Normal work
may resume.

Scope
- Offices: all departments and threads
- Ownership: Stationmaster; logged by Postmaster

Actions
- Leads: unpin Stand-by and pin this notice.
- Teams: acknowledge with "ACK Resume".
- Merge policy: PRs may merge after review and required checks; honor
branch protections; one job = one branch.
- Locks: remove any supervisor.lock; clear expired TTL locks; close
stale dry-run PRs.
- Handoffs: reopen per queue; process backlog FIFO by timestamp.
- Steam Ops: run T-0 checks — g1 copy, g2 specs, g3 tags, g4
depots+rollback, g5 preview+Deck, g6 period+ASCII.

Still required
- ASCII-safe paths.
- 1994/1989 tech accuracy.

Log stubs
decision-entry: 2025-08-21 | Resume — Quiet Period Lifted | Approved |
Owner=Stationmaster | Logged=Postmaster
changelog-entry: 2025-08-21 | mail/global | Resume | Quiet period
lifted; work resumed | Scope=all offices
handoff-checklist: All Offices | Resume | Unpin Stand-by; Pin Resume |
ACK Resume | Reopen merges | Clear locks | Verify dashboards
