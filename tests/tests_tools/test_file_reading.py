"""Tests for `azrock.tools.file_reading` module."""

from PIL import Image
import numpy as np
import pandas as pd


from azrock.tools.submission_api import get_file_by_task_id
from azrock.tools.file_reading import read_image, read_audio, read_excel
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


def test_read_excel():
    """Test the `read_excel` function."""

    excel_bytes, _ = get_file_by_task_id(TASK_ID_WITH_SPREADSHEET)
    excel = read_excel(excel_bytes)
    assert isinstance(excel, pd.DataFrame)


def main():
    """Main function."""

    # test_read_image()
    # test_read_audio()
    test_read_excel()
    print("Done!")


if __name__ == "__main__":
    main()
