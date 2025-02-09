"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    """Get score and output to grade"""
    score = get_score()
    grade = determine_grade(score)
    print(f"Your score is {grade}")
    random_number = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE + 1)
    random_grade = determine_grade(random_number)
    print(f"{random_number} - {random_grade}")


def get_score():
    """Get the score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_grade(score):
    """Determine the grade of score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
