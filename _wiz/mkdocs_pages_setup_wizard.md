# mkdocs_pages_setup_wizard
**Macro name:** `mkdocs_pages_setup_wizard`  
**Trigger:** `wiz git-rider`  
**Mode:** One-step-at-a-time. After each step, user replies `y` (done, next) or `n` (repeat with fixes). Do not advance without `y`.

## Operator Notes
- Work on `main` in both repos. Never edit `gh-pages`. Deploy writes to `gh-pages` (project) or `main` (hub).
- Before any force push, display `git remote -v` and branch to confirm the correct repo.
- If a command fails, show the minimal fix and re-offer the same step.
- Use Windows-safe commands and Bash syntax. Do not close the shell on error.
- Risks: `ghp-import -f` rewrites history on the deploy branch. DNS/HTTPS may lag. `mkdocs --strict` fails on warnings.

---

## Step 1 — GitHub Pages and Custom Domains
**Goal:** Set Pages source and custom domains.  
**Repos:**
- Project: `Diplomagic_GDD` → **source:** `gh-pages` (root) → **domain:** `diplomagic.goldmanvision.com` → Enforce HTTPS.
- Hub: `goldmanvision.github.io` → **source:** `main` (root) → **domain:** `docs.goldmanvision.com` → Enforce HTTPS.

**DNS (create at your DNS provider):**
```
diplomagic   CNAME   goldmanvision.github.io
docs         CNAME   goldmanvision.github.io
```

**Success criteria:** Pages saved, domains set, HTTPS toggle enabled or pending.

**Prompt:** Confirm Pages settings and DNS records are set as above. Reply `y` to continue or `n` to repeat with help.

---

## Step 2 — Rider Git + Bash configuration
**Goal:** Rider uses Git and Bash correctly.

1) Rider › Settings › Tools › Terminal → Shell path points to Git Bash (e.g. `C:\Program Files\Git\bin\bash.exe --login -i`).  
2) Rider › Settings › Version Control › Git → Path to Git executable → **Test**.

**Quick check:**
```bash
git --version && echo $SHELL
```

**Success criteria:** Git version prints, shell is Bash.

**Prompt:** If the check passes, `y`. Else `n` to adjust.

---

## Step 3 — Repo structure and branches
**Goal:** You are on `main`, files exist, deploy branch present (or will be created).

Project repo:
```bash
cd /f/repos/Diplomagic_GDD
git remote -v
git branch --show-current || git branch
git fetch origin
git ls-tree --name-only origin/gh-pages | head || true
ls -la mkdocs.yml docs .gitattributes .gitignore 2>/dev/null || true
```

Hub repo:
```bash
cd /f/repos/goldmanvision.github.io
git remote -v
git branch --show-current || git branch
git fetch origin
git ls-tree --name-only origin/main | head || true
ls -la mkdocs.yml docs .gitattributes .gitignore 2>/dev/null || true
```

**Success criteria:** On `main` in each repo. `mkdocs.yml` and `docs/` exist (or you’ll bootstrap in Step 4/5).

**Prompt:** `y` if both repos look correct. `n` to fix paths/branches/files.

---

## Step 4 — Build & publish PROJECT (Diplomagic_GDD → gh-pages)
**Goal:** Build MkDocs and deploy to `gh-pages` with CNAME `diplomagic.goldmanvision.com`.

From project root:
```bash
cd /f/repos/Diplomagic_GDD
git remote -v && git branch --show-current

# Optional bootstrap if missing
[ -f mkdocs.yml ] || {
  mkdir -p docs
  cat > mkdocs.yml <<'YML'
site_name: DIPLOMAGIC
site_url: https://diplomagic.goldmanvision.com
nav:
  - Home: index.md
YML
  echo "# DIPLOMAGIC\n\nDay-1 placeholder." > docs/index.md
}

# Build
python -m pip install -q mkdocs ghp-import
mkdocs build --strict

# Deploy
ghp-import -n -p -f site
```

**Expected output:** mkdocs build completes; ghp-import pushes to `origin gh-pages`.

**Prompt:** If deploy succeeded, `y`. If errors (missing mkdocs.yml/docs), `n` to re-run with fixes.

---

## Step 5 — Build & publish HUB (goldmanvision.github.io → main)
**Goal:** Build MkDocs and deploy to `main` with CNAME `docs.goldmanvision.com`.

From hub root:
```bash
cd /f/repos/goldmanvision.github.io
git remote -v && git branch --show-current

# Optional bootstrap if missing
[ -f mkdocs.yml ] || {
  mkdir -p docs
  cat > mkdocs.yml <<'YML'
site_name: Goldmanvision Docs Hub
site_url: https://docs.goldmanvision.com
nav:
  - Home: index.md
YML
  echo "# Docs Hub\n\nDay-1 placeholder." > docs/index.md
}

# Build
python -m pip install -q mkdocs ghp-import
mkdocs build --strict

# Deploy to main (not gh-pages)
ghp-import -n -p -f -b main site
```

**Expected output:** mkdocs build completes; ghp-import pushes to `origin main`.

**Prompt:** If deploy succeeded, `y`. Else `n` to retry with guidance.

---

## Step 6 — Validate DNS, HTTPS, and site reachability
**Goal:** Both domains return 200 over HTTPS.

```bash
curl -I "https://diplomagic.goldmanvision.com/?t=$(date +%s)"
curl -I "https://docs.goldmanvision.com/?t=$(date +%s)"
```

**Success criteria:** `HTTP/2 200` (or `HTTP/1.1 200`).

**If failing:** Wait a few minutes. Re-check GitHub Pages settings and that CNAME files exist in the deployed branches. Verify DNS CNAMEs point to `goldmanvision.github.io`.

**Prompt:** When both return 200, reply `y` to complete. `n` for targeted troubleshooting.

---

## Optional hardening
- Protect branches: `gh-pages` (project), `main` (hub).
- Add a GitHub Actions workflow to build and deploy on push.

Example `.github/workflows/mkdocs.yml` (adjust per repo):
```yaml
name: Build MkDocs
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - run: python -m pip install mkdocs ghp-import
      - run: mkdocs build --strict
      - name: Publish to gh-pages (project)
        if: github.repository == 'Goldmanvision/Diplomagic_GDD'
        run: ghp-import -n -p -f site
      - name: Publish to main (hub)
        if: github.repository == 'Goldmanvision/goldmanvision.github.io'
        run: ghp-import -n -p -f -b main site
```

**Prompt:** Apply hardening now? Reply `y` to proceed (I will walk you through), or `n` to finish.
