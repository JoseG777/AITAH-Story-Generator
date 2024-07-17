from langgraph.graph import StateGraph, END
from langchain_core.messages import ToolMessage
from agents.base_agent import AgentState
import logging

logging.basicConfig(level=logging.DEBUG)


class SearchAgent:
    def __init__(self, model, tools, system=""):
        self.system = system
        self.tools = {tool.__class__.__name__: tool for tool in tools}
        self.model = model
        graph = StateGraph(AgentState)
        graph.add_node("search", self.search_with_tavily)
        graph.add_edge("search", END)
        graph.set_entry_point("search")
        self.graph = graph.compile()

    def search_with_tavily(self, state: AgentState) -> dict:
        """Use Tavily to search for tech news."""
        messages = state["messages"]
        query = messages[-1].content
        # logging.debug(f"Query received: {query}")

        tool = self.tools["TavilySearchResults"]
        results = tool.invoke({"query": query})

        # for response in results:
        # print(response["content"])
        combined_list = [response["content"] for response in results]
        combined_responses = "".join([str(item) for item in combined_list])
        tool_call_id = state.get("tool_call_id", "default_id")

        return {
            "messages": [
                ToolMessage(
                    tool_call_id=tool_call_id,
                    name="TavilySearchResults",
                    content=combined_responses,
                )
            ]
        }
