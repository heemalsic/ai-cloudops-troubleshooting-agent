# import streamlit as st
# import requests

# st.title("CloudOps AI Troubleshooter")

# question = st.text_input("Ask a question about your cloud system")

# if st.button("Diagnose"):

#     response = requests.get(
#         "http://127.0.0.1:8000/ask",
#         params={"question": question}
#     )

#     result = response.json()

#     st.subheader("Diagnosis")
#     st.write(result["analysis"])

# import streamlit as st
# import requests

# API_URL = "https://gemini-cloudops-agent-861080173298.us-central1.run.app/ask"
# # /docs#/default/ask_agent_ask_get

# st.title("AI CloudOps Troubleshooting Agent")

# question = st.text_input("Ask about a cloud issue")

# if st.button("Diagnose"):

#     response = requests.get(
#         API_URL,
#         params={"question": question}
#     )

#     if response.status_code == 200:
#         st.write(response.json())
#     else:
#         st.error("API request failed")

# import streamlit as st
# import requests

# API_URL = "https://gemini-cloudops-agent-861080173298.us-central1.run.app/ask"

# st.title("AI CloudOps Troubleshooting Agent")

# question = st.text_input("Ask about a cloud issue")

# if st.button("Diagnose"):

#     with st.spinner("Analyzing logs and metrics..."):

#         response = requests.get(
#             API_URL,
#             params={"question": question}
#         )

#         if response.status_code == 200:

#             data = response.json()

#             st.subheader("Question")
#             st.write(data["question"])

#             st.subheader("Diagnosis")
#             st.markdown(data["analysis"])

#         else:
#             st.error("API request failed")


import streamlit as st
import requests

API_URL = "https://gemini-cloudops-agent-861080173298.us-central1.run.app/ask"
# API_URL = "http://127.0.0.1:8000/ask"  # Local testing URL

st.title("AI CloudOps Troubleshooting Agent")

project_id = st.text_input("GCP Project ID")

question = st.text_input("Ask about a cloud issue")

if st.button("Diagnose"):

    with st.spinner("Analyzing logs and metrics..."):

        response = requests.get(
            API_URL,
            params={
                "question": question,
                "project_id": project_id
            }
        )

        if response.status_code == 200:

            data = response.json()

            st.subheader("Question")
            st.write(data["question"])

            st.subheader("Diagnosis")
            st.markdown(data["analysis"])

        else:
            st.error("API request failed")