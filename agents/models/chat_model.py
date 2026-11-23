from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_chat_model():
    
    model = ChatGoogleGenerativeAI(
        api_key = GEMINI_API_KEY,
        model = "gemini-3.5-flash-lite"
    )
    
    return model