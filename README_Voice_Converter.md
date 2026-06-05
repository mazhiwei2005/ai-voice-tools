# AI Voice Converter

## Features

1. **Text → Voice**: Input text, output character voice (GPT-SoVITS + RVC)
2. **Audio → Voice**: Input MP3/WAV, convert to character voice (RVC)

## Supported Characters

### Genshin Impact
- Raiden Shogun (雷电将军)
- Hu Tao (胡桃)
- Ganyu (甘雨)
- Nahida (纳西妲)
- Ayaka (神里绫华)

### Uma Musume
- Special Week (特别周)
- Silence Suzuka (无声铃鹿)
- Tokai Teio (东海帝王)

## Prerequisites

1. **Python 3.10+** installed
2. **GPT-SoVITS** running at http://127.0.0.1:9874
3. **RVC** running at http://127.0.0.1:7897
4. **RVC Models** downloaded to `RVC/assets/weights/`

## Quick Start

1. Double-click `Start_Voice_Converter.bat`
2. Select mode (Text or Audio)
3. Select character voice
4. Enter text or select audio file
5. Click Convert

## Download Models

### From Hugging Face
- Genshin: https://huggingface.co/models?search=genshin+rvc
- Uma Musume: https://huggingface.co/models?search=uma+musume+rvc

### Model Files
Place downloaded files in:
```
D:\stdio\RVC\assets\weights\
├── raiden_shogun.pth
├── raiden_shogun.index
├── hu_tao.pth
├── hu_tao.index
└── ...
```

## Workflow

```
Text Input
    ↓
GPT-SoVITS (TTS)
    ↓
Raw Audio (.wav)
    ↓
RVC (Voice Conversion)
    ↓
Final Output (.wav)
```

## Troubleshooting

### "Service not running"
- Start GPT-SoVITS: `Start_GPT-SoVITS-Complete.bat`
- Start RVC: `Start_RVC_Web.bat`

### "Model not found"
- Download model from Hugging Face
- Place .pth and .index files in `RVC/assets/weights/`

### "Conversion failed"
- Check if both services are running
- Check console for error messages
- Try different input audio/text

## Links

- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- [Model Resources](模型资源大全.md)
