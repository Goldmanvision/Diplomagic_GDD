DIPLOMAGIC Local UI Wizard
==========================

Usage
1) .\wizard_local_ui.ps1
2) Start backend: .\tools\local-ui\run_backend.bat
3) Frontend: cd tools\local-ui\frontend && npm i && npm run dev -- --port 5173
4) Open http://localhost:5173

Notes
- Set repo root in the UI.
- CSV export returns text; client should download.
- Place JSON schemas in data/schemas.
