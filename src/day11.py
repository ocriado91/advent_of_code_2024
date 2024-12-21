"""Advent Of Code 2024 - Solution of Day 11."""

from solution import Solution


class Day11(Solution):
    """Solution class of AoC Day 11 Solution."""

    def __init__(self, puzzle_input: str = "data/day11.dat") -> None:
        """Initialize the Day 11 solution class."""
        Solution.__init__(self, puzzle_input)

        # Store the initial stones digits
        self.stones = self.lines[0].split()

    def solution_problem_one(self) -> int:
        """Solution of the first problem of AoC - Day 11."""
        blinking_times = 0
        blinking_end = 25
        while blinking_end > blinking_times:
            stones = []
            for stone in self.stones:
                # Apply first rule -> If the stone is engraved with the number
                # 0, it is replaced by a stone engraved with the number 1.
                if stone == "0":
                    stone = "1"
                    stones.append(stone)
                # Apply second rule -> If the stone is engraved with a number
                # that has an even number of digits, it is replaced by two
                # stones. The left half of the digits are engraved on the new
                # left stone,and the right half of the digits are engraved on
                # the new right stone. (The new numbers don't keep extra
                # leading zeroes: 1000 would become stones 10 and 0.)
                elif len(stone) % 2 == 0:
                    half_position = int(len(stone) / 2)
                    first_half_stone = str(int(stone[:half_position]))
                    second_half_stone = str(int(stone[half_position:]))
                    stones.append(first_half_stone)
                    stones.append(second_half_stone)
                # Apply third rule -> If none of the other rules apply, the
                # stone is replaced by a new stone; the old stone's number
                # multiplied by 2024 is engraved on the new stone.
                else:
                    stone = str(int(stone) * 2024)
                    stones.append(stone)
            blinking_times += 1
            # Update original stones
            self.stones = stones
        return len(self.stones)

    def solution_problem_two(self) -> int:
        """Solution of the second problem of AoC - Day 11."""
        pass


if __name__ == "__main__":
    day11 = Day11()
    solution1 = day11.solution_problem_one()
    print(solution1)

    solution2 = day11.solution_problem_two()
    print(solution2)
