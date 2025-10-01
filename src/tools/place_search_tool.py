import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from langchain.tools import tool
from src.utils.place_search import TavilyPlaceSearchTool

# Load environment variables
load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _normalize_result(self, source: str, category: str, place: str, result: Any, error: str = None) -> Dict:
        """
        Normalize result into a clean JSON structure.
        """
        return {
            "source": source,
            "category": category,
            "place": place,
            "error": error,
            "results": result if result else []
        }

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""

        @tool
        def search_attractions(place: str) -> Dict:
            """Search attractions of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return self._normalize_result("tavily", "attractions", place, tavily_result)
            except Exception as e:
                return self._normalize_result("tavily", "attractions", place, [], str(e))

        @tool
        def search_restaurants(place: str) -> Dict:
            """Search restaurants of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return self._normalize_result("tavily", "restaurants", place, tavily_result)
            except Exception as e:
                return self._normalize_result("tavily", "restaurants", place, [], str(e))

        @tool
        def search_activities(place: str) -> Dict:
            """Search activities of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return self._normalize_result("tavily", "activities", place, tavily_result)
            except Exception as e:
                return self._normalize_result("tavily", "activities", place, [], str(e))

        @tool
        def search_transportation(place: str) -> Dict:
            """Search transportation of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return self._normalize_result("tavily", "transportation", place, tavily_result)
            except Exception as e:
                return self._normalize_result("tavily", "transportation", place, [], str(e))
        
        @tool
        def search_hotels(place: str) -> dict:
            """Search hotels in a place"""
            try:
                result = self.tavily_search.tavily_search_hotels(place)
                return self._normalize_result("tavily", "hotels", place, result)
            except Exception as e:
                return self._normalize_result("tavily", "hotels", place, None, str(e))


        return [search_attractions, search_restaurants, search_activities, search_transportation, search_hotels]
