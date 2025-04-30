"""Tests for the submission API."""

import pytest

from azrock.tools.submission_api import get_file_by_task_id
from tests.tests_tools.conftest_ import (
    TASK_ID_WITH_IMAGE,
    TASK_ID_WITH_AUDIO,
    TASK_ID_WITH_CODE,
    TASK_ID_WITH_SPREADSHEET,
)


# NOTE: To generalize, the agents might need to be able to work with other type of files like video, PDF, zip, web pages (html code).
class TestGetFileByTaskId:
    """Tests for the get_file_by_task_id function."""

    task_id_with_image = TASK_ID_WITH_IMAGE
    task_id_with_audio = TASK_ID_WITH_AUDIO
    task_id_with_code = TASK_ID_WITH_CODE
    task_id_with_spreadsheet = TASK_ID_WITH_SPREADSHEET

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
