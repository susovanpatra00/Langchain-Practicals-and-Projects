from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

# Loading Required Environment variables
groq_api_key = os.getenv('GROQ_API_KEY')


# 1. Create Prompt template
system_template = "Translate the following text into {language} language"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])


## 2. Model Initialisation (Groq Model)
model = ChatGroq(model='gemma2-9b-it', api_key=groq_api_key)


## 3. Create String Output Parser
parser = StrOutputParser()

## 4. Create Chain
chain = prompt_template | model | parser


## 5. App Definition
app = FastAPI(
    title="Langchain Server",
    version='0.0',
    description="A Simple API server using Langchain",
)


## 6. Adding Chain Routes
add_routes(
    app=app,
    runnable=chain,
    path='/chain'
)


if __name__=='__main__':
    import uvicorn
    uvicorn.run(app)
