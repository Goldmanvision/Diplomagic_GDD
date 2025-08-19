#!/usr/bin/env bash
set -euo pipefail
# ci_add_validation_filter.sh
# Run from repo root. Creates branch, adds post-filter script, inserts workflow snippet,
# commits, pushes, and creates a PR.

BRANCH="ci/add-validation-filter"
WORKFLOW=".github/workflows/epilogue-validate.yml"
SCRIPT=".github/scripts/validation_postfilter.py"
BACKUP_SUFFIX=".bak-$(date +%s)"
PR_TITLE="ci: add validation post-filter and upload cleaned report"
PR_BODY="Add a validation post-processing filter to remove negated false-positive hits and upload the cleaned report as an artifact. This helps QA and reduces noise."

if [ ! -f "${WORKFLOW}" ]; then
  echo "ERROR: workflow not found: ${WORKFLOW}"
  exit 1
fi

echo "Backing up ${WORKFLOW} -> ${WORKFLOW}${BACKUP_SUFFIX}"
cp -v "${WORKFLOW}" "${WORKFLOW}${BACKUP_SUFFIX}"

# write the postfilter script
mkdir -p "$(dirname "${SCRIPT}")"
cat > "${SCRIPT}" <<'PY'
#!/usr/bin/env python3
\"\"\"validation_postfilter.py

Usage:
  python3 .github/scripts/validation_postfilter.py <input_report> <output_report> [--window N]

Reads input_report line by line. Writes only lines that contain a configured keyword
and are not negated within a window of N tokens before the keyword (default N=5).
\"\"\"
import sys
import re
from pathlib import Path

NEG_TOKENS = re.compile(r\"\\b(no|none|without|don't|do not|remove|removed|absent|not|never|exclude|excluded)\\b\", re.I)
KEYWORDS = re.compile(r\"\\b(Evidence|BlueOnBlue|CH6|Blue-on-Blue|CCTV|K-9|K9|K-9|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|raid)\\b\", re.I)

def neg_within_n_tokens(line, keyword_span_start, n=5):
    prefix = line[:keyword_span_start]
    tokens = re.findall(r\"\\w+|[-']\", prefix)
    window = ' '.join(tokens[-n:]) if tokens else ''
    return bool(NEG_TOKENS.search(window))

def process(inpath, outpath, window=5):
    inpath = Path(inpath)
    outpath = Path(outpath)
    if not inpath.exists():
        print(f\"Input report not found: {inpath}\", file=sys.stderr)
        return 2
    outpath.parent.mkdir(parents=True, exist_ok=True)
    kept = 0
    total = 0
    with inpath.open('r', encoding='utf-8', errors='ignore') as inf, outpath.open('w', encoding='utf-8') as outf:
        for line in inf:
            total += 1
            m = KEYWORDS.search(line)
            if not m:
                continue
            if neg_within_n_tokens(line, m.start(), n=window):
                continue
            outf.write(line)
            kept += 1
    print(f\"Processed {total} lines. Kept {kept} matching lines (window={window}).\")
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(\"Usage: validation_postfilter.py <input> <output> [--window N]\", file=sys.stderr)
        sys.exit(2)
    inrep = sys.argv[1]
    outre = sys.argv[2]
    window = 5
    if len(sys.argv) >= 4:
        try:
            window = int(sys.argv[3])
        except:
            pass
    rc = process(inrep, outre, window=window)
    sys.exit(rc)

PY
chmod +x "${SCRIPT}"
git add "${SCRIPT}"

# Prepare YAML snippet to append if not already present
SNIPPET=$(cat <<'YAML'
# --- inserted by ci/add-validation-filter (post-process + upload) ---
- name: Post-process validation report
  if: always()
  run: |
    python3 .github/scripts/validation_postfilter.py reports/validation-rerun.log reports/validation-clean.log 5 || true

- name: Upload cleaned validation report
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: validation-report-clean
    path: |
      reports/validation-clean.log
      reports/*.txt
      artifacts/**
# --- end insert ---
YAML
)

# Check for existing insertion marker
if grep -q "validation_postfilter.py" "${WORKFLOW}" || grep -q "validation-report-clean" "${WORKFLOW}"; then
  echo "Workflow already references validation_postfilter or upload step. Skipping append."
else
  echo "Appending post-process snippet to ${WORKFLOW}"
  printf "\n\n%s\n" "${SNIPPET}" >> "${WORKFLOW}"
  git add "${WORKFLOW}"
fi

# show diff for review
git --no-pager diff -- ${WORKFLOW} || true

read -p "Proceed to create branch '${BRANCH}', commit and push? [y/N] " RESP
RESP=${RESP:-N}
if [ "${RESP}" != "y" ] && [ "${RESP}" != "Y" ]; then
  echo "Aborted by user. Workflow and script updated locally. Review changes and commit manually when ready."
  exit 0
fi

git fetch origin
git checkout -b "${BRANCH}"
git commit -m "ci: add validation post-filter and upload cleaned report (validation-clean.log)"
git push -u origin "${BRANCH}"

# open PR
gh pr create --base main --head "${BRANCH}" --title "${PR_TITLE}" --body "${PR_BODY}" --label "ci" || true
echo "Branch pushed and PR created (or attempted)."
