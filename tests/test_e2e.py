"""Test the end-to-end agent."""

from azrock.agent import create_agent

TASK = {
    "task_id": "9d191bce-651d-4746-be2d-7ef8ecadb9c2",
    "question": "Examine the video at https://www.youtube.com/watch?v=1htKBjuUWec.\n\nWhat does Teal'c say in response to the question \"Isn't that hot?\"",
    "Level": "1",
    "file_name": "",
}


def test_e2e():
    """Test the end-to-end agent."""

    agent = create_agent()
    result = agent.run(TASK["question"])
    print("-" * 20)
    print(result)
    print("-" * 20)
    assert "extremely" in result.lower(), result
    # assert False, result


if __name__ == "__main__":
    test_e2e()
