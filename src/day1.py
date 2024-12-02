"""Advent Of Code 2024 - Solution of Day 1."""


def solution_day_one_problem_one(puzzle_input: str = "data/day1.dat") -> int:
    """Solution of day 1."""
    # Read all lines of puzzle input
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    # Remove end of line character
    lines = [line.replace("\n", "") for line in lines]

    # Split the location IDs of group 1 and group 2 and convert them
    # to integer
    data = [line.split("   ") for line in lines]

    loc_group1 = [int(loc[0]) for loc in data]
    loc_group2 = [int(loc[1]) for loc in data]

    # Sort location IDs
    loc_group1.sort()
    loc_group2.sort()

    # Compute the distance of each pair of sorted location IDs of both groups
    # and return the sum of distances
    total_diff = 0
    for idx in range(len(loc_group1)):
        diff = abs(loc_group2[idx] - loc_group1[idx])
        total_diff += diff

    return total_diff


if __name__ == "__main__":
    solution1 = solution_day_one_problem_one()
    print(solution1)
