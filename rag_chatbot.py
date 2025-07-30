from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def answer_query(vector_store, query):
    # Search for relevant document chunks using the user’s query
    docs = vector_store.similarity_search(query)

    # Load a simple QA chain using OpenAI's LLM
    llm = OpenAI(temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff")

    # Run the chain to generate an answer using context from FAISS
    response = chain.run(input_documents=docs, question=query)

    return response
