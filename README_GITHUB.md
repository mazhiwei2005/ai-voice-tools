# AI Voice Tools 🎭

AI语音克隆和变声工具集，支持原神、赛马娘等角色声音克隆。

## 🚀 功能

- **GPT-SoVITS**: 语音克隆，5秒音频即可克隆声音
- **RVC**: 实时变声，支持多种角色模型
- **Voice Converter**: 一键文字/音频转角色声音

## 📦 包含工具

| 工具 | 说明 | 启动方式 |
|------|------|----------|
| GPT-SoVITS | 语音克隆 | `Start_GPT-SoVITS-Complete.bat` |
| RVC Web | 变声器Web版 | `Start_RVC_Web.bat` |
| RVC Realtime | 实时变声 | `Start_RVC_Realtime.bat` |
| Voice Converter | 一键转换 | `Start_Voice_Converter.bat` |

## 🎮 已下载模型

### 原神 (Genshin Impact)
- 刻晴 (Keqing)
- 夜兰 (Yelan)
- 宵宫 (Yoimiya)

### 赛马娘 (Uma Musume)
- 待下载...

## 📋 使用方法

### 1. 启动 GPT-SoVITS
```bash
双击 Start_GPT-SoVITS-Complete.bat
访问 http://127.0.0.1:9874
```

### 2. 启动 RVC
```bash
双击 Start_RVC_Web.bat
访问 http://127.0.0.1:7897
```

### 3. 使用转换器
```bash
双击 Start_Voice_Converter.bat
选择角色 → 输入文字/音频 → 转换
```

## 📥 下载更多模型

### Hugging Face
- 原神: https://huggingface.co/models?search=genshin+rvc
- 赛马娘: https://huggingface.co/models?search=uma+musume+rvc

### 模型放置位置
```
RVC/assets/weights/
├── 角色名.pth    (模型文件)
└── 角色名.index  (索引文件)
```

## 📁 目录结构

```
D:\stdio\
├── GPT-SoVITS/                    # GPT-SoVITS源码
├── GPT-SoVITS-Complete/           # GPT-SoVITS完整版(推荐)
├── RVC/                           # RVC变声器
│   └── assets/weights/            # RVC模型目录
├── voice_converter.py             # 自动转换工具
├── Start_*.bat                    # 启动脚本
└── README_*.md                    # 说明文档
```

## ⚠️ 注意事项

- 需要 NVIDIA GPU (推荐 RTX 3070+)
- 需要 CUDA 11.8+
- GPT-SoVITS 完整版自带 Python，无需额外安装
- RVC 源码版需要 Python 3.10+（建议下载整合包）

## 🔗 相关项目

- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

## 📄 License

MIT License
