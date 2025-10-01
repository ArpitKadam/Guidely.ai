from typing import List, Union
from langchain.tools import tool
from src.utils.expense_calculator import Calculator
from src.logger import logger
from src.exception import CustomException

Number = Union[int, float]

class CalculatorTool:
    """
    Wrapper class to expose Calculator methods as LangChain-compatible tools.
    """

    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup all calculator tools and return as a list.

        Returns
        -------
        List
            List of LangChain tool functions.
        """

        @tool
        def estimate_total_hotel_cost(price_per_night: Number, total_days: Number) -> float:
            """
            Calculate total hotel cost.

            Parameters
            ----------
            price_per_night : int or float
                Cost of hotel per night.
            total_days : int or float
                Number of nights.

            Returns
            -------
            float
                Total hotel cost.
            """
            try:
                logger.info(f"Calculating hotel cost: {price_per_night} x {total_days}")
                price_per_night = float(price_per_night)
                total_days = float(total_days)
                return self.calculator.multiply(price_per_night, total_days)
            except Exception as e:
                logger.exception("Failed to calculate total hotel cost")
                raise CustomException(f"estimate_total_hotel_cost error: {e}")

        @tool
        def calculate_total_expense(*costs: Number) -> float:
            """
            Calculate total expense of the trip.

            Parameters
            ----------
            costs : int or float
                List of individual expenses.

            Returns
            -------
            float
                Total sum of all expenses.
            """
            try:
                logger.info(f"Calculating total expense for costs: {costs}")
                costs = [float(c) for c in costs]
                return self.calculator.calculate_total(*costs)
            except Exception as e:
                logger.exception("Failed to calculate total expense")
                raise CustomException(f"calculate_total_expense error: {e}")

        @tool
        def calculate_daily_expense_budget(total_cost: Number, days: int) -> float:
            """
            Calculate daily expense budget.

            Parameters
            ----------
            total_cost : int or float
                Total expense of the trip.
            days : int
                Number of days.

            Returns
            -------
            float
                Daily expense budget.
            """
            try:
                logger.info(f"Calculating daily budget: total_cost={total_cost}, days={days}")
                total_cost = float(total_cost)
                return self.calculator.calculate_daily_budget(total_cost, days)
            except Exception as e:
                logger.exception("Failed to calculate daily expense budget")
                raise CustomException(f"calculate_daily_expense_budget error: {e}")

        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]
