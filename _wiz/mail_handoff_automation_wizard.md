# mail_handoff_automation_wizard
**Macro name:** `mail_handoff_automation_wizard`  
**Trigger:** `wiz mail`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Mail routing, handoff checklist, DECISIONS.md/CHANGELOG.md logging, CLI helpers.  
**Risks:** Mail quotas, script limits, wrong repo path, branch protection. Use ASCII‑safe names and paths.

---

## Step 1 — Repo structure for Mail
**Goal:** Add canonical ops paths and logs to the main repo.

Create folders and base files:
```bash
mkdir -p ops/mail/bin ops/mail/templates
:> DECISIONS.md
:> CHANGELOG.md
git add ops/mail DECISIONS.md CHANGELOG.md
git commit -m "mail: init ops paths and logs" || true
git push || true
```
Success: Paths exist on `main`.  
Prompt: `y` / `n`.

---

## Step 2 — Handoff checklist template
**Goal:** Standardize cross‑dept handoffs.

Create `ops/mail/templates/handoff_checklist.md`:
```markdown
# Handoff Checklist
- [ ] Owner set
- [ ] Links attached (spec, build, evidence)
- [ ] Repro / acceptance steps included
- [ ] Risks noted
- [ ] Decision logged (DECISIONS.md path)
```
Commit:
```bash
git add ops/mail/templates/handoff_checklist.md
git commit -m "mail: add handoff checklist template"
git push
```
Success: Template committed.  
Prompt: `y` / `n`.

---

## Step 3 — Mail templates
**Goal:** Reusable messages for ops events.

Create `ops/mail/templates/standby.md`:
```markdown
From: Postmaster (Mail)
To: All Offices
Subj: Stand-by — Quiet Period — {{DATE}}

Effective now. Hold non-critical commits and chat traffic until Resume is posted by Stationmaster.
Critical hotfixes require Double Confirm.

Scope
- Offices: all departments and threads
- Duration: until explicit Resume notice
- Ownership: Stationmaster; logged by Postmaster

Rules
1) Non-critical work: defer commits, pause batch uploads, minimize chatter.
2) Critical hotfixes only if build blocking, data loss, security, or store deadline.
   Double Confirm = reply "y" then token HOTFIX. Mail logs the decision.
3) Handoffs freeze unless pre-approved.
4) ASCII-safe paths and 1994/1989 accuracy remain required.

Actions
- Leads: pin this notice in your office.
- Teams: acknowledge with "ACK Stand-by" after reading.
- Hotfix requests: include impact, files, and rollback plan.
```

Create `ops/mail/templates/ack_request.md`:
```markdown
From: Postmaster (Mail)
To: {{TEAM}}
Subj: Stand-by — ACK request — {{DATE}}

Reply "ACK Stand-by" to confirm receipt. Quiet Period is active.
Hotfixes require Double Confirm ("y" then HOTFIX). Pin the notice.
```

Commit:
```bash
git add ops/mail/templates/*.md
git commit -m "mail: add standby and ack templates"
git push
```
Success: Templates committed.  
Prompt: `y` / `n`.

---

## Step 4 — CLI logger: decisions
**Goal:** Append structured entries to DECISIONS.md.

Create `ops/mail/bin/decision.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
owner="${1:-Postmaster}"
title="${2:-Stand-by Quiet Period}"
status="${3:-Approved}"
scope="${4:-global}"

ts="$(date -u +%F)"
echo "decision-entry: ${ts} | ${title} | ${status} | Owner=${owner} | Scope=${scope}" >> DECISIONS.md
git add DECISIONS.md
git commit -m "log: decision '${title}' (${status}) by ${owner}" || true
git push || true
echo "Logged: ${title} (${status})"
```

Make executable and commit:
```bash
chmod +x ops/mail/bin/decision.sh
git add ops/mail/bin/decision.sh
git commit -m "mail: add decision logger"
git push
```
Success: Script committed.  
Prompt: `y` / `n`.

---

## Step 5 — CLI logger: changelog
**Goal:** Append entries to CHANGELOG.md.

