"""Unit Test for AoC Day 2."""

from day2 import solution_day_two_problem_one


def test_solution_day_two_problem_one() -> None:
    """Check the example solution of first problem of day 2."""
    solution = solution_day_two_problem_one("tests/data/example_day2.dat")
    assert solution == 2
