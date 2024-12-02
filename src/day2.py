"""Advent Of Code 2024 - Solution of Day 1."""


def read_puzzle_input(puzzle_input: str) -> list:
    """Read and preprocess puzzle input."""
    # Read all lines of puzzle input
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    # Remove end of line characters.
    lines = [line.replace("\n", "") for line in lines]

    return lines


def solution_day_two_problem_one(puzzle_input: str = "data/day2.dat") -> int:
    """Solution of first problem of day 1."""
    reports = read_puzzle_input(puzzle_input)

    safe_count = 0
    for report in reports:
        # Extract levels and convert them to integers
        levels = report.split()
        levels = [int(level) for level in levels]

        # Compute the difference between two adjency items.
        diffs = []
        for idx in range(len(levels) - 1):
            diff = levels[idx + 1] - levels[idx]
            diffs.append(diff)

        # Check if all differences are positive or negative (first condition)
        all_increasing = all(diff >= 0 for diff in diffs)
        all_decreasing = all(diff <= 0 for diff in diffs)

        if not all_increasing and not all_decreasing:
            continue

        # If first condition is meet, check the second condition
        second_condition = all(
            abs(diff) <= 3 and abs(diff) >= 1 for diff in diffs
        )
        if not second_condition:
            continue

        safe_count += 1
    return safe_count


if __name__ == "__main__":
    solution1 = solution_day_two_problem_one()
    print(solution1)
