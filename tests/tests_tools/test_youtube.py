import pytest
from smolagents import Tool
import whisper
from transformers.pipelines import Pipeline
from azrock.tools.youtube import (
    youtube_search_tool,
    get_audio_tool,
    get_summary_tool,
    get_text_tool,
    get_model,
    get_summarizer,
    get_audio,
    get_text,
    get_summary,
    PATH_TO_DOWNLOADS,
)


def test_path_to_downloads():
    """Test the path to downloads."""

    assert PATH_TO_DOWNLOADS.exists(), PATH_TO_DOWNLOADS


def test_youtube_search_tool():
    """Test the youtube search tool."""

    assert isinstance(youtube_search_tool, Tool), youtube_search_tool


def test_get_audio_tool():
    """Test the get audio tool."""

    assert isinstance(get_audio_tool, Tool), get_audio_tool


def test_get_text_tool():
    """Test the get text tool."""

    assert isinstance(get_text_tool, Tool), get_text_tool


def test_get_summary_tool():
    """Test the get summary tool."""

    assert isinstance(get_summary_tool, Tool), get_summary_tool


def test_get_model():
    """Test the get model function."""

    assert isinstance(get_model(), whisper.Whisper), get_model()


def test_get_summarizer():
    """Test the get summarizer function."""

    assert isinstance(get_summarizer(), Pipeline), get_summarizer()


def test_get_audio():
    """Test the get audio function."""

    url = "https://www.youtube.com/watch?v=1htKBjuUWec"
    assert isinstance(get_audio(url), str), get_audio(url)


@pytest.mark.xfail(reason="Feature is buggy")
def test_get_text():
    """Test the get text function."""

    url = "https://www.youtube.com/watch?v=1htKBjuUWec"
    assert isinstance(get_text(url), str), get_text(url)


@pytest.mark.xfail(reason="Feature is buggy")
def test_get_summary():
    """Test the get summary function."""

    url = "https://www.youtube.com/watch?v=1htKBjuUWec"
    assert isinstance(get_summary(url), str), get_summary(url)


def main():
    """Main function."""

    test_path_to_downloads()
    test_youtube_search_tool()
    test_get_audio_tool()
    test_get_text_tool()
    test_get_summary_tool()
    test_get_model()
    test_get_summarizer()
    test_get_audio()
    test_get_text()
    test_get_summary()


if __name__ == "__main__":
    main()
