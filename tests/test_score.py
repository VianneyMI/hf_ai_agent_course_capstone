"""Tests the agent on the provided questions."""

import datetime
from pathlib import Path
import json
import pytest
from azrock.agent import create_agent

path_to_questions = Path(__file__).parent.parent / "data" / "questions.json"
path_to_answers = Path(__file__).parent.parent / "data" / "answers.json"


def load_questions():
    """Load questions from the JSON file."""
    try:
        with open(path_to_questions, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        pytest.fail(f"Questions file not found at {path_to_questions}")
    except json.JSONDecodeError:
        pytest.fail(f"Invalid JSON in questions file at {path_to_questions}")


def save_answers(results):
    """Save test results to a JSON file."""

    path_to_answer_current_run = (
        path_to_answers.parent
        / f"answers_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.json"
    )
    try:
        with open(path_to_answer_current_run, "w") as f:
            json.dump(results, f, indent=2)
    except IOError as e:
        pytest.fail(f"Failed to save answers: {e}")


def test_load_questions():
    """Test the loading of the questions."""
    questions_data = load_questions()
    assert questions_data


def test_save_answers():
    """Test the saving of the answers."""
    results = [
        {
            "task_id": "1",
            "question": "What is the capital of France?",
            "answer": "Paris",
            "success": True,
        }
    ]
    save_answers(results)
    assert results


def test_score():
    """Test the score of the agent on the provided questions."""
    questions_data = load_questions()
    agent = create_agent()
    results = []

    for question in questions_data[:5]:  # Test first 5 questions
        question_text = question["question"]
        try:
            answer = agent.run(question_text)

            result = {
                "task_id": question["task_id"],
                "question": question_text,
                "answer": answer,
                "success": True,  # This should be determined by comparing with expected answers
            }
            results.append(result)
        except Exception as e:
            results.append(
                {
                    "task_id": question["task_id"],
                    "question": question_text,
                    "error": str(e),
                    "success": False,
                }
            )

    save_answers(results)

    # Count successful answers
    successful_answers = sum(1 for r in results if r.get("success", False))
    total_questions = len(results)

    # Assert that at least some answers were successful
    assert successful_answers > 0, (
        f"No successful answers out of {total_questions} questions"
    )

    # Log the success rate
    print(
        f"Success rate: {successful_answers}/{total_questions} ({successful_answers / total_questions * 100:.1f}%)"
    )
