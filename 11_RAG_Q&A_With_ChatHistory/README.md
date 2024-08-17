# Conversational RAG with PDF Uploads and Chat History

This project is a web-based application that allows users to interactively chat with the content of uploaded PDF files. The application leverages LangChain, Groq, and Hugging Face embeddings to create a retrieval-augmented generation (RAG) system that provides contextual answers based on the content of the uploaded documents. The user can ask questions, and the system will retrieve relevant information from the PDFs and provide concise answers while maintaining a chat history.

## Features

- **PDF Upload**: Upload multiple PDF files to the application, which will be processed for content extraction.
- **Conversational Interface**: Ask questions related to the content of the PDFs, and receive answers that take into account the entire conversation history.
- **Chat History Management**: The system maintains chat history across multiple sessions, allowing for context-aware question answering.
- **Powered by Groq and Hugging Face**: Utilizes the Groq API for language model processing and Hugging Face for embedding generation.

## Prerequisites

- Python 3.10 or higher
- Pip package manager
- A Groq API Key
- A Hugging Face API Key


## Usage

1. **Run the Streamlit application:**

   ```bash
   streamlit run rag_app.py
   ```

2. **Upload PDFs:**

   Use the file uploader in the interface to select and upload one or more PDF files.

3. **Enter your Groq API Key:**

   Input your Groq API Key when prompted to enable the language model processing.

4. **Interact with the PDFs:**

   Ask questions related to the uploaded PDFs, and the system will provide concise, context-aware answers. The chat history will be preserved throughout the session.

5. **Session ID:**

    You can either change session ids or use the default one and you can also create different sessions.

## Project Structure

- `app.py`: The main application script that sets up the Streamlit interface and handles the conversational RAG logic.
- `requirements.txt`: A list of Python dependencies required to run the application.
- `.env`: Environment variables file for storing API keys (not included, create your own).

## Key Components

- **LangChain**: A library for building chains of language model calls and retrievers.
- **Groq API**: Provides access to a powerful language model for processing natural language queries.
- **Hugging Face Embeddings**: Generates embeddings for document retrieval, enabling context-aware question answering.
- **Streamlit**: A framework for creating interactive web applications directly from Python scripts.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request. I will be happy to apply it. Let's learn it together.
