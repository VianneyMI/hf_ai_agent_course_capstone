"""Youtube tools."""

from smolagents import Tool
from langchain_community.tools import YouTubeSearchTool
# from langchain_community.agent_toolkits.load_tools import load_tools


youtube_search_tool = Tool.from_langchain(YouTubeSearchTool())
