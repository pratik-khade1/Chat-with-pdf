# 🧠 Chat with Your PDF using LangChain & OpenAI

This project demonstrates a simple Retrieval-Augmented Generation (RAG) based chatbot that allows users to interact with the contents of a PDF using natural language. It leverages LangChain for orchestration, FAISS for vector storage, and OpenAI for language modeling — all wrapped in an interactive Streamlit UI.

---

## 📌 Features

- Upload any PDF and extract its text
- Embed PDF content using OpenAI Embeddings
- Store and search using FAISS vector database
- Ask questions and get context-aware answers
- Clean and user-friendly Streamlit interface

---

## ⚙️ Tech Stack

- **LangChain**
- **OpenAI API (gpt-3.5)**
- **FAISS**
- **Python**
- **Streamlit**

---

## 🏁 How to Run Locally

```bash
git clone https://github.com/your-username/chat-with-pdf.git
cd chat-with-pdf
pip install -r requirements.txt
streamlit run app.py
