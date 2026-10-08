from langchain_community.embeddings import HuggingFaceEmbeddings
def create_embeddings(texts):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    text_embeddings = embeddings.embed_documents(texts)
    return text_embeddings