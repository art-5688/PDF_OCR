# PDF OCR & Question Answering System

## Project Overview

This project processes PDF documents and enables users to extract text, generate embeddings, retrieve relevant document content, and perform question answering using a Retrieval-Augmented Generation (RAG) approach.

It is designed to work with PDF documents where information needs to be extracted, processed, indexed, and retrieved efficiently for question answering.

## Key Features

- PDF document loading and text extraction
- OCR-based text extraction from PDF documents
- Document splitting into smaller chunks
- Text embedding generation
- Vector-based document retrieval
- Retrieval-Augmented Question Answering
- Modular Python implementation

## Project Workflow

```text
PDF Document
     ↓
PDF Loading / OCR
     ↓
Text Extraction
     ↓
Document Splitting
     ↓
Text Embeddings
     ↓
Vector Store
     ↓
Retriever
     ↓
Relevant Context
     ↓
Question Answering
```

## Technologies Used

- Python
- PDF processing
- OCR
- LangChain
- Text Embeddings
- Vector Search
- Retrieval-Augmented Generation (RAG)

## Project Structure

```text
PDF_OCR/
│
├── OCR_on_PDF.py
├── main.py
├── pdf_embeddings.py
├── pdf_loader.py
├── pdf_qa.py
├── pdf_splitter.py
├── pdf_vector_strore.py
├── retriever.py
├── .gitignore
└── README.md
```

## Setup

Clone the repository:

```bash
git clone https://github.com/art-5688/PDF_OCR.git
```

Navigate to the project:

```bash
cd PDF_OCR
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the main application using:

```bash
python main.py
```

Depending on the selected workflow, the individual Python modules can also be executed for PDF loading, splitting, embedding, retrieval, and question answering.

## Learning Outcomes

This project demonstrates practical implementation of:

- Document processing pipelines
- OCR integration
- Text chunking
- Embedding generation
- Vector similarity search
- Information retrieval
- RAG-based question answering
- Modular Python application development

## Future Improvements

- Add a web interface using Streamlit
- Add support for multiple documents
- Improve OCR accuracy for scanned PDFs
- Add metadata-based filtering
- Add advanced reranking
- Add evaluation metrics for retrieval and generated answers
- Containerize the application using Docker

## Author

**Aishwarya Teke**

GitHub: https://github.com/art-5688