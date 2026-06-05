# GitHub 发布指南

## 步骤 1: 创建 Personal Access Token

1. 打开 https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 填写:
   - Note: `ai-voice-tools`
   - Expiration: `90 days`
   - 勾选: `repo` (全部仓库权限)
4. 点击 "Generate token"
5. **复制保存 token** (只显示一次)

## 步骤 2: 创建仓库

1. 打开 https://github.com/new
2. 填写:
   - Repository name: `ai-voice-tools`
   - Description: `AI语音克隆和变声工具集`
   - 选择: `Public` 或 `Private`
   - **不要**勾选 "Add a README file"
3. 点击 "Create repository"

## 步骤 3: 推送代码

在 D:\stdio 目录打开 CMD/PowerShell，执行:

```bash
# 设置远程仓库 (替换 YOUR_TOKEN 和 YOUR_USERNAME)
git remote add origin https://359923331:YOUR_TOKEN@github.com/359923331/ai-voice-tools.git

# 推送
git push -u origin master
```

## 或者用 GitHub CLI (推荐)

```bash
# 安装 GitHub CLI
winget install GitHub.cli

# 登录
gh auth login

# 创建仓库并推送
gh repo create ai-voice-tools --public --source=. --push
```
