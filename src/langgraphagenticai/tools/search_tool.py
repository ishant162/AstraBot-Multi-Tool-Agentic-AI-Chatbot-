from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Get the tools available for the chatbot.
    This function initializes a search tool using TavilySearchResults
    and returns it as a list of tools.
    """
    tools = [TavilySearch(max_results=2)]
    return tools


def create_tool_node(tools):
    """
    Create a tool node for the graph.
    This function initializes a ToolNode with the provided tools
    and returns it.
    """
    return ToolNode(tools=tools)
