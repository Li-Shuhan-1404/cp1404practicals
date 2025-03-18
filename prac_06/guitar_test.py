"""
CP1404/CP5632 Practical
Program for testing Guitar class can identify
"""

from prac_06.guitar import Guitar


def run_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar_1 = Guitar(name, year, cost)
    guitar_2 = Guitar("Another Guitar", 2013, 1512.9)

    print(f"{guitar_1.name} get_age() - Excepted {103}. Got {guitar_1.get_age()}")
    print(f"{guitar_2.name} get_age() - Excepted {12}. Got {guitar_2.get_age()}")
    print(f"{guitar_1.name} is_vintage() - Except {True}. Got {guitar_1.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Except {False}. Got {guitar_2.is_vintage()}")


run_test()
