"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a silver service taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Taxi information"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string output"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get current fare"""
        return self.flagfall + super().get_fare()
