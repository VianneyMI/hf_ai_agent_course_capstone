"""Test the Litellm model."""

from smolagents import LiteLLMModel
from azrock.agent import setup


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


def test_litellm_with_google():
    """Test the Litellm model with Google."""

    setup()
    model_id = "gemini/gemini-2.5-flash-preview-04-17"
    llm = LiteLLMModel(model_id=model_id)
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
