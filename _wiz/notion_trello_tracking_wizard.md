# notion_trello_tracking_wizard
**Macro name:** `notion_trello_tracking_wizard`  
**Trigger:** `wiz tracker`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Project tracking in Notion and Trello. You may use one or both.  
**Risks:** Over‑permission, field drift, duplicate sources of truth. Keep ASCII‑safe names.

---

## Step 1 — Canonical taxonomy
**Goal:** Shared language across tools.

Statuses
```text
Backlog, Planned, In Progress, Review, Blocked, Done, Archived
```

Departments (from charters)
```text
Narrative, Combat & Systems, Statblocks & Enemies, A&R, QA & UX, Steam Ops, Mail
```

Priorities
```text
P0-Blocker, P1-High, P2-Med, P3-Low
```

Success: You accept these lists or supply replacements.  
Prompt: `y` to accept, `n` to adjust.

---

## Step 2 — Notion: create database
**Goal:** Central tracker in Notion.

Actions
```text
• Create database: DIPLOMAGIC — Tracker
• Properties (Type in parentheses)
  - Title (Title)
  - Type (Select: Task, Bug, Scene, Research, Asset, Release)
  - Dept (Select: values from Step 1)
  - Priority (Select: values from Step 1)
  - Status (Select: values from Step 1)
  - Assignee (People)
  - Due (Date)
  - Links (URL)
  - SceneID (Text)
  - BuildID (Text)
  - EstimateH (Number)
  - ActualH (Number)
  - Notes (Rich text)
  - Created (Created time)
  - Done (Date)
  - CycleDays (Formula): dateBetween(prop("Done"), prop("Created"), "days")
```

Views
```text
• My Queue (Assignee = me, Status not Done/Archived)
• Blockers (Status = Blocked)
• By Dept (Group by Dept, filter Status != Archived)
• Bugs (Type = Bug, sort Priority asc)
• Calendar (Calendar by Due)
```

Templates
```text
• Bug: fields preset Type=Bug, Priority=P1, checklist Handoff
• Scene Task: Type=Scene, fields for SceneID, link to spec doc
```

Success: DB exists with properties, at least one view.  
Prompt: `y` / `n`.

---

## Step 3 — Notion: lightweight automations
**Goal:** Reduce manual steps.

Actions
```text
• Add “Done” date rollup: when Status changes to Done, set Done = now (Notion Automations)
• Optional reminder: When Due arrives and Status != Done, notify Assignee
```
Success: Automation toggles saved.  
Prompt: `y` / `n`.

---

## Step 4 — Trello: board and lists
**Goal:** Mirror taxonomy for teams preferring Trello.

Actions
```text
• Create board: DIPLOMAGIC — Tracker
• Lists (left→right): Inbox, Backlog, Planned, In Progress, Review, Blocked, Done, Archive
• Labels: Narrative, Systems, Enemies, A&R, QA/UX, Steam Ops, Mail, Blocked
```
Success: Board created with lists and labels.  
Prompt: `y` / `n`.

---

## Step 5 — Trello: Custom Fields and templates
**Goal:** Add key metadata to cards.

Enable “Custom Fields” power‑up. Create fields:
```text
Priority (Dropdown: P0, P1, P2, P3)
Dept (Dropdown: per Step 1)
SceneID (Text)
BuildID (Text)
```

Card templates (Create in “Templates” section):
```text
• Bug — includes checklist “Handoff Checklist”
• Scene Task — includes fields Dept=Narrative, SceneID placeholder
```

Success: Fields and templates exist.  
Prompt: `y` / `n`.

---

## Step 6 — Trello: Butler rules (auto‑routing)
**Goal:** Move work and alert people automatically.

Create rules
```text
1) When a card is moved to “Review” → add checklist “Handoff”, add label “Mail”, @mention Postmaster.
2) When the “Blocked” label is added → move the card to “Blocked”, set Priority=P0.
3) When a card is moved to “Done” → set due date complete, move to “Archive” after 7 days.
```

Optional (notifications)
```text
• If on paid plan: create Butler rule to send a webhook to Discord/Slack on Blocked.
• Else: enable Slack/Discord power‑up and map list moves to channel posts.
```

Success: Rules saved and visible under Automation.  
Prompt: `y` / `n`.

---

## Step 7 — GitHub linking
**Goal:** Trace work to commits and PRs.

Actions
```text
• On Notion items, paste GitHub Issue/PR URL in Links.
• On Trello cards, Attach → Link → GitHub URL.
• Naming convention for branches: feature/<SceneID> or fix/<IssueID>
```

Success: One sample item linked to a repo artifact.  
Prompt: `y` / `n`.

---

## Step 8 — Mail/Handoff integration
**Goal:** Keep Integration & Validation in the loop.

Checklist content (use in Notion template and Trello template):
```text
[ ] Owner filled
[ ] Links added (spec, build, evidence)
[ ] Repro or acceptance steps attached
[ ] Risks noted
[ ] Decision logged (DECISIONS.md path)
```

Success: “Handoff” checklist present on new items.  
Prompt: `y` / `n`.

---

## Step 9 — Reports
**Goal:** Visibility without manual work.

Notion
```text
• Create Dashboard page with linked views:
  - Throughput (table, last 7/14/30 days)
  - CycleDays distribution (group by Priority)
  - Overdue items (Due < today, Status != Done)
```

Trello
```text
• Enable Dashboard (if plan supports) for card counts by list and label.
• Or export CSV and chart elsewhere.
```

Success: One dashboard or saved view exists.  
Prompt: `y` / `n`.

---

## Step 10 — Exports and backup
**Goal:** Keep Markdown as the durable format.

Actions
```text
• Notion: Export → Markdown & CSV for the Tracker once per milestone.
• Trello: Append `.json` to board URL to fetch a JSON snapshot; save to /_exports/.
```
Success: One export saved to your repo or Drive.  
Prompt: `y` to finish, `n` for help on any sub‑step.

---

## Troubleshooting quick refs
```text
• Fields missing in views → edit view columns (Notion) or card back (Trello).
• Butler not running → disabled by admin or plan limits reached.
• Too many sources of truth → pick one primary (Notion) and mirror minimal fields to Trello.
```
