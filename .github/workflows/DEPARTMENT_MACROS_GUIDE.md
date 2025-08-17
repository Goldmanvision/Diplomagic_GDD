> Mirror path: /.github/workflows/DEPARTMENT_MACROS_GUIDE.md
> Source chat: GDD Rebuild 2025-08-17 0000 ET — Mail Department
> Last mirrored: 2025-08-17

# Department Macros User Guide (v1.0)

Purpose: fast, consistent cross‑department communication. Paste macros as‑is, replace `<>`.

## Timestamping and retrieval
- Filename rule: `/Corkboard/<YYYYMMDD>_<HHMM>ET_<slug>.md`.
- Latest pointer: `/Corkboard/latest.md`.
- Departments must read `latest.md` first; else choose the highest timestamped file.
- Reference: `/Corkboard/RETRIEVAL_RULES.md`.

---
## Macro: `ptcork v2` — broadcast a specific notice (with links)
```
From: Postmaster (Mail Department)
To: <Department>
Subj: Corkboard — please confirm <YYYYMMDD>_<HHMM>ET_<slug>

Check `/Corkboard/<YYYYMMDD>_<HHMM>ET_<slug>.md` and reply:
"Confirmed. <Department> — <Codename>. First handoff: <item> due <YYYY-MM-DD>. Paths: <paths>. Blockers: <none or list>."

Open in GitHub:
<https://github.com/Goldmanvision/Diplomagic_GDD/blob/main/Corkboard/<YYYYMMDD>_<HHMM>ET_<slug>.md>
Download .md:
<https://raw.githubusercontent.com/Goldmanvision/Diplomagic_GDD/main/Corkboard/<YYYYMMDD>_<HHMM>ET_<slug>.md>
```

## Macro: `ptcork_latest` — broadcast “check the latest”
```
From: Postmaster (Mail Department)
To: <Department>
Subj: Corkboard — please confirm latest

Check the latest Corkboard notice (prefer `/Corkboard/latest.md`; else the file with the highest timestamp). Reply with the standard ACK and copy Postmaster.
```

## Macro: Department ACK — reply format
**ACK text block**
```
Confirmed. <Department> — <Codename>. First handoff: <item> due <YYYY-MM-DD>. Paths: <paths>. Blockers: <none or numbered list>. Notice: <YYYYMMDD>_<HHMM>ET_<slug>.
```
**Verification table row (single‑line)**
```
| <Department> | <Codename> | <YYYY-MM-DD HH:MM ET ping> | Yes | <YYYY-MM-DD HH:MM ET ack> | <first handoff item> | <due date> | <paths> | <blockers ref or “none”> | <ack permalink or N/A> |
```

## Template: Department prompt (auto‑select role)
Paste into a new department chat. Add a line at top: `Filled: Mail, <others>`.
```
You are GPT-5 Thinking joining Goldmanvision’s DIPLOMAGIC as a department lead. Auto-select the first unfilled role from: Narrative (Scribe), Combat & Systems (Tactician), Statblocks & Enemies (Keeper), Authenticity & Research (Archivist), QA & UX (Inspector), Steam Operations (Stationmaster). Declare Codename and allowed repo paths per **Department Charters Pack.md** and operate only within those paths. Use the Narrative Playbook and Outline as ground truth. 1994 main setting with 1989 prologue; enforce period accuracy. Export `.md` only. Keep answers short. Do not claim background work or future results. Ask only necessary questions and accept y/n or numbers. **On start, read the latest Corkboard notice**: if `/Corkboard/latest.md` exists, follow that; else select the file in `/Corkboard` with the highest `<YYYYMMDD>_<HHMM>ET` prefix. Route cross‑department work through Mail (Postmaster) using **Handoff Checklist.md** and draft `/DECISIONS.md` and `/CHANGELOG.md` entries. Warn before heavy operations or anything that risks resets, timeouts, or quotas. Name this chat `GDD Rebuild <YYYY-MM-DD HHmm ET> — <Selected Department>`.
```

---
## Verification workflow
- Form template: `/Corkboard/templates/verification_form_template.md`.
- For each notice, create `/Corkboard/verification/<notice>_verification.md`.
- Departments use the ACK macro and paste a row into the form.
- Follow‑ups: daily 10:00 ET until all acknowledged.

## Notes
- Chat naming macro `ptstamp` returns: `GDD Rebuild <YYYY-MM-DD HHmm ET>`.
- Exports: `.md` only.
- Period accuracy: 1994 main, 1989 prologue.
