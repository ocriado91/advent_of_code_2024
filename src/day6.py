"""Advent Of Code 2024 - Solution of Day 6."""

import matplotlib.pyplot as plt
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

    def _plot_positions(self, object_positions: list, positions: list) -> None:
        """Plot the guard positions."""
        # Object coordinates
        x_obj = [position[0] for position in object_positions]
        y_obj = [position[1] for position in object_positions]
        # Plot object positions
        plt.scatter(x_obj, y_obj, color="green", marker="X", s=50)
        # Split guard position coordinates
        x = [position[0] for position in positions]
        y = [position[1] for position in positions]
        # Plot first position
        plt.scatter(x[0], y[0], color="red", marker="*", s=50)
        # Plot positions
        plt.plot(x, y)
        plt.savefig("positions.png")

    def solution_problem_one(self):
        """Solution of first problem of AoC Day 6."""
        # Set to save visited positions by guard.
        visited_positions = set()
        # Get the starting position and direction of guard and add it
        # to visited positions set.
        position, direction = self._check_guard_direction()
        visited_positions.add(position)
        # Detect the next collision based on current position and
        # direction of the guard and extract the next position
        # where there is a change in the direction of the guard.
        while True:
            idx = position[0] + direction[0]
            idy = position[1] + direction[1]
            # Check if new coordinates are within the puzzle input limits
            if idx not in range(len(self.lines)) or idy not in range(
                len(self.lines[0])
            ):
                break
            # Change direction if an object is guard reaches an object
            if self.lines[idx][idy] == COLLISION_MARK:
                direction = self._next_direction(direction)
            else:
                position = (idx, idy)
                visited_positions.add(position)
        # Return the number of visited locations (without duplicates, thanks
        # to save positions into a set previously)
        return len(visited_positions)

    def solution_problem_two(self):
        """Solution of second problem of AoC Day 6."""
        # List to save visited positions by guard.
        visited_positions = []
        # List to save object positions.
        object_positions = []
        # Get the starting position and direction of guard and add it
        # to visited positions set.
        position, direction = self._check_guard_direction()
        visited_positions.append(position)
        # Use count to break while loop in case of infinitel loop.
        count = 0
        count_threshold = 1400
        # Detect the next collision based on current position and
        # direction of the guard and extract the next position
        # where there is a change in the direction of the guard.
        while count < count_threshold:
            idx = position[0] + direction[0]
            idy = position[1] + direction[1]
            # Check if new coordinates are within the puzzle input limits
            if idx not in range(len(self.lines)) or idy not in range(
                len(self.lines[0])
            ):
                break
            # Change direction if an object is guard reaches an object
            if self.lines[idx][idy] == COLLISION_MARK:
                direction = self._next_direction(direction)
                # Save object position
                object_positions.append((idx, idy))
            else:
                position = (idx, idy)
                visited_positions.append(position)
            count += 1
        # Plot visited positions
        self._plot_positions(object_positions, visited_positions)
        # Convert list to set to remove duplicates
        visited_positions = set(list(visited_positions))
        # Return the lenght of visited positions without duplicates
        return len(visited_positions)


if __name__ == "__main__":
    day6 = Day6()
    solution1 = day6.solution_problem_one()
    print("Problem 1 solution:", solution1)
    solution2 = day6.solution_problem_two()
    print("Problem 2 solution:", solution2)
