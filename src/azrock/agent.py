"""`azrock.agent`

Module defining the Azrock Agent.
"""

import os

from smolagents import CodeAgent, FinalAnswerTool, LiteLLMModel
from azrock.tools.file_reading import (
    read_spreadsheet_tool,
    read_image_tool,
    read_audio_tool,
)
from dotenv import load_dotenv


AGENT_NAME = "Azrock"
PLANNING_INTERVAL = 5
AZROCK_TEMPERATURE = 0

DESCRIPTION = """
Azrock is an AI agent trained to perform well on the GAIA benchmark.
GAIA is a benchmark designed to evaluate AI assistants on real-world tasks that require a combination of core capabilities—such as reasoning, multimodal understanding, web browsing, and proficient tool use.

GAIA requires the following capabilities:

* Generating structured response format
* Multimodal reasoning
* Planning and sequential reasoning with memory
* Executing sequencing in the right order
* Web browsing
* Coding
* Diverse filetype reading

Azrock manages a set of other specialized AI agents to help him in his task of defeating the GAIA benchmark.


""".strip()


def setup():
    """Setup the environment."""

    load_dotenv()


def is_dev_environment():
    """Check if the environment is a development environment."""

    return os.getenv("ENVIRONMENT") == "development"


def get_llm():
    """Get the LLM."""

    setup()
    if is_dev_environment():
        model_id = "gemini-1.5-flash"
        provider = "google"
    else:
        # model_id = "anthropic/claude-3-5-sonnet-latest"
        model_id = "o4-mini"
        provider = "openai"

    return LiteLLMModel(
        model_id=model_id,
        provider=provider,
        temperature=AZROCK_TEMPERATURE,
    )


def create_agent():
    """Creates the Azrock Agent."""

    llm = get_llm()

    final_answer_tool = FinalAnswerTool()

    agent = CodeAgent(
        model=llm,
        name=AGENT_NAME,
        description=DESCRIPTION,
        planning_interval=PLANNING_INTERVAL,
        tools=[
            final_answer_tool,
            read_spreadsheet_tool,
            read_image_tool,
            read_audio_tool,
        ],
    )

    return agent
