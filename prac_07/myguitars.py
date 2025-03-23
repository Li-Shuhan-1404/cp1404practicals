"""
CP1404/CP5632 Practical
Program to sort by year and output guitars
"""

import csv
from prac_07.guitar import Guitar
FILENAME = "guitars.csv"


def mian():
    """"""
    data = open_file(FILENAME)
    data.sort()
    for a in data:
        print(a)


def open_file(filename):
    guitars = []
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file)
        for line in reader:
            name = line[0]
            year = int(line[1])
            cost = float(line[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars






mian()
