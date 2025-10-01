import os
from typing import List
from dotenv import load_dotenv
from langchain.tools import tool
from src.utils.weather_info import WeatherForecastTool
from src.logger import logger
from src.exception import CustomException


class WeatherInfoTool:
    """
    Wrapper class to expose weather-related tools (current weather and forecast)
    as LangChain-compatible tools using OpenWeatherMap API.
    """

    def __init__(self):
        """
        Initialize the WeatherInfoTool with API key from environment variables.
        """
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")

        if not self.api_key:
            logger.error("OPENWEATHERMAP_API_KEY not found in environment variables.")
            raise CustomException("Missing API key for OpenWeatherMap.")

        logger.info("Initializing WeatherInfoTool with OpenWeatherMap API.")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup all weather-related tools.

        Returns:
            List: A list of LangChain tool functions.
        """

        @tool
        def get_current_weather(city: str) -> str:
            """
            Get the current weather for a city.

            Args:
                city (str): Name of the city.

            Returns:
                str: Weather summary (temperature and description).
            """
            try:
                logger.info(f"Fetching current weather for: {city}")
                weather_data = self.weather_service.get_current_weather(city)

                if weather_data:
                    temp = weather_data.get("main", {}).get("temp", "N/A")
                    desc = (
                        weather_data.get("weather", [{}])[0].get("description", "N/A")
                    )
                    result = f"Current weather in {city}: {temp}°C, {desc}"
                    logger.info(f"✅ Current weather fetched successfully for {city}")
                    return result

                logger.warning(f"❌ Could not fetch current weather for {city}")
                return f"Could not fetch weather for {city}"

            except Exception as e:
                logger.exception(f"Error in get_current_weather tool for {city}")
                raise CustomException(f"Weather tool error: {e}")

        @tool
        def get_weather_forecast(city: str) -> str:
            """
            Get the weather forecast for a city.

            Args:
                city (str): Name of the city.

            Returns:
                str: Multi-day weather forecast summary.
            """
            try:
                logger.info(f"Fetching forecast weather for: {city}")
                forecast_data = self.weather_service.get_forecast_weather(city)

                if forecast_data and "list" in forecast_data:
                    forecast_summary = []
                    for item in forecast_data["list"]:
                        date = item.get("dt_txt", "").split(" ")[0]
                        temp = item.get("main", {}).get("temp", "N/A")
                        desc = (
                            item.get("weather", [{}])[0].get("description", "N/A")
                        )
                        forecast_summary.append(f"{date}: {temp}°C, {desc}")

                    result = f"Weather forecast for {city}:\n" + "\n".join(
                        forecast_summary
                    )
                    logger.info(f"✅ Forecast weather fetched successfully for {city}")
                    return result

                logger.warning(f"❌ Could not fetch forecast weather for {city}")
                return f"Could not fetch forecast for {city}"

            except Exception as e:
                logger.exception(f"Error in get_weather_forecast tool for {city}")
                raise CustomException(f"Forecast tool error: {e}")

        return [get_current_weather, get_weather_forecast]
