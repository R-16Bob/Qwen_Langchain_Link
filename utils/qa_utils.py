import os
# from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from utils.model_utils import load_embedding_model, load_chat_model

def qa_agnet(uploaded_file, question, memory):
    # 加载模型
    model, tokenizer = load_chat_model(r"D:\AI_models\Qwen2.5-0.5B-Instruct")
    embeddings_model = load_embedding_model("Qwen3-Embedding-0.6B")
    # 先保存上传的文件，再加载
    os.makedirs("cache", exist_ok=True)

    file_content = uploaded_file.read()
    file_path = os.path.join("cache", "temp.pdf")
    with open(file_path, "wb") as f:
        f.write(file_content)
    # 加载文档
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    # split
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", "。", "！", "？" , "，", "、", ""]
    )
    split_docs = text_splitter.split_documents(docs)
    # embedding

    # vectorstore
    db = FAISS.from_documents(split_docs, embeddings_model)
    retriever = db.as_retriever()

    # chain
    qa = ConversationalRetrievalChain.from_llm(
        llm=model,
        retriever=retriever,
        memory=memory
    )
    response = qa.invoke({"chat_history": memory, "question": question})
    return response
