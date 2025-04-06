"""
CP1404/CP5632 Practical
Program to sort by year and output guitars
"""

import csv
from prac_07.guitar import Guitar
FILENAME = "guitars.csv"


def mian():
    """Add guitar and write in the list"""
    guitars = []
    print("My guitars!")
    read_file(guitars)
    get_guitar(guitars)

    guitars.sort()

    if guitars:
        print("There are my guitars:")

        for i, guitar in enumerate(guitars, 1):
            print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f}")
        save_guitar(guitars)
    else:
        print("No guitars")


def get_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(f"{guitar_add} added.")
        name = input("Name: ")


def read_file(guitars):
    """Get guitar from file"""
    with open(FILENAME, 'r') as in_file:
        reader = csv.reader(in_file)
        for line in reader:
            name = line[0]
            year = int(line[1])
            cost = float(line[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)


def save_guitar(guitars):
    """Save guitar to the file"""
    with open(FILENAME, 'w') as save_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=save_file)


mian()
