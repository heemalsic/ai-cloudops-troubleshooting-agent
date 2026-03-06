from fastapi import FastAPI
from tools import read_logs, analyze_metrics
from rag import build_vector_db
from agent import run_agent

app = FastAPI()

db = build_vector_db("docs/gcp_docs.txt")


@app.get("/")
def home():
    return {"message": "Gemini CloudOps AI Agent Running"}


@app.get("/ask")
def ask_agent(question: str, project_id: str):

    logs = read_logs(project_id)

    metrics = analyze_metrics()

    docs = db.similarity_search(question, k=3)

    docs_text = "\n".join([d.page_content for d in docs])

    diagnosis = run_agent(question, logs, metrics, docs_text)

    return {
        "question": question,
        "analysis": diagnosis
    }