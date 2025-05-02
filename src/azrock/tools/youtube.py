"""Youtube tools."""

import whisper
from pytubefix import YouTube
from pytubefix.cli import on_progress
from transformers import pipeline
from transformers.pipelines.base import Pipeline
from smolagents import Tool, tool
from langchain_community.tools import YouTubeSearchTool
# from langchain_community.agent_toolkits.load_tools import load_tools


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
        The path to the mp3 file downloaded.
    """

    yt = YouTube(url, on_progress_callback=on_progress)
    audio_stream = yt.streams.get_audio_only()
    out_file = audio_stream.download(mp3=True)  # This will directly download as mp3
    return out_file  # Returns the path to the mp3 file


def get_text(url: str) -> str:
    """Get the text of a Youtube video.

    Args:
        url: The URL of the Youtube video.

    Returns:
        The text of the Youtube video.
    """

    model = get_model()
    result = model.transcribe(get_audio(url))
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
