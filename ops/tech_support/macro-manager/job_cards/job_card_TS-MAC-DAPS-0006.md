# Job Card TS-MAC-DAPS-0006 — JC-WIN-03: Context API for Workthreads

**Owner:** diplomagic-codex-agent
**Labels:** ops, windows, daps, context
**Branch:** ops/win-client-03-context-api
**Goal:** Expose API for Workthreads to push and retrieve context for prompts.
**Prerequisite:** JC-WIN-01 scaffold layout.

## Tasks
- Provide local HTTP endpoint or file-watch API for context ingestion.
- Require auth token for pushes.
- Add settings toggle to retain or clear history per session.
- Supply example script demonstrating context push.

## Acceptance
- Example script pushes context successfully.
- Client injects last N messages into prompt before dispatch.
- History toggle works as configured.

## Notes
- Use PR template (scope, screenshots, run steps).
- Run lint and unit tests; attach zipped artifact.
- Keep changes under `clients/windows/**` plus CI files.
- Reuse Prompt Hub visuals where feasible.
