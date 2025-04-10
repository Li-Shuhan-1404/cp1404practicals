from prac_09.unreliable_car import UnreliableCar


def main():
    """Test car can drive or not"""
    car = UnreliableCar("Mika", 90, 40)

    print(f"{car.name} drove {car.drive(100)}km")


main()
