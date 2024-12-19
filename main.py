"""Main script to execute all AoC solutions."""

from day1 import solution_day_one_problem_one, solution_day_one_problem_two
from day2 import solution_day_two_problem_one, solution_day_two_problem_two
from day3 import solution_day_three_problem_one, solution_day_three_problem_two
from day4 import solution_day_four_problem_one, solution_day_four_problem_two
from day5 import solution_day_five_problem_one, solution_day_five_problem_two
from day6 import Day6
from day7 import Day7
from day8 import Day8
from day9 import Day9

if __name__ == "__main__":
    # Day One - Problem 1
    print("Problem 1 - Day 1 Solution:", solution_day_one_problem_one())
    # Day One - Problem 2
    print("Problem 2 - Day 1 Solution:", solution_day_one_problem_two())

    # Day Two - Problem 1
    print("Problem 1 - Day 2 Solution:", solution_day_two_problem_one())
    # Day Two - Problem 2
    print("Problem 2 - Day 2 Solution:", solution_day_two_problem_two())

    # Day Three - Problem 1
    print("Problem 1 - Day 3 Solution:", solution_day_three_problem_one())
    # Day Three - Problem 2
    print("Problem 2 - Day 3 Solution:", solution_day_three_problem_two())

    # Day Four - Problem 1
    print("Problem 1 - Day 4 Solution:", solution_day_four_problem_one())
    # Day Four - Problem 2
    print("Problem 2 - Day 4 Solution:", solution_day_four_problem_two())

    # Day Five - Problem 1
    print("Problem 1 - Day 5 Solution:", solution_day_five_problem_one())
    # Day Five - Problem 2
    print("Problem 2 - Day 5 Solution:", solution_day_five_problem_two())

    # Day Six
    day6 = Day6()
    print("Problem 1 - Day 6 Solution:", day6.solution_problem_one())
    print("Problem 2 - Day 6 Solution:", day6.solution_problem_two())

    # Day Seven
    day7 = Day7()
    print("Problem 1 - Day 7 Solution:", day7.solution_problem_one())
    print("Problem 2 - Day 7 Solution:", day7.solution_problem_two())

    # Day Eight
    day8 = Day8()
    print("Problem 1 - Day 8 Solution:", day8.solution_problem_one())
    print("Problem 2 - Day 8 Solution:", day8.solution_problem_two())

    # Day Nine
    day9 = Day9()
    print("Problem 1 - Day 9 Solution:", day9.solution_problem_one())
    print("Problem 2 - Day 9 Solution:", day9.solution_problem_two())
