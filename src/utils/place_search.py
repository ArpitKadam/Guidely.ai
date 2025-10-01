import os
from langchain_tavily import TavilySearch
from src.logger import logger
from src.exception import CustomException
from dotenv import load_dotenv
load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

class TavilyPlaceSearchTool:
    """
    Wrapper around Tavily Search for retrieving attractions, restaurants,
    activities, and transportation options for a given place.
    """

    def __init__(self):
        """
        Initialize TavilyPlaceSearchTool.
        """
        logger.info("TavilyPlaceSearchTool initialized successfully.")

    def tavily_search_attractions(self, place: str) -> dict:
        """Search for top attractions in and around the place."""
        return self._run_query(f"top attractive places in and around {place}")

    def tavily_search_restaurants(self, place: str) -> dict:
        """Search for top 10 restaurants in and around the place."""
        return self._run_query(
            f"what are the top 10 restaurants and eateries in and around {place}."
        )

    def tavily_search_activity(self, place: str) -> dict:
        """Search for popular activities in and around the place."""
        return self._run_query(f"activities in and around {place}")

    def tavily_search_transportation(self, place: str) -> dict:
        """Search for available modes of transportation in the place."""
        return self._run_query(
            f"What are the different modes of transportations available in {place}"
        )

    def tavily_search_hotels(self, place: str) -> dict:
        """Search for hotels in the place."""
        return self._run_query(f"hotels in {place}")


    def _run_query(self, query: str) -> dict:
        """
        Execute a query using TavilySearch.
        """
        try:
            logger.info(f"Running TavilySearch query: {query}")
            tavily_tool = TavilySearch(topic="general", include_answer="advanced")
            result = tavily_tool.invoke({"query": query})

            if isinstance(result, dict) and result.get("answer"):
                return result["answer"]

            return result
        except Exception as e:
            logger.exception(f"TavilySearch query failed: {query}")
            raise CustomException(f"TavilySearch query error: {e}")
