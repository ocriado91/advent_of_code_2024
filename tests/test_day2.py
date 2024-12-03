"""Unit Test for AoC Day 2."""

from day2 import (
    read_puzzle_input,
    _compute_differences,
    _check_all_increasing,
    _check_all_decreasing,
    _check_adjacent_levels,
    solution_day_two_problem_one,
)


def test_read_puzzle_input() -> None:
    """Check the reading puzzle input."""
    levels = read_puzzle_input("tests/data/example_day2.dat")
    assert len(levels) == 6
    assert levels[0] == [7, 6, 4, 2, 1]


def test_compute_differences() -> None:
    """Chech the computation of difference between adjenct levels."""
    levels = read_puzzle_input("tests/data/example_day2.dat")
    diffs = _compute_differences(levels[0])
    assert len(diffs) == 4
    assert diffs == [-1, -2, -2, -1]


def test_check_all_increasing() -> None:
    """Check all increasing reports into incoming data."""
    count = 0
    reports = read_puzzle_input("tests/data/example_day2.dat")
    for report in reports:
        diffs = _compute_differences(report)
        increasing_values = _check_all_increasing(diffs)
        if increasing_values == len(diffs):
            count += 1
    assert count == 2


def test_check_all_decreasing() -> None:
    """Check all decreasing reports into incoming data."""
    count = 0
    reports = read_puzzle_input("tests/data/example_day2.dat")
    for report in reports:
        diffs = _compute_differences(report)
        decreasing_values = _check_all_decreasing(diffs)
        if decreasing_values == len(diffs):
            count += 1
    assert count == 2


def test_check_adjacent_levels() -> None:
    """Check adjacent difference threshold into incoming data."""
    count = 0
    reports = read_puzzle_input("tests/data/example_day2.dat")
    for report in reports:
        diffs = _compute_differences(report)
        adj_values = _check_adjacent_levels(diffs)
        if adj_values == len(diffs):
            count += 1
    assert count == 3


def test_solution_day_two_problem_one() -> None:
    """Check the example solution of first problem of day 2."""
    solution = solution_day_two_problem_one("tests/data/example_day2.dat")
    assert solution == 2
