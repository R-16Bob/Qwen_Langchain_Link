from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from langchain_huggingface import HuggingFaceEmbeddings
import time

# 将本地部署的 Qwen 模型封装为 LangChain 可用的Chat模型
def load_chat_model(model_path):
    start_time = time.time()  # 记录模型加载开始时间
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype="auto",
    )
    end_time = time.time()  # 记录模型加载结束时间
    elapsed_time = end_time - start_time  # 计算模型加载耗时
    print(f"{model_path} 模型加载完成，耗时 {elapsed_time:.2f} 秒")

    pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=1024,
            # temperature=0.3,
            return_full_text=False  # 只返回新生成的部分
        )

    # 将 pipeline 封装成 LangChain 可用的 HuggingFacePipeline 实例
    llm = HuggingFacePipeline(pipeline=pipe)

    chat_model = ChatHuggingFace(llm=llm, tokenizer=tokenizer)

    return chat_model, tokenizer

def load_embedding_model(embeding_model, device="cpu"):
    model_map = {
        "Qwen3-Embedding-0.6B": r"D:\AI_models\Qwen\Qwen3-Embedding-0___6B",
    }
    model_path = model_map[embeding_model]
    model_kwargs = {
        "device": device,  # 根据设备情况选择使用 GPU 或 CPU
        "trust_remote_code": True  # 允许加载远程代码
    }
    # 初始化 HuggingFaceEmbeddings
    embeddings_model = HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs=model_kwargs
    )
    return embeddings_model

def apply_chat_template(prompt, tokenizer, enable_thinking=False):
    return tokenizer.apply_chat_template(prompt, tokenize=False, add_generation_prompt=True, enable_thinking=enable_thinking)

# 一个生成消息的示例函数
def generate_messages(question, tokenizer, enable_thinking=False):
    system_message = {"role": "system", "content": "你是一个乐于助人的中文助手。"}
    message = [system_message, {"role": "user", "content": question}]
    return apply_chat_template(message, tokenizer, enable_thinking)

if __name__ == "__main__":
    model_path = r"D:\AI_models\Qwen2.5-0.5B-Instruct"  # 替换为你的模型路径
    # 1. 加载模型
    chat_model, tokenizer = load_chat_model(model_path)
    # 2. 生成消息
    question = "简单介绍大语言模型。"
    messages = generate_messages(question, tokenizer)
    # 3. 调用模型生成回复
    response = chat_model.invoke(messages)
    print(response)
