"""Calculator class."""


class Calculator:
    """A Calculator class to compute basic operations."""

    def sum(self, a: float, b: float) -> float:
        """Compute the sum between two float variables."""
        return a + b

    def substract(self, a: float, b: float) -> float:
        """Compute the substraction between two float variables."""
        return a - b

    def multiplication(self, a: float, b: float) -> float:
        """Computhe the multiplication between two float variables."""
        return a * b

    def division(self, a: float, b: float) -> float:
        """Compute the division between two float variables."""
        try:
            return a / b
        except ZeroDivisionError:
            error_msg = "ERROR: Divisor must be different from 0."
            raise ZeroDivisionError(error_msg) from None
