# AI Voice Tools - Quick Start

## Startup Scripts

| Script | Description | Access URL |
|--------|-------------|------------|
| `Start_GPT-SoVITS.bat` | GPT-SoVITS (source, needs Python) | http://127.0.0.1:9874 |
| `Start_GPT-SoVITS-Complete.bat` | GPT-SoVITS v3 (with runtime, recommended) | http://127.0.0.1:9874 |
| `Start_RVC_Web.bat` | RVC Web Interface (needs Python) | http://127.0.0.1:7897 |
| `Start_RVC_Realtime.bat` | RVC Realtime Voice Changer (needs Python) | Desktop App |

## Versions

### GPT-SoVITS
- **Source Version** (`GPT-SoVITS/`): Requires Python 3.10+ installed
- **Complete Version** (`GPT-SoVITS-Complete/`): Includes Python runtime, ready to use

### RVC
- **Source Version** (`RVC/`): Requires Python 3.10+ installed

## Requirements

- Windows 10/11
- NVIDIA GPU (RTX 3070 recommended)
- CUDA 11.8+ or 12.x
- Python 3.10+ (for source versions)

## Usage

### Recommended (Complete Version)
1. Double-click `Start_GPT-SoVITS-Complete.bat`
2. Wait for the web server to start
3. Open http://127.0.0.1:9874 in your browser

### Source Versions
1. Install Python 3.10+ from python.org
2. Install dependencies: `pip install -r requirements.txt`
3. Double-click the desired `.bat` file
4. Wait for the web server to start
5. Open the URL in your browser

## Notes

- First run may take longer to initialize
- Keep the console window open while using
- Press Ctrl+C in console to stop the server
- If you get errors, use the Complete version instead
