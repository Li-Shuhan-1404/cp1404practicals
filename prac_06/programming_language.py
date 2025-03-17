"""
CP1404/CP5632 Practical
Own simple class for a programming language
"""


class ProgrammingLangauge:

    def __init__(self, name="", typing="", is_reflection=False, year=0):
        """Initializing Properties"""
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        """Returns true if the input is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_reflection}, First appeared in {self.year}"
