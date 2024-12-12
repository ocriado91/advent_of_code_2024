"""Template class for AoC Challenge solutions."""

from abc import ABC, abstractmethod


class Solution(ABC):
    """Abstract class of Aoc Solutions."""

    def __init__(self, puzzle_input: str):
        """Read the puzzle input at the initialization method."""
        self.read_puzzle_input(puzzle_input)

    def read_puzzle_input(self, puzzle_input: str) -> list:
        """Read the puzzle input of challenge."""
        with open(puzzle_input, "r") as f:
            self.lines = f.readlines()

        # Remove end of line characters.
        self.lines = [line.replace("\n", "") for line in self.lines]

    @abstractmethod
    def solution_problem_one(self) -> int:
        """Abstract method of solution for the first challenge."""
        pass

    @abstractmethod
    def solution_problem_two(self) -> int:
        """Abstract method of solution for the second challenge."""
        pass
