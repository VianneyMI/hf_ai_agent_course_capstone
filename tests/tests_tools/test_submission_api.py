"""Tests for the submission API."""

import pytest

from azrock.tools.submission_api import get_file_by_task_id


class TestGetFileByTaskId:
    """Tests for the get_file_by_task_id function."""

    TASK_ID_WITH_IMAGE = "cca530fc-4052-43b2-b130-b30968d8aa44"
    TASK_ID_WITH_AUDIO = "99c9cc74-fdc8-46c6-8f8d-3ce2d3bfeea3"
    TASK_ID_WITH_CODE = "f918266a-b3e0-4914-865d-4faa564f1aef"
    TASK_ID_WITH_SPREADSHEET = "7bd855d8-463d-4ed5-93ca-5fe35145f733"

    @pytest.mark.non_deterministic
    def test_get_image(self):
        """Test the get_image function."""

        assert False

    def test_get_audio(self):
        """Test the get_audio function."""

        assert False

    def test_get_code(self):
        """Test the get_code function."""

        assert False

    def test_get_spreadsheet(self):
        """Test the get_spreadsheet function."""

        assert False
