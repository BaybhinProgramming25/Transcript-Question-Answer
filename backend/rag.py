import os
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


DATA_DIR = "data"
_embeddings: OpenAIEmbeddings | None = None


def get_embeddings(openai_api_key: str) -> OpenAIEmbeddings:
    global _embeddings
    if _embeddings is None:
        _embeddings = OpenAIEmbeddings(api_key=openai_api_key, model="text-embedding-3-small")
    return _embeddings


_index_cache: dict[str, FAISS] = {}


def init_db(chunks: list[tuple[str, dict]], index_key: str, openai_api_key: str):
    """Embed chunks and save a FAISS index for the given document."""

    os.makedirs(DATA_DIR, exist_ok=True)
    index_path = os.path.join(DATA_DIR, f"faiss_index_{index_key}")

    if os.path.exists(index_path):
        print(f"[cache hit] Index for {index_key} already exists, skipping")
        return

    docs = [Document(page_content=chunk, metadata=metadata) for chunk, metadata in chunks]

    print(f"[embedding] Embedding {len(docs)} chunks for {index_key}...")
    vector_store = FAISS.from_documents(docs, get_embeddings(openai_api_key))

    print(f"[saving] Writing FAISS index to {index_path}")
    vector_store.save_local(index_path)
    del vector_store
    print(f"[saved] Done")


def load_db(index_key: str, openai_api_key: str) -> FAISS:
    """Load a FAISS index for the given document, caching it in memory."""

    if index_key not in _index_cache:
        index_path = os.path.join(DATA_DIR, f"faiss_index_{index_key}")
        _index_cache[index_key] = FAISS.load_local(index_path, get_embeddings(openai_api_key), allow_dangerous_deserialization=True)
        print(f"[cache miss] Loaded index for {index_key} from disk")
    else:
        print(f"[cache hit] Index for {index_key} already in memory")

    return _index_cache[index_key]


def delete_index(index_key: str):
    """Remove a FAISS index from disk and evict it from the in-memory cache."""

    index_path = os.path.join(DATA_DIR, f"faiss_index_{index_key}")
    if os.path.exists(index_path):
        import shutil
        shutil.rmtree(index_path)
        print(f"[deleted] Removed FAISS index at {index_path}")

    _index_cache.pop(index_key, None)


def query(question: str, index_key: str, openai_api_key: str) -> str:
    """Retrieve relevant chunks and answer the question using the LLM."""

    vector_store = load_db(index_key, openai_api_key)
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    prompt = PromptTemplate.from_template("""
You are a helpful assistant that answers questions about a student's academic transcript. \
Use only the context provided to answer. Answer directly as if you were talking to a real student. \
Start with the answer and only add relevant details if necessary \
If the answer is not in the context, say you don't know.

Context:
{context}

Question: {question}

Answer:""")

    llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini", temperature=0)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke(question)
