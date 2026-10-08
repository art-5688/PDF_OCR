from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
def create_vector_store(texts, collection_name="pdf_collection"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma.from_texts(texts, embeddings, collection_name=collection_name)
    return vector_store     
