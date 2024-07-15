import os
from dotenv import load_dotenv


def load_env():
    """Load environment variables from a .env file."""
    load_dotenv()


def get_openai_api_key():
    """Retrieve the OpenAI API key from environment variables."""
    return os.getenv("OPENAI_API_KEY")


def get_tavily_api_key():
    """Retrieve the Tavily API key from environment variables."""
    return os.getenv("TAVILY_API_KEY")
