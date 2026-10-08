from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

# if __name__ == "__main__":
#     file_path = "Colab.pdf"            # Replace with your PDF file path
#     documents = load_pdf(file_path)       
#     for doc in documents:
#         print(doc.page_content)
