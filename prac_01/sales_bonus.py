"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LESS_BONUS = 0.10
MORE_BONUS = 0.15
LIMIT_SALES = 1000
MINIMUM = 0

sales = float(input("Enter sales: $"))
while sales >= MINIMUM:
    bonus = sales
    if sales < LIMIT_SALES:
        bonus *= LESS_BONUS
    else:
        bonus *= MORE_BONUS
    print(f"The sales bonus is ${bonus:.0f}")
    sales = float(input("Enter sales: $"))

print("Done")
