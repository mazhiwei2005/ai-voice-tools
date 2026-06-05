@echo off
cd /d "D:\stdio\GPT-SoVITS-Complete\GPT-SoVITS-v3lora-20250228"
set "PATH=%cd%\runtime;%PATH%"
echo Starting GPT-SoVITS v3 Complete...
echo Access at: http://127.0.0.1:9874
runtime\python.exe -I webui.py zh_CN
pause
