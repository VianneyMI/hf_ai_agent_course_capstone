"""Test the end-to-end agent."""

from azrock.agent import create_agent

TASK_1 = {
    "task_id": "9d191bce-651d-4746-be2d-7ef8ecadb9c2",
    "question": "Examine the video at https://www.youtube.com/watch?v=1htKBjuUWec.\n\nWhat does Teal'c say in response to the question \"Isn't that hot?\"",
    "Level": "1",
    "file_name": "",
}

TASK_2 = {
    "task_id": "f918266a-b3e0-4914-865d-4faa564f1aef",
    "question": "What is the final numeric output from the attached Python code?",
    "Level": "1",
    "file_name": "f918266a-b3e0-4914-865d-4faa564f1aef.py",
}


class TestE2E:
    """Tests the agent on sample questions."""

    def test_with_task_1(self):
        """Checks that the agent can solve the first task.

        In this task, the agents needs to be able to read a video transcript and answer a question about it.
        """

        agent = create_agent()
        result = agent.run(str(TASK_1))
        print("-" * 20)
        print(result)
        print("-" * 20)
        assert "extremely" in result.lower(), result

        assert result == "extremely" or result == "Extremely", result

    def test_with_task_2(self):
        """Checks that the agent can solve the second task.

        In this task, the agent needs to be able to read a Python code and answer a question about it.
        """

        agent = create_agent()
        result = agent.run(str(TASK_2))
        print("-" * 20)
        print(result)
        print("-" * 20)
        assert result in [0, "0"], result


if __name__ == "__main__":
    TestE2E().test_with_task_1()
    TestE2E().test_with_task_2()
