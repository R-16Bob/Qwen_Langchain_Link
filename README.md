## 项目简介
Qwen_Langchain_Link 项目致力于将本地部署的 Qwen 模型封装为 LangChain 可用的 Chat 模型，借助 LangChain 丰富的功能，实现各类自然语言处理应用。通过本项目，开发者能便捷地将 Qwen 模型集成到 LangChain 生态中，充分发挥两者的优势。

## 项目结构
项目主要包含以下目录和文件：
```
Qwen_Langchain_Link/
├── utils/
│   └── model_utils.py      # 工具类文件，包含模型加载、消息生成等功能
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
demo1.py提供了一个简单的聊天示例。你可以在model_utils中定义自己的提示词模版。

## 贡献
欢迎对本项目进行贡献，如果你有任何问题或建议，请提交 Issues 或 Pull Requests。
