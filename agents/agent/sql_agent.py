from langchain.agents import create_agent
from models.chat_model import get_chat_model
from tools.sql_tools import get_sql_query, get_sql_result
from pydantic import BaseModel
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.types import Command

class SQLResponse(BaseModel):
    query : str
    sql_query : str
    result : list
    
    
def sql_agent(query: str):
    
    middleware = HumanInTheLoopMiddleware(
        HumanInTheLoopMiddleware(
                interrupt_on={
                    "query_result": {
                        "allowed_decisions": ["approve", "reject"]
                    }
                },
                interrupt_mode="batched"
            )
    )
    
    agent = create_agent(
        name = "SqlAgent",
        model = get_chat_model(),
        tools = [get_sql_query, get_sql_result],
        middleware = [middleware],
        response_format = SQLResponse
    )
    
    messages = {
        'role' : 'user',
        'content' : query
    }
    
    while result.get("__interrupt__"):

        print("\n---------- Approval is required -----------")

        decisions = {}
        
        thread = {
            'configuration' : {
                'config' : 'sql_123'
            }
        }

        for interrupt in result.get("__interrupt__"):

            # Each interrupt has its own ID
            interrupt_id = interrupt.id

            # Per-call provides tool details directly
            action_required = interrupt.value

            
            while True:
                decision = input(
                    "Enter your decision: "
                ).strip().lower()

                if decision in ["approve", "reject"]:
                    break

                print("Invalid decision! Try again.")


            # Approve or Reject
            if decision in ["approve", "reject"]:
                resume_value = {
                    "type": decision
                }

            # Store decision using interrupt ID
            decisions[interrupt_id] = resume_value

            # Resume agent with decisions mapped to interrupt IDs
            result = agent.invoke(
                Command(resume=decisions),
                config=thread
            )

    
    response = agent.invoke({'messages' : messages})
    
    result = {
        'query' : response['structured_response'].query,
        'sql_query' : response['structured_response'].sql_query,
        'result' : response['structured_response'].result
    }
    
    return result