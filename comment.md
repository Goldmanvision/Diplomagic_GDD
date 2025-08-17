CI: validation post-filter added — runner wrapper added, please rerun

Summary:
- I added `.github/scripts/validation_postfilter.py` and workflow snippet to produce `reports/validation-clean.log`.
- The runner previously failed because `./scripts/validation-rerun.sh` did not exist and no `reports/validation-rerun.log` was produced.

What I changed in this branch:
- Added `scripts/validation-rerun.sh` wrapper so workflows produce `reports/validation-rerun.log`.
- Added/updated `validation_postfilter.py` and workflow upload step.

Observed failure:
- Run 17014685471 shows `-bash: ./scripts/validation-rerun.sh: No such file or directory` and therefore no artifact uploaded.

Request:
1. Please re-run the epilogue-validate workflow for this PR (or rerun the latest run for branch `ci/add-validation-filter`).
2. Confirm that the artifact `validation-report-clean` is uploaded.
3. If the run still fails, attach the runner logs or notify me so I can adjust the wrapper or the upload path.

Attached logs (gist): $GIST_URL

Local commands I ran:

./scripts/ch6_validation_rerun.sh > reports/validation-main.log 2>&1 || true
python3 .github/scripts/validation_postfilter.py reports/validation-main.log reports/validation-clean.log 5 || true

Thanks.
