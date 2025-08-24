# Job Card TS-MAC-DAPS-0005 — JC-WIN-02: Chat-history persistence & repo sync

**Owner:** diplomagic-codex-agent
**Labels:** ops, windows, daps, history
**Branch:** ops/win-client-02-history-sync
**Goal:** Persist chat transcripts and synchronize with repository handoff files.
**Prerequisite:** JC-WIN-01 scaffold layout.

## Tasks
- Define JSON or Markdown transcript schema under `clients/windows/`.
- Implement import/export logic to read and write `handoff/` folder files.
- Establish merge policy for concurrent updates (app vs repo).
- Add unit tests covering round-trip and merge scenarios.

## Acceptance
- App round-trips transcripts between GUI and `handoff/` without data loss.
- Merge policy preserves all messages.
- Tests pass in CI.

## Notes
- Use PR template (scope, screenshots, run steps).
- Run lint and unit tests; attach zipped artifact.
- Keep changes under `clients/windows/**` plus CI files.
- Reuse Prompt Hub visuals where feasible.
