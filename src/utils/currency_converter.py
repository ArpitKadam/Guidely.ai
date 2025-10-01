import requests
from src.logger import logger
from src.exception import CustomException


class CurrencyConverter:
    """
    A utility class for converting amounts between currencies using ExchangeRate API.
    """

    def __init__(self, api_key: str):
        """
        Initialize the CurrencyConverter with an API key.

        Parameters
        ----------
        api_key : str
            API key for exchangerate-api.com
        """
        if not api_key:
            raise ValueError("API key for CurrencyConverter is required.")
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest"
        logger.info("CurrencyConverter initialized successfully.")

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Convert the amount from one currency to another.

        Parameters
        ----------
        amount : float
            The amount of money to convert.
        from_currency : str
            Currency code to convert from (e.g., "USD").
        to_currency : str
            Currency code to convert to (e.g., "EUR").

        Returns
        -------
        float
            Converted amount in the target currency.

        Raises
        ------
        CustomException
            If API call fails or target currency is not found.
        """
        try:
            logger.info(f"Converting {amount} from {from_currency} to {to_currency}")
            url = f"{self.base_url}/{from_currency.upper()}"
            response = requests.get(url)
            if response.status_code != 200:
                raise CustomException(f"API call failed with status {response.status_code}: {response.text}")

            data = response.json()
            rates = data.get("conversion_rates")
            if not rates:
                raise CustomException("No conversion rates found in API response.")

            to_currency = to_currency.upper()
            if to_currency not in rates:
                raise CustomException(f"{to_currency} not found in exchange rates.")

            converted_amount = amount * rates[to_currency]
            logger.info(f"Converted amount: {converted_amount}")
            return converted_amount

        except Exception as e:
            logger.exception("Currency conversion failed.")
            raise CustomException(f"Error converting currency: {e}")
