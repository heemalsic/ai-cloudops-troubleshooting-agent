from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def build_vector_db(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    db = FAISS.from_texts(chunks, embeddings)

    return db