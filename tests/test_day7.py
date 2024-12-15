"""Unit Test for AoC Day 7."""

from day7 import Day7


def test_solution_day_seven_first_problem():
    """Check the example solution of first problem of AoC - Day 7."""
    day7 = Day7("tests/data/example_day7.dat")
    solution = day7.solution_problem_one()
    assert solution == 3749


def test_solution_day_seven_second_problem():
    """Check the example solution of second problem of AoC - Day 7."""
    day7 = Day7("tests/data/example_day7.dat")
    solution = day7.solution_problem_two()
    assert solution == 11387
