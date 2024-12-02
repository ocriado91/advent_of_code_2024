"""Example of Calculator package usage."""

from calculator import Calculator

if __name__ == "__main__":
    print("10 + 4 = ", Calculator.sum(10, 4))
    print("10 - 4 = ", Calculator.substract(10, 4))
    print("10 * 4 = ", Calculator.multiplication(10, 4))
    print("10 / 4 = ", Calculator.division(10, 4))
