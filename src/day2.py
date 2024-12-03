"""Advent Of Code 2024 - Solution of Day 1."""


def read_puzzle_input(puzzle_input: str) -> list:
    """Read and preprocess puzzle input."""
    # Read all lines of puzzle input
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    # Remove end of line characters.
    reports = [line.replace("\n", "") for line in lines]

    # Split reports into levels and convert them into integer.
    _reports = [x.split() for x in reports]
    reports = []
    for report in _reports:
        report = [int(level) for level in report]
        reports.append(report)

    return reports


def _compute_differences(report: list) -> list:
    """Compute the difference between levels."""
    diffs = []
    for idx in range(len(report) - 1):
        diff = report[idx + 1] - report[idx]
        diffs.append(diff)
    return diffs


def _check_all_increasing(diff: list) -> int:
    """Check if difference elements are in increased order."""
    count = [x > 0 for x in diff].count(True)
    return count


def _check_all_decreasing(diff: list) -> int:
    """Check if all levels are in decreasing order."""
    count = [x < 0 for x in diff].count(True)
    return count


def _check_adjacent_levels(diff: list) -> int:
    """Check adjacent levels levels."""
    count = [abs(x) <= 3 and abs(x) >= 1 for x in diff].count(True)
    return count


def solution_day_two_problem_one(puzzle_input: str = "data/day2.dat") -> int:
    """Solution of first problem of day 1."""
    reports = read_puzzle_input(puzzle_input)

    safe_count = 0
    for report in reports:
        # Compute the difference between two adjency items.
        diffs = _compute_differences(report)

        # Check if all differences are positive or negative (first condition)
        all_increasing = _check_all_increasing(diffs) == len(diffs)
        all_decreasing = _check_all_decreasing(diffs) == len(diffs)

        if not all_increasing and not all_decreasing:
            continue

        # If first condition is meet, check the second condition
        second_condition = _check_adjacent_levels(diffs) == len(diffs)
        if not second_condition:
            continue

        safe_count += 1
    return safe_count


if __name__ == "__main__":
    solution1 = solution_day_two_problem_one()
    print(solution1)
