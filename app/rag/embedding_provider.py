from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    ),
    api_key=os.getenv(
        "AZURE_OPENAI_KEY"
    ),
    azure_deployment=os.getenv(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
    ),
    openai_api_version="2024-02-01"
)