from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage
from agents.base_agent import AgentState


class SummarizationAgent:
    def __init__(self, model, system=""):
        self.system = system
        graph = StateGraph(AgentState)
        graph.add_node("summarize", self.summarize_tool)
        graph.add_edge("summarize", END)
        graph.set_entry_point("summarize")
        self.graph = graph.compile()
        self.model = model

    def summarize_tool(self, state: AgentState) -> dict:
        """Summarize the provided text using OpenAI."""
        messages = state["messages"]
        text_to_summarize = messages[-1].content
        response = self.model.invoke(
            [HumanMessage(content=f"Summarize the following text: {text_to_summarize}")]
        )
        summary = response.content
        return {"messages": [SystemMessage(content=summary)]}
