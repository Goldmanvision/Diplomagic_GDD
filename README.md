## Local UI (FastAPI + Vite)

A small local tool to parse dashboards, view department mail, and export CSVs for UE DataTables.

### Prerequisites
- Windows 10/11, PowerShell 5+.
- Python 3.11+.
- Node.js LTS (`winget install OpenJS.NodeJS.LTS`).

### Start services
Backend:
```powershell
cd tools\local-ui
.\run_backend.bat
# Health: http://127.0.0.1:5174/health  -> {"status":"ok"}
### Quick launch
Run \	ools\\local-ui\\dsdk-dev.cmd\ to start backend, frontend, and open browser tabs.
