
items = [
    ("Coffee", 4.50),
    ("Sandwich", 8.90),
    ("Orange Juice", 5.20),
    ("Chocolate Cake", 6.75),
]

store = "the daily grind"
city = "sydney"

space = 18

print('=' * 40)
print(f"{store} - {city}".upper().center(40))
print('=' * 40)

print("Item".ljust(space) + "Price")
print(("-" * 4).ljust(space) + "-" * 5)

total = 0

sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

for item, price in sorted_items:

    total += price

    print(f"{item}".ljust(space) + f"${price:.2f}")


print('=' * 40)
print(f"Total:".ljust(space) + f"${total:.2f}")
print('=' * 40)

