"""Advent Of Code 2024 - Solution of Day 6."""

import copy
from solution import Solution

# Define the guard characters into the map and their respective directions
# with 90 degrees between them.
GUARD_DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

COLLISION_MARK = "#"


class Day6(Solution):
    """Day6 Solution class."""

    def __init__(self, puzzle_input: str = "data/day6.dat"):
        """Initialize the Day6 solution class."""
        Solution.__init__(self, puzzle_input)

    def _check_guard_direction(self) -> tuple:
        """Extract the current guard position into lab."""
        for idx in range(len(self.lines)):
            for guard_mark in GUARD_DIRECTIONS.keys():
                if guard_mark in self.lines[idx]:
                    idy = self.lines[idx].index(guard_mark)
                    direction = GUARD_DIRECTIONS[guard_mark]
                    return ((idx, idy), direction)

    def _next_direction(self, direction) -> tuple:
        """Compute the next direction according to current direction."""
        if direction == (-1, 0):
            return (0, 1)
        elif direction == (0, 1):
            return (1, 0)
        elif direction == (1, 0):
            return (0, -1)
        elif direction == (0, -1):
            return (-1, 0)

    def _compute_journey(self) -> dict:
        """Extract visited positions."""
        # List to save visited positions and directions of guard.
        visited_positions = []
        directions = []
        # List to save object positions.
        object_positions = []
        # Get the starting point and direction of guard and add it
        # to visited position and direction lists.
        position, direction = self._check_guard_direction()
        visited_positions.append(position)
        directions.append(direction)
        # Counter to avoid infinite while loop.
        count = 0
        count_threshold = 100000
        while count < count_threshold:
            idx = position[0] + direction[0]
            idy = position[1] + direction[1]
            # Check if new coordinates are within the puzzle input limits.
            if idx not in range(len(self.lines)) or idy not in range(
                len(self.lines[0])
            ):
                break
            # Change direction if guard reaches and object.
            if self.lines[idx][idy] == COLLISION_MARK:
                direction = self._next_direction(direction)
                object_positions.append(position)
            else:
                # Update position value and add it to visited position list
                position = (idx, idy)
                visited_positions.append(position)
                directions.append(direction)
            count += 1
        stuck_flag = count == count_threshold
        return visited_positions, stuck_flag

    def solution_problem_one(self) -> int:
        """Solution of first problem of AoC Day 6."""
        visited_positions, _ = self._compute_journey()
        return len(set(visited_positions))

    def solution_problem_two(self) -> int:
        """Solution of second problem of AoC Day 6."""
        # Extract visited positions into a normal journey.
        visited_positions, _ = self._compute_journey()
        # Brute force. Try to add a new object into each of visited positions
        original_lines = copy.deepcopy(self.lines)
        candidates = set()
        for position in visited_positions:
            if self.lines[position[0]][position[1]] == "^":
                continue
            # Restore self.lines value
            self.lines = copy.deepcopy(original_lines)
            # Create a new string with the modified character
            self.lines[position[0]] = (
                self.lines[position[0]][: position[1]]
                + COLLISION_MARK
                + self.lines[position[0]][position[1] + 1 :]
            )
            _, stuck = self._compute_journey()
            if stuck:
                candidates.add(position)
        return len(candidates)


if __name__ == "__main__":
    day6 = Day6()
    solution1 = day6.solution_problem_one()
    print("Problem 1 solution:", solution1)
    solution2 = day6.solution_problem_two()
    print("Problem 2 solution:", solution2)
