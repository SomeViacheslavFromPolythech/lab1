@echo off
setlocal

if not exist ".venv\Scripts\python.exe" python -m venv .venv
if errorlevel 1 exit /b %errorlevel%

".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 exit /b %errorlevel%

".venv\Scripts\python.exe" src\main.py
if errorlevel 1 exit /b %errorlevel%

".venv\Scripts\python.exe" -m pytest
if errorlevel 1 exit /b %errorlevel%
