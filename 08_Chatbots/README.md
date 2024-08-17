# Conversational RAG Chatbot with LangChain

This project implements a Conversational Retrieval-Augmented Generation (RAG) chatbot using LangChain. The chatbot can answer questions based on a specific web article while maintaining conversation history across multiple sessions.

## Key Components

1. **Data Ingestion**: Web scraping using WebBaseLoader
2. **Text Processing**: Chunking text with RecursiveCharacterTextSplitter
3. **Embedding**: Using OllamaEmbeddings with the "gemma2:2b" model
4. **Vector Store**: Chroma for storing and retrieving document embeddings
5. **Language Model**: ChatGroq with the "Llama3-8b-8192" model
6. **Retrieval Chain**: History-aware retriever for context-based question answering
7. **Conversation Management**: Session-based chat history storage

## Implementation Steps

1. Load and process web content
2. Create text chunks and generate embeddings
3. Store embeddings in a Chroma vector database
4. Set up a retriever for the vector store
5. Initialize the language model (LLM)
6. Create contextualized prompts for question reformulation
7. Implement a question-answering chain
8. Develop a history-aware retriever
9. Combine components into a full conversational RAG chain
10. Implement session-based conversation history management

## Key Features

- Web scraping and processing of specific HTML elements
- Chunking of long texts for better processing
- Use of embeddings for semantic search
- Context-aware question reformulation
- Maintenance of conversation history across multiple chat sessions
- Integration of retrieval and generation for more informed responses

## Usage

The notebook demonstrates how to use the conversational RAG chain with different session IDs, allowing for multiple concurrent conversations while maintaining separate histories for each.

Example usage:
```python
result = conversational_rag_chain.invoke(
    {"input": "What is Task Decomposition?"},
    config={"configurable": {"session_id": "abc123"}}
)
print(result["answer"])
```

## Learnings

- Implementation of a full RAG pipeline using LangChain
- Handling of conversation context and history in chatbots
- Integration of various LLM components (embedding, retrieval, generation)
- Session management for multi-user chatbot scenarios
- Use of prompt engineering for context-aware question reformulation
