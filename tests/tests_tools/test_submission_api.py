"""Tests for the submission API."""

import pytest

from azrock.tools.submission_api import get_file_by_task_id


# NOTE: To generalize, the agents might need to be able to work with other type of files like video, PDF, zip, web pages (html code).
class TestGetFileByTaskId:
    """Tests for the get_file_by_task_id function."""

    task_id_with_image = "cca530fc-4052-43b2-b130-b30968d8aa44"
    task_id_with_audio = "99c9cc74-fdc8-46c6-8f8d-3ce2d3bfeea3"
    task_id_with_code = "f918266a-b3e0-4914-865d-4faa564f1aef"
    task_id_with_spreadsheet = "7bd855d8-463d-4ed5-93ca-5fe35145f733"

    def test_get_image(self):
        """Tests `get_file_by_task_id` when fetching an image."""

        content, filename = get_file_by_task_id(self.task_id_with_image)
        assert isinstance(content, bytes)
        assert isinstance(filename, str)
        assert filename == f"{self.task_id_with_image}.png"

    def test_get_audio(self):
        """Test the get_audio function."""

        content, filename = get_file_by_task_id(self.task_id_with_audio)
        assert isinstance(content, bytes)
        assert isinstance(filename, str)
        assert filename == f"{self.task_id_with_audio}.mp3"

    def test_get_code(self):
        """Test the get_code function."""

        content, filename = get_file_by_task_id(self.task_id_with_code)
        assert isinstance(content, bytes)
        assert isinstance(filename, str)
        assert filename == f"{self.task_id_with_code}.py"

    def test_get_spreadsheet(self):
        """Test the get_spreadsheet function."""

        content, filename = get_file_by_task_id(self.task_id_with_spreadsheet)
        assert isinstance(content, bytes)
        assert isinstance(filename, str)
        assert filename == f"{self.task_id_with_spreadsheet}.xlsx"
