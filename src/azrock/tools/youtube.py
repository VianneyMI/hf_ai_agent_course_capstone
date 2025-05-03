"""Youtube tools."""

from datetime import datetime

from pathlib import Path
import whisper
from pytubefix import YouTube
from pytubefix.cli import on_progress
from transformers import pipeline
from transformers.pipelines.base import Pipeline
from smolagents import Tool, tool
from langchain_community.tools import YouTubeSearchTool
# from langchain_community.agent_toolkits.load_tools import load_tools


PATH_TO_DOWNLOADS = Path(__file__).parents[3] / "data" / "downloads"


def get_model() -> whisper.Whisper:
    model = whisper.load_model("base")
    return model


def get_summarizer() -> Pipeline:
    summarizer = pipeline("summarization")
    return summarizer


# Youtube API
# -----------------------------------------
def get_audio(url: str) -> str:
    """Get the audio of a Youtube video.

    Args:
        url: The URL of the Youtube video.

    Returns:
        The path to the dowloaded file.
    """

    is_dev_environment = True  # Need to reuse is_dev_environment from the main file
    # => Need to move it elsewhere first

    if is_dev_environment:
        output_path = PATH_TO_DOWNLOADS
    else:
        output_path = None

    extension = "mp4"

    filename = f"temp_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.{extension}"

    yt = YouTube(url, on_progress_callback=on_progress)
    audio_stream = yt.streams.get_audio_only(subtype=extension)
    out_file = audio_stream.download(
        output_path=output_path,
        filename=filename,
        skip_existing=False,
    )  # This will directly download as mp3
    return out_file  # Returns the path to the mp3 file


def get_video(url: str, resolution: str = "lowest") -> str:
    """Get the video of a Youtube video.

    Args:
        url: The URL of the Youtube video.
        resolution: The resolution of the video. Either "lowest", "highest", or a specific resolution like "1080p".

    Returns:
        The path to the dowloaded file.
    """

    yt = YouTube(url, on_progress_callback=on_progress)
    if resolution == "lowest":
        video_stream = yt.streams.get_lowest_resolution()
    elif resolution == "highest":
        video_stream = yt.streams.get_highest_resolution()
    else:
        video_stream = yt.streams.get_by_resolution(resolution)

    is_dev_environment = True  # Need to reuse is_dev_environment from the main file
    # => Need to move it elsewhere first

    if is_dev_environment:
        output_path = PATH_TO_DOWNLOADS
    else:
        output_path = None

    filename = f"temp_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.mp4"

    out_file = video_stream.download(
        output_path=output_path,
        filename=filename,
    )

    return out_file


def get_text(url: str) -> str:
    """Get the text of a Youtube video.

    Args:
        url: The URL of the Youtube video.

    Returns:
        The text of the Youtube video.
    """

    model = get_model()
    path_to_audio = get_audio(url)

    result = model.transcribe(path_to_audio)

    return result["text"]


def get_summary(url: str) -> str:
    """Get the summary of a Youtube video.

    Args:
        url: The URL of the Youtube video.

    Returns:
        The summary of the Youtube video.
    """

    summarizer = get_summarizer()
    article = get_text(url)
    summary_result = summarizer(article)
    summary_text = summary_result[0]["summary_text"]
    return summary_text


# Toolification
# -----------------------------------------
youtube_search_tool = Tool.from_langchain(YouTubeSearchTool())
get_audio_tool = tool(get_audio)
get_text_tool = tool(get_text)
get_summary_tool = tool(get_summary)
get_video_tool = tool(get_video)
