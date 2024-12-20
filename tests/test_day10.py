"""Unit Test for AoC Day 10."""

from day10 import Day10


def test_solution_day_ten_first_problem():
    """Check the example solution of first problem of AoC Day 10."""
    day10 = Day10("tests/data/example_day10.dat")
    solution = day10.solution_problem_one()
    assert solution == 4
