from data_injection import final_vectorstore
from langchain.tools import tool
from models.chat_model import get_chat_model
from utils.prompts import rag_prompt

@tool
def get_metadata(query : str):
    docs = final_vectorstore.similarity_search(query,k = 5)
    meta_list = []

    for d in docs:
        meta_list.append(d.metadata)
        
    return meta_list


@tool
def get_final_response(query : str, meta_data : list):
    llm = get_chat_model()
    
    response = llm.invoke(rag_prompt())
    
    return response.content[0]['text']