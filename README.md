# DIPLOMAGIC — CH7 Packaging Placeholder

This folder contains files to stage a packaging-only Chapter 7. Use when narrative sources omit CH7.

- Place `Patches/CH7-placeholder.md` into repo `/Patches/`.
- Place `Trackers/CH7-state.md` into repo `/Trackers/`.
- Use `PR_BODY.md` for the pull request description.

Suggested branch: `feat/ch7-packaging-placeholder`

Commit message:
```
chore(ch7): add packaging-only placeholder and state tracker
=======
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
## Local UI Quickstart (Windows)


### Backend (Python 3.12)
    py -3.12 -m venv tools\local-ui\.venv312
    tools\local-ui\.venv312\Scripts\python -m pip install -r tools\local-ui\backend\requirements.txt
    tools\local-ui\.venv312\Scripts\python -m uvicorn main:app --reload --port 5174 --app-dir tools\local-ui\backend

### Frontend (Node LTS)
    cd tools\local-ui\frontend
    npm ci
    npx vite --port 5173

Health: http://127.0.0.1:5174/docs and http://127.0.0.1:5173



### Backend (Python 3.12)
    py -3.12 -m venv tools\local-ui\.venv312
    tools\local-ui\.venv312\Scripts\python -m pip install -r tools\local-ui\backend\requirements.txt
    tools\local-ui\.venv312\Scripts\python -m uvicorn main:app --reload --port 5174 --app-dir tools\local-ui\backend

### Frontend (Node LTS)
    cd tools\local-ui\frontend
    npm ci
    npx vite --port 5173

Health: http://127.0.0.1:5174/docs and http://127.0.0.1:5173


