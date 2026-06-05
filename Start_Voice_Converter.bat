@echo off
cd /d "D:\stdio"
echo Starting AI Voice Converter...
python voice_converter.py
if errorlevel 1 (
    echo.
    echo [ERROR] Python not found or script failed
    echo Please install Python 3.10+ and requests: pip install requests
    echo.
)
pause
