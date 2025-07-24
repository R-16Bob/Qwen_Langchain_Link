from utils.model_utils import load_chat_model, apply_chat_template

def get_chat_response(messages, model="Qwen2.5-0.5B-Instruct", enable_thinking=False):
    print(messages)
    model_map ={
        "Qwen2.5-0.5B-Instruct": r"D:\AI_models\Qwen2.5-0.5B-Instruct",
        "Qwen3-0.6B": r"D:\AI_models\Qwen\Qwen3-0___6B"
    }
    model_path = model_map[model]
    model, tokenizer = load_chat_model(model_path)

    messages = apply_chat_template(messages, tokenizer, enable_thinking)
    # 调用模型生成回复
    response = model.invoke(messages)
    return response.content

if __name__ == "__main__":
    messages = [
        {"role": "assistant", "content": "我是你的AI助手，有什么可以帮你的吗？"},
        {"role": "user", "content": "你是谁？"}]
    response = get_chat_response(messages)
    print(response)