from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage
from agents.base_agent import AgentState


class CoherenceAgent:
    def __init__(self, model, system=""):
        self.system = system
        graph = StateGraph(AgentState)
        graph.add_node("validate", self.validate_coherence)
        graph.add_edge("validate", END)
        graph.set_entry_point("validate")
        self.graph = graph.compile()
        self.model = model

    def validate_coherence(self, state: AgentState) -> dict:
        """Validate the coherence of the provided summary using OpenAI."""
        messages = state["messages"]
        summary_to_validate = messages[-1].content
        response = self.model.invoke(
            [
                HumanMessage(
                    content=(
                        "Is the following summary coherent? "
                        "Answer 1 for yes, 0 for no: "
                        f"{summary_to_validate}"
                    )
                )
            ]
        )
        coherence_result = response.content.strip()
        return {"messages": [SystemMessage(content=coherence_result)]}