Create `ops/mail/bin/changelog.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
area="${1:-mail/global}"
summary="${2:-Stand-by}"
detail="${3:-Logged}"
scope="${4:-A&R}"

ts="$(date -u +%F)"
echo "changelog-entry: ${ts} | ${area} | ${summary} | ${detail} | Scope=${scope}" >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "log: changelog ${area} — ${summary}"
git push || true
echo "Logged: ${area} — ${summary}"
```

Make executable and commit:
```bash
chmod +x ops/mail/bin/changelog.sh
git add ops/mail/bin/changelog.sh
git commit -m "mail: add changelog logger"
git push
```
Success: Script committed.  
Prompt: `y` / `n`.

---

## Step 6 — Compose helper (optional)
**Goal:** Fill templates with tokens for quick copy.

Create `ops/mail/bin/compose.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
template="${1:?template path}"
out="${2:-/tmp/mail_out.md}"
date_str="$(date +%F)"
team="${TEAM:-All Offices}"
sed -e "s/{{DATE}}/${date_str}/g" -e "s/{{TEAM}}/${team}/g" "$template" > "$out"
echo "Wrote $out"
```
Commit:
```bash
chmod +x ops/mail/bin/compose.sh
git add ops/mail/bin/compose.sh
git commit -m "mail: add compose helper"
git push
```
Success: Script committed.  
Prompt: `y` / `n`.

---

## Step 7 — Gmail labels and filters
**Goal:** Route ops mail to labels.

Create labels:
```
DIPLOMAGIC/Mail
DIPLOMAGIC/INTAKE
DIPLOMAGIC/Alerts
```

Filters (Gmail Settings → Filters → Create):
```
Matches: subject has [INTAKE]          → Apply label DIPLOMAGIC/INTAKE, Skip Inbox
Matches: subject has Stand-by          → Apply label DIPLOMAGIC/Mail
Matches: subject has [ALERT] or [HOTFIX] → Apply label DIPLOMAGIC/Alerts, Star
```
Success: Filters saved; test by sending yourself a sample.  
Prompt: `y` / `n`.

---

## Step 8 — Ops protocol tokens
**Goal:** Standardize confirmations.

Tokens
```
y          → proceed / confirm
HOTFIX     → critical fix approval (requires prior y)
ACK Stand-by → acknowledge quiet period
ROLLOVER   → office rename/archive packet
```
Document these in `ops/mail/README.md`. Commit:
```bash
printf "# Mail Ops\n\nTokens: y, HOTFIX, ACK Stand-by, ROLLOVER\n" > ops/mail/README.md
git add ops/mail/README.md
git commit -m "mail: add ops tokens"
git push
```
Success: README committed.  
Prompt: `y` / `n`.

---

## Step 9 — End-to-end test
**Goal:** Validate logs and templates.

Run:
```bash
bash ops/mail/bin/decision.sh Postmaster "Stand-by Quiet Period" "ACK" "A&R"
bash ops/mail/bin/changelog.sh mail/global "Stand-by" "A&R acknowledged" "A&R"
TEAM="Publishing Studio" bash ops/mail/bin/compose.sh ops/mail/templates/ack_request.md ./ops/mail/out_ack.md
```
Check:
```
• DECISIONS.md has an appended decision-entry line.
• CHANGELOG.md has an appended changelog-entry line.
• ops/mail/out_ack.md contains the templated message.
```
Success: All three artifacts present and correct.  
Prompt: `y` / `n`.

---

## Step 10 — Optional integrations
**Goal:** Connect Mail to trackers and chat.

Options
```
• Notion/Trello: paste DECISIONS.md line into the card comment.
• Discord (#9 wizard): POST new decision-entry to a webhook.
• Google Workspace (#4 wizard): route [INTAKE] emails by label.
```
Success: At least one integration tested.  
Prompt: `y` to finish, `n` for targeted troubleshooting.

---

## Troubleshooting quick refs
```
• Protected branch blocks log commit → allow commits to main or use a docs branch with PRs.
• Windows shells lack bash → install Git Bash and run scripts via Rider terminal.
• Gmail filter not matching → remove quotes/brackets or match on “subject includes”.
• Sed placeholders not replaced → ensure {{DATE}} and {{TEAM}} in templates.
```
