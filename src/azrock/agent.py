"""`azrock.agent`

Module defining the Azrock Agent.
"""

import os

from smolagents import CodeAgent, FinalAnswerTool
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

PLANNING_INTERVAL = 5


def setup():
    """Setup the environment."""

    load_dotenv()


def is_dev_environment():
    """Check if the environment is a development environment."""

    return os.getenv("ENVIRONMENT") == "development"


def get_llm():
    """Get the LLM."""

    if is_dev_environment():
        return ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    else:
        return ChatOpenAI(model="gpt-4o-mini", temperature=0)


def create_agent():
    """Creates the Azrock Agent."""

    llm = get_llm()

    final_answer_tool = FinalAnswerTool()

    agent = CodeAgent(
        model=llm,
        name="Azrock",
        description="A helpful assistant that can code, read, and write files.",
        planning_interval=PLANNING_INTERVAL,
        tools=[final_answer_tool],
    )

    return agent
