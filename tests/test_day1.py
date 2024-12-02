"""Calculator package Unit tests."""

from day1 import (
    read_puzzle_input,
    extract_location_ids,
    solution_day_one_problem_one,
    solution_day_one_problem_two,
)


def test_read_puzzle_input() -> None:
    """Check reading puzzle input behaviour."""
    lines = read_puzzle_input("tests/data/example_day1.dat")
    assert len(lines) == 6
    assert lines[0] == "3   4"


def test_extract_location_id() -> None:
    """Check split the location ID by group."""
    lines = ["3   4"]
    loc_group1, loc_group2 = extract_location_ids(lines)
    assert loc_group1[0] == 3
    assert loc_group2[0] == 4


def test_solution_day_one_problem_one() -> None:
    """Check the example solution of fist problem of day 1."""
    assert solution_day_one_problem_one("tests/data/example_day1.dat") == 11


def test_solution_day_one_problem_two() -> None:
    """Check the example solution of second problem of day 1."""
    assert solution_day_one_problem_two("tests/data/example_day1.dat") == 31
