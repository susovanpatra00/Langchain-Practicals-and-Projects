from langchain_community.document_loaders import GithubFileLoader               # For loading files from GitHub
from langchain_core.prompts import ChatPromptTemplate                           # For creating prompt templates
from langchain.chains.combine_documents import create_stuff_documents_chain     # For combining documents into a chain
from langchain_groq import ChatGroq                                             # Groq LLM integration
from langchain_core.documents.base import Document                              # Document class to handle content
import os                                                                       # For handling environment variables
from dotenv import load_dotenv                                                  # For loading environment variables from a .env file
load_dotenv()

# GitHub API key and Groq API key from .env
ACCESS_TOKEN = os.getenv('GITHUB_API_KEY')
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# GitHub file loader 
loader = GithubFileLoader(
    repo="susovanpatra00/Langchain-Practicals-and-Projects",    # Repository name
    access_token=ACCESS_TOKEN,                                  # GitHub access token
    github_api_url="https://api.github.com",                    # GitHub API URL
    branch='main',                                              # Branch to load files from
    file_filter=lambda file_path: file_path.endswith(".md"),    # Filter for markdown files only
)

documents = loader.load()
contents = [doc.page_content for doc in documents[:-1]]   # Skipping the last document as it was previous README.md for the repository


llm = ChatGroq(model="llama-3.1-70b-versatile", api_key=GROQ_API_KEY)   # Using Llama3-70b from Groq

# Prompt For README.md Generator
prompt = ChatPromptTemplate.from_template(
    """
    You are a GitHub README generator. Based on the following README contents 
    from various projects and learning activities "I have done by myself", create a 
    comprehensive, detailed (at least 2000 words) and attractive super README for the entire 
    repository. Summarize the contents of each folder, highlight the key learnings or 
    accomplishments, and provide an overview of the repository. And do mention that I
    have explored all these yself. The sections should be:
    **Overview**
    **Projects and Learning Activities**
    **Key Learnings and Accomplishments**
    **Additional Resources**
    **Conclusion**
    In Additional Resources give link to all the links given in other README along with give 
    some more relevant links.
    <context>
    {context}
    <context>
    """
)


combined_content = "\n\n\n\n\n".join(contents)
combined_document = Document(page_content=combined_content)     # Creating Document as can not give normal string to LLM 

document_chain = create_stuff_documents_chain(llm, prompt)
response = document_chain.invoke({'context': [combined_document]})


# Save the generated README to the main README.md file
readme_path = "/Users/susovanpatra/Langchain-Practicals-and-Projects/README.md"
with open(readme_path, "w") as readme_file:
    readme_file.write(response)

print(f"Super README has been successfully saved to {readme_path}")