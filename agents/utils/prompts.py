def rag_prompt(query : str, metadata : list):
    rag_response_prompt = f""" 
    You are response generation assisstant for user question using the rag metadata.

    your task is to generate the root cause and resoluation notes for the user question using the metadata chunks of resoluation notes and root cause

    user question : {query}
    metadata : {metadata}

    """
    return rag_response_prompt

def rag_agent_prompt():
    
    return f"""
    You are a RAG Agent you have access to two tools.
    
    1. get_metadata : this tool is to retrive the matching chunks in the form of metadata in the list format.
    2. get_final_response : this tool is to generate the final response using the list of metadata chunks.
    
    So, based on the user question generate the response using this tools
    
    First you need to call get_metadata and retrive the result and send it to get_final_response tool and generate the final response.

"""


def sql_generation_prompt(query:str):
    

    
    prompt = f""" You are sql specialist used to generate sql query for sqlite database for the user query {query}.
    
    columns in my table are 
    {{id : defines employee id,
    gender : defines gender (male/female),
    bdate : date of birth ,
    educ : education years,
    jobcat : which category of job he/she belongs,
    prevexp : previous years of experience,
    salary : salary of that person,
    salbegin : slaray which he started ,
    jobtime : time of the job, 
    minority : yes / no}}
    
    final result need to be only plain sql query.
    """
    
    return prompt


def supervisor_prompt(query):
    prompt = f"""
    You are supervisor agent your work is rout to particular agents.
    
    You have access to 2 agents:
    
    SqlAgent : User asks for employee related information.
    RagAgent : User asks for issues related details or resoluation notes or root cause.
    
    based on the user question just return 'sql' if it sql agent related question, return 'rag' if it is rag related query.
    
    User question : {query}
    """
    return prompt
