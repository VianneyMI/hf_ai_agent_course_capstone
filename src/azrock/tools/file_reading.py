"""`azrock.tools.file_reading` contains functions for reading files."""

from io import BytesIO
from typing import Any
import tempfile
from PIL import Image
import soundfile as sf
import numpy as np
import pandas as pd
from smolagents import tool, Tool

IMAGE_FORMATS = [
    "jpeg",
    "jpg",
    "png",
    "gif",
    "bmp",
]


# File reading API
# ------------------------------------------------------------------------------
def read_image(image_bytes: bytes) -> Image.Image:
    """Reads an image from bytes.

    Args:
        image_bytes: bytes
            The bytes of the image to read.

    Returns:
        Image.Image: The image data as a PIL Image object.
    """

    img = Image.open(BytesIO(image_bytes))
    img.verify()  # Verify that the image is valid
    img = Image.open(BytesIO(image_bytes))  # Reopen for further operations
    assert img.format and img.format.lower() in IMAGE_FORMATS

    return Image.open(BytesIO(image_bytes))


def read_audio(audio_bytes: bytes) -> tuple[np.ndarray, int]:
    """Reads an audio from bytes.

    Args:
        audio_bytes: bytes
            The bytes of the audio to read.

    Returns:
        tuple[np.ndarray, int]: A tuple containing:
            - The audio data as a numpy array
            - The sample rate of the audio
    """
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file.write(audio_bytes)
        temp_file.flush()
        data, samplerate = sf.read(temp_file.name)

    return data, samplerate


def read_spreadsheet(
    file_bytes: bytes,
    file_type: str = "excel",
    sheet_name: int | str | list[str | int] | None = 0,
) -> dict[str, pd.DataFrame]:
    """Reads spreadsheet data from bytes, supporting multiple formats and sheets.

    This function can read Excel files (xlsx, xls), CSV files, and Google Sheets.
    For Excel files with multiple sheets, it can return either a single sheet or
    a dictionary of all sheets.

    Args:
        file_bytes: bytes
            The bytes of the spreadsheet file to read.
        file_type: str, optional
            The type of spreadsheet file. One of: "excel", "csv", "google_sheets".
            Defaults to "excel".
        sheet_name: int | str | list[str | int] | None, optional
            For Excel files: Name of sheet(s) to read. If None, reads all sheets.
            For CSV files: Ignored.
            For Google Sheets: Sheet ID or name to read.
            Defaults to 0.

    Returns:
        pd.DataFrame | dict[str, pd.DataFrame]:
            - For single sheet requests: Returns a single DataFrame
            - For multiple sheets: Returns a dictionary mapping sheet names to DataFrames

    Examples:
        >>> # Read a single sheet from Excel
        >>> df = read_spreadsheet(excel_bytes, sheet_name="Sheet1")

        >>> # Read all sheets from Excel
        >>> sheets = read_spreadsheet(excel_bytes)
        >>> sheet1_df = sheets["Sheet1"]

        >>> # Read a CSV file
        >>> df = read_spreadsheet(csv_bytes, file_type="csv")

        >>> # Read specific sheets from Excel
        >>> sheets = read_spreadsheet(excel_bytes, sheet_name=["Sheet1", "Sheet2"])
    """
    if file_type == "csv":
        return pd.read_csv(BytesIO(file_bytes))
    elif file_type == "google_sheets":
        # For Google Sheets, we'd need to implement the Google Sheets API integration
        # This is a placeholder for future implementation
        raise NotImplementedError("Google Sheets support is not yet implemented")
    else:  # excel
        return pd.read_excel(BytesIO(file_bytes), sheet_name=sheet_name)


# Toolification
# ------------------------------------------------------------------------------
read_image_tool = tool(read_image)
read_audio_tool = tool(read_audio)
# read_spreadsheet_tool = tool(read_spreadsheet)


class ReadSpreadsheetTool(Tool):
    """Reads a spreadsheet from bytes."""

    name = read_spreadsheet.__name__
    description = read_spreadsheet.__doc__
    inputs = {
        "file_bytes": {
            "type": "object",
            "description": "The bytes of the spreadsheet file to read.",
        },
        "file_type": {
            "type": "string",
            "description": "The type of the spreadsheet file either 'excel', 'csv', or 'google_sheets'.",
            "nullable": True,
        },
        "sheet_name": {
            "type": "object",
            "description": "The name of the sheet to read from the spreadsheet. Can either be a string, a list of strings, or None. If None, reads all sheets.",
            "nullable": True,
        },
    }
    output_type = "object"

    def forward(
        self,
        file_bytes: bytes,
        file_type: str = "excel",
        sheet_name: str | list[str] | None = None,
    ) -> Any:
        return read_spreadsheet(file_bytes, file_type, sheet_name)


read_spreadsheet_tool = ReadSpreadsheetTool()
