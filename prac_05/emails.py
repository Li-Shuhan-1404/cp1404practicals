"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    """Convert email to name and print the list"""
    SPECIAL_CHARACTER = "@"
    EMAIL_TO_NAME = {}

    email = input("Email: ")
    while email != "":
        while SPECIAL_CHARACTER not in email:
            print("Error")
            email = input("Email: ")

        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        EMAIL_TO_NAME[email] = name
        email = input("Email: ")
    display_email(EMAIL_TO_NAME)


def get_name(email):
    """Extract the name from the email"""
    name = email.split('@')[0]
    part = name.split('.')
    full_name = " ".join(part).title()
    return full_name


def display_email(EMAIL_TO_NAME):
    """Display name and email"""
    for email, name in EMAIL_TO_NAME.items():
        print(f"{name} ({email})")


main()
