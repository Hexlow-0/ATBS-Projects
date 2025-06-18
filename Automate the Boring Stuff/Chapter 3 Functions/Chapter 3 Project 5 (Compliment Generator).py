"""
🌱 Mini Project: Compliment Generator

Asks the user for their name ✅
Uses a function to generate a random compliment ✅
Uses another function to say goodbye ✅
"""
import random

def compliment(name):
    compliments = ["You're awesome!", "You're smart!", "You're kind!", "You're doing great!"]
    return f"Hello {name}, {random.choice(compliments)}"

def farewell():
    print("Cya later!")

# Ask for name once
name = input("What is your name? ")

# Give the first compliment
print(compliment(name))

# Keep offering compliments
while True:
    again = input("Would you like another compliment? (y/n): ").lower()
    if again == "y":
        print(compliment(name))
    elif again == "n":
        farewell()
        break
    else:
        print("Please enter y or n.")
