"""Advent Of Code 2024 - Solution of Day 10."""

from heapq import heapify, heappop, heappush
from solution import Solution


class Day10(Solution):
    """Solution class of AoC Day 10 Solution."""

    def __init__(self, puzzle_input: str = "data/day10.dat") -> None:
        """Initialize the Day 10 solution class."""
        Solution.__init__(self, puzzle_input)

        self.graph = dict()
        self.convert_to_graph()

    def extact_neighbors(self, position=tuple) -> dict:
        """Compute the neighbors from a given position."""
        directions = [
            (-1, 0),  # Up
            (1, 0),  # Down
            (0, -1),  # Right
            (0, 1),  # Left
        ]
        neigh_dict = dict()
        for direction in directions:
            x_pos = position[0] + direction[0]
            y_pos = position[1] + direction[1]
            if x_pos not in range(len(self.lines)) or y_pos not in range(
                len(self.lines[0])
            ):
                continue
            neigh_position = (x_pos, y_pos)
            neigh_value = self.lines[x_pos][y_pos]
            neigh_dict[neigh_position] = int(neigh_value)
        return neigh_dict

    def shortest_path(self, source: tuple):
        """Extract the shortest path using Dijkstra algorithm."""
        weights = {node: float("inf") for node in self.graph}
        weights[source] = 0

        # Node with the smallest value and visit its neighbors.
        priority_queue = [(0, source)]
        heapify(priority_queue)

        # Create a set to store visited nodes.
        visited = set()
        while priority_queue:
            # Extract the first element of queue.
            current_distance, current_node = heappop(priority_queue)
            # Discard current node if has been visited before.
            if current_node in visited:
                continue
            # Add current node to visited set.
            visited.add(current_node)

            # Extract the neighbors and their weights of the current node
            for neighbor, weight in self.graph[current_node].items():
                # Compute the gradient of the neighbor and its
                # related node.
                gradient = weight - current_distance
                # According to the challenge description, this gradient must be
                # "even, gradual and uphill slope", so just extract the
                # neighbors with a gradient equal to one to report accomplish
                # trails with the challenge requirements.
                if gradient == 1:
                    weights[neighbor] = weight
                    heappush(priority_queue, (weight, neighbor))

        return weights

    def convert_to_graph(self) -> list:
        """Convert puzzle lines to neighbors graph."""
        for idx in range(len(self.lines)):
            for idy in range(len(self.lines[0])):
                position = (idx, idy)
                self.graph[position] = self.extact_neighbors(position)

    def solution_problem_one(self) -> int:
        """Solution of the first problem of AoC - Day 10."""
        sum = 0
        for idx, row in enumerate(self.lines):
            cols = row.strip()
            for idy, col in enumerate(cols):
                if col == "0":
                    trails = self.shortest_path((idx, idy))
                    # According to shortest_path method,
                    # the trails variable contains the trail with a gradient
                    # equal to one within elements. If there is a element with
                    # a weight equal to 9, there is a trail with an "even,
                    # gradual and uphill slope" that reaches the element 9 =
                    # there is trailhead.
                    sum += list(trails.values()).count(9)
        return sum

    def extract_number_positions(self, numbe: int = 9):
        """Extract all positions into the grid of a given number."""
        positions = []
        for idx, row in enumerate(self.lines):
            cols = row.strip()
            for idy, col in enumerate(cols):
                if col == "9":
                    positions.append((idx, idy))
        return positions

    def depth_first_search(
        self,
        node: tuple,
        previous_value: int = 0,
        count: int = 0,
        visited: set = None,
    ):
        """Implement a recursive DSF algorithm."""
        # Initialize visited set if is empty.
        if visited is None:
            visited = set()

        # Add node to visited
        visited.add(node)
        # Check if current node is within the desired values
        if node in self.extract_number_positions():
            count += 1

        # Extract all neighbors of current node and their related values.
        for neighbor_node, value in self.graph[node].items():
            diff_value = value - previous_value
            if diff_value == 1:
                count = self.depth_first_search(
                    neighbor_node, value, count, visited
                )
        return count

    def solution_problem_two(self) -> int:
        """Solution of the second problem of AoC - Day 10."""
        total_count = 0
        for idx, row in enumerate(self.lines):
            cols = row.strip()
            for idy, col in enumerate(cols):
                if col == "0":
                    source_node = (idx, idy)
                    count = self.depth_first_search(source_node)
                    total_count += count
        return total_count


if __name__ == "__main__":
    day10 = Day10()
    solution1 = day10.solution_problem_one()
    print(solution1)

    solution2 = day10.solution_problem_two()
    print(solution2)
