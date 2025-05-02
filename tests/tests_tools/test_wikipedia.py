from azrock.tools.wikipedia import get_wikipedia_page, get_wikipedia_summary


def test_get_wikipedia_summary():
    """Test the get Wikipedia page tool."""

    result = get_wikipedia_summary("Python (programming language)")
    assert isinstance(result, str), result

    checkpoints = [
        "Guido van Rossum",
    ]

    checks = []
    missing_checks = []

    for checkpoint in checkpoints:
        if checkpoint in result:
            checks.append(True)
        else:
            checks.append(False)
            missing_checks.append(checkpoint)

    assert all(checks), f"""The following {missing_checks} are missing.\n\n 
    Results preview:\n\t\t\t\t {result[:100]}"""


def test_get_wikipedia_page():
    """Test the get Wikipedia page tool."""

    result = get_wikipedia_page("Python (programming language)")
    assert isinstance(result, str), result

    checkpoints = [
        "Guido van Rossum",
        "Python Software Foundation",
        "PyCon",
        "Zen of Python",
    ]

    checks = []
    missing_checks = []

    for checkpoint in checkpoints:
        if checkpoint in result:
            checks.append(True)
        else:
            checks.append(False)
            missing_checks.append(checkpoint)

    assert all(checks), f"""The following {missing_checks} are missing.\n\n 
    Results preview:\n\t\t\t\t {result[:100]}"""
