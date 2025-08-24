# Job Card TS-MAC-DAPS-0004 — JC-WIN-01: Windows DAPS client scaffold

**Owner:** diplomagic-codex-agent
**Labels:** ops, windows, daps
**Branch:** ops/win-client-01-scaffold
**Goal:** Scaffold a Windows DAPS client with pluggable model interfaces.

## Tasks
- Choose Electron or .NET MAUI for `clients/windows/`; justify choice in README.
- Set up project skeleton and wiring for build scripts and CI.
- Implement configuration and secure OpenAI key storage (Windows credential vault or equivalent; no secrets in repo).
- Define service-layer interfaces for OpenAI and local Ollama with mock adapters.
- Add minimal GUI: prompt input box and transcript pane.
- Document install/build/run steps in README.

## Acceptance
- Build runs locally on Windows.
- GUI can hit mock OpenAI/Ollama adapters (no real calls).
- README includes framework rationale and run instructions.

## Notes
- Use PR template (scope, screenshots, run steps).
- Run lint and unit tests; attach zipped artifact.
- Keep changes under `clients/windows/**` plus CI files.
- Reuse existing Prompt Hub visuals when possible.
- Tag `win-client-v0.1` after all WIN job cards merge.
