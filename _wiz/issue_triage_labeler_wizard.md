# issue_triage_labeler_wizard
**Macro name:** `issue_triage_labeler_wizard`  
**Trigger:** `wiz triage`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Lightweight, rule-based labels for PRs and Issues. No external AI.  
**Risks:** Over-labeling, missing paths, repo without labels created.

---

## Step 1 — Create labels
**Goal:** Ensure target labels exist.

Option A — GitHub UI
```text
Repo → Issues → Labels → New label
Create: Narrative, QA & UX, A&R, Steam Ops, Builds, Mail, Docs
```

Option B — GitHub CLI (Windows PowerShell)
```powershell
gh label create "Narrative" -c "#1abc9c" -d "Narrative work"        2>$null
gh label create "QA & UX"   -c "#e67e22" -d "Quality and usability" 2>$null
gh label create "A&R"       -c "#9b59b6" -d "Authenticity & Research" 2>$null
gh label create "Steam Ops" -c "#3498db" -d "Steam store/depots"    2>$null
gh label create "Builds"    -c "#2ecc71" -d "Build system/artifacts" 2>$null
gh label create "Mail"      -c "#95a5a6" -d "Ops mail/handoff"      2>$null
gh label create "Docs"      -c "#34495e" -d "Documentation"         2>$null
```
Success: Labels listed in the repo.  
Prompt: `y` / `n`.

---

## Step 2 — PR path-based labeling
**Goal:** Label PRs by changed file paths.

Create `.github/labeler.yml`:
```yaml
Narrative:
  - changed-files:
      - any-glob-to-any-file: ['departments/narrative/**']
QA & UX:
  - changed-files:
      - any-glob-to-any-file: ['departments/qa_ux/**', 'qa/**']
A&R:
  - changed-files:
      - any-glob-to-any-file: ['departments/authenticity_research/**', 'research/**']
Steam Ops:
  - changed-files:
      - any-glob-to-any-file: ['departments/steam_ops/**', 'ops/steam/**']
Builds:
  - changed-files:
      - any-glob-to-any-file: ['build/**', 'Engine/**', 'ops/builds/**']
Mail:
  - changed-files:
      - any-glob-to-any-file: ['departments/mail/**', 'ops/mail/**', 'DECISIONS.md', 'CHANGELOG.md']
Docs:
  - changed-files:
      - any-glob-to-any-file: ['**/*.md', 'docs/**']
```

Create `.github/workflows/pr_labeler.yml`:
```yaml
name: PR Labeler
on:
  pull_request_target:
    types: [opened, synchronize, reopened, edited]
permissions:
  contents: read
  pull-requests: write
jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          sync-labels: true
```
Commit and push both files.  
Success: Workflow active.  
Prompt: `y` / `n`.

---

## Step 3 — Issue keyword-based labeling
**Goal:** Label Issues by title/body regex.

Create `.github/issue_labeler.yml`:
```yaml
# Uses github/issue-labeler
Narrative:
  - '(?i)\b(scene|dialog|story|narrative|script)\b'
QA & UX:
  - '(?i)\b(qa|regression|usability|ux|accessibility)\b'
A&R:
  - '(?i)\b(authenticity|citation|source|verify|research)\b'
Steam Ops:
  - '(?i)\b(steam|depot|branch|app id|store page)\b'
Builds:
  - '(?i)\b(build|ci|unity|unreal|packaging|artifact)\b'
Mail:
  - '(?i)\b(stand-?by|handoff|postmaster|decision)\b'
Docs:
  - '(?i)\b(readme|docs?|documentation|mkdocs)\b'
enable-versioned-regex: true
```

Create `.github/workflows/issue_labeler.yml`:
```yaml
name: Issue Labeler
on:
  issues:
    types: [opened, edited]
permissions:
  issues: write
  contents: read
jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: github/issue-labeler@v3
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          configuration-path: .github/issue_labeler.yml
          include-title: true
          include-body: true
          dry-run: false
```
Commit and push both files.  
Success: New issues get labels.  
Prompt: `y` / `n`.

---

## Step 4 — Noise control
**Goal:** Avoid over-labeling docs-only PRs or private forks.

Options
```yaml
# In pr_labeler.yml, limit triggers
on:
  pull_request_target:
    types: [opened, ready_for_review, reopened]

# Or restrict docs label:
Docs:
  - changed-files:
      - any-glob-to-any-file: ['docs/**', 'ops/site/docs/**']
```

Add path-negation rules if needed.  
Success: Only high-signal labels applied.  
Prompt: `y` / `n`.

---

## Step 5 — Test
**Goal:** Validate both workflows.

PR test
```bash
# create a branch and modify a file in departments/qa_ux/
git checkout -b test/triage-qa
echo "# QA tweak" >> departments/qa_ux/CHANGELOG.md
git add departments/qa_ux/CHANGELOG.md
git commit -m "docs(qa_ux): trigger labeler"
git push -u origin HEAD
# open PR in GitHub UI
```
Expected: PR gets **QA & UX** and **Docs**.

Issue test
```text
Open a new Issue titled "Regression: controller no longer detected (QA)"
Expected labels: QA & UX
```
Success: Labels applied automatically.  
Prompt: `y` / `n`.

---

## Step 6 — Maintenance
**Goal:** Keep rules accurate.

Checklist
```text
• Update .github/labeler.yml when paths change.
• Update regexes if team vocabulary shifts.
• Keep labels small in number and high-signal.
```
Success: Stable labels with low noise.  
Prompt: `y` to finish, `n` for help.

---

## Troubleshooting quick refs
```text
• PR labels missing → ensure event is pull_request_target and labeler.yml exists on default branch.
• Issue labels missing → repo private without Actions? Check permissions: issues: write.
• Wrong labels → tighten regexes or paths; test with dedicated branches/issues.
```
