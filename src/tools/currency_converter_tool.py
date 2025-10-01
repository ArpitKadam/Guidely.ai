import os
from typing import List
from dotenv import load_dotenv
from langchain.tools import tool
from src.utils.currency_converter import CurrencyConverter
from src.logger import logger
from src.exception import CustomException


class CurrencyConverterTool:
    """
    Wraps the CurrencyConverter utility as LangChain-compatible tools.
    """

    def __init__(self):
        """
        Initialize the CurrencyConverter tool with API key from environment variables.
        """
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        if not self.api_key:
            logger.warning("EXCHANGE_RATE_API_KEY not found in environment variables.")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup all LangChain tools for currency conversion.

        Returns
        -------
        List
            List of LangChain tool functions.
        """

        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
            """
            Convert amount from one currency to another.

            Parameters
            ----------
            amount : float
                The amount of money to convert.
            from_currency : str
                Source currency code (e.g., 'USD').
            to_currency : str
                Target currency code (e.g., 'EUR').

            Returns
            -------
            float
                Converted amount.

            Raises
            ------
            CustomException
                If conversion fails due to API or invalid currency.
            """
            try:
                logger.info(f"Converting {amount} from {from_currency} to {to_currency}")
                return self.currency_service.convert(amount, from_currency, to_currency)
            except Exception as e:
                logger.exception("Currency conversion tool failed.")
                raise CustomException(f"convert_currency tool error: {e}")

        return [convert_currency]
