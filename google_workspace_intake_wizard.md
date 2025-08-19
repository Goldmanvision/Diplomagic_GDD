# google_workspace_intake_wizard
**Macro name:** `google_workspace_intake_wizard`  
**Trigger:** `wiz gws`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Drive structure, permissions, Forms→Sheets intake, Apps Script mail alerts, review flow.  
**Risks:** Wrong sharing scope, PII in forms, trigger quotas, spam blocks. Use ASCII‑safe names.

---

## Step 1 — Create a Shared Drive and folders
**Goal:** One canonical Workspace location.

Structure (create in a Shared Drive named `DIPLOMAGIC`)
```text
/_intake/            # raw form responses (Sheets)
/_review/            # in‑progress docs
/published/          # approved exports (md only)
/templates/          # doc templates
/_automation/        # Apps Script project files
```
Success: Shared Drive exists with the folders above.  
Prompt: `y` / `n`.

---

## Step 2 — Set permissions
**Goal:** Least‑privilege access.

Roles
```text
Stationmaster: Manager
Postmaster: Content manager
Dept leads: Contributor
External reviewers: Commenter (time‑boxed links)
```
Apply roles on the Shared Drive root. Inherit to children.  
Success: Roles saved.  
Prompt: `y` / `n`.

---

## Step 3 — Add templates
**Goal:** Fast, consistent docs.

Create Docs in `/templates/`:
```text
Scene_Review_Template
Research_Request_Template
Task_Signoff_Template
```
Each should contain a one‑page checklist and required fields.  
Success: Templates created.  
Prompt: `y` / `n`.

---

## Step 4 — Build “Narrative Review” Google Form
**Goal:** Collect scene reviews.

Form fields (short answer unless noted):
```text
Scene ID (e.g., CH2_SCN03)
Department (dropdown: Narrative, Systems, QA, A&R, Steam Ops)
Owner handle
Link to draft (Drive URL)
Blocking? (checkbox)
Notes (paragraph)
```
Settings: Collect email, restrict to domain, limit to 1 response per user (optional).  
Success: Form created.  
Prompt: `y` / `n`.

---

## Step 5 — Link Form to a Sheet
**Goal:** Responses persist to Sheets.

Actions
```text
• In the Form → Responses → “Link to Sheets” → create new Sheet named:
  _intake_narrative_review
• Move the Sheet to `/_intake/`
```
Success: Sheet linked and moved.  
Prompt: `y` / `n`.

---

## Step 6 — Add tracker columns and data validation
**Goal:** Make the Sheet actionable.

Open `/_intake/_intake_narrative_review` and add columns to the right:
```text
Status (Data validation: New, In Review, Approved, Rework, Archived)
Assignee
Due (date)
Decision URL (md export path)
```
Freeze row 1. Protect Status/Assignee cells if needed.  
Success: Columns added.  
Prompt: `y` / `n`.

---

## Step 7 — Apps Script project
**Goal:** Create automation for alerts and stamping.

Actions
```text
• Open the linked Sheet → Extensions → Apps Script.
• Name the project: intake_narrative_review_automation
• File: Code.gs (replace contents with script below)
```
Paste:
```javascript
function onFormSubmit(e) {
  const sheet = e.range.getSheet();
  const row = e.range.getRow();
  const values = sheet.getRange(row, 1, 1, sheet.getLastColumn()).getValues()[0];

  // Columns (adjust indexes if your form order differs)
  const timestamp = values[0];
  const email = values[1];
  const sceneId = values[2];
  const dept = values[3];
  const owner = values[4];
  const draftLink = values[5];
  const blocking = values[6];
  const notes = values[7];

  // Stamp defaults
  const statusCol = sheet.getLastColumn() - 3; // Status column per Step 6 order
  const assigneeCol = sheet.getLastColumn() - 2;
  const decisionCol = sheet.getLastColumn() - 0;

  // Set initial Status if empty
  if (!sheet.getRange(row, statusCol).getValue()) {
    sheet.getRange(row, statusCol).setValue('New');
  }

  // Email alert
  const to = 'YOUR_MAIL_ALIAS@yourdomain.tld'; // TODO: set Postmaster alias
  const subject = `[INTAKE][Narrative Review] ${sceneId} — ${dept}`;
  const body = [
    `Time: ${timestamp}`,
    `Scene: ${sceneId}`,
    `Dept: ${dept}`,
    `Owner: ${owner}`,
    `Blocking: ${blocking}`,
    `Draft: ${draftLink}`,
    `Notes:\n${notes}`,
    `Sheet: ${SpreadsheetApp.getActiveSpreadsheet().getUrl()}`
  ].join('\n');

  try {
    GmailApp.sendEmail(to, subject, body);
  } catch (err) {
    console.error(err);
  }
}

function installTrigger() {
  const ss = SpreadsheetApp.getActive();
  ScriptApp.newTrigger('onFormSubmit')
    .forSpreadsheet(ss)
    .onFormSubmit()
    .create();
}
```
Success: Script saved without errors.  
Prompt: `y` / `n`.

---

## Step 8 — Authorize and install trigger
**Goal:** Ensure the script runs on new submissions.

Actions
```text
• Click “Run” → select `installTrigger` → authorize scopes when prompted.
• Verify trigger in Triggers panel (left sidebar).
```
Success: One trigger listed for “On form submit”.  
Prompt: `y` / `n`.

---

## Step 9 — Test submission
**Goal:** Validate end‑to‑end flow.

Actions
```text
• Submit the Narrative Review form with sample data.
• Confirm: row appears in Sheet; Status = New; email alert received by Postmaster.
```
Success: Email arrives and Sheet updated.  
Prompt: `y` / `n`.

---

## Step 10 — Build “Research Request” Form + Sheet
**Goal:** Intake for Authenticity & Research.

Repeat Steps 4–9 using these fields:
```text
Claim to verify (paragraph)
In‑game reference (scene/page/line)
Needed by (date)
Risk (dropdown: Low, Medium, High)
Links / sources (paragraph)
```
Name Sheet: `_intake_research_requests`.  
Update script `subject` prefix to `[INTAKE][Research Request]`.  
Success: Alerts work for A&R.  
Prompt: `y` / `n`.

---

## Step 11 — Views and filters
**Goal:** Quick queues for leads.

In each intake Sheet, create Filter Views:
```text
• My queue (Assignee = you)
• Blocking only (Status != Approved AND Blocking = TRUE)
• Due soon (Due within 7 days)
```
Success: Views saved and named.  
Prompt: `y` / `n`.

---

## Step 12 — Review flow and exports
**Goal:** Move from intake → review → published.

Process
```text
• Reviewer opens draft link; makes a copy from /templates/ to /review/.
• On approval, export final to Markdown and move to /published/ with name:
  <topic>_<YYYYMMDD>.md
• Paste the published file URL into “Decision URL” in the intake Sheet.
• Set Status → Approved.
```
Success: One sample item progressed to Approved with a Decision URL.  
Prompt: `y` / `n`.

---

## Optional — Gmail routing for Postmaster
**Goal:** Keep alerts tidy.

Create Gmail filters and labels:
```text
Matches: subject has [INTAKE]
Do this: Apply label DIPLOMAGIC/INTAKE, Skip Inbox (optional)
```
Success: New alerts land under the label.  
Prompt: `y` to finish, `n` for targeted troubleshooting.

---

## Troubleshooting quick refs
```text
• No emails → Script not authorized or trigger missing.
• Duplicate emails → Multiple triggers installed; keep exactly one.
• Form edits broke column order → Adjust indexes in Apps Script.
• “You need permission” on draft links → Fix Drive sharing on /review/ folder.
```
