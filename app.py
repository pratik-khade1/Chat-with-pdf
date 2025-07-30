import streamlit as st
from pdf_loader import extract_text_from_pdf
from vector_store import create_vector_store
from rag_chatbot import answer_query
from dotenv import load_dotenv
load_dotenv()

import os

# Set your OpenAI API key here (or load from env)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page settings
st.set_page_config(page_title="Chat with PDF", layout="centered")
st.title("📄 Chat with Your PDF")
st.markdown("Upload any PDF and ask questions about its content using GenAI!")

# PDF upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("📄 Extracting text from PDF..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        if not raw_text.strip():
            st.error("No readable text found in the PDF.")
        else:
            st.success("Text extracted successfully.")

            with st.spinner("🔍 Creating vector store..."):
                vector_store = create_vector_store(raw_text)
                st.success("Vector store created.")

            user_input = st.text_input("Ask a question about the document")

            if user_input:
                with st.spinner("🤖 Generating answer..."):
                    response = answer_query(vector_store, user_input)
                    st.markdown("### 💬 Answer:")
                    st.write(response)
