# Hybrid Search with Pinecone and LangChain

## Overview

This project demonstrates the implementation of a **Hybrid Search** system, which combines both dense vector search and traditional keyword-based (sparse) search to retrieve the most relevant results. This approach leverages the strengths of both search methods to improve the accuracy and relevance of search results, making it particularly useful in scenarios such as information retrieval and question-answering systems.

## What You Will Learn

### 1. Understanding Hybrid Search
- Hybrid Search is a search technique that combines dense vector search (embeddings capturing semantic meaning) with traditional keyword-based search (sparse search).
- It is designed to improve the precision and relevance of search results by integrating both semantic and keyword-based search methodologies.

### 2. Introduction to Pinecone
- Pinecone is a managed vector database optimized for similarity search and real-time analytics.
- Pinecone allows you to store and search high-dimensional vectors efficiently, supporting both dense vector and sparse search functionalities.

### 3. Implementing Dense Vector Search
- Utilized the `HuggingFaceEmbeddings` from Hugging Face to perform dense vector search.
- Dense vector search is based on semantic embeddings, which capture the underlying meaning of the text.

### 4. Implementing Sparse Search
- Implemented sparse search using `SpladeEncoder`, which uses techniques like TFIDF to capture the importance of individual keywords.
- Sparse search is more traditional, focusing on the exact match of terms.

### 5. Creating and Managing Pinecone Indexes
- Initialized a Pinecone client and created a vector index for hybrid search.
- Learned how to combine both dense and sparse search results using the `PineconeHybridSearchRetriever`.

## Steps to Reproduce

1. **Set Up the Environment**:
    - Install required Python packages.
    - Set up environment variables for API keys.
        - PINECONE_API_KEY
        - HUGGINGFACE_API_KEY
        
2. **Initialize Pinecone**:
    - Connect to Pinecone using the API key.
    - Create or access a vector index.

3. **Dense Vector Search**:
    - Import and configure the embedding model from Hugging Face.
    - Encode your corpus into dense vectors.

4. **Sparse Search**:
    - Import and configure the sparse encoder (SpladeEncoder).
    - Encode your corpus for keyword-based search.

5. **Hybrid Search Integration**:
    - Combine the results of dense and sparse searches using `PineconeHybridSearchRetriever`.

## Technologies Used
- **Pinecone**: For managing vector databases.
- **LangChain**: For integrating various components in the search pipeline.
- **Hugging Face**: For dense vector embeddings.
- **SpladeEncoder**: For sparse search encoding.

## Conclusion

This project provided hands-on experience with creating a robust hybrid search system by integrating Pinecone for vector management, LangChain for orchestration, and various embedding techniques for search optimization.
