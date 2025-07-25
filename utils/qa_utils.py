import os
# from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from utils.model_utils import load_embedding_model, load_chat_model, apply_chat_template
from langsmith import traceable

"""
这是一个RAG应用，我认为，并不需要多轮对话的记忆。因为它实际上是一个搜索引擎，就算有记忆，还是会不断检索，而且token长度增长很快
。
"""

def generate_rag_message(context, question, tokenizer, enable_thinking=False):
    system_message = {
        "role": "system", "content": f"""使用以下上下文片段来回答用户的问题。
如果你不知道答案，就直接说不知道，不要试图编造答案。\n----------------\n{context}"""}
    message = [system_message, {"role": "user", "content": question}]
    return apply_chat_template(message, tokenizer, enable_thinking)

@traceable
def qa_agnet(uploaded_file, question, chunk_size=500, k=2):  # k表示检索的文档数量
    # 加载模型
    model, tokenizer = load_chat_model(r"D:\AI_models\Qwen2.5-0.5B-Instruct")
    embeddings_model = load_embedding_model("Qwen3-Embedding-0.6B")
    # 保存上传的文档
    os.makedirs("cache", exist_ok=True)
    file_content = uploaded_file.read()
    file_path = os.path.join("cache", "temp.pdf")
    with open(file_path, "wb") as f:
        f.write(file_content)

    # 1. 加载文档
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    # 2. split
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=50,
        separators=["\n\n", "\n", "。", "！", "？" , "，", "、", ""]
    )
    split_docs = text_splitter.split_documents(docs)
    # 3. vectorstore
    db = FAISS.from_documents(split_docs, embeddings_model)
    retriever = db.as_retriever()
    # 4. 执行检索
    retrieved_docs = (retriever.invoke(question))[:k] # 选择前k条结果
    print(f"检索结果:{retrieved_docs}")
    # 5. 生成消息
    context = "\n".join([doc.page_content for doc in retrieved_docs])
    message = generate_rag_message(context, question, tokenizer)
    response = model.invoke(message)
    return response.content
