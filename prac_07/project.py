"""
CP1404/CP5632 Practical
Class for project
"""


class Project:
    def __init__(self, name="", start_date="", priority=int, cost=float, complete=int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.complete = complete

    def __str__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost}, {self.complete}"

    def __lt__(self, other):
        return self.priority <= other.priority
