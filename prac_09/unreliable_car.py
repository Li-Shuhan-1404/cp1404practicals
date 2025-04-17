"""
CP1404/CP5632 Practical
Unreliable car class
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """A version of the car that includes unreliable models."""

    def __init__(self, name, fuel, reliability):
        """Car information"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car when higher than random number"""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance = 0
        distance_drive = super().drive(distance)
        return distance_drive
