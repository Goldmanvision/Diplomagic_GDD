---
Title: Macro — rollovernc (new chat rollover)
Department: Mail
Codename: Postmaster
Date: 2025-08-17
Status: Active
---

Purpose
- Create a fresh department chat and post a Corkboard memo announcing rollover. Append decision log.

Inputs
- `dept`  — e.g., "Mail Department"
- `codename` — e.g., "Postmaster"
- `suffix` — e.g., "Ops Thread 2"
- `channel` — default `#ops`
- `link` — default `/DECISIONS.md`
- `note` — optional extra sentence

Outputs
1) **ptcork v2** block for the Corkboard.
2) **DECISIONS.md** append line.
3) Commit/PR copy blocks.

ptcork template
```
ptcork v2
title: {dept} rollover
channel: {channel}
content: {dept} is moving to “{codename} — {suffix}” due to log size. Old thread enters naptime. All routing and logs continue in the new thread. Double-Confirm remains for multi-file batches. {note}
link: {link}
---
```

DECISIONS append template
```
## {date}
- {dept} chat rollover to “{codename} — {suffix}”; prior thread archived with naptime; routing unchanged.
```

Commit/PR blocks
**Summary**
```
ops: {dept|lower} chat rollover → {codename} — {suffix}
```
**Description**
```
- ops/reports/ptcork_{dept|lower|kebab}_rollover_{date}.md: corkboard memo.
- DECISIONS.md: append rollover entry.

notes:
- ascii-safe paths
- validator g1–g6 ready
```

Usage
- Fill placeholders and paste the blocks. Or run the helper scripts in `ops/scripts/`.
