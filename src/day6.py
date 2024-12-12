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

    def _plot_positions(
        self,
        object_positions: list,
        positions: list,
        new_object_position: tuple = None,
    ) -> None:
        """Plot the guard positions."""
        plt.figure()
        # Object coordinates
        x_obj = [position[0] for position in object_positions]
        y_obj = [position[1] for position in object_positions]
        # Plot object positions
        plt.scatter(x_obj, y_obj, color="green", marker="X", s=50)
        # Plot new object position
        if new_object_position:
            plt.scatter(
                new_object_position[0],
                new_object_position[1],
                color="red",
                marker="X",
                s=50,
            )
        # Split guard position coordinates
        x = [position[0] for position in positions]
        y = [position[1] for position in positions]
        # Plot first position
        plt.scatter(x[0], y[0], color="red", marker="*", s=50)
        # Plot positions
        plt.plot(x, y, color="blue")
        plt.savefig("positions.png")

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
        return visited_positions, object_positions, directions, stuck_flag

    def solution_problem_one(self) -> int:
        """Solution of first problem of AoC Day 6."""
        visited_positions, _, _, _ = self._compute_journey()
        return len(set(visited_positions))

    def solution_problem_two(self) -> int:
        """Solution of second problem of AoC Day 6."""
        candidates = self._candidates_object()
        print(candidates)

    def _candidates_object(self) -> list:
        """Build a list of candidate positions to add the extract object."""
        # List to store candidate positions to create a infinite loop into
        # guard path.
        candidates = []
        # Extract visited positions and directions take by guard.
        visited_positions, object_positions, directions, _ = (
            self._compute_journey()
        )
        print(len(visited_positions))
        print(len(directions))
        # Extract of each visited position, if the guard could change its
        # direction to go to previous positions that follows the new direction.
        for idx in range(len(visited_positions)):
            # Extract current position and direction
            current_position = visited_positions[idx]
            current_direction = directions[idx]
            # print("Current position:", current_position)
            # print("Current direction:", current_direction)
            # Compute the direction of turn.
            turn_direction = self._next_direction(current_direction)
            # print("Turn direction:", turn_direction)

            # Extract previous coordinates
            x_prev = [x[0] for x in visited_positions[:idx]]
            y_prev = [x[1] for x in visited_positions[:idx]]
            # print("X prev:", x_prev)
            # print("Y prev:", y_prev)

            # Check if any current coordinate matches with previous positions
            # coordinates and also matches the turn direction with the
            # direction of matched previous position (the guard can follow
            # the same path through previous positions with the
            # turn direction).
            matched_pos_index = None
            if current_position[0] in x_prev:
                matched_pos_index = x_prev.index(current_position[0])
            elif current_position[1] in y_prev:
                matched_pos_index = y_prev.index(current_position[1])
            if matched_pos_index is not None:
                match_pos_direction = directions[matched_pos_index]
                if match_pos_direction == turn_direction:
                    print("Detected position:", current_position)

        # # Extract of each visited position, if the guard could change
        # # its direction to go through previous positions.
        # for idx in range(len(visited_positions)-1):
        #     # Compute the current position and direction.
        #     current_position = visited_positions[idx]
        #     print("Current position:", current_position)
        #     current_direction = directions[idx]
        #     # Compute the next direction based on current direction.
        #     next_direction = self._next_direction(current_direction)
        #     # Get the coordinates in next_direction.
        #     next_position = (
        #         current_position[0] + next_direction[0],
        #         current_position[1] + next_direction[1]
        #     )
        #     # Check if current position is not in the object position list
        #     # to avoid extract candidates where a change of direction can be
        #     # taken by a object in the current direction, and check if
        #     # next_position is within visited previous positions.
        #     if (current_position not in object_positions and
        #         next_position in visited_positions[:idx]):
        #         # Candidate position to place an object is the next
        #         # position of current position if guard follows
        #         # the current direction.
        #         candidate_posiiton = (
        #             current_position[0] + current_direction[0],
        #             current_position[1] + current_direction[1]
        #         )
        #         candidates.append(candidate_posiiton)
        # print("Candidates:", candidates)
        return candidates


if __name__ == "__main__":
    day6 = Day6()
    solution1 = day6.solution_problem_one()
    print("Problem 1 solution:", solution1)
    solution2 = day6.solution_problem_two()
    print("Problem 2 solution:", solution2)
