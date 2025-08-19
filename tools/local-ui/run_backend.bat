@echo off
setlocal
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  py -3 -m venv .venv 2>nul || python -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
uvicorn backend.main:app --reload --port 5174
