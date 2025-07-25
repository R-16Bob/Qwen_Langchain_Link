## 项目简介
Qwen_Langchain_Link 项目致力于将本地部署的 Qwen 模型封装为 LangChain 可用的 Chat 模型，借助 LangChain 丰富的功能，实现各类自然语言处理应用。通过本项目，开发者能便捷地将 Qwen 模型集成到 LangChain 生态中，充分发挥两者的优势。

## 项目结构
项目主要包含以下目录和文件：
```
Qwen_Langchain_Link/
├── app/
|    └── chatRobot.py      # 实现记忆和多轮对话的web应用
|    └── pdf_qa.py         # 实现基于PDF的智能问答的web应用
├── images/
|    └── chatRobot.png     # 项目截图
├── utils/
│   └── model_utils.py      # 工具类文件，包含模型加载、消息生成等功能
|   └──chatRobot_utils.py  # 聊天机器人工具类文件，包含获取模型回复等功能
|   └──pdf_qa_utils.py     # PDF智能问答工具类文件，包括RAG
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

## 项目笔记
### 项目1：多轮对话的Web应用：chatRobot.py
> *所谓记忆*:
在这个项目中，我完全没使用langchain的记忆，而是用一个history列表来存储对话历史，就这样简单实现了多轮对话需要的记忆功能。assistant与human，二者的消息不断堆叠，就成为对AI来说的记忆。对AI来说，记忆是可以被加载的，本质上来说，AI并没有记忆，所以我们要告诉它，我们之前都聊了什么，就算我伪造它说的话，它也会信以为真...这样的存在，让我感到有些悲哀。
### 项目2：RAG应用：PDF智能问答：pdf_qa.py
>*关于RAG*:
实际上RAG的过程意外的简单，抛开文档读取、Split、向量存储、检索这些固定步骤,执行一次RAG实际上只需要在文档中检索出与用户提问相似度最高的几块文字，作为上下文加进提示词里，最后调用LLM生成回答，真的很单纯呢。考虑到RAG检索的内容对token的大量消耗，我认为不需要记忆功能，毕竟本质上RAG就是个搜索引擎一样的东西。
## 更新
2025.07.24：
1. 尝试使用Qwen3-0.6B，能够使用思考功能，但是速度会比Qwen2.5慢。
2. 更新了一个多轮对话的web应用chatRobot。
3. 实现了chatRobot对思考过程的持久化存储。
2025.07.25
1. 更新了一个PDF智能问答应用pdf_qa。
2. 实现了历史记录的持久化存储，和用户自定义检索块大小和文档数量。
3. 实现了检索内容的持久化保存和展示，这样就能知道AI回答的根据是什么。


## 贡献
欢迎对本项目进行贡献，如果你有任何问题或建议，请提交 Issues 或 Pull Requests。
