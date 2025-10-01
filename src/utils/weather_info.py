import requests
from src.logger import logger
from src.exception import CustomException


class WeatherForecastTool:
    """
    A utility class for fetching current and forecast weather data
    using the OpenWeatherMap API.

    Example:
        weather_tool = WeatherForecastTool(api_key="YOUR_API_KEY")
        current = weather_tool.get_current_weather("Mumbai")
        forecast = weather_tool.get_forecast_weather("Delhi")
    """

    def __init__(self, api_key: str):
        """
        Initialize the WeatherForecastTool.

        Args:
            api_key (str): OpenWeatherMap API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
        logger.debug("WeatherForecastTool initialized with provided API key.")

    def get_current_weather(self, place: str) -> dict:
        """
        Fetch the current weather of a place.

        Args:
            place (str): City or location name.

        Returns:
            dict: Weather data if successful, otherwise empty dict.

        Raises:
            CustomException: If the API call fails.
        """
        try:
            url = f"{self.base_url}/weather"
            params = {"q": place, "appid": self.api_key, "units": "metric"}
            logger.info(f"Fetching current weather for: {place}")
            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                logger.info(f"✅ Current weather fetched successfully for {place}")
                return response.json()
            else:
                logger.error(
                    f"❌ Failed to fetch current weather for {place}. "
                    f"Status: {response.status_code}, Response: {response.text}"
                )
                return {}

        except requests.RequestException as e:
            logger.exception(f"❌ Network/API error while fetching current weather for {place}")
            raise CustomException(f"API request error: {e}")
        except Exception as e:
            logger.exception("❌ Unexpected error in get_current_weather")
            raise CustomException(f"Unexpected error: {e}")

    def get_forecast_weather(self, place: str) -> dict:
        """
        Fetch the weather forecast for a place (next few intervals).

        Args:
            place (str): City or location name.

        Returns:
            dict: Forecast weather data if successful, otherwise empty dict.

        Raises:
            CustomException: If the API call fails.
        """
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": place,
                "appid": self.api_key,
                "cnt": 10,  # Limit forecast count
                "units": "metric",
            }
            logger.info(f"Fetching forecast weather for: {place}")
            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                logger.info(f"✅ Forecast weather fetched successfully for {place}")
                return response.json()
            else:
                logger.error(
                    f"❌ Failed to fetch forecast weather for {place}. "
                    f"Status: {response.status_code}, Response: {response.text}"
                )
                return {}

        except requests.RequestException as e:
            logger.exception(f"❌ Network/API error while fetching forecast for {place}")
            raise CustomException(f"API request error: {e}")
        except Exception as e:
            logger.exception("❌ Unexpected error in get_forecast_weather")
            raise CustomException(f"Unexpected error: {e}")
