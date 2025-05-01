from smolagents import Tool

from azrock.tools.youtube import youtube_search_tool


def test_youtube_search_tool():
    """Test the youtube search tool."""

    assert isinstance(youtube_search_tool, Tool), youtube_search_tool
