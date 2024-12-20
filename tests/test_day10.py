"""Unit Test for AoC Day 10."""

from day10 import Day10


def test_solution_day_ten_first_problem():
    """Check the example solution of first problem of AoC Day 10."""
    day10 = Day10("tests/data/example_day10_p1.dat")
    solution = day10.solution_problem_one()
    assert solution == 4


def test_solution_day_ten_second_problem_first_example():
    """Check the first example solution of first problem of AoC Day 10."""
    day10 = Day10("tests/data/example_day10_p2.dat")
    solution = day10.solution_problem_two()
    assert solution == 81
