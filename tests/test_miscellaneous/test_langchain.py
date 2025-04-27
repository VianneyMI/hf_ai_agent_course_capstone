from azrock.agent import get_llm


def test_simple_task():
    """Test the simple task."""

    question = """What is the capital of France?
    Answer with a single word.
    """
    expected_answer = "Paris"

    llm = get_llm()
    result = llm.invoke(question)
    assert result.content == expected_answer


if __name__ == "__main__":
    test_simple_task()
