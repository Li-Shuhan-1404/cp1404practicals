"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    def __init__(self, name=""):
        """Band information"""
        self.name = name
        self.members = []
        self.member_instruments = {}

    def __str__(self):
        """Band output"""
        return f"{self.name} ({str(self.members).strip('[').strip(']')}"

    def add(self, musician):
        """Add musician to band"""
        self.member_instruments[musician.name] = musician.instruments
        self.members.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        """Musician play instruments if they have"""
        for member in self.member_instruments:
            if not self.member_instruments[member]:
                print(f"{member} needs an instrument!")
            else:
                print(f"{member} is playing: {self.member_instruments[member][0]}")
