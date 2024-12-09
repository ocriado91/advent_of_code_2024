"""Advent Of Code 2024 - Solution of Day 5."""

import copy
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
    invalid_updates = []
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
            # Detected a page into the update that breaks the order. Set the
            # invalid update flag as True and stop to search into the next
            # pages
            if before_pages:
                invalid_update = True
                invalid_updates.append(update)
                break
        if not invalid_update:
            valid_updates.append(update)
    return valid_updates, invalid_updates


def fix_updates(invalid_updates: list, ordering_rules: list) -> list:
    """Fix update according to ordering rules."""
    fixed_updates = []
    for invalid_update in invalid_updates:
        for idx, page in enumerate(invalid_update):
            previous_pages = [
                x
                for x, y in ordering_rules
                if y == page and x in invalid_update[idx + 1 :]
            ]
            if previous_pages:
                # Check the indexes of previous pages and corrupted page
                replace_index = max(
                    [invalid_update.index(x) for x in previous_pages]
                )
                page_index = invalid_update.index(page)
                # Replace the corrupt page with the last index
                fixed_update = copy.deepcopy(invalid_update)
                fixed_update[replace_index] = page
                fixed_update[page_index] = invalid_update[replace_index]
                # Add current fixed update to list
                fixed_updates.append(fixed_update)
                # Detected one corrupted page. Stop the current search loop
                break
    return fixed_updates


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
    valid_updates, _ = _check_updates(ordering_rules, updates)
    # Add the middle page numbers of valid pages.
    sum = 0
    for valid_update in valid_updates:
        sum += compute_middle_page_number(valid_update)
    return sum


def solution_day_five_problem_two(puzzle_input: str = "data/day5.dat") -> int:
    """Solution of the second problem of Aoc Day 5."""
    lines = read_puzzle_input(puzzle_input)
    # Divide the lines of puzzle input into ordering rules and updates
    ordering_rules, updates = _split_ordering_updates(lines)
    # Check the validity of update list.
    _, invalid_updates = _check_updates(ordering_rules, updates)
    # Try to fix invalid updates until list is empty (all invalid updates has
    # been fixed)
    valid_fixed_updates = []
    while invalid_updates:
        # Fix invalid updates
        fixed_updates = fix_updates(invalid_updates, ordering_rules)
        # Check the validity of fixed updates
        _valid_fixed_updates, invalid_updates = _check_updates(
            ordering_rules, fixed_updates
        )
        # Save valid fixed updates into list.
        for _valid_fixed_update in _valid_fixed_updates:
            valid_fixed_updates.append(_valid_fixed_update)

    # Compute the sum of all middle page numbers of fixed updates.
    sum = 0
    for valid_update in valid_fixed_updates:
        sum += compute_middle_page_number(valid_update)
    return sum


if __name__ == "__main__":
    solution1 = solution_day_five_problem_one()
    print(solution1)
    solution2 = solution_day_five_problem_two()
    print(solution2)
