import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load environment variables from a .env file
load_dotenv()

# Set Hugging Face API key from environment variables
os.environ['HUGGINGFACE_API_KEY'] = os.getenv("HUGGINGFACE_API_KEY")

# Initialize Hugging Face embeddings model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Set up Streamlit app
st.title("Conversational RAG With PDF Uploads and Chat History")
st.write("Upload PDFs and chat with their content")

# Input field for the Groq API Key
api_key = st.text_input("Enter your Groq API Key:", type="password")

# Check if the Groq API key is provided
if api_key:
    # Initialize the LLM (Language Model) using Groq's API
    llm = ChatGroq(groq_api_key=api_key, model_name="Gemma2-9b-It")

    # Input field for the session ID (used to manage chat history)
    session_id = st.text_input("Session ID", value="default_session")

    # Initialize session state to store chat history if not already present
    if 'store' not in st.session_state:
        st.session_state.store = {}

    # File uploader for selecting multiple PDF files
    uploaded_files = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=True)

    # Process uploaded PDFs
    if uploaded_files:
        documents = []

        # Save each uploaded PDF temporarily and load its content
        for uploaded_file in uploaded_files:
            temppdf = f"./temp.pdf"
            with open(temppdf, "wb") as file:
                file.write(uploaded_file.getvalue())
                file_name = uploaded_file.name

            # Load the PDF content using PyPDFLoader
            loader = PyPDFLoader(temppdf)
            docs = loader.load()
            documents.extend(docs)

        # Split the documents into smaller chunks and create embeddings
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
        splits = text_splitter.split_documents(documents)
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
        retriever = vectorstore.as_retriever()

        # System prompt for contextualizing user questions based on chat history
        contextualize_q_system_prompt = (
            """
                Given a chat history and the latest user's question,
                which may reference earlier context in the conversation,
                rephrase the question into a standalone query that can be
                understood independently of the prior chat history. Do NOT
                provide an answer to the question; instead, focus solely on 
                rephrasing it as necessary. If no rephrasing is required, 
                return the original question.
            """
        )

        # Create a chat prompt template for contextualizing questions
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # Create a history-aware retriever using the LLM and the contextualization prompt
        history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

        # System prompt for answering questions based on retrieved context
        system_prompt = (
            """
                You are an assistant designed for question-answering tasks.
                Utilize the provided context to respond to the question.
                If the answer is not clear from the context, indicate that you don't know.
                Limit your response to three sentences and keep it concise.
                {context}
            """
        )

        # Create a chat prompt template for question answering
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        # Create a document chain for answering questions
        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

        # Create a retrieval-based chain for handling questions with context
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        # Function to retrieve the chat history for a session
        def get_session_history(session: str) -> BaseChatMessageHistory:
            if session_id not in st.session_state.store:
                st.session_state.store[session_id] = ChatMessageHistory()
            return st.session_state.store[session_id]

        # Wrap the RAG chain with message history management
        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain, get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )

        # Input field for the user's question
        user_input = st.text_input("Your question:")
        if user_input:
            # Retrieve the chat history for the session
            session_history = get_session_history(session_id)
            
            # Invoke the conversational RAG chain with the user's input
            response = conversational_rag_chain.invoke(
                {"input": user_input},
                config={
                    "configurable": {"session_id": session_id}
                },
            )
            
            # Display the current state, assistant's response, and chat history
            st.write(st.session_state.store)
            st.write("Assistant:", response['answer'])
            st.write("Chat History:", session_history.messages)
else:
    # Display a warning if the Groq API key is not provided
    st.warning("Please enter the Groq API Key")
