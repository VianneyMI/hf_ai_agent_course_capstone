"""Test the agent."""

import pytest
from smolagents import CodeAgent

from azrock.agent import create_agent, setup


def test_create_agent():
    """Test the creation of the agent."""

    agent = create_agent()
    assert isinstance(agent, CodeAgent)


class TestAgent:
    """Test the agent."""

    @pytest.mark.non_deterministic
    def test_simple_task(self):
        """Test the creation of the agent."""

        agent = create_agent()
        result = agent.run("What is the capital of France?")
        assert result == "Paris", f"Expected 'Paris', got {result}"


def main():
    """Main function."""

    test_create_agent()
    print("Testing the Agent")
    test_agent = TestAgent()
    test_agent.test_simple_task()


if __name__ == "__main__":
    main()
