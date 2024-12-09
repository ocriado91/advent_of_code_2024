"""Unit Test for AoC Day 5."""

from day5 import solution_day_five_problem_one, solution_day_five_problem_two


def test_solution_day_five_problem_one() -> None:
    """Check the example solution of first problem AoC - Day 5."""
    solution = solution_day_five_problem_one("tests/data/example_day5.dat")
    assert solution == 143


def test_solution_day_five_problem_two() -> None:
    """Check the example solution of second problem AoC - Day 5."""
    solution = solution_day_five_problem_two("tests/data/example_day5.dat")
    assert solution == 123
