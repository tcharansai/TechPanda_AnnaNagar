from langgraph.graph import StateGraph,START,END
from agent.rag_agent import get_rag_agent
from agent.sql_agent import sql_agent
from agent.supervisor_agent import supervisor

class BotResponse(StateGraph):
    query : str
    agent : str
    rag_result : str
    sql_result : str
    
    
builder = StateGraph(BotResponse)

builder.add_node('sqlagent',sql_agent)
builder.add_node('ragagent',get_rag_agent)

builder.add_conditional_edges(
    START,
    supervisor,{
        'rag' : 'ragagent',
        'sql' : 'sqlagent'
    }
)

builder.add_edge('ragagent',END)
builder.add_edge('sqlagent',END)


app = builder.compile()

app.invoke(
    
)
