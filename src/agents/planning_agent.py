from langgraph.graph import MessagesState
from langchain_openai import ChatOpenAI

def query_or_respond(state: MessagesState, llm: ChatOpenAI, retrieval_tool: function):
    """Respond or generate a tool call for retrieval"""
    llm_with_tools = llm.bind_tools([retrieval_tool])
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}