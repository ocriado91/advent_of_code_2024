"""Unit Test for AoC Day 3."""

from day3 import (
    read_puzzle_input,
    solution_day_three_problem_one,
    solution_day_three_problem_two,
)


def test_read_puzzle_input() -> None:
    """Check the reading puzzle input of AoC - Day 3."""
    lines = read_puzzle_input("tests/data/example_day3.dat")
    assert len(lines) == 1


def test_solution_day_three_problem_one() -> None:
    """Check the example solution of first problem of AoC - Day 3."""
    solution = solution_day_three_problem_one("tests/data/example_day3.dat")
    assert solution == 161


def test_solution_day_three_problem_two() -> None:
    """CHeck the example solution of second problem of AoC - Day 3."""
    solution = solution_day_three_problem_two("tests/data/example_day3.dat")
    assert solution == 48
