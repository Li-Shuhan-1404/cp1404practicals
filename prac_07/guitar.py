"""
CP1404/CP5632 Practical
Class for guitar
"""
CURRENT_YEAR = 2025
VINTAGE_YEAR = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        """Construct guitar data name"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Repeat data text output"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Determine the Age of Your Guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determining whether a guitar is good quality"""
        return self.get_age() >= VINTAGE_YEAR
