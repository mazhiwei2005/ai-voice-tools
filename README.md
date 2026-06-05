# 🎭 AI 语音工具集

> AI 语音克隆和变声工具，支持文字转语音、声音转换、实时变声

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

## ✨ 功能特性

### 🎤 语音克隆 (GPT-SoVITS)
- **5 秒克隆** - 仅需 5 秒音频即可克隆声音
- **文字转语音** - 输入文字生成角色语音
- **多语言支持** - 支持中文、日语、英语
- **情感控制** - 可调整语音情感和语调

### 🔄 声音转换 (RVC)
- **实时变声** - 实时转换声音
- **批量处理** - 批量转换音频文件
- **模型丰富** - 支持多种预训练模型
- **高质量输出** - 保持原始音质

### 🎮 游戏角色声音
- **原神角色** - 雷电将军、胡桃、甘雨等
- **赛马娘** - Special Week、Silence Suzuka 等
- **自定义模型** - 可训练自己的声音模型

## 🚀 快速开始

### 环境要求
- Windows 10/11
- Python 3.10+
- NVIDIA GPU（推荐）
- 8GB+ 显存

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/mazhiwei2005/ai-voice-tools.git
cd ai-voice-tools
```

2. **安装 GPT-SoVITS**
```bash
# 下载 GPT-SoVITS 完整版
# 解压到 GPT-SoVITS-Complete 目录
```

3. **安装 RVC**
```bash
# 下载 RVC 整合包
# 解压到 RVC 目录
```

4. **下载模型**
```bash
# 下载预训练模型
# 放到 RVC/assets/weights/ 目录
```

## 📁 项目结构

```
ai-voice-tools/
├── Start_GPT-SoVITS-Complete.bat  # GPT-SoVITS 启动脚本
├── Start_RVC_Web.bat              # RVC Web 界面启动
├── Start_RVC_Realtime.bat         # RVC 实时变声启动
├── Start_Voice_Converter.bat      # 一键转换工具
├── voice_converter.py             # 转换工具源码
├── GPT-SoVITS/                    # GPT-SoVITS 源码
├── GPT-SoVITS-Complete/           # GPT-SoVITS 完整版
├── RVC/                           # RVC 变声器
│   └── assets/weights/            # 模型文件
│       ├── Keqing_e500_s13000.pth # 刻晴模型
│       ├── Yelan_YelanJP.pth      # 夜兰模型
│       └── Yoimiya_YoimiyaJP.pth  # 宵宫模型
└── README.md
```

## 🎯 使用场景

### 场景 1：文字转语音
1. 启动 GPT-SoVITS: `Start_GPT-SoVITS-Complete.bat`
2. 打开 http://127.0.0.1:9874
3. 上传 5 秒参考音频
4. 输入文字
5. 生成语音

### 场景 2：声音转换
1. 启动 RVC: `Start_RVC_Web.bat`
2. 打开 http://127.0.0.1:7897
3. 选择模型（如刻晴）
4. 上传音频文件
5. 转换并下载

### 场景 3：一键转换
1. 启动转换器: `Start_Voice_Converter.bat`
2. 选择模式（文字/音频）
3. 选择角色
4. 输入文字或选择音频
5. 点击转换

## 🎮 预训练模型

### 原神角色
| 角色 | 模型文件 | 声线特点 |
|------|----------|----------|
| 刻晴 | Keqing_e500_s13000.pth | 活泼、俏皮 |
| 夜兰 | Yelan_YelanJP.pth | 性感、神秘 |
| 宵宫 | Yoimiya_YoimiyaJP.pth | 热情、开朗 |

### 赛马娘
| 角色 | 模型文件 | 声线特点 |
|------|----------|----------|
| Special Week | special_week.pth | 元气、主角 |
| Silence Suzuka | silence_suzuka.pth | 冷静、天才 |
| Tokai Teio | tokai_teio.pth | 活泼、不服输 |

## ⚙️ 配置说明

### GPT-SoVITS 配置
- **模型路径** - GPT-SoVITS-Complete/pretrained_models
- **音频格式** - WAV, MP3, FLAC
- **采样率** - 16kHz, 22.05kHz, 44.1kHz

### RVC 配置
- **模型路径** - RVC/assets/weights/
- **索引路径** - RVC/assets/indices/
- **音频格式** - WAV, MP3

## 🔧 高级功能

### 模型训练
- 支持自定义声音模型训练
- 支持微调预训练模型
- 支持多 GPU 训练

### 批量处理
- 支持文件夹批量导入
- 支持批量转换
- 支持批量生成

### 实时变声
- 支持麦克风输入
- 支持实时预览
- 支持多种音效

## 📊 性能优化

### GPU 加速
- 支持 NVIDIA CUDA
- 支持半精度推理
- 支持模型量化

### 内存优化
- 流式处理大文件
- 分批处理长音频
- 自动释放内存

## 🐛 常见问题

### Q: GPT-SoVITS 启动失败？
A: 检查 Python 环境，确保安装了所有依赖。

### RVC 模型加载失败？
A: 检查模型文件是否完整，确保路径正确。

### 生成语音质量差？
A: 尝试使用更好的参考音频，或调整参数。

### GPU 内存不足？
A: 减小批处理大小，或使用更小的模型。

## 📝 更新日志

### v1.0 (2025-06-01)
- 初始版本发布
- 支持 GPT-SoVITS 语音克隆
- 支持 RVC 声音转换
- 添加原神角色模型

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 语音克隆框架
- [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) - 声音转换框架
- [Hugging Face](https://huggingface.co/) - 模型托管平台

## 📞 联系方式

- GitHub: [@mazhiwei2005](https://github.com/mazhiwei2005)
- Email: 359923331@qq.com

---

⭐ 如果这个项目对你有帮助，请给个 Star 支持一下！
