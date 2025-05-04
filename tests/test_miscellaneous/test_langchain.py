from langchain_google_genai import ChatGoogleGenerativeAI
import pytest
from smolagents import CodeAgent


def test_simple_task():
    """Test the simple task."""

    question = """What is the capital of France?
    Answer with a single word.
    """
    expected_answer = "Paris"

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
    )
    result = llm.invoke(question)
    assert result.content == expected_answer


def test_compatibility_with_smolagents():
    """Test the compatibility with Smolagents.

    Langchain is NOT compatible with smolagents
    """

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
    )
    agent = CodeAgent(
        model=llm,
        tools=[],
        add_base_tools=True,
    )

    result = agent.run("What is the capital of France?")
    assert "Error" in result


if __name__ == "__main__":
    test_simple_task()
