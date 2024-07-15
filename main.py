import os
from datetime import date
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import openai
from tavily import TavilyClient

# from agents.summary_agent import SummarizationAgent
# from agents.validation_agent import CoherenceAgent
# from langchain_core.messages import HumanMessage
# from langgraph.graph import END, StateGraph, MessagesState
# from langgraph.checkpoint import MemorySaver


load_dotenv()

# OpenAI set up
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

model = ChatOpenAI(model="gpt-4o")

# Tavily set up
current_date = date.today()
tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily = TavilyClient(tavily_api_key)
response = tavily.search(
    f"What are the most important pieces of tech news as of {current_date}",
    max_results=5,
    search_depth="advanced",
)

responses = [response["content"] for response in response["results"]]

print(responses)
