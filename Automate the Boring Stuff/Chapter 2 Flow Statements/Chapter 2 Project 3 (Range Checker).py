"""
Write a program that:
Asks the user to enter a number.
Uses try/except to make sure it’s actually a number.

Once you have a valid number, check:
If it’s between 1 and 10 → print: "That’s a small number."
If it’s between 11 and 100 → print: "That’s a medium number."
If it’s greater than 100 → print: "That’s a large number!"
If it’s less than 1 → print: "Too small to count!"

Then ask if they want to check another number.
If yes → repeat.
If no → print a goodbye message and end the program.
"""

# User inputs a number
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Error, enter numbers only, try again.")
        continue

# elif statements check the range
    if num in range(1, 11):
        print("That is a small number.")
    elif num in range(11, 101):
        print("That is a medium number.")
    elif num >= 101:
        print("That's a large number!")
    elif num < 1:
        print("Too small to count!")
        continue

# Ask if the user wants to go again
    again = input("Do you want to check another number? (y/n): ")
    if again == "y": # Program repeats here
        continue
    elif again == "n": # Program exits here
        break
    else:
        print("Error, try again. Enter a 'y' or 'n'.")
        continue





