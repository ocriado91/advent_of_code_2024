"""Calculator package Unit tests."""

import pytest

from calculator import Calculator


def test_sum() -> None:
    """Check the sum operation between two float variables."""
    assert Calculator().sum(10, 4) == 14


def test_substract() -> None:
    """Check the substract operation between two float variables."""
    assert Calculator().substract(10, 4) == 6


def test_multiplication() -> None:
    """Check the multiplication operation between two float variables."""
    assert Calculator().multiplication(10, 4) == 40


def test_division() -> None:
    """Check the division operation between two float variables."""
    assert Calculator().division(10, 4) == 2.5


def test_zero_division() -> None:
    """Check the ZeroDivisionError exception handling."""
    # Check raising of ZeroDivisonError exception.
    with pytest.raises(ZeroDivisionError) as excinfo:
        Calculator().division(10, 0)

    # Check the custom message of the exception.
    assert str(excinfo.value) == "ERROR: Divisor must be different from 0."
