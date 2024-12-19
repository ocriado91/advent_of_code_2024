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

    def _extract_block_free_sizes(self, block_files: deque) -> deque:
        """Extract the starting point and the size of the free space blocks."""
        block_free_index_sizes = []
        start = 0
        while True:
            try:
                block_id = block_files.index(None, start)
            except ValueError:
                break
            starting_block_id = block_id
            block_size = 0
            while block_files[block_id] is None:
                block_size += 1
                block_id += 1
                if block_id == len(block_files):
                    break
            block_free_index_sizes.append((starting_block_id, block_size))
            start = block_id
        return block_free_index_sizes

    def _move_entire_block_files(self, block_files: deque) -> deque:
        """Move all block sizes to a free space location."""
        block_id = max(x for x in block_files if x is not None)
        # Transform block list to list to allow slicing operations.
        block_files = list(block_files)
        while block_id > 0:
            # We need to detect the starting point and the size of the
            # free space blocks.
            block_free_index_sizes = self._extract_block_free_sizes(
                block_files
            )
            # Extract the block size of current block ID.
            block_size = block_files.count(block_id)
            block_id_start = block_files.index(block_id)
            # Compute the available free blocks for current block size.
            for start, size in block_free_index_sizes:
                if block_size > size or start > block_id_start:
                    # Current free space block cannot allocate current
                    # block size or the start point of free space is to the
                    # right of the block file. Try with the next one.
                    continue
                # Found an available free space size that fits the current
                # block size. Move the block file to this position
                count = 0
                while block_size > count:
                    block_files[start + count] = block_id
                    others = block_files[start + count + 1 :]
                    other_block_id_positions = [
                        idx for idx, x in enumerate(others) if x == block_id
                    ]
                    for x in other_block_id_positions:
                        others[x] = None

                    block_files[start + count + 1 :] = others
                    count += 1
                # Already found a free space block. Break the loop.
                break
            # Decrease the block ID to the next iteration.
            block_id -= 1
        return deque(block_files)

    def _update_filesystem_checksum(self, block_files: deque) -> int:
        """Compute the filesystem checksum."""
        sum = 0
        for idx, x in enumerate(block_files):
            if x is None:
                continue
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
        block_files = self._extract_block_files()
        block_files = self._move_entire_block_files(block_files)
        solution = self._update_filesystem_checksum(block_files)
        return solution


if __name__ == "__main__":
    day9 = Day9()
    solution1 = day9.solution_problem_one()
    print(solution1)
