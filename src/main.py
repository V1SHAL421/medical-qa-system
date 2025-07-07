from src.agents.planning_agent import query_or_respond
from src.agents.retrieval_agent import call_healthlake_api
from src.utils.setup_llm import setup_openai_llm
from langgraph.graph import MessagesState, StateGraph

llm = setup_openai_llm()
graph_builder = StateGraph(MessagesState)
graph_builder.add_node(query_or_respond(llm=llm, retrieval_tool=call_healthlake_api()))