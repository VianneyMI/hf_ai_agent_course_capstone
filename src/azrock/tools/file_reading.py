"""`azrock.tools.file_reading` contains functions for reading files."""

from io import BytesIO
import tempfile
from PIL import Image
import soundfile as sf
import numpy as np
import pandas as pd
from smolagents import tool

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


def read_excel(excel_bytes: bytes) -> pd.DataFrame:
    """Reads an excel file from bytes.

    Args:
        excel_bytes: bytes
            The bytes of the excel file to read.

    Returns:
        pd.DataFrame: The excel data as a pandas DataFrame.
    """

    return pd.read_excel(BytesIO(excel_bytes))


# Toolification
# ------------------------------------------------------------------------------
read_image_tool = tool(read_image)
read_audio_tool = tool(read_audio)
read_excel_tool = tool(read_excel)
