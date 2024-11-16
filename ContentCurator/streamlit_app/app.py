from ContentCurator.flask_app.utils import get_data , process_data , lemmatize_text , llm_response
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# data = get_data('what is Ai?')
# print(f"Data Downlaoded from search engine : {len(data)}")

# proceesed_data = process_data(data)
# print(f"Data proceesd using nltk {len(proceesed_data)}")





# print(len(data[0]))
# print(len(proceesed_data[0]))


# print(llm_response(data[1],'What is Ai?'))



import streamlit as st
import requests

st.title("LLM-Based RAG System 🤖 -- ContentCurator")

st.text('''Project Description:

A web application designed to answer user queries by searching relevant content and generating responses using a language model (LLM).
It integrates a search engine for fetching data based on the user’s input and utilizes AI-driven processing to generate context-aware answers.
Effective Usage:

User Query Input: Users can submit questions through a simple API call.
Data Retrieval: The system efficiently searches articles and sources to gather relevant data.
AI Response Generation: The retrieved data is processed by an LLM to generate accurate and context-aware responses.
Scalable Integration: Can be easily integrated into various applications (e.g., chatbots, virtual assistants) for real-time query handling.


''')

query = st.text_input("Enter your query:")

if st.button("Submit"):
    with st.spinner("Fetching data and generating response..."):
        response = requests.post("http://localhost:5000/query", json={"query": query})
        print(response.status_code)
        if response.status_code == 200:
            result = response.json().get("response", "No response available")
            st.success("Generated Response:")
            st.write(result)
        else:
            st.error("Error occurred while fetching data.")