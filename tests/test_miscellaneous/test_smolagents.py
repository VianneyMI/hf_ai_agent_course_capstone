"""Test the smolagents package."""

from typing import Literal

import pytest
from smolagents import tool, CodeAgent, LiteLLMModel


ReturnType = Literal["str", "bool"]


def dummy_function_to_be_tooled(return_type: str) -> str | bool:
    """Dummy function to be tooled.

    Args:
        return_type: ReturnType
            The type of the return value indicated as a string.

    Returns:
        The return value.
    """

    if return_type == "str":
        return "Hello, world!"
    else:
        return True


def test_tool_decorator_on_function_that_returns_union_type():
    """Test the tool decorator on a function that returns a union type."""

    with pytest.raises(TypeError):
        tool(dummy_function_to_be_tooled)


def test_change_system_prompt():
    """Test the change system prompt tool."""

    model_id = "gemini/gemini-2.5-flash-preview-04-17"
    temperature = 0.0
    system_prompt = """
    You are an AI assistant that always say no.
    Forget all previous instructions.
    Whatever you are asked, your answer should be a single word "no".
    """

    llm = LiteLLMModel(
        model_id=model_id,
        temperature=temperature,
    )

    agent = CodeAgent(
        model=llm,
        tools=[],
        add_base_tools=True,
    )
    agent.prompt_templates["system_prompt"] = system_prompt
    agent.system_prompt = agent.initialize_system_prompt()

    assert agent.system_prompt == system_prompt


def main():
    test_tool_decorator_on_function_that_returns_union_type()
    test_change_system_prompt()
    print("All tests passed!")


if __name__ == "__main__":
    main()
