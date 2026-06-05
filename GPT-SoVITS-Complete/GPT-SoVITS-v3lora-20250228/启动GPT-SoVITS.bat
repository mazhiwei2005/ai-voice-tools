@echo off
chcp 65001 >nul
title GPT-SoVITS
echo ========================================
echo    GPT-SoVITS - AI Text-to-Speech
echo ========================================
echo.
cd /d "%~dp0"
echo Starting GPT-SoVITS...
echo Browser will open at http://127.0.0.1:9874
echo.
runtime\python.exe webui.py zh_CN
pause
