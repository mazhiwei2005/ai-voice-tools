@echo off
cd /d "D:\stdio\GPT-SoVITS"
echo Starting GPT-SoVITS WebUI...
echo Access at: http://127.0.0.1:9874
python -I webui.py zh_CN
if errorlevel 1 (
    echo.
    echo [ERROR] Python not found or webui.py failed
    echo Please use Start_GPT-SoVITS-Complete.bat instead
    echo.
)
pause
