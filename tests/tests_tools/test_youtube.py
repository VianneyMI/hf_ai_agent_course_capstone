from smolagents import Tool

from azrock.tools.youtube import (
    youtube_search_tool,
    get_audio_tool,
    get_summary_tool,
    get_text_tool,
)


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
