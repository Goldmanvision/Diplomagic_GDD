# Job Card TS-MAC-DAPS-0002 — DAPS CI install & configure

**Owner:** diplomagic-codex-agent  
**Labels:** ops, daps, ci  
**Goal:** Install DAPS CLI, wire `daps-ci.yml` and `ops-runner-dispatch.yml`, verify dispatch on `main`.

## Tasks
- Install DAPS locally (py project) and set env/PATs as needed.
- Ensure `.github/workflows/daps-ci.yml` runs on `pull_request` and `workflow_dispatch`.
- Verify `ops-runner-dispatch.yml` can `workflow_dispatch` → `daps-ci.yml`.
- Prove with a green run on `main` and a PR.

## Acceptance
- Green `daps-ci / smoke-routes` on a PR.
- Manual dispatch from Actions tab succeeds.
