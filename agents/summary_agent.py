from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from agents.base_agent import AgentState
import logging


logging.basicConfig(level=logging.DEBUG)


class SummarizationAgent:
    def __init__(self, model, tools, system=""):
        self.system = system
        self.tools = {tool.__class__.__name__: tool for tool in tools}
        graph = StateGraph(AgentState)
        graph.add_node("search", self.search_with_tavily)
        graph.add_node("summarize", self.summarize_tool)
        graph.add_edge("search", "summarize")
        graph.add_edge("summarize", END)
        graph.set_entry_point("search")
        self.graph = graph.compile()
        self.model = model

    def search_with_tavily(self, state: AgentState) -> dict:
        """Use Tavily to search for tech news."""
        messages = state["messages"]
        query = messages[-1].content
        logging.debug(f"Query received: {query}")

        tool = self.tools["TavilySearchResults"]
        results = tool.invoke({"query": query})
        logging.debug(f"Tavily search results: {results}")

        combined_responses = " ".join(result["content"] for result in results)
        tool_call_id = state.get("tool_call_id", "default_id")
        logging.debug(f"Combined Tavily responses: {combined_responses}")

        return {
            "messages": [
                ToolMessage(
                    tool_call_id=tool_call_id,
                    name="TavilySearchResults",
                    content=combined_responses,
                )
            ]
        }

    def summarize_tool(self, state: AgentState) -> dict:
        """Summarize the provided text using OpenAI."""
        messages = state["messages"]
        text_to_summarize = messages[-1].content
        logging.debug(f"Text to summarize: {text_to_summarize}")

        response = self.model.invoke(
            [HumanMessage(content=f"Summarize the following text: {text_to_summarize}")]
        )
        summary = response.content
        logging.debug(f"Summary: {summary}")

        return {"messages": [SystemMessage(content=summary)]}
