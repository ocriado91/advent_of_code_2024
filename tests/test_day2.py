"""Unit Test for AoC Day 2."""

from day2 import (
    read_puzzle_input,
    solution_day_two_problem_one,
    solution_day_two_problem_two,
)


def test_read_puzzle_input() -> None:
    """Check the reading puzzle input."""
    levels = read_puzzle_input("tests/data/example_day2.dat")
    assert len(levels) == 6
    assert levels[0] == [7, 6, 4, 2, 1]


def test_solution_day_two_problem_one() -> None:
    """Check the example solution of first problem of day 2."""
    solution = solution_day_two_problem_one("tests/data/example_day2.dat")
    assert solution == 2


def test_solution_day_two_problem_two() -> None:
    """CHeck the example solution of second problem of day 2."""
    solution = solution_day_two_problem_two("tests/data/example_day2.dat")
    assert solution == 4
