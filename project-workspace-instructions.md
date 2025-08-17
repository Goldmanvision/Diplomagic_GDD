# Project Workspace Instructions

**Last updated:** August 16, 2025 (America/New_York)  
**Source of truth for directory paths:**  
<https://github.com/Goldmanvision/Diplomagic_GDD/blob/main/.github/workflows/repoDirs.md>

> Always consult the repoDirs list for authoritative locations. If paths differ anywhere else, **repoDirs.md wins**.

---

## 1) Branch & PR flow (CI-ready)

1. Create or update your working branch off `main`.
2. Commit changes; keep messages scoped and conventional (e.g., `ci:`, `docs:`, `feat:`).
3. Push and open a PR against `main`.
4. CI runs on PR open/sync; artifacts are attached to the run.

**Tip:** If a workflow run **cannot be retried**, push a trivial commit (e.g., update README) or use `workflow_dispatch` (see §6).

---

## 2) Validation (CH5–CH7 quick rules)

- **1994 period tech guardrails:** target **zero** hits for `smartphone`, `Wi‑Fi`, `Bluetooth`, `GPS`, `SMS`.
- **CH6 (Raid)**  
  - **Blue‑on‑Blue:** any friendly/civilian hits = **hard FAIL**.  
  - **Evidence cap:** 3 total (HUD shows `Evidence 0/3 + BlueOnBlue`).  
  - Lethal force allowed against hostiles per CH6 design; keep friendly fire at **0**.
- **CH7 (City)**  
  - **Evidence cap:** 2.  
  - **Non‑lethal compliance:** no friendly/civilian hits.
- Keep prompts/strings ≤ 14 chars where specified by design trackers.
- Use the tracker docs in `Trackers/` for gating details; repoDirs.md points to the exact files.

---

## 3) Re‑running the CH6 validator locally (example)

```bash
# From repo root; write full output
mkdir -p reports artifacts
./scripts/ch6_validation_rerun.sh > reports/validation-main.log 2>&1 || true

# Post-filter (window=5 by default)
python3 .github/scripts/validation_postfilter.py reports/validation-main.log reports/validation-clean.log 5

# Inspect
nl -ba reports/validation-clean.log | sed -n '1,200p'
```

**Post‑filter behavior:** keeps lines with keywords while dropping lines negated within N tokens (default **5**).  
Update `NEG_TOKENS` or the window only if false positives persist; commit changes and re‑run CI (see §6).

---

## 4) CI artifact you should see

- **Name:** `validation-report-clean`  
- **Contents:** `reports/validation-clean.log` (+ any `reports/*.txt`, `artifacts/**` configured in the workflow).

If missing, confirm the workflow’s post‑process and upload steps are present and paths match the log you generate (see §5).

---

## 5) Where the workflow logic lives

- CI workflow: `.github/workflows/epilogue-validate.yml`
- Post‑filter: `.github/scripts/validation_postfilter.py`

Cross‑check paths against **repoDirs.md** (source of truth).

---

## 6) GitHub CLI: list runs, rerun, and download artifacts

```bash
# Latest runs for the branch
gh run list --repo Goldmanvision/Diplomagic_GDD --branch ci/add-validation-filter   --limit 5 --json databaseId,conclusion,createdAt,headBranch   --jq '.[] | "\(.databaseId)\t\(.conclusion)\t\(.headBranch)\t\(.createdAt)"'

# If a run cannot be retried, make a tiny commit to trigger CI:
git checkout ci/add-validation-filter
echo "# trigger CI run" >> README.md
git add README.md
git commit -m "ci: trigger run to test validation filter"
git push origin ci/add-validation-filter

# After the new run starts, capture its ID
RUN_ID=$(gh run list --repo Goldmanvision/Diplomagic_GDD --branch ci/add-validation-filter   --limit 1 --json databaseId --jq '.[0].databaseId')

# Download artifacts (after run completes)
gh run download "$RUN_ID" --repo Goldmanvision/Diplomagic_GDD --dir ./ci-artifacts || echo "no artifacts"
ls -la ./ci-artifacts || echo "no artifacts"
```

**Note:** If the UI/CLI says “This workflow run cannot be retried,” prefer the small “trigger commit” above.

---

## 7) Troubleshooting quick hits

- **No `validation-clean.log` in artifacts:** Verify the post‑filter step points to the same input your validator writes
  (e.g., `reports/validation-rerun.log` vs `reports/validation-main.log`) and that upload paths include the output file.
- **Zero filtering effect:** Confirm the keywords and negation tokens in `validation_postfilter.py`. Increase the window to `7–9` only if needed.
- **PR comment summary missing:** Ensure the summarizer job has required secrets, or disable it temporarily to unblock validation.

---

## 8) Ground rules when editing content

- Stay period‑accurate (1994). Avoid disallowed modern tech terms; if present in quotes, annotate and justify.
- Maintain **POV‑only** cutscene rule and diegetic media (VHS, TV, camcorder) where applicable.
- Respect CH6/CH7 gating and evidence caps; **no** friendly/civilian harm in city content.

---

## 9) Single source of truth reminder

- For every path, directory, or file location, **consult repoDirs.md first**:  
  <https://github.com/Goldmanvision/Diplomagic_GDD/blob/main/.github/workflows/repoDirs.md>
- If another doc conflicts, update that doc to match repoDirs.md or fix repoDirs.md—do not diverge silently.
