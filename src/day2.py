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


def compute_safe(levels: int):
    """Compute the safe levels."""
    # Check thresholds into levels and levels +1 lists and check if
    # all elements are in increasing or decreasing order comparing the values
    # against the sorted list and reverse sorted list.
    return all(1 <= abs(x - y) <= 3 for x, y in zip(levels, levels[1:])) and (
        levels == sorted(levels) or levels == sorted(levels)[::-1]
    )


def solution_day_two_problem_one(puzzle_input: str = "data/day2.dat") -> int:
    """Solution of first problem of day 1."""
    reports = read_puzzle_input(puzzle_input)
    return sum(compute_safe(report) for report in reports)


def solution_day_two_problem_two(puzzle_input: str = "data/day2.dat") -> int:
    """Solution of Problem 2 of second day."""
    reports = read_puzzle_input(puzzle_input)
    safe_reports = []
    for report in reports:
        safe_results = []
        for idx in range(len(report)):
            replaced_report = report[:idx] + report[idx + 1 :]
            safe_results.append(compute_safe(replaced_report))
        safe_reports.append(any(safe_results))

    return sum(safe_reports)


if __name__ == "__main__":
    solution1 = solution_day_two_problem_one()
    print(solution1)
    solution2 = solution_day_two_problem_two()
    print(solution2)
