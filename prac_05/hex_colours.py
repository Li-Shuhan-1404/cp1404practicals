"""
CP1404/CP5632 Practical
Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.
"""

COLOUR_TO_CODE = {"Alice Blue": "#f0f8ff", "Aqua": "#00ffff", "Blond": "#faf0be", "Bistre": "#3d2b1f",
                  "Buff": "#f0dc82", "Cyclamen": "#f56fa1", "Ebony": "#555d50", "Floral White": "#fffaf0",
                  "Indigo": "#4b0082", "Iris": "#5a4fcf"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
