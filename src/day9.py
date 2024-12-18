"""Advent Of Code 2024 - Solution of Day 9."""

from collections import deque
from solution import Solution


class Day9(Solution):
    """Solution class of AoC Day9 Solution."""

    def __init__(self, puzzle_input: str = "data/day9.dat") -> None:
        """Initialize the Day 9 solution class."""
        Solution.__init__(self, puzzle_input)

        self.line = self.lines[0]

    def _extract_block_files(self) -> deque:
        """Extract the block files of the disk map."""
        # Extract the size files and free spaces on the disk.
        block_file_sizes = self.line[::2]
        block_free_sizes = self.line[1::2]

        # Initialize the total block file string.
        block_files = ""

        # Iterate over block file sizes to compute and concatenate
        # and file and free size blocks.
        block_files = deque()
        for idx, block_file_size in enumerate(block_file_sizes):
            block_files.extend([idx] * int(block_file_size))
            # Discard to add the free in the last iteration
            if idx == len(block_free_sizes):
                break
            block_files.extend([None] * int(block_free_sizes[idx]))
        return deque(block_files)

    def _move_block_files(self, block_files: deque) -> deque:
        """Apply block files following the procedure."""
        while True:
            # Search first free space block from the left. If any
            # free space block is found, this function returns the
            # index otherwise, raises a ValueError exception. Catch this
            # exception to break the loop (none free space remaining into
            # block files).
            try:
                block_free_index = block_files.index(None)
            except ValueError:
                break

            # There is a free space to be moved. Extract the last size from
            # right size and moved into free space position (insert file size
            # block + remove previous free space block, there is not a replace
            # method into current deque version:
            # https://docs.python.org/3/library/collections.html#collections.deque).
            block = block_files.pop()
            if not block:
                continue

            block_files.insert(block_free_index, block)
            block_files.remove(None)
        return block_files

    def _update_filesystem_checksum(self, block_files: deque) -> int:
        """Compute the filesystem checksum."""
        sum = 0
        for idx, x in enumerate(block_files):
            sum += idx * int(x)
        return sum

    def solution_problem_one(self) -> int:
        """Solution of the first problem AoC - Day 9."""
        block_files = self._extract_block_files()
        block_files = self._move_block_files(block_files)
        solution = self._update_filesystem_checksum(block_files)
        return solution

    def solution_problem_two(self) -> int:
        """Solution of the second problem AoC - Day 9."""
        pass


if __name__ == "__main__":
    day9 = Day9()
    solution1 = day9.solution_problem_one()
    print(solution1)
