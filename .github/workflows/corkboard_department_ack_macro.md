> Mirror path: /Corkboard/templates/department_ack_macro.md
> Source chat: GDD Rebuild 2025-08-17 0000 ET — Mail Department
> Last mirrored: 2025-08-17

# Department ACK Macro
Use to acknowledge a Corkboard notice and auto‑fill the verification form. Replace `<>` and post in your department chat, copying Postmaster.

## ACK text block
```
Confirmed. <Department> — <Codename>. First handoff: <item> due <YYYY-MM-DD>. Paths: <paths>. Blockers: <none or numbered list>. Notice: <YYYYMMDD>_<HHMM>ET_<slug>.
```

## Verification table row (pasteable)
Paste this single line into the verification table for the matching notice.
```
| <Department> | <Codename> | <YYYY-MM-DD HH:MM ET ping> | Yes | <YYYY-MM-DD HH:MM ET ack> | <first handoff item> | <due date> | <paths> | <blockers ref or “none”> | <ack permalink if available> |
```

Notes
- Timezone is ET.  
- If you do not know the ping time, leave it blank; Postmaster will fill.  
- “ACK link” can be a chat permalink or N/A.

