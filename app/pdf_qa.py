import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.qa_utils import qa_agnet

st.title("📑AI智能PDF问答工具")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

uploaded_file = st.file_uploader("请上传PDF文件", type=["pdf"])
k = st.slider("检索文档数量：", value=2, min_value=1, max_value=4, step=1)  
chunk_size = st.slider("文档分块大小：", value=500, min_value=200, max_value=1000, step=100)
question = st.text_input("对PDF的内容进行提问", disabled=not uploaded_file)

if uploaded_file and question:
    with st.spinner("AI正在思考中..."):
        response = qa_agnet(uploaded_file, question, chunk_size, k)
    st.write("### 答案")
    st.write(response)
    st.session_state["chat_history"].append({"question": question, "answer": response})

if "chat_history" in st.session_state:
    with st.expander("历史消息"):
        for i in range(0, len(st.session_state["chat_history"])):
            q = st.session_state['chat_history'][i]["question"]
            a = st.session_state['chat_history'][i]["answer"]
            st.write(q)
            st.write(a)
            if i<len(st.session_state["chat_history"])-1:
                st.divider()
        