from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from agents.base_agent import AgentState


class SummarizationAgent:
    def __init__(self, model, tools, system=""):
        self.system = system
        graph = StateGraph(AgentState)
        graph.add_node("search", self.search_with_tavily)
        graph.add_node("summarize", self.summarize_tool)
        graph.add_edge("summarize", "search")
        graph.add_edge("summarize", END)
        graph.set_entry_point("search")
        self.graph = graph.compile()
        self.model = model
        self.tools = tools

    def search_with_tavily(self, state: AgentState) -> dict:
        """Use Tavily to search for tech news."""
        messages = state["messages"]
        query = messages[-1].content
        tool = self.tools["tavily_search_results"]
        results = tool.invoke({"query": query})
        combined_responses = " ".join(result["content"] for result in results)
        return {"messages": [ToolMessage(content=combined_responses)]}

    def summarize_tool(self, state: AgentState) -> dict:
        """Summarize the provided text using OpenAI."""
        messages = state["messages"]
        text_to_summarize = messages[-1].content
        response = self.model.invoke(
            [HumanMessage(content=f"Summarize the following text: {text_to_summarize}")]
        )
        summary = response.content
        return {"messages": [SystemMessage(content=summary)]}
