"""Advent Of Code 2024 - Solution of Day 1."""


def read_puzzle_input(puzzle_input: str) -> list:
    """Read and preprocess puzzle input."""
    # Read all lines of puzzle input
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    # Remove end of line characters.
    lines = [line.replace("\n", "") for line in lines]

    return lines


def extract_location_ids(lines: list) -> tuple:
    """Extract the location ID by groups."""
    # Split the location IDs of group 1 and group 2 and convert them
    # to integer
    data = [line.split("   ") for line in lines]

    loc_group1 = [int(loc[0]) for loc in data]
    loc_group2 = [int(loc[1]) for loc in data]

    # Sort location IDs
    loc_group1.sort()
    loc_group2.sort()

    return loc_group1, loc_group2


def solution_day_one_problem_one(puzzle_input: str = "data/day1.dat") -> int:
    """Solution of first problem of day 1."""
    lines = read_puzzle_input(puzzle_input)

    # Extract location IDs by group
    loc_group1, loc_group2 = extract_location_ids(lines)

    # Compute the distance of each pair of sorted location IDs of both groups
    # and return the sum of distances
    total_diff = 0
    for idx in range(len(loc_group1)):
        diff = abs(loc_group2[idx] - loc_group1[idx])
        total_diff += diff

    return total_diff


def solution_day_one_problem_two(puzzle_input: str = "data/day1.dat") -> int:
    """Solution of first problem of day 1."""
    lines = read_puzzle_input(puzzle_input)

    # Extract location IDs by group
    loc_group1, loc_group2 = extract_location_ids(lines)

    # Compute the similarity score.
    similarity_score = 0
    for loc in loc_group1:
        loc_count = loc_group2.count(loc)
        similarity_score += loc * loc_count
    return similarity_score


if __name__ == "__main__":
    solution1 = solution_day_one_problem_one()
    print(solution1)
    solution2 = solution_day_one_problem_two()
    print(solution2)
