from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

# from langchain_core.messages import HumanMessage
# from agents.summary_agent import SummarizationAgent
# from agents.validation_agent import ValidationAgent

load_dotenv()

# Tavily tool set up
tavily_tool = TavilySearchResults(max_results=5, search_depth="advanced")

# Initialize the OpenAI model
model = ChatOpenAI(model="gpt-4o")
