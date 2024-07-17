from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage
from agents.base_agent import AgentState

# import logging


# logging.basicConfig(level=logging.DEBUG)


# The purpose of this agent is to create a new r/AITAH story
class CreationAgent:
    def __init__(self, model, system=""):
        self.system = system
        graph = StateGraph(AgentState)
        graph.add_node("create", self.creation_tool)
        graph.add_edge("create", END)
        graph.set_entry_point("create")
        self.graph = graph.compile()
        self.model = model

    def creation_tool(self, state: AgentState) -> dict:
        """Create a new r/AITAH reddit story based on the provided text using OpenAI."""
        messages = state["messages"]
        text_to_create = messages[-1].content
        # logging.debug(f"Text to summarize: {text_to_summarize}")

        response = self.model.invoke(
            [
                HumanMessage(
                    content=f"""
                    Based on these make a new trending r/AITAH story.
                    Follow similar formats and length.
                    Do not return it with any markdown:
                    {text_to_create}"""
                )
            ]
        )
        creation = response.content
        # logging.debug(f"creation: {creation}")

        return {"messages": [SystemMessage(content=creation)]}
