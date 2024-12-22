"""Unit Test for AoC Day 11."""

from day11 import Day11


def test_solution_day_eleven_first_problem():
    """Check the example solution of first problem of AoC Day 11."""
    day11 = Day11("tests/data/example_day11.dat")
    solution = day11.solution_problem_one()
    assert solution == 55312


def test_solution_day_eleven_second_problem():
    """Check the example solution of second problem of AoC Day 11."""
    day11 = Day11("tests/data/example_day11.dat")
    solution = day11.solution_problem_two()
    assert solution == 65601038650482
