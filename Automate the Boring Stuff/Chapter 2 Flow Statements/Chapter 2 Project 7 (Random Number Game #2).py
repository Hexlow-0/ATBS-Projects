"""
🧩 Requirements:
The secret number is hardcoded, e.g. 13.
The user gets up to 5 guesses.

After each wrong guess:
If the guess is too high, tell them "Too high!"
If the guess is too low, tell them "Too low!"
If they guess correctly, congratulate them and end the game early.
If they fail all 5 times, tell them the number and end the game.
"""

# Import random module
import random

# Define secret number range
secret = random.randint(1, 50)
attempts = 0

# While loop continues while guesses are less than 5
while attempts < 5:
    try:
        guess = int(input("Guess a number between 1 and 50: "))
        if guess > 50 or guess < 1: # Ensures user enters a number between 1 and 50
            print("Enter a number between 1 and 50!")
            continue
    except ValueError:
        print("Invalid, numbers only.")
        continue

# "attempts" keeps track of the users tries and the elif statements tell the user to guess higher or lower
    if guess > secret:
        attempts += 1
        print("Too high! Attempts left:", 5 - attempts)
    elif guess < secret:
        attempts += 1
        print("Too low! Attempts left:", 5 - attempts)
    elif guess == str(): # Anything that isn't a number won't count to the attempts
        print("Error, numbers only, try again!")
    else:
        print("Congratulations! You guessed it in", attempts, "attempts.")
        break

else: # Break the loop if the exceed reach/exceed 5 guesses
    print("No luck! The number was:", secret)
    exit()

