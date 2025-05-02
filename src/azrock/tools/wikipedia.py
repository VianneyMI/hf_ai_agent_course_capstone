"""`azrock.tools.wikipedia` module.

Defines tools to interact with Wikipedia.
"""

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from smolagents import Tool, tool


# Langchain Adapter
# -----------------------------------------
class WikipediaSummaryTool(WikipediaQueryRun):
    """Tool that searches the Wikipedia API."""

    name: str = "wikipedia_summary"
    description: str = """Use this tool to get the summary of a Wikipedia page.
    Useful for when you need to answer general questions about 
    people, places, companies, facts, historical events, or other subjects. 
    Input should be a search query.
    """


class WikipediaPageTool(WikipediaQueryRun):
    """Tool that searches the Wikipedia API."""

    name: str = "wikipedia_page"
    description: str = """Use this tool to get the page of a Wikipedia page.
    Useful for when you need to answer general questions in greater detail.
    """

    def _run(
        self,
        query: str,
        run_manager: CallbackManagerForToolRun | None = None,
    ) -> str:
        """Use the Wikipedia tool."""

        documents = self.api_wrapper.load(query)
        if len(documents) > 0:
            return documents[0].page_content
        else:
            return "No results found"


# Wikipedia API
# -----------------------------------------
def get_wikipedia_summary(query: str) -> str:
    """Get the Wikipedia page for a given query.

    Args:
        query: str
            The query to search Wikipedia for.

    Returns:
        str
            The Wikipedia page for the given query returned as a string.
    """

    wikipedia_api_wrapper = WikipediaAPIWrapper()  # type: ignore[call-arg]
    wikipedia_runner = WikipediaSummaryTool(api_wrapper=wikipedia_api_wrapper)
    return wikipedia_runner.run(query)


def get_wikipedia_page(query: str) -> str:
    """Get the Wikipedia page for a given query.

    Args:
        query: str
            The query to search Wikipedia for.

    Returns:
        str
            The Wikipedia page for the given query returned as a string.
    """

    wikipedia_api_wrapper = WikipediaAPIWrapper(doc_content_chars_max=100_000)  # type: ignore[call-arg]
    wikipedia_runner = WikipediaPageTool(api_wrapper=wikipedia_api_wrapper)
    return wikipedia_runner.run(query)


# Toolification
# -----------------------------------------
wikipedia_summary_tool = tool(get_wikipedia_summary)
wikipedia_page_tool = tool(get_wikipedia_page)
