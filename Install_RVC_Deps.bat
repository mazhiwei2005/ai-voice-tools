@echo off
echo ========================================
echo Installing RVC Dependencies
echo ========================================
echo.
echo Activating conda environment 'rvc'...
call C:\Users\Lenovo\anaconda3\Scripts\activate.bat rvc
echo.
echo Python version:
python --version
echo.
cd /d "D:\stdio\RVC"
echo Installing requirements...
pip install -r requirements.txt
echo.
echo ========================================
echo Done! Now run Start_RVC_Web.bat
echo ========================================
pause
