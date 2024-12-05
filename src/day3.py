"""Advent Of Code 2024 - Solution of Day 3."""

import re


def read_puzzle_input(puzzle_input: str) -> list:
    """Read and pre-process the puzzle input of Day 3 of AoC."""
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    return lines


def solution_day_three_problem_one(puzzle_input: str = "data/day3.dat") -> int:
    """Solution of the first problem of AoC - Day 3."""
    # Read puzzle input.
    lines = read_puzzle_input(puzzle_input)

    # Use re.findall return tuple functionallity to extract mul instructions
    # and get its values at the same time.
    regex_pattern = r"(mul\((\d{1,3}),(\d{1,3})\))"

    sum = 0
    for line in lines:
        # Extract the pattern using regex.
        matches = re.findall(pattern=regex_pattern, string=line)

        for _, value1, value2 in matches:
            sum += int(value1) * int(value2)
    return sum


def solution_day_three_problem_two(puzzle_input: str = "data/day3.dat") -> int:
    """Solution of the second problem of AoC - Day 3."""
    lines = read_puzzle_input(puzzle_input)

    # Initialize variable to return
    sum = 0

    # Capture mul instructions (and its values), do instructions or don't
    # instructions. According to re.findall documentation
    # (https://docs.python.org/3/library/re.html#re.findall), the line
    # is scanned left-to-right, and matches are returned in the order found.
    # We use this behaviour to check the pressence of don't() instructions
    # to disable (do_flag = False) the computation of next mult instructions
    # until a new do_flag = True) is found.
    regex_pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    do_flag = True
    for line in lines:
        matches = re.findall(pattern=regex_pattern, string=line)
        for instruction, value1, value2 in matches:
            if instruction == "don't()":
                do_flag = False
            elif instruction == "do()":
                do_flag = True
            elif "mul" in instruction and do_flag:
                sum += int(value1) * int(value2)
    return sum


if __name__ == "__main__":
    solution1 = solution_day_three_problem_one()
    print(solution1)
    solution2 = solution_day_three_problem_two()
    print(solution2)
