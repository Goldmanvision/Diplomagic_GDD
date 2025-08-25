# Branch Protection Bypass Policy

The `local-ui-pack` workflow normally builds UI artifacts for every pull request. In limited cases, this job may be bypassed while backend tests continue to run.

### When a bypass is allowed
- The pull request is labeled `ci-bypass-localui`.
- The change is documentation-only or has a preapproved hotfix label.

### Effect of bypass
- Backend tests still execute.
- The `local-ui-build` job is marked as skipped with an annotation.
- The workflow summary records the actor and labels involved.

Misuse of the bypass may result in reverted changes.
