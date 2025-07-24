import streamlit as st
import sys
import os 
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.chatRobot_utils import get_chat_response

st.title("💭ChatRobot")

if "history" not in st.session_state:
    st.session_state["history"] = [{"role": "assistant", "content": "我是你的AI助手，有什么可以帮你的吗？"}]
# 新增思考过程存储
if "think_history" not in st.session_state:
    st.session_state["think_history"] = [None]

# 显示聊天记录和思考过程
for i, message in enumerate(st.session_state["history"]):
    think_content = st.session_state["think_history"][i]
    if think_content:
        with st.expander("思考过程", expanded=False):
            st.info(think_content)
    st.chat_message(message["role"]).write(message["content"])
    
    


prompt = st.chat_input("给AI发送消息")
model = st.selectbox("模型选择", ["Qwen2.5-0.5B-Instruct", "Qwen3-0.6B"])  
# 添加开关组件
enable_thinking = st.toggle("开启思考功能", value=False)
if prompt:
    # 新增用户消息
    st.session_state["history"].append({"role": "user", "content": prompt})
    st.session_state["think_history"].append(None)
    st.chat_message("user").write(prompt)
    with st.spinner("AI思考中..."):
        # AI回答
        response = get_chat_response(st.session_state["history"], model, enable_thinking)
        if enable_thinking:
            # 使用正则表达式提取 <think></think> 之间的内容
            think_match = re.search(r'<think>(.*?)</think>', response, re.DOTALL)
            think_content = think_match.group(1).strip() if think_match else ""
            # 移除 <think></think> 标签及其内容
            clean_response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()
            st.session_state["think_history"].append(think_content)
            if think_content:
                with st.expander("思考过程", expanded=True):
                    st.info(think_content)
        else:
            clean_response = response
            st.session_state["think_history"].append(None)

        st.session_state["history"].append({"role": "assistant", "content": clean_response})
        st.chat_message("assistant").write(clean_response)

if st.button("清除对话历史"):
    # 清空会话记录，重置messages
    st.session_state["history"] = [{"role": "ai", "content": "我是你的AI助手，有什么可以帮你的吗？"}]
    st.session_state["think_history"] = [None]