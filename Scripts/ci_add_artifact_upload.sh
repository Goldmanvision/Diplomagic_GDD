#!/usr/bin/env bash
set -euo pipefail

# ci_add_artifact_upload.sh
# Usage: run from repo root. It creates a branch, inserts an upload step into
# .github/workflows/epilogue-validate.yml after the validation step that runs
# ./scripts/validation-rerun.sh, commits, pushes, and opens a PR.
# Review the modified file before merging.

BRANCH="ci/add-artifact-upload"
WORKFLOW=".github/workflows/epilogue-validate.yml"
BACKUP_SUFFIX=".bak-$(date +%s)"
PR_TITLE="ci: upload validation artifacts for epilogue-validate"
PR_BODY="Add actions/upload-artifact step so validation reports and artifacts are available for PR and run debugging.\n\nRequired to support QA verification and downstream packaging."
LABEL="ci"

if [ ! -f "${WORKFLOW}" ]; then
  echo "ERROR: workflow file not found: ${WORKFLOW}"
  exit 1
fi

echo "Backing up ${WORKFLOW} -> ${WORKFLOW}${BACKUP_SUFFIX}"
cp -v "${WORKFLOW}" "${WORKFLOW}${BACKUP_SUFFIX}"

PYTHON_SNIPPET=$(cat <<'PY'
SNIPPET = """- name: Save validation report
  if: always()
  run: |
    mkdir -p reports artifacts || true
    cp -v "${{ github.workspace }}/reports/validation-rerun.log" ./reports/validation-rerun.log 2>/dev/null || true
    cp -rv "${{ github.workspace }}/artifacts" ./artifacts 2>/dev/null || true

- name: Upload validation report
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: validation-report
    path: |
      reports/validation-rerun.log
      reports/*.txt
      artifacts/**
"""
import sys, re
p = sys.argv[1]
with open(p, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find first occurrence of validation script in file
match_idx = None
for i,l in enumerate(lines):
    if 'validation-rerun.sh' in l or 'ci-smoke.sh' in l:
        match_idx = i
        break

if match_idx is None:
    # append snippet at end with two newlines
    out = ''.join(lines).rstrip() + "\n\n" + SNIPPET + "\n"
    with open(p, 'w', encoding='utf-8') as f:
        f.write(out)
    print("Inserted snippet at end of file (no validation step found).")
    sys.exit(0)

# look backward for the step '- name:' that contains this run
step_name_idx = None
for j in range(match_idx, -1, -1):
    if re.match(r'^\s*-\s*name\s*:', lines[j]):
        step_name_idx = j
        break

if step_name_idx is None:
    # fallback: append at end
    out = ''.join(lines).rstrip() + "\n\n" + SNIPPET + "\n"
    with open(p, 'w', encoding='utf-8') as f:
        f.write(out)
    print("Inserted snippet at end of file (no preceding '- name:' found).")
    sys.exit(0)

# compute indent from the '- name:' line
m = re.match(r'^(\s*)-\s*name\s*:', lines[step_name_idx])
indent = m.group(1) if m else ''

# find next step start at same indent after match_idx
insert_idx = None
for k in range(match_idx+1, len(lines)):
    if re.match(r'^\s*-\s*name\s*:', lines[k]):
        # if this '- name' has same or less indent than the original step, insert before it
        mk = re.match(r'^(\s*)-\s*name\s*:', lines[k])
        if mk:
            indent_k = mk.group(1)
            if len(indent_k) <= len(indent):
                insert_idx = k
                break

if insert_idx is None:
    insert_idx = len(lines)

# build indented snippet
indented = ''
for sline in SNIPPET.splitlines():
    indented += indent + sline + '\\n'

# insert
new_lines = lines[:insert_idx] + [indented] + lines[insert_idx:]
with open(p, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print(f"Inserted snippet after validation step at line {match_idx+1}.")
PY
PYTHON_SNIPPET

# run python insertion
python - <<'PY' || { echo "Python insertion failed"; exit 1; }
$PYTHON_SNIPPET
PY

# show diff
echo "Showing git diff for ${WORKFLOW}:"
git --no-pager diff -- ${WORKFLOW} || true

read -p "Proceed to create branch '${BRANCH}', commit and push? [y/N] " RESP
RESP=${RESP:-N}
if [ "${RESP}" != "y" ] && [ "${RESP}" != "Y" ]; then
  echo "Aborted by user. Workflow file updated locally. Review ${WORKFLOW} and commit manually when ready."
  exit 0
fi

# create branch and commit
git fetch origin
git checkout -b "${BRANCH}"
git add "${WORKFLOW}"
git commit -m "ci: upload validation report and artifacts for epilogue-validate workflow"

# push
git push -u origin "${BRANCH}"

# create PR using gh
gh pr create --base main --head "${BRANCH}" --title "${PR_TITLE}" --body "${PR_BODY}" --label "${LABEL}" || true

echo "Branch pushed and PR created (or PR creation attempted)."
echo "Review PR and run a rerun of the workflow to confirm artifacts are uploaded."
