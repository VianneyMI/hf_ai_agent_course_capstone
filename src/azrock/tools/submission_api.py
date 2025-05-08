"""`azrock.tools.submission_api` module.
Contains tools for interacting with the submission API used by the Azrock AI agent.

"""

import requests
from smolagents import tool
from pydantic import BaseModel


BASE_URL = "https://agents-course-unit4-scoring.hf.space"


class Answer(BaseModel):
    """An answer to a task.

    Attributes:
    -----------------------
        task_id: str
            The ID of the task
        submitted_answer: str
            The answer submitted by the agent
    """

    task_id: str
    submitted_answer: str


class SubmitRequest(BaseModel):
    """A request to submit answers to the submission API.

    Attributes:
    -----------------------
        username: str
            Hugging Face username
        agent_code: str
            The Python class code for the agent
        answers: list[Answer]
            List of answers submitted by the agent
    """

    username: str
    agent_code: str
    answers: list[Answer]


class SubmitResponse(BaseModel):
    """A response from the submission API.

    Attributes:
    -----------------------
        username: str
            Hugging Face username
        score: float
            The score of the agent
        correct_count: int
            The number of correct answers
        total_attempted: int
    """

    username: str
    score: float
    correct_count: int
    total_attempted: int
    message: str
    timestamp: str


# API integration
# ------------------------------------------------------------------------------
def get_file_by_task_id(task_id: str) -> tuple[bytes, str]:
    """Downloads a file from a task id.

    Retrieves a file from the submission API by using the id (`task_id`) of the task requiring that file.

    Args:
        task_id: str
            The ID of the task to get the file for.

    Returns:
        tuple[bytes, str]: A tuple containing the file content as bytes and the filename
    """

    url = f"{BASE_URL}/files/{task_id}"
    response = requests.get(url)

    # Extract filename from Content-Disposition header
    content_disposition = response.headers.get("Content-Disposition", "")
    filename = ""
    if "filename=" in content_disposition:
        filename = content_disposition.split("filename=")[1].strip('"')

    return response.content, filename


def submit_answers(body: SubmitRequest) -> SubmitResponse:
    """Submit answers to the submission API.

    Args:
        body: SubmitRequest
            The body of the request to submit the answers.

    Returns:
        SubmitResponse: The response from the submission API.
    """

    url = f"{BASE_URL}/submit"
    response = requests.post(url, json=body)
    return SubmitResponse(**response.json())


# Toolification
# ------------------------------------------------------------------------------
get_file_by_task_id_tool = tool(get_file_by_task_id)
submit_answers_tool = tool(submit_answers)
