@echo off

REM Check Python version
python -c "import sys; sys.exit(1 if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 6) else 0)"
IF ERRORLEVEL 1 (
    echo Python version 3.6 or later is required
    exit /b
)

REM Install dependencies
python -m pip install -r requirements.txt
IF ERRORLEVEL 1 (
    echo Failed to install dependencies
    exit /b
)

REM Run the script
python main.py
