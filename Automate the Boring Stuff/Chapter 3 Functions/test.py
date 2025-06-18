

while True:
    try:
        bill = int(input("Enter bill amount: "))
        tip = int(input("Enter tip percentage: "))
        break
    except ValueError:
        print("Invalid input, numbers only")
        continue

tip_amount = bill * tip
print(tip_amount)