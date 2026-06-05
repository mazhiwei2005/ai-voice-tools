# RVC Installation Guide

## Problem
RVC source code requires Python 3.10 and many dependencies (fairseq, etc.) that are difficult to install.

## Recommended Solution: Download RVC Windows Package

### Option 1: RVC WebUI Package (Recommended)
Download the pre-built Windows package from:
- https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/releases

Look for `RVCWebUI.zip` or similar - it includes everything needed.

### Option 2: Use GPT-SoVITS Instead
GPT-SoVITS Complete version already includes voice cloning capabilities:
- Start: `Start_GPT-SoVITS-Complete.bat`
- URL: http://127.0.0.1:9874
- Supports: Text-to-Speech with voice cloning

## Quick Alternative: Use GPT-SoVITS for Voice Cloning

GPT-SoVITS can do voice cloning with just 5 seconds of audio:

1. Start GPT-SoVITS: `Start_GPT-SoVITS-Complete.bat`
2. Go to http://127.0.0.1:9874
3. Upload reference audio (5+ seconds)
4. Enter text
5. Generate speech in that voice

## Downloaded RVC Models
Your models are in `D:\stdio\RVC\assets\weights\`:
- Keqing (刻晴)
- Yelan (夜兰)  
- Yoimiya (宵宫)

These will work once you have a working RVC installation.

## Next Steps
1. Download RVC Windows package from GitHub releases
2. Extract to `D:\stdio\RVC-WebUI\`
3. Copy your models to `D:\stdio\RVC-WebUI\assets\weights\`
4. Run `go-web.bat` in the new directory
