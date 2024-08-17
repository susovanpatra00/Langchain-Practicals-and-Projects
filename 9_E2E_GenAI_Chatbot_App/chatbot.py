import os
from dotenv import load_dotenv
import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Loading environment variables from my .env file
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")        # Set the API key for LangChain from the environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"                             # Enable LangChain tracing for monitoring and debugging
os.environ["LANGCHAIN_PROJECT"] = "Enhanced Q&A Chatbot With Ollama"    # Set the LangChain project name for organized tracing


# Chat Prompt template with system and user messages
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)


# Response from LLM function
def generate_response(question, llm_model, temperature, max_tokens):
    """
    Generate a response from the LLM based on the user's question.

    Args:
        question (str): The user's question.
        llm_model (str): The name of the LLM model to use.
        temperature (float): Sampling temperature for response variability.
        max_tokens (int): Maximum number of tokens in the response.

    Returns:
        str: The generated response from the LLM.
    """

    # OllamaLLM with the specified model, temperature, and max tokens 
    llm = OllamaLLM(model=llm_model, temperature=temperature, max_tokens=max_tokens)
    
    # Output Parser to process the LLM's output
    output_parser = StrOutputParser()
    
    # Processing chain that passes the prompt to the LLM and then parses the output
    chain = prompt | llm | output_parser            # This is called LCEL (Langchain Expression Language)

    # Response by invoking the chain with the user's question
    response = chain.invoke({'question': question})
    return response


# Streamlit App 
st.title("Enhanced Q&A Chatbot With Ollama Models")
llm_model = st.sidebar.selectbox(
        label="Select Open Source model", 
        options=["gemma2:2b", "mistral"]
    )
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


st.write("Go ahead and ask any question:")
user_input = st.text_input("You:")


if user_input:
    response = generate_response(user_input, llm_model, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide a question to get started.")
