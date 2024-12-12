"""Unit Test for AoC Day 6."""

from day6 import Day6


def test_solution_day_six_problem_one() -> None:
    """Check the example solution of the first problem of AoC - Day 6."""
    day6 = Day6("tests/data/example_day6.dat")
    solution = day6.solution_problem_one()
    assert solution == 41


def test_solution_day_six_problem_two() -> None:
    """Check the example solution of the second problem of AoC - Day 6."""
    day6 = Day6("tests/data/example_day6.dat")
    solution = day6.solution_problem_two()
    assert solution == 6
