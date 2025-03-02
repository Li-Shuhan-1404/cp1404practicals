DISCOUNT = 0.10
PRICE_LIMIT = 100
total_price = 0

number = int(input("Number of items: "))

while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))

for items in range(number):
    item = float(input("Price of item: "))
    total_price += item

if total_price > PRICE_LIMIT:
    total_price = total_price - total_price * DISCOUNT
print(f"Total price for {number} items is ${total_price:.2f}")
