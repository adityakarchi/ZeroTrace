@echo off
REM ZeroTrace Backend Runner for Windows
echo Starting ZeroTrace API server...
cd secure-comm\backend
call venv\Scripts\activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
pause