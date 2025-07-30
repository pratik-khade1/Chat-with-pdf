from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

import os

def create_vector_store(text):
    # Split the text into smaller chunks for efficient embedding and search
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    texts = text_splitter.split_text(text)

    # Initialize OpenAI Embeddings
    embeddings = OpenAIEmbeddings()

    # Create a FAISS vector store from the text chunks
    vector_store = FAISS.from_texts(texts, embedding=embeddings)

    return vector_store
