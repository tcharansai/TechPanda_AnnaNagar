from models.chat_model import get_chat_model
from utils.prompts import supervisor_prompt


def supervisor(query : str):
    llm = get_chat_model()
    prompt = supervisor_prompt(query)

    
    result = llm.invoke(prompt)
    
    return result