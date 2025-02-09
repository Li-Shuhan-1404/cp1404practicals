"""Score menu"""


MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
choices = "GPSQ"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    """Score menu"""
    score = ""
    print(MENU)
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            grade = determine_grade(score)
            print(f"Your {score} is {grade}")
        elif choice == "S":
            print("*" * score)
        print(MENU)
        choice = get_choice()
    print("Farewell")


def get_score():
    """Get score"""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_grade(score):
    """Determine the grade of the score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_choice():
    """Determine choice is valid or not"""
    choice = (input(">>> ")).upper()
    while choice not in choices:
        print("Invalid choice")
        choice = (input(">>> ")).upper()
    return choice


main()
