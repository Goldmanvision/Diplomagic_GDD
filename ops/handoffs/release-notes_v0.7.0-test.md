\# v0.7.0-test — 2025-08-25



\## Summary

Local-UI backend stabilized. Windows RAG client gains offline embeddings and `retrieve.query`. CSV export and schema listing are available. Python 3.11 lockfiles regenerated.



\## Backend

\- Endpoints: `/health` (`ok=true`), `/schemas` (JSON list), `/export/csv` (embeddings dump)

\- Dev server: `uvicorn <auto-discovered-module>:app --host 127.0.0.1 --port 8765`



\## Windows RAG Client

\- Offline embeddings path enabled when `RAG\_EMBED\_URL` is empty

\- `retrieve.query` added for local semantic search



\## Testing

\- All Python tests run locally per guardrail

\- Backend tests green

\- RAG suites triaged; remaining cases under review



\## CI

\- `build-windows` and `local-ui-pack` workflows green on `main` ≥ PR #179 merge commit

\- Artifact: Local-UI pack attached to v0.7.0-test



\## Upgrade Notes

\- Prefer short repo paths on Windows or enable long paths

\- Normalize I/O to `utf-8` with LF for cross-env consistency



\## PRs

\#179



