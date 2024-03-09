# ChatWithDataWhale

ChatWithDataWhale 是一个与 DataWhale 现有仓库和学习内容对话的项目,旨在帮助用户快速找到想学习的内容和可以贡献的内容。

## 功能特点

- 与 DataWhale 的学习资源进行自然语言交互
- 通过对话方式发现感兴趣的学习内容
- 找到可以贡献和改进的项目领域
- 利用大语言模型总结仓库的 README 内容

## 环境配置

在运行项目之前,请确保您的环境满足以下要求:

- Python 3.10 或更高版本
- 安装所需的 Python 依赖包:
pip install -r requirements.txt

复制

## .env 文件配置

为了正常运行项目,您需要在项目根目录下创建一个 `.env` 文件,并配置以下内容:

```
# GitHub 访问令牌
TOKEN=your_github_access_token

# 任意选择一个 remote llm api
# DeepSeek API 密钥
deepseekapi=your_deepseek_api_key
# Moonshot API 密钥
moonapi=your_moonshot_api_key
# OpenAI API 密钥
chatgptapi=your_openai_api_key
```

请将 `your_github_access_token`、`your_deepseek_api_key`、`your_moonshot_api_key` 和 `your_openai_api_key` 替换为您自己的 API 密钥。

## 使用方法

1. 克隆本仓库到本地
2. 安装所需的 Python 依赖包
3. 在 `.env` 文件中配置所需的 API 密钥
4. 运行 `python text_summary_readme.py` 对仓库的 README 进行自动总结
5. 运行对话脚本与学习资源进行交互

## 项目结构

- `get_issues_pipeline.py`: 获取 GitHub 仓库 issue 的脚本
- `test_get_all_repo.py`: 获取 DataWhale 组织下所有仓库的脚本 
- `text_summary_readme.py`: 利用大语言模型自动总结 README 的脚本
- `README.md`: 项目说明文档

## 贡献指南

欢迎对本项目进行改进和贡献!您可以通过以下方式参与:

1. 提交 Issue 反馈问题或建议新功能
2. 提交 Pull Request 改进代码或文档
3. 分享项目,让更多人参与和受益

## 致谢

感谢 DataWhale 组织提供了丰富的学习资源!

## 许可证

本项目基于 MIT 许可证进行开源。请查看 `LICENSE` 文件了解详情。