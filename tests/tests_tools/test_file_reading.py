"""Tests for `azrock.tools.file_reading` module."""

from PIL import Image
import numpy as np
import pandas as pd


from azrock.tools.submission_api import get_file_by_task_id
from azrock.tools.file_reading import read_image, read_audio, read_spreadsheet
from tests.tests_tools.conftest_ import (
    TASK_ID_WITH_IMAGE,
    TASK_ID_WITH_AUDIO,
    TASK_ID_WITH_SPREADSHEET,
)


def test_read_image():
    """Test the `read_image` function."""

    image_bytes, _ = get_file_by_task_id(TASK_ID_WITH_IMAGE)
    image = read_image(image_bytes)
    assert isinstance(image, Image.Image)


def test_read_audio():
    """Test the `read_audio` function."""

    audio_bytes, _ = get_file_by_task_id(TASK_ID_WITH_AUDIO)
    data, samplerate = read_audio(audio_bytes)
    assert isinstance(data, np.ndarray)
    assert isinstance(samplerate, int)
    assert samplerate > 0


class TestReadSpreadsheet:
    """Test the `read_spreadsheet` function."""

    def test_single_sheet_excel(self):
        """Test the `read_excel` function."""

        excel_bytes, _ = get_file_by_task_id(TASK_ID_WITH_SPREADSHEET)
        excel = read_spreadsheet(excel_bytes)
        assert isinstance(excel, pd.DataFrame)

    def test_csv(self):
        """Test the `read_csv` function."""

        assert False

    def test_multiple_sheets_excel(self):
        """Test the `read_excel` function with multiple sheets."""

        assert False

    def test_google_sheets(self):
        """Test the `read_google_sheets` function."""

        assert False


def main():
    """Main function."""

    # test_read_image()
    # test_read_audio()
    test_read_spreadsheet = TestReadSpreadsheet()
    test_read_spreadsheet.test_single_sheet_excel()
    test_read_spreadsheet.test_csv()
    test_read_spreadsheet.test_multiple_sheets_excel()
    test_read_spreadsheet.test_google_sheets()
    print("Done!")


if __name__ == "__main__":
    main()
