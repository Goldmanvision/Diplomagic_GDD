# GitHub Actions CI/CD Wizard — Diplomagic
**Macro name suggestion:** `github_actions_ci_wizard`  
**Mode:** One-step. Reply `y` = done/next, `n` = repeat/fix.  
**Repos:** Project `Diplomagic_GDD` (publishes to `gh-pages`), Hub `goldmanvision.github.io` (publishes to `main`).  
**Export policy:** `.md` only. ASCII-safe names.

---

## Step 1 — MkDocs deploy for `Diplomagic_GDD` → `gh-pages`
**Goal:** Build docs on push to `main` and publish to `gh-pages`.

Create `.github/workflows/mkdocs.yml`:
```yaml
name: Build and Deploy MkDocs

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs ghp-import
      - name: Build
        run: mkdocs build --strict
      - name: Deploy to gh-pages
        run: ghp-import -n -p -f site
```
**Success:** Workflow shows green on Actions tab; `gh-pages` updated.  
**Prompt:** `y` to continue, `n` to retry.

---

## Step 2 — MkDocs deploy for `goldmanvision.github.io` → `main`
**Goal:** Build docs on push to `main` and publish back to `main`.

Create `.github/workflows/mkdocs.yml`:
```yaml
name: Build and Deploy MkDocs (User Site)

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs ghp-import
      - name: Build
        run: mkdocs build --strict
      - name: Deploy to main
        run: ghp-import -n -p -f -b main site
```
**Success:** Workflow green; `main` updated with built site.  
**Prompt:** `y` to continue, `n` to retry.

---

## Step 3 — Placeholder game build pipeline (Windows runner)
**Goal:** Create CI scaffold in the game repo (replace echos later).

`.github/workflows/game_build.yml`:
```yaml
name: Game Build and Test (Placeholder)

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install deps (placeholder)
        run: echo Installing game dependencies
      - name: Build (placeholder)
        run: echo Building project
      - name: Tests (placeholder)
        run: echo Running tests
```
**Success:** Run completes on push.  
**Prompt:** `y` to continue, `n` to retry.

---

## Step 4 — Protect branches
**Goal:** Prevent history rewrites and accidental deletes.

GitHub UI → Settings → Branches → Add rules:
- Protect `gh-pages` (project) and `main` (both repos).
- Keep **Allow force pushes** off.
- Optional: require status checks or reviews.

**Success:** Rules visible under Branch protection.  
**Prompt:** `y` to continue, `n` to retry.

---

## Step 5 — Verify Actions runs
**Goal:** Confirm pipelines operate.

UI: Repo → **Actions** → select workflow → check latest run.  
CLI (optional):
```bash
gh run list --limit 10
# view a run's logs:
gh run view <run-id> --log
```
**Success:** Recent successful runs visible.  
**Prompt:** `y` to finish, `n` to revisit a previous step.

---

## Notes
- Custom domains: ensure `CNAME` exists in the deployed branch contents.  
- `mkdocs build --strict` will fail on warnings; remove `--strict` if blocking.  
- `ghp-import -f` force-pushes deploy branches; verify `git remote -v` before running.
