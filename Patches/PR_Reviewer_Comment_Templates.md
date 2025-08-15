# PR Reviewer Comment Templates — CH5–CH6
Repo dir: /Patches

## Approve (no blocking issues)
```
LGTM. ✅
- 1994 audit passed
- Prompts ≤14
- Raid ROE + Blue-on-Blue fail present
- Evidence cap 3 present
- Ambient phrase usage OK
Merging on QA ✅
```

## Request changes (specific)
```
Requesting changes:
1) SEC-07 prompts table includes >14-char label(s): <refs>. Replace per ROOT_Prompts_Conflict_Map.md.
2) Narrative CH6 missing Blue-on-Blue fail line.
3) Evidence cap 3 not stated in Systems/UI.
After fixes, re-run Validation Tasklist and tag me.
```

## Question (non-blocking)
```
Question: Should "Ward Jam" appear in HUD alerts as well as prompts? If yes, add to SEC-07 Alerts.
```

## Period-1994 concern
```
Found possible period leak: "<term>" in <file/line>. Please replace with MicroTAC/pager/payphone/Polaroid or remove.
```
