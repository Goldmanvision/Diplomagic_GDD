# changelog_distiller_wizard
**Macro name:** `changelog_distiller_wizard`  
**Trigger:** `wiz changelog`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Generate CHANGELOG.md sections from merged PR titles between tags. Opens a PR.  
**Risks:** Missing tags, squash merges without PR number, branch protection blocking auto-commit.

---

## Step 1 — Baseline file
**Goal:** Ensure a CHANGELOG exists.

Commands
```bash
[ -f CHANGELOG.md ] || cat > CHANGELOG.md <<'MD'
# Changelog
All notable changes to this project will be documented here.
Follows a simplified Keep a Changelog + SemVer style.

## [Unreleased]
- Placeholder
MD
git add CHANGELOG.md
git commit -m "docs: add CHANGELOG.md baseline" || true
git push || true
```
Success: CHANGELOG.md present.  
Prompt: `y` / `n`.

---

## Step 2 — Workflow: distill PRs between tags
**Goal:** Add a manual workflow to build a changelog section and open a PR.

Create `.github/workflows/changelog_distiller.yml`:
```yaml
name: Changelog Distiller

on:
  workflow_dispatch:
    inputs:
      from_tag:
        description: "Base tag (e.g., v0.1.0)"
        required: true
      to_tag:
        description: "Head tag or branch (e.g., v0.2.0 or main)"
        required: true
        default: main
      version:
        description: "Release version for section header (e.g., 0.2.0)"
        required: true
      dry_run:
        description: "Do not open PR, just attach artifact"
        type: boolean
        default: false

permissions:
  contents: write
  pull-requests: write

jobs:
  distill:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: {fetch-depth: 0}

      - name: Generate changelog section
        id: gen
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const core = require('@actions/core');
            const owner = context.repo.owner;
            const repo = context.repo.repo;
            const from = core.getInput('from_tag');
            const to = core.getInput('to_tag');
            const version = core.getInput('version');
            const compare = await github.rest.repos.compareCommits({owner, repo, base: from, head: to});
            const commits = compare.data.commits || [];
            const prNums = new Set();

            // Find PR numbers in commit messages like "... (#123)"
            for (const c of commits) {
              const m = c.commit && c.commit.message || "";
              const matches = m.match(/\(#(\d+)\)/g) || [];
              for (const hit of matches) {
                const n = hit.match(/\d+/)[0];
                prNums.add(parseInt(n, 10));
              }
            }

            // Also scan merge commits titles
            for (const c of commits) {
              const m = c.commit && c.commit.message || "";
              if (m.startsWith('Merge pull request #')) {
                const n = parseInt(m.split('#')[1], 10);
                if (!Number.isNaN(n)) prNums.add(n);
              }
            }

            // Fetch PR details
            const prs = [];
            for (const n of prNums) {
              try {
                const { data } = await github.rest.pulls.get({owner, repo, pull_number: n});
                if (data.merged) prs.push(data);
              } catch (e) {
                // ignore missing
              }
            }

            // Categorize
            const buckets = {
              Added: [], Changed: [], Fixed: [], Docs: [], Internal: []
            };
            const pick = (pr) => {
              const title = pr.title;
              const labels = (pr.labels || []).map(l => (typeof l === 'string') ? l : l.name);
              const lower = title.toLowerCase();
              if (labels.includes('feat') || lower.startsWith('feat')) return 'Added';
              if (labels.includes('fix') || lower.startsWith('fix')) return 'Fixed';
              if (labels.includes('docs') || lower.startsWith('docs')) return 'Docs';
              if (labels.includes('refactor') || lower.startsWith('refactor') || labels.includes('chore') || lower.startsWith('chore')) return 'Internal';
              return 'Changed';
            };

            for (const pr of prs) {
              const line = `- ${pr.title} (#${pr.number})`;
              buckets[pick(pr)].push(line);
            }

            const date = new Date().toISOString().slice(0,10);
            let section = `## [${version}] - ${date}\n`;
            const order = ['Added','Changed','Fixed','Docs','Internal'];
            for (const k of order) {
              if (buckets[k].length) {
                section += `\n### ${k}\n` + buckets[k].sort().join('\n') + '\n';
              }
            }
            if (prs.length === 0) section += '\n- No PRs detected between the selected range.\n';

            fs.writeFileSync('.github/_CHANGELOG_SECTION.md', section, 'utf8');
            core.setOutput('empty', String(prs.length === 0));

      - name: Dry run artifact
        if: ${{ inputs.dry_run }}
        uses: actions/upload-artifact@v4
        with:
          name: changelog-section
          path: .github/_CHANGELOG_SECTION.md

      - name: Update CHANGELOG.md
        if: ${{ !inputs.dry_run }}
        run: |
          set -e
          if [ ! -f CHANGELOG.md ]; then echo "# Changelog\n\n" > CHANGELOG.md; fi
          cat .github/_CHANGELOG_SECTION.md CHANGELOG.md > CHANGELOG.new && mv CHANGELOG.new CHANGELOG.md
          echo "CHANGELOG updated"

      - name: Create PR
        if: ${{ !inputs.dry_run }}
        uses: peter-evans/create-pull-request@v6
        with:
          commit-message: "docs: update CHANGELOG for v${{ inputs.version }}"
          title: "docs: update CHANGELOG for v${{ inputs.version }}"
          body: "Automated changelog distillation between `${{ inputs.from_tag }}` and `${{ inputs.to_tag }}`."
          branch: "chore/changelog-v${{ inputs.version }}"
          labels: docs
```
Commit and push.  
Success: Workflow listed under Actions.  
Prompt: `y` / `n`.

---

## Step 3 — Run a dry run
**Goal:** Validate the range and output before opening a PR.

Actions
```text
• Open GitHub → Actions → Changelog Distiller → Run workflow
• Inputs:
  from_tag: last release tag (e.g., v0.1.0)
  to_tag:   main
  version:  0.2.0
  dry_run:  true
```
Success: Workflow green. An artifact `changelog-section` is attached. Download to review.  
Prompt: `y` / `n`.

---

## Step 4 — Open a PR
**Goal:** Write to CHANGELOG.md via a PR.

Actions
```text
• Re-run the workflow with the same inputs but dry_run=false
• Review the PR → merge when approved
```
Success: PR merged; CHANGELOG updated on main.  
Prompt: `y` / `n`.

---

## Step 5 — Tag the release (optional)
**Goal:** Mark the release in Git.

Commands
```bash
git fetch --tags
git tag -a v0.2.0 -m "Release 0.2.0"
git push origin v0.2.0
```
Success: Tag visible on GitHub.  
Prompt: `y` / `n`.

---

## Step 6 — Tune categories (optional)
**Goal:** Map labels to buckets for your repo.

Edit the `buckets` and `pick()` logic inside the workflow to reflect your labels:
```text
feat → Added
fix  → Fixed
docs → Docs
perf/refactor/chore → Internal
fallback → Changed
```
Success: Next run reflects the new mapping.  
Prompt: `y` to finish, `n` for help.

---

## Troubleshooting quick refs
```text
• "CompareCommits: 404" → wrong tag names or missing fetch-depth: 0.
• Empty section → squash merge without (#123) pattern; ensure PR numbers appear in commit messages.
• PR cannot be created → branch protection requires reviews; approve and merge manually.
• Categories off → add/align PR labels; script prioritizes labels over title prefixes.
```
