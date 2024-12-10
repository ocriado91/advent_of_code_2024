"""Unit Test for AoC Day 6."""

from day6 import Day6


def test_solution_day_six_problem_one() -> None:
    """Check the example solution of the first problem of AoC - Day 6."""
    day6 = Day6("tests/data/example_day6.dat")
    solution = day6.solution_problem_one()
    assert solution == 41


def test_guard_stuck_option_one() -> None:
    """Check if introducing a new object into (6,3) causes guard stuck."""
    new_object_position = (6, 3)

    day6 = Day6("tests/data/example_day6.dat")
    _, _, guard_stuck_flag = day6._compute_journey(new_object_position)
    assert guard_stuck_flag


def test_guard_stuck_option_two() -> None:
    """Check if introducing a new object into (6,3) causes guard stuck."""
    new_object_position = (7, 6)

    day6 = Day6("tests/data/example_day6.dat")
    _, _, guard_stuck_flag = day6._compute_journey(new_object_position)
    assert guard_stuck_flag


def test_guard_stuck_option_three() -> None:
    """Check if introducing a new object into (6,3) causes guard stuck."""
    new_object_position = (7, 7)

    day6 = Day6("tests/data/example_day6.dat")
    _, _, guard_stuck_flag = day6._compute_journey(new_object_position)
    assert guard_stuck_flag


def test_guard_stuck_option_four() -> None:
    """Check if introducing a new object into (6,3) causes guard stuck."""
    new_object_position = (8, 1)

    day6 = Day6("tests/data/example_day6.dat")
    _, _, guard_stuck_flag = day6._compute_journey(new_object_position)
    assert guard_stuck_flag


def test_guard_stuck_option_five() -> None:
    """Check if introducing a new object into (6,3) causes guard stuck."""
    new_object_position = (8, 3)

    day6 = Day6("tests/data/example_day6.dat")
    _, _, guard_stuck_flag = day6._compute_journey(new_object_position)
    assert guard_stuck_flag


def test_guard_stuck_option_six() -> None:
    """Check if introducing a new object into (6,3) causes guard stuck."""
    new_object_position = (9, 7)

    day6 = Day6("tests/data/example_day6.dat")
    _, _, guard_stuck_flag = day6._compute_journey(new_object_position)
    assert guard_stuck_flag


def test_solution_day_six_problem_two() -> None:
    """Check the example solution of the second problem of AoC - Day 6."""
    day6 = Day6("tests/data/example_day6.dat")
    solution = day6.solution_problem_two()
    assert solution == 6
