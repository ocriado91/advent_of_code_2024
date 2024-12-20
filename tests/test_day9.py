"""Unit Test for AoC Day 9."""

from day9 import Day9


def test_extract_block_files() -> None:
    """Check the extraction of block files from disk."""
    expected_block_files = [
        0,
        0,
        None,
        None,
        None,
        1,
        1,
        1,
        None,
        None,
        None,
        2,
        None,
        None,
        None,
        3,
        3,
        3,
        None,
        4,
        4,
        None,
        5,
        5,
        5,
        5,
        None,
        6,
        6,
        6,
        6,
        None,
        7,
        7,
        7,
        None,
        8,
        8,
        8,
        8,
        9,
        9,
    ]

    day9 = Day9("tests/data/example_day9.dat")
    block_files = day9._extract_block_files()
    assert list(block_files) == expected_block_files


def test_move_block_files() -> None:
    """Check the process of move block files into left free spaces."""
    expected_moved_block_files = [
        0,
        0,
        9,
        9,
        8,
        1,
        1,
        1,
        8,
        8,
        8,
        2,
        7,
        7,
        7,
        3,
        3,
        3,
        6,
        4,
        4,
        6,
        5,
        5,
        5,
        5,
        6,
        6,
    ]

    day9 = Day9("tests/data/example_day9.dat")
    block_files = day9._extract_block_files()
    block_files = day9._move_block_files(block_files)
    print(list(block_files))
    assert list(block_files) == expected_moved_block_files


def test_filesystem_checksum() -> None:
    """Check the computation of filesystem checksum."""
    expected_checksum = 1928

    day9 = Day9("tests/data/example_day9.dat")
    block_files = day9._extract_block_files()
    block_files = day9._move_block_files(block_files)
    checksum = day9._update_filesystem_checksum(block_files)

    assert checksum == expected_checksum


def test_solution_day_nine_first_problem():
    """Check the example solution of first problem of AoC Day 9."""
    day9 = Day9("tests/data/example_day9.dat")
    solution = day9.solution_problem_one()
    assert solution == 1928


def test_solution_day_nine_second_problem():
    """Check the example solutuon of the second problem of AoC Day 9."""
    day9 = Day9("tests/data/example_day9.dat")
    solution = day9.solution_problem_two()
    assert solution == 2858
