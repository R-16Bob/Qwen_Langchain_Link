import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.qa_utils import qa_agnet
from langchain.memory import ConversationBufferMemory

st.title("📑AI智能PDF问答工具")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )

uploaded_file = st.file_uploader("请上传PDF文件", type=["pdf"])
question = st.text_input("对PDF的内容进行提问", disabled=not uploaded_file)

if uploaded_file and question:
    with st.spinner("AI正在思考中..."):
        response = qa_agnet(uploaded_file, question, st.session_state["memory"])
    st.write("### 答案")
    st.write(response["answer"])
    st.session_state["chat_history"] = response["chat_history"]

if "chat_history" in st.session_state:
    with st.expander("历史消息"):
        for i in range(0, len(st.session_state["chat_history"]), 2):
            st.write(st.session_state['chat_history'][i])
            st.write(st.session_state['chat_history'][i+1])
            if i<len(st.session_state["chat_history"])-2:
                st.divider()
        