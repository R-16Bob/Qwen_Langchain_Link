from utils.model_utils import load_chat_model, generate_messages

# 一个聊天的简单示例
# 1. 加载模型
model_path = r"D:\AI_models\Qwen2.5-0.5B-Instruct"  # 替换为你的模型路径
# model_path = r"D:\AI_models\Qwen\Qwen3-0___6B" # 感觉不是很需要思考功能，为了性能，我还是使用Qwen2.5

model, tokenizer = load_chat_model(model_path)
# 2. 生成消息
message = generate_messages("简单介绍大语言模型", tokenizer)  
# 3. 调用模型生成回复
response = model.invoke(message)
print(response.content)