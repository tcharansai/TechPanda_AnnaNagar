from langchain.tools import tool
from utils.prompts import sql_generation_prompt
from models.chat_model import get_chat_model
import sqlite3

@tool
def get_sql_query(query : str):
    
    """This tool is used to generate sql query from the user query"""
    
    llm = get_chat_model()
    
    prompt = sql_generation_prompt(query)
    
    response = llm.invoke(prompt)
    
    return response.content[0]['text']


@tool
def get_sql_result(query:str):
    """This tool is used to execute sql query and get the result from the database"""
    
    database_path = "employee.db"
    data = sqlite3.connect(database_path)
    try:
        cursor = data.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
    