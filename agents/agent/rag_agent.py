from langchain.agents import create_agent
from models.chat_model import get_chat_model
from tools.rag_tools import get_metadata, get_final_response
from utils.prompts import rag_agent_prompt
from langchain.messages import AIMessage
from pydantic import BaseModel

class RagResponse(BaseModel):
    query : str
    root_cause : str
    resolution_notes : str

def get_rag_agent(state):
    
    agent = create_agent(
        name = 'RagAgent',
        model = get_chat_model(),
        tools = [get_metadata,get_final_response],
        system_prompt=rag_agent_prompt(),
        response_format=RagResponse
    )
    
    response = {}
        
    result = agent.invoke({'messages': {
            'role' : 'user',
            'content' : state['query']
        }
    })
    
    response['query'] = result['structured_response'].query
    response['root_cause'] = result['structured_response'].root_cause
    response['resoluation_notes'] = result['structured_response'].resolution_notes

    print(response)
    
    return {'rag_result' : response,'result' : [AIMessage(content=str(response))]}
    
    