"""`azrock.agent`

Module defining the Azrock Agent.
"""

import os

import litellm
from smolagents import CodeAgent, FinalAnswerTool, LiteLLMModel
from azrock.tools.file_reading import (
    read_spreadsheet_tool,
    read_image_tool,
    read_audio_tool,
)
from azrock.tools.youtube import (
    youtube_search_tool,
    get_audio_tool,
    get_summary_tool,
    get_text_tool,
)
from dotenv import load_dotenv


AGENT_NAME = "Azrock"
DEFAULT_PLANNING_INTERVAL = 5
DEFAULT_AZROCK_TEMPERATURE = 0

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

litellm.drop_params = True  # 👈 KEY CHANGE


def setup():
    """Setup the environment."""

    load_dotenv()


def is_dev_environment():
    """Check if the environment is a development environment."""

    return os.getenv("ENVIRONMENT") == "development"


def is_debug_environment():
    """Check if the environment is a debug environment."""

    return os.getenv("ENVIRONMENT") == "debug"


def get_llm(temperature: float = DEFAULT_AZROCK_TEMPERATURE):
    """Get the LLM."""

    setup()
    if is_dev_environment():
        model_id = "gemini/gemini-2.5-flash-preview-04-17"
    elif is_debug_environment():
        model_id = "anthropic/claude-3-5-sonnet-latest"
    else:
        # model_id = "anthropic/claude-3-5-sonnet-latest"
        model_id = "openai/o4-mini"

    return LiteLLMModel(
        model_id=model_id,
        temperature=temperature,
    )


def create_agent(temperature: float = DEFAULT_AZROCK_TEMPERATURE):
    """Creates the Azrock Agent."""

    llm = get_llm(temperature=temperature)

    final_answer_tool = FinalAnswerTool()

    agent = CodeAgent(
        model=llm,
        name=AGENT_NAME,
        description=DESCRIPTION,
        planning_interval=DEFAULT_PLANNING_INTERVAL,
        tools=[
            final_answer_tool,
            read_spreadsheet_tool,
            read_image_tool,
            read_audio_tool,
            youtube_search_tool,
            get_audio_tool,
            get_summary_tool,
            get_text_tool,
        ],
        add_base_tools=True,
    )

    return agent
