"""Advent Of Code 2024 - Solution of Day 8."""

import re
from collections import defaultdict
from solution import Solution


class Day8(Solution):
    """Solution class of AoC Day8 Solution."""

    def __init__(self, puzzle_input: str = "data/day8.dat") -> None:
        """Initialize the Day 8 solution class."""
        Solution.__init__(self, puzzle_input)

    def _extract_antenna_positions(self) -> list:
        """Extract the antenna positions from the puzzle input."""
        antenna_positions = defaultdict(list)
        # Each antenna frequency is represented by a single lowercase letter,
        # uppercase lette, or digit.
        antenna_freq_regex_pattern = r"[A-Za-z0-9]"
        for row, line in enumerate(self.lines):
            matches = {
                match
                for match in re.findall(
                    pattern=antenna_freq_regex_pattern, string=line
                )
            }
            for match in matches:
                for idx, x in enumerate(line):
                    if x == match:
                        antenna_positions[match].append((row, idx))
        return antenna_positions

    def _extract_antenna_antinodes(self, antenna_positions: dict) -> dict:
        """Compute the antinode positions of each antenna."""
        antenna_antinodes = defaultdict(list)
        # Extract the difference between each antenna and all antennas of
        # its type and compute the antinode position of each antenna pair.
        for antenna_type in antenna_positions:
            positions = antenna_positions[antenna_type]
            for idx in range(len(positions)):
                current_position = positions[idx]
                next_positions = [
                    pos for i, pos in enumerate(positions) if i != idx
                ]
                diffs = [
                    (
                        next_pos[0] - current_position[0],
                        next_pos[1] - current_position[1],
                    )
                    for next_pos in next_positions
                ]

                for next_pos, diff in zip(next_positions, diffs):
                    x_pos = next_pos[0] + diff[0]
                    y_pos = next_pos[1] + diff[1]
                    # Check if x_pos or y_pos is within the grid limits.
                    if x_pos not in range(
                        len(self.lines)
                    ) or y_pos not in range(len(self.lines[0])):
                        continue
                    antenna_antinodes[antenna_type].append((x_pos, y_pos))
        return antenna_antinodes

    def _extract_harmonic_antinodes(self, antenna_positions: dict) -> dict:
        """Compute the harmonic antinode positions of each antenna."""
        harmonic_antinodes = defaultdict(set)
        # Extract the difference between each antenna and all antennas of
        # its type and compute the antinode position of each antenna pair.
        for antenna_type in antenna_positions:
            positions = antenna_positions[antenna_type]
            for idx in range(len(positions)):
                current_position = positions[idx]
                next_positions = [
                    pos for i, pos in enumerate(positions) if i != idx
                ]
                diffs = [
                    (
                        next_pos[0] - current_position[0],
                        next_pos[1] - current_position[1],
                    )
                    for next_pos in next_positions
                ]
                for next_pos, diff in zip(next_positions, diffs):
                    x_pos = next_pos[0] + diff[0]
                    y_pos = next_pos[1] + diff[1]
                    # Check if x_pos or y_pos is within the grid limits.
                    if x_pos not in range(
                        len(self.lines)
                    ) or y_pos not in range(len(self.lines[0])):
                        continue
                    harmonic_antinodes[antenna_type].add((x_pos, y_pos))
        return harmonic_antinodes

    def solution_problem_one(self) -> int:
        """Solution of the first problem AoC - Day 8."""
        # Extract the positions of all antennas
        antenna_positions = self._extract_antenna_positions()
        antenna_antinodes = self._extract_antenna_antinodes(antenna_positions)

        # Create a set with all antenna antinodes.
        antenna_antinodes_set = set()
        for antenna_type in antenna_antinodes:
            antinodes = antenna_antinodes[antenna_type]
            [antenna_antinodes_set.add(x) for x in antinodes]

        return len(antenna_antinodes_set)

    def solution_problem_two(self) -> int:
        """Solution of the second problem AoC - Day 8."""
        # Extract the positions of all antennas
        positions = self._extract_antenna_positions()
        harmonic_antinodes = self._extract_harmonic_antinodes(positions)

        total_antinodes = set()
        for antinode in harmonic_antinodes:
            total_antinodes.update(harmonic_antinodes[antinode])

        return len(total_antinodes)


if __name__ == "__main__":
    day8 = Day8()
    # solution1 = day8.solution_problem_one()
    # print(solution1)

    solution2 = day8.solution_problem_two()
    print(solution2)
