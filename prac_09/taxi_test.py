from prac_09.taxi import Taxi


def main():
    """Test Taxi class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)

    print(f"Taxi details: {my_taxi}")
    print(f"Current fare: ${my_taxi.get_fare()}")

    my_taxi.start_fare()
    my_taxi.drive(100)

    print(f"Taxi details: {my_taxi}")
    print(f"Current fare: ${my_taxi.get_fare()}")


main()
