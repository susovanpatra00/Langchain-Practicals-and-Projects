from langchain_community.document_loaders import GithubFileLoader
import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('GITHUB_API_KEY')

loader = GithubFileLoader(
    repo = "susovanpatra00/Langchain-Practicals-and-Projects",  
    access_token = ACCESS_TOKEN,
    github_api_url = "https://api.github.com",
    branch = 'main',
    file_filter = lambda file_path: file_path.endswith(
        ".md"
    ),  
)

documents = loader.load()
contents = [doc.page_content for doc in documents[:-1]]



