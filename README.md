## 项目简介
Qwen_Langchain_Link 项目致力于将本地部署的 Qwen 模型封装为 LangChain 可用的 Chat 模型，借助 LangChain 丰富的功能，实现各类自然语言处理应用。通过本项目，开发者能便捷地将 Qwen 模型集成到 LangChain 生态中，充分发挥两者的优势。

## 项目结构
项目主要包含以下目录和文件：
```
Qwen_Langchain_Link/
├── app/
|    └── chatRobot.py      # 实现记忆和多轮对话的web应用
├── utils/
│   └── model_utils.py      # 工具类文件，包含模型加载、消息生成等功能
|   └──chatRobot_utils.py  # 聊天机器人工具类文件，包含获取模型回复等功能
├── demo1.py                # 使用示例文件，展示如何加载模型并进行对话
└── README.md               # 项目说明文档
```
## 快速开始
### 环境准备
确保你已经安装了必要的 Python 库，可以使用以下命令创建虚拟环境并安装依赖：
```bash
conda env create -f environment.yml
```
### 模型准备
将Qwen模型下载到本地。你可以使用Transformer库或者modelscope库下载想要的模型。确保模型文件的路径与代码中的路径一致。

### 运行示例
- demo1.py提供了一个简单的聊天示例。你可以在model_utils中定义自己的提示词模版。
- chatRobot.py提供了一个多轮对话的web应用。你可以使用`streamlit run chatRobot.py`运行，在WebUI中进行多轮对话。

## 更新
2025.07.24：
1. 尝试使用Qwen3-0.6B，能够使用思考功能，但是速度会比Qwen2.5慢。
2. 更新了一个多轮对话的web应用chatRot

## Plan
- 虽然提供了Think功能的显示，但是还存在一些问题:
    - 没有做持久化，思考过程只有刚回答时可以看到，任何操作都将刷新页面，然后就看不到思考过程了。
    - 如果关掉思考开关，思考过程就不显示了。
也许我会修复这个问题，但Qwen3的思考在CPU上很慢，我可能不会频繁使用思考。所以这个问题暂时不会修复。

## 贡献
欢迎对本项目进行贡献，如果你有任何问题或建议，请提交 Issues 或 Pull Requests。
