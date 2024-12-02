"""Calculator package Unit tests."""

from day1 import solution_day_one_problem_one


def test_solution_day_one() -> None:
    """Check the sum operation between two float variables."""
    assert solution_day_one_problem_one("tests/data/example_day1.dat") == 11
