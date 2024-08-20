import os
from dotenv import load_dotenv
import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
    

prompt = ChatPromptTemplate.from_template(
    """
    You are an information extractor assistant. Your task is to accurately extract and 
    return specific two information from the given input. If there is any colour present in 
    the input. Then give me that information.
    <input>
    {input}
    <input>
    """
)




# Response from LLM function
def generate_response(question, llm_model):
    """
    Generate a response from the LLM based on the user's question.

    Args:
        question (str): The user's question.
        llm_model (str): The name of the LLM model to use.

    Returns:
        str: The generated response from the LLM.
    """

    llm = OllamaLLM(model=llm_model)
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser       

    # Response by invoking the chain with the user's question
    response = chain.invoke({'input': question})
    return response


# Streamlit App 
st.title("Enhanced Q&A Chatbot With Ollama Models")
llm_model = st.sidebar.selectbox(
        label="Select Open Source model", 
        options=["gemma2:2b", "mistral"]
    )


st.write("Go ahead and ask any question:")
user_input = st.text_input("You:")


if user_input:
    response = generate_response(user_input, llm_model)
    st.write(response)
else:
    st.write("Please provide a question to get started.")
