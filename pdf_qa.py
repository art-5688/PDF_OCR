from langchain.chains.retrieval_qa import RetrievalQA
from langchain_community.llms import CTransformers

def create_qa_chain(retriever):
    llm = CTransformers(model="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF", model_type="llama")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa_chain