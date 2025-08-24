@echo off
setlocal
where pip >nul 2>nul || (echo Python not found & exit /b 1)
pip show fastapi >nul 2>nul || python -m pip install fastapi uvicorn >nul
python backend\main.py
