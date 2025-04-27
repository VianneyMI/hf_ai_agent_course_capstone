"""Test the Litellm model."""

from smolagents import LiteLLMModel


def test_litellm():
    """Test the Litellm model."""

    llm = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest")
    result = llm(
        [
            {
                "role": "user",
                "content": """what is the capital of France?
                
                Answer with a single word.
                """,
            }
        ],
    )
    assert result.content == "Paris"


def main():
    """Main function."""

    test_litellm()
    print("All tests passed.")


if __name__ == "__main__":
    main()
