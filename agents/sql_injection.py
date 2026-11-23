from langchain.tools import tool
from models.chat_model import get_chat_model


def get_sql_query(query : str):
    llm = get_chat_model()
    
    prompt = ""
    
    llm.invoke(prompt)
