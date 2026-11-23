from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_embedding_model():
    
    model = GoogleGenerativeAIEmbeddings(
        api_key = GEMINI_API_KEY,
        model = "gemini-embedding-001"
    )
    
    return model