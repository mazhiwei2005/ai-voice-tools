@echo off
cd /d "D:\stdio\RVC"
echo ========================================
echo Starting RVC Realtime Voice Changer
echo ========================================
echo.
echo Activating conda environment 'rvc'...
call C:\Users\Lenovo\anaconda3\Scripts\activate.bat rvc
echo.
python gui_v1.py
pause
