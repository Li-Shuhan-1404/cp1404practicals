"""Password stars"""


LENGTH = 8


def main():
    """Get the password and type it with asterisks"""
    password = get_password()
    asterisks = print_asterisks(password)
    print(f"{asterisks}")


def print_asterisks(password):
    """Turn password to asterisks"""
    return '*' * len(password)


def get_password():
    """Sure password at least length"""
    password = input("Enter a password: ")
    while len(password) < LENGTH:
        print(f"Password must be at least {LENGTH} characters long. Please try again.")
        password = input("Enter a password: ")
    return password


main()
