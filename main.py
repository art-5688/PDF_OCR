from pdf_loader import load_pdf
from pdf_splitter import split_text
from pdf_embeddings import create_embeddings
from pdf_vector_strore import create_vector_store
from retriever import create_retriever
from pdf_qa import create_qa_chain
if __name__ == "__main__":
    file_path = "Colab.pdf"            # Replace with your PDF file path
    documents = load_pdf(file_path)       
    for doc in documents:
        print(doc.page_content)
        chunks = split_text(doc.page_content)
        for chunk in chunks:
            print(chunk)
    # Create embeddings for the chunks
    text_embeddings = create_embeddings([chunk for chunk in chunks])
    print(text_embeddings)
    # Create a vector store for the chunks   
    vector_store = create_vector_store(chunks)
    print("This is from vector store")
    print(vector_store)
    # Create a retriever for the vector store
    retriever = create_retriever(vector_store)  
    print("This is from retriever")
    print(retriever)
    # Create a QA chain using the retriever and a language model
    qa_chain = create_qa_chain(retriever)   
    print("This is from QA chain")
    print(qa_chain)
    print("QA chain ready. Ask a question, or type 'exit'.")
    while True:
        query = input("Q: ").strip()
        if query.lower() in ("exit", "quit", "q"):
            print("Bye.")
            break
        answer = qa_chain.run(query)
        print(f"A: {answer}")     

    


