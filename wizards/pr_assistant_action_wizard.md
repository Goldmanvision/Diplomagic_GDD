# pr_assistant_action_wizard
**Macro name:** `pr_assistant_action_wizard`  
**Trigger:** `wiz pr-assist`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** GitHub Action that posts a PR summary and risk notes as a comment. No external AI.  
**Risks:** Overposting on every push, noisy comments, shallow fetch breaking diffs.

---

## Step 1 — Create workflow and script skeleton
**Goal:** Add a CI job that runs on pull requests and drafts a summary.

Create folders:
```bash
mkdir -p .github/workflows .github/scripts
```

Create `.github/workflows/pr_assistant.yml`:
```yaml
name: PR Assistant

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

permissions:
  contents: read
  pull-requests: write

jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate summary
        env:
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
        run: |
          bash .github/scripts/pr_assistant.sh "$BASE_SHA" "$HEAD_SHA" "$PR_NUMBER"

      - name: Upsert PR comment
        uses: actions/github-script@v7
        env:
          COMMENT_BODY_FILE: .github/scripts/_pr_assistant_out.md
        with:
          script: |
            const fs = require('fs');
            const body = fs.readFileSync(process.env.COMMENT_BODY_FILE, 'utf8');
            const {owner, repo, number} = context.issue;
            const marker = '<!-- PR_ASSISTANT_MARKER -->';
            const { data: comments } = await github.rest.issues.listComments({owner, repo, issue_number: number, per_page: 100});
            const existing = comments.find(c => c.body && c.body.includes(marker));
            if (existing) {
              await github.rest.issues.updateComment({owner, repo, comment_id: existing.id, body});
            } else {
              await github.rest.issues.createComment({owner, repo, issue_number: number, body});
            }
```

Create `.github/scripts/pr_assistant.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail
BASE_SHA="${1:-}"
HEAD_SHA="${2:-}"
PR_NUM="${3:-}"
OUT=".github/scripts/_pr_assistant_out.md"

if [[ -z "$BASE_SHA" || -z "$HEAD_SHA" ]]; then
  echo "Missing SHAs"; exit 1
fi

# Collect changes
CHANGED_FILES=$(git diff --name-status "$BASE_SHA" "$HEAD_SHA" | sed 's/\t/ /g')
STATS=$(git diff --shortstat "$BASE_SHA" "$HEAD_SHA" || true)
LINES_ADDED=$(git diff --numstat "$BASE_SHA" "$HEAD_SHA" | awk '{a+=$1} END{print a+0}')
LINES_REMOVED=$(git diff --numstat "$BASE_SHA" "$HEAD_SHA" | awk '{a+=$2} END{print a+0}')

# Basic risk heuristics
RISK=()
echo "$CHANGED_FILES" | grep -Ei '^A|^M' | grep -E '\.ya?ml$|\.yml$' | grep -E '\.github/workflows' >/dev/null && RISK+=("Workflow change")
echo "$CHANGED_FILES" | grep -E '\.ps1$|\.sh$|\.bat$|\.cmd$' >/dev/null && RISK+=("Script change")
echo "$CHANGED_FILES" | grep -E '^D' >/div/null && RISK+=("Deletes present") || true
echo "$CHANGED_FILES" | grep -E '^A|^M' | grep -E 'ops/|ops/site/|mkdocs\.yml|mkdocs.yml' >/dev/null && RISK+=("Docs/ops pipeline touched")
echo "$CHANGED_FILES" | grep -E '^A|^M' | grep -E 'departments/' >/dev/null && RISK+=("Department dashboards updated")
git diff "$BASE_SHA" "$HEAD_SHA" -- .github/workflows 2>/dev/null | grep -E 'pull_request_target|secrets|\${{\s*secrets' >/dev/null && RISK+=("Workflow secrets/pull_request_target usage")

# Summaries
TOTAL_FILES=$(git diff --name-only "$BASE_SHA" "$HEAD_SHA" | wc -l | awk '{print $1}')
BIG_DIFF=$((LINES_ADDED + LINES_REMOVED))
[[ $BIG_DIFF -gt 800 ]] && RISK+=("Large diff: ${BIG_DIFF} lines changed")

# Build markdown
{
  echo "<!-- PR_ASSISTANT_MARKER -->"
  echo "# PR Assistant Summary"
  echo ""
  echo "**PR #${PR_NUM}**"
  echo ""
  echo "## Overview"
  echo "- Base: \`$BASE_SHA\`"
  echo "- Head: \`$HEAD_SHA\`"
  echo "- Files changed: **$TOTAL_FILES**"
  echo "- Lines + / - : **$LINES_ADDED** / **$LINES_REMOVED**"
  echo ""
  echo "## Changed files"
  echo '```text'
  echo "$CHANGED_FILES" | head -n 200
  [[ $(echo "$CHANGED_FILES" | wc -l) -gt 200 ]] && echo "... (truncated)"
  echo '```'
  echo ""
  echo "## Risk notes"
  if [[ ${#RISK[@]} -gt 0 ]]; then
    for r in "${RISK[@]}"; do echo "- $r"; done
  else
    echo "- None detected by heuristics"
  fi
  echo ""
  echo "## Merge gate checklist"
  echo "- [ ] Tests or manual validation performed"
  echo "- [ ] Secrets unchanged or reviewed"
  echo "- [ ] Deployment impact assessed"
  echo "- [ ] Rollback plan noted"
} > "$OUT"

echo "Wrote $OUT"
```

Add and commit:
```bash
git add .github/workflows/pr_assistant.yml .github/scripts/pr_assistant.sh
git commit -m "ci: add PR assistant action (summary + risk notes)"
git push
```
Success: Files committed.  
Prompt: `y` / `n`.

---

## Step 2 — Make the script executable and style-safe
**Goal:** Ensure POSIX line endings and exec bit for the runner.

```bash
git update-index --add --chmod=+x .github/scripts/pr_assistant.sh
git commit -m "ci: make pr_assistant.sh executable" || true
git push || true
```
Success: No permission errors on workflow run.  
Prompt: `y` / `n`.

---

## Step 3 — Open a test PR
**Goal:** Trigger the workflow and see the comment.

```bash
# create a small change
echo "# touch" >> README.md
git add README.md
git commit -m "docs: touch readme to trigger PR assistant"
git push -u origin HEAD:test/pr-assistant

# open PR from branch test/pr-assistant into main (via GitHub UI)
```
Success: A bot comment appears on the PR with the summary and risk notes.  
Prompt: `y` / `n`.

---

## Step 4 — Reduce comment noise (optional)
**Goal:** Only comment when not a draft and skip trivial changes.

Edit `.github/workflows/pr_assistant.yml`:
```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
    paths-ignore:
      - '**/*.md'
      - 'docs/**'
      - 'departments/**'
      - '**/*.png'
      - '**/*.jpg'
```

Add a guard to the job:
```yaml
jobs:
  summarize:
    if: ${{ !github.event.pull_request.draft }}
    runs-on: ubuntu-latest
    steps:
      # ...unchanged...
```
Commit and push.  
Success: Workflow skips drafts and doc-only PRs.  
Prompt: `y` / `n`.

---

## Step 5 — Customize heuristics (optional)
**Goal:** Tailor risk rules to Diplomagic.

Examples to add inside `pr_assistant.sh`:
```bash
echo "$CHANGED_FILES" | grep -E '^A|^M' | grep -E 'Engine/Unreal|Engine/Unity' >/dev/null && RISK+=("Game engine build paths touched")
echo "$CHANGED_FILES" | grep -E '^A|^M' | grep -E 'ops/mail|DECISIONS.md|CHANGELOG.md' >/dev/null && RISK+=("Ops mail/logging changed")
```
Commit and push.  
Success: Risk notes reflect your codebase.  
Prompt: `y` to finish, `n` for help on any sub‑step.

---

## Troubleshooting quick refs
```text
• No comment posted → check job permissions: pull-requests: write; confirm event is pull_request not push.
• Empty diff → ensure actions/checkout uses fetch-depth: 0; SHAs passed correctly.
• Multiple comments → the upsert marker is missing; do not remove the marker line.
• Windows line endings break script → ensure LF for .sh; set core.autocrlf=input for repo or add .gitattributes.
```
