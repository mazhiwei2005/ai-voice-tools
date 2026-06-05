@echo off
cd /d "D:\stdio\RVC"
echo ========================================
echo Starting RVC Web Interface
echo ========================================
echo.
echo Activating conda environment 'rvc'...
call C:\Users\Lenovo\anaconda3\Scripts\activate.bat rvc
echo Access at: http://127.0.0.1:7897
echo.
python infer-web.py --pycmd python --port 7897
pause
