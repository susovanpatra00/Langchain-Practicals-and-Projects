# LangChain Practicals & Projects 

This repository contains a series of practical exercises I completed to deepen my understanding of various concepts related to data ingestion, transformation, embedding, and vector stores. These exercises are not part of a project but are instead meant for learning purposes only.

## 1. Data Ingestion

In this section, I explored different methods for loading and ingesting data. These methods include:

- **TextLoader**: Used for loading plain text files.
- **PyPDFLoader**: Utilized for ingesting data from PDF documents.
- **WebBaseLoader**: Applied for scraping and loading data from websites.
- **ArxivLoader**: Specialized for loading research papers from the Arxiv repository.
- **WikipediaLoader**: Used for fetching and loading data from Wikipedia articles.



## 2. Data Transformation

This section covers techniques for transforming and processing the ingested data, preparing it for embedding and further analysis. Key transformations include:

- **RecursiveCharacterTextSplitter**
- **CharacterTextSplitter**
- **HTMLTextSplitter**
- **RecursiveJsonSplitter**


## 3. Embedding

Here, I experimented with different models to convert text data into embeddings (vector representations). The models used include:

- **OpenAI Embeddings**
- **Ollama Embedding**
- **HuggingFace Embedding**

## 4. Vector Stores

This section is focused on storing and querying embeddings using vector databases. I used the following techniques:

- **FAISS**: A library for efficient similarity search.
- **Chroma**: A high-performance vector store.


## Dependencies

The dependencies used in this repository are listed in:
- `requirements.txt`
- `requirements_detail.txt` (with version details)
