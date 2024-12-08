"""Advent Of Code 2024 - Solution of Day 4."""


def read_puzzle_input(puzzle_input: str) -> list:
    """Read and pre-process the puzzle input of Day 3 of AoC."""
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    # Remove end of line character.
    lines = [line.replace("\n", "") for line in lines]
    return lines


def solution_day_four_problem_one(puzzle_input: str = "data/day4.dat") -> int:
    """Solution of the first problem of AoC - Day 4."""
    lines = read_puzzle_input(puzzle_input)

    # Define all possible directions of XMAS words into
    # the crossword.
    directions = [
        (1, 0),  # Horizontal forward
        (0, 1),  # Vertical forward
        (-1, 0),  # Horizontal backward
        (0, -1),  # Vertical backward
        (-1, -1),  # Left-up diagonal
        (1, 1),  # Right-up diagonal
        (1, -1),  # Righ-down diagonal
        (-1, 1),  # Left-down diagonal
    ]

    count = 0
    for i in range(len(lines)):
        # Extract the current line
        line = lines[i]
        # Check all directions of words starting at X character
        for x_pos, x_value in enumerate(line):
            # If character is different from X, continue with the next one.
            if x_value != "X":
                continue
            # Check all directions of words starting with X character.
            for direction in directions:
                idx, idy = direction
                # Continue with the next direction if any of the limits
                # are outside of borders.
                if (i + 3 * idy < 0) or (x_pos + 3 * idx < 0):
                    continue
                try:
                    word = [
                        lines[i][x_pos],
                        lines[i + idy][x_pos + idx],
                        lines[i + 2 * idy][x_pos + 2 * idx],
                        lines[i + 3 * idy][x_pos + 3 * idx],
                    ]
                except IndexError:
                    continue
                # Convert list to string
                word = "".join(word)
                if word == "XMAS":
                    count += 1

    return count


def solution_day_four_problem_two(puzzle_input: str = "data/day4.dat") -> int:
    """Solution of the second problem of AoC - Day 4."""
    lines = read_puzzle_input(puzzle_input)

    # Define all possible directions of XMAS words into
    # the crossword.
    directions = [
        (1, 1),  # Left-up diagonal
        (1, -1),  # Right-up diagonal
    ]

    count = 0
    for i in range(len(lines)):
        # Extract the current line
        line = lines[i]

        # Check the position of the A character into the line to set
        # as central position and extract its right and left diagonals
        # from this position to extract candidate word.
        central_positions = [idx for idx, x in enumerate(line) if x == "A"]
        if central_positions:
            for central_pos in central_positions:
                match_diagonal = False
                for idx, idy in directions:
                    # Check if indexes are within the limits.
                    if (central_pos - idx < 0) or (i - idy < 0):
                        break
                    # Extract candidate word.
                    try:
                        word = [
                            lines[i - idy][central_pos - idx],
                            lines[i][central_pos],
                            lines[i + idy][central_pos + idx],
                        ]
                    except IndexError:
                        break
                    word = "".join(word)

                    # If candidate word of current diagonal is different
                    # from "MAS" (forward) or "SAM" (backward), break the
                    # current loop and move to the next A character.
                    if word != "MAS" and word != "SAM":
                        break

                    # Check if a diagonal has been matched previously. If not,
                    # set the flag to true and continue with the next diagonal.
                    if not match_diagonal:
                        match_diagonal = True
                        continue
                    count += 1

    return count


if __name__ == "__main__":
    solution1 = solution_day_four_problem_one()
    print(solution1)
    solution2 = solution_day_four_problem_two()
    print(solution2)
