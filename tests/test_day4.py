"""Unit Test for AoC Day 4."""

from day4 import solution_day_four_problem_one, solution_day_four_problem_two


def test_solution_day_four_problem_one() -> None:
    """Check the example solution of first problem of AoC - Day 4."""
    solution = solution_day_four_problem_one("tests/data/example_day4_p1.dat")
    assert solution == 18


def test_solution_day_four_problem_two() -> None:
    """Check the example solution of second problem of AoC - Day 4."""
    solution = solution_day_four_problem_two("tests/data/example_day4_p2.dat")
    assert solution == 9
