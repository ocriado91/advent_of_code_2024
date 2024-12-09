"""Advent Of Code 2024 - Solution of Day 5."""

import math
import re


def read_puzzle_input(puzzle_input: str) -> list:
    """Read AoC Day 5 puzzle input."""
    with open(puzzle_input, "r") as f:
        lines = f.readlines()

    return lines


def _split_ordering_updates(lines: list) -> tuple:
    """Split the ordering rules and updates from puzzle input."""
    # Extract both terms into ordering rules separated by "|" character.
    ordering_rule_pattern = r"(\d+)\|(\d+)"
    ordering_rules = []

    update_pattern = r"\d+"
    updates = []
    for line in lines:
        ordering_rule_match = re.findall(
            pattern=ordering_rule_pattern, string=line
        )
        # Check if there is a match, and append the value as tuple.
        if ordering_rule_match:
            val1, val2 = ordering_rule_match[0]
            ordering_rules.append((int(val1), int(val2)))

        if "|" not in line:
            update_match = re.findall(pattern=update_pattern, string=line)
            if update_match:
                update_match = [int(x) for x in update_match]
                updates.append(update_match)

    return ordering_rules, updates


def _check_updates(ordering_rules: list, updates: list) -> list:
    """Check the validity of the updates according to the ordering rules."""
    valid_updates = []
    # Check page by page of each update, if there is any page that must be
    # printed before of current page and if these pages are into next pages
    # positions within the update.
    for update in updates:
        invalid_update = False
        for idx, page in enumerate(update):
            before_pages = [
                x
                for x, y in ordering_rules
                if y == page and x in update[idx + 1 :]
            ]
            if before_pages:
                invalid_update = True
                break
        if not invalid_update:
            valid_updates.append(update)
    return valid_updates


def compute_middle_page_number(update: list) -> int:
    """Compute the middle page number of a specific update."""
    middle_page_index = math.floor(len(update) / 2)
    return update[middle_page_index]


def solution_day_five_problem_one(puzzle_input: str = "data/day5.dat") -> int:
    """Solution of the first problem of AoC Day 5."""
    lines = read_puzzle_input(puzzle_input)
    # Divide the lines of puzzle input into ordering rules and updates
    ordering_rules, updates = _split_ordering_updates(lines)
    # Check the validity of update list.
    valid_updates = _check_updates(ordering_rules, updates)
    # Add the middle page numbers of valid pages.
    sum = 0
    for valid_update in valid_updates:
        sum += compute_middle_page_number(valid_update)
    return sum


if __name__ == "__main__":
    solution1 = solution_day_five_problem_one()
    print(solution1)
