from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


prompt = PromptTemplate(
    input_variables=["logs", "metrics", "docs", "question"],
    template="""
You are an expert Google Cloud Site Reliability Engineer.

Analyze the following system information.

Logs:
{logs}

Metrics:
{metrics}

Relevant Documentation:
{docs}

User Question:
{question}

Provide:

1. Root Cause
2. Evidence
3. Recommended Fix

Be concise.
"""
)


def run_agent(question, logs, metrics, docs):

    chain = prompt | llm

    response = chain.invoke({
        "logs": logs,
        "metrics": metrics,
        "docs": docs,
        "question": question
    })

    return response.content