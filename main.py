from datetime import date
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from agents.search_agent import SearchAgent
from agents.creation_agent import CreationAgent
from agents.validation_agent import ValidationAgent
from agents.base_agent import AgentState

load_dotenv()

# Initializing Tavily. adjust max_results to reduce tokens used
tavily_tool = TavilySearchResults(max_results=5, search_depth="advanced")

# Initializing the OpenAI model
model = ChatOpenAI(model="gpt-4o")

# Initializing the agents
search_agent = SearchAgent(model, [tavily_tool])
creation_agent = CreationAgent(model)
validation_agent = ValidationAgent(model)

# Defining the work flow
workflow = StateGraph(AgentState)
workflow.add_node("search", search_agent.graph)
workflow.add_node("summarize", creation_agent.graph)
workflow.add_node("validate", validation_agent.graph)
workflow.add_edge("search", "summarize")
workflow.add_edge("summarize", "validate")


def should_continue(state: AgentState):
    coherence_message = state["messages"][-1].content.strip()
    return "summarize" if coherence_message == "0" else "__end__"


workflow.add_conditional_edges(
    "validate", should_continue, {"summarize": "summarize", "__end__": END}
)
workflow.set_entry_point("search")
compiled_workflow = workflow.compile()


# Function to run the workflow with the user's input
def run_workflow(user_input):
    initial_message = [HumanMessage(content=user_input)]
    state = {"messages": initial_message}
    workflow_result = compiled_workflow.invoke(state)
    return workflow_result


constant_input = f"Trending r/AITAH reddit stories {date.today()}"
result = run_workflow(constant_input)

print(result["messages"][-2].content)
