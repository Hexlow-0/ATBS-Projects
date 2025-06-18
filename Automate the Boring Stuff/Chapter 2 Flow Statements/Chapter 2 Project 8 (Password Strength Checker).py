"""
🧱 What it should do:
Prompt the user to enter a password.

Evaluate that password based on the following criteria:

Length:
Less than 6 = “Too short!”
6–10 = “Okay, but could be stronger.”
11+ = “Nice length.”

Contains both letters and numbers = bonus points
Contains at least one special character (like !@#$%^&*) = bonus points

Print a final verdict:
Weak
Medium
Strong

After the result, ask: “Would you like to check another password?”
"""

import string

bonus_points = 0

while True:
    password = input("Enter a password: ")
    bonus_points = 0  # Reset points for each new password

    # Length check
    if len(password) < 6:
        print("Too short!")
        bonus_points += 1
    elif len(password) <= 10:
        print("Okay, but could be stronger.")
        bonus_points += 2
    elif len(password) >= 11:
        print("Nice length.")
        bonus_points += 3

    # Check for both letters and numbers
    if any(char.isalpha() for char in password) and any(char.isdigit() for char in password):
        bonus_points += 1
    else:
        bonus_points -= 1

    # Check for at least one special character
    special_chars = string.punctuation
    if any(char in special_chars for char in password):
        bonus_points += 1

    # Verdict
    if bonus_points <= 2:
        print("Your password has weak strength.")
    elif bonus_points <= 4:
        print("Your password has medium strength.")
    else:
        print("You have a strong password!")

    # Ask if they want to try again
    again = input("Would you like to try another password? (y/n): ")
    if again.lower() != "y":
        print("Goodbye!")
        break
