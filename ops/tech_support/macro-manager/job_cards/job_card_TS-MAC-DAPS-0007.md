# Job Card TS-MAC-DAPS-0007 — JC-WIN-04: Dynamic model routing (OpenAI ↔ Ollama)

**Owner:** diplomagic-codex-agent
**Labels:** ops, windows, daps, routing
**Branch:** ops/win-client-04-routing
**Goal:** Enable runtime model selection and fallback between OpenAI and local Ollama.
**Prerequisite:** JC-WIN-01 scaffold layout and adapter interfaces.

## Tasks
- Add settings UI to choose backend and model.
- Implement adapters for OpenAI REST API and local Ollama service.
- Provide fallback rules and user-facing error surfaces when a backend is unavailable.
- Support runtime switching between backends without restarting.

## Acceptance
- User can switch backends at runtime.
- Client continues with degraded operation if one backend is down.
- Errors are surfaced to the UI.

## Notes
- Use PR template (scope, screenshots, run steps).
- Run lint and unit tests; attach zipped artifact.
- Keep changes under `clients/windows/**` plus CI files.
- Reuse Prompt Hub visuals where feasible.
- Tag `win-client-v0.1` after all WIN job cards merge.
