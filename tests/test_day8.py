"""Unit Test for AoC Day 8."""

from day8 import Day8


def test_antenna_positions():
    """Check the antenna positions of example puzzle input."""
    day8 = Day8("tests/data/example_day8_p1.dat")
    antenna_positions = day8._extract_antenna_positions()
    assert antenna_positions["A"] == [
        (5, 6),
        (8, 8),
        (9, 9),
    ]


def test_antenna_antinodes():
    """Check the antenna antinodes of example puzzle input."""
    day8 = Day8("tests/data/example_day8_p1.dat")
    antenna_positions = day8._extract_antenna_positions()
    antenna_antinodes = day8._extract_antenna_antinodes(antenna_positions)
    print(antenna_antinodes["A"])
    assert antenna_antinodes["A"] == [
        (11, 10),
        (2, 4),
        (10, 10),
        (1, 3),
        (7, 7),
    ]


def test_solution_day_eight_first_problem():
    """Check the example solution of first problem of AoC - Day 8."""
    day8 = Day8("tests/data/example_day8_p1.dat")
    solution = day8.solution_problem_one()
    assert solution == 14


def test_solution_day_eight_second_problem():
    """Check the example solution of second problem of AoC - Day 8."""
    day8 = Day8("tests/data/example_day8_p2.dat")
    solution = day8.solution_problem_two()
    assert solution == 34


def test_solution_day_eight_second_problem_t_antennas():
    """Check the T-antenna example solution of second problem of Aoc Day 8."""
    day8 = Day8("tests/data/example_day8_p2_t.dat")
    solution = day8.solution_problem_two()
    assert solution == 9
