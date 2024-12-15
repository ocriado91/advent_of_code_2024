"""Advent Of Code 2024 - Solution of Day 7."""

from solution import Solution


class Day7(Solution):
    """Solution class of AoC Day7 Solution."""

    def __init__(self, puzzle_input: str = "data/day7.dat") -> None:
        """Initialize the Day7 solution class."""
        Solution.__init__(self, puzzle_input)

        # Split expected results from numbers
        self.expected_results = []
        self.numbers = []
        for line in self.lines:
            _expected_result, _number = line.split(":")
            self.expected_results.append(int(_expected_result))

            # Split all numbers and convert them to integers
            _number = _number.split()
            _number = [int(x) for x in _number]
            self.numbers.append(_number)

    def solution_problem_one(self) -> int:
        """Solution of first problem of AoC - Day 7."""
        sum = 0
        for index in range(len(self.expected_results)):
            expected_result = self.expected_results[index]
            numbers = self.numbers[index]

            # Add first number into result list
            results = []
            results.append(numbers[0])

            running = False
            for idx in range(1, len(numbers)):
                # Break the current loop if any set of operators
                # match with the expected output or the add operations
                # exceeds the expected number.
                if running:
                    break
                number = numbers[idx]
                new_results = []
                for idy in range(-(2 ** (idx - 1)), 0):
                    result = results[idy]

                    add_result = number + result
                    new_results.append(add_result)

                    # Check if adding result matches with the expected
                    # output and breaks the current loop and set the running
                    # flag.
                    if add_result == expected_result:
                        running = True
                        sum += expected_result
                        break

                    mult_result = number * result
                    new_results.append(mult_result)

                    # Same for multiplication operation.
                    if mult_result == expected_result:
                        running = True
                        sum += expected_result
                        break

                # Concatenate new results to results.
                results += new_results
        return sum

    def solution_problem_two(self) -> int:
        """Solution of the second problem of Aoc - Day 7."""
        solution = 0
        return solution


if __name__ == "__main__":
    day7 = Day7()
    solution1 = day7.solution_problem_one()
    print("Solution1:", solution1)

    solution2 = day7.solution_problem_two()
    # print(solution2)
