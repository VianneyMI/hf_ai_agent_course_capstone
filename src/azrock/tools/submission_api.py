"""`azrock.tools.submission_api` module.
Contains tools for interacting with the submission API used by the Azrock AI agent.

"""

import requests
from smolagents import tool


BASE_URL = "https://agents-course-unit4-scoring.hf.space"


# API integration
# ------------------------------------------------------------------------------
def get_file_by_task_id(task_id: str) -> bytes:
    """Get a file by task ID."""

    url = f"{BASE_URL}/files/{task_id}"
    response = requests.get(url)
    return response.content


def submit_answers(body: dict) -> dict:
    """Submit answers to the submission API."""

    url = f"{BASE_URL}/submit"
    response = requests.post(url, json=body)
    return response.json()


# Toolification
# ------------------------------------------------------------------------------
get_file_by_task_id_tool = tool(get_file_by_task_id)
submit_answers_tool = tool(submit_answers)
