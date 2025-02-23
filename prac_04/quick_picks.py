import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

turn = int(input("How many quick picks? "))
for i in range(turn):
    numbers = []
    for n in range(NUMBERS_PER_PICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(number)
    numbers.sort()
    number_format = " ".join(f"{number:2}" for number in numbers)
    print(number_format)
