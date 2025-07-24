from utils.model_utils import load_chat_model, generate_messages

# 一个聊天的简单示例
# 1. 加载模型
model_path = r"D:\AI_models\Qwen2.5-0.5B-Instruct"  # 替换为你的模型路径
model, tokenizer = load_chat_model(model_path)
# 2. 生成消息
message = generate_messages("介绍你自己。", tokenizer)
# 3. 调用模型生成回复
response = model.invoke(message)
print(response.content)