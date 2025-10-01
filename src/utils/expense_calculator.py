from typing import Union


Number = Union[int, float]


class Calculator:
    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """
        Multiply two numbers.

        Parameters
        ----------
        a : int or float
            The first number.
        b : int or float
            The second number.

        Returns
        -------
        int or float
            The product of `a` and `b`.
        """
        return a * b

    @staticmethod
    def calculate_total(*x: Number) -> Number:
        """
        Calculate the sum of the given numbers.

        Parameters
        ----------
        x : tuple of int or float
            Numbers to be summed.

        Returns
        -------
        int or float
            The sum of all numbers in `x`.
        """
        return sum(x)

    @staticmethod
    def calculate_daily_budget(total: Number, days: int) -> float:
        """
        Calculate daily budget.

        Parameters
        ----------
        total : int or float
            Total cost.
        days : int
            Number of days.

        Returns
        -------
        float
            Expense for a single day. Returns 0.0 if `days` <= 0.
        """
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        return float(total) / days
