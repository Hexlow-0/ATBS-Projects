# Guess the number, twat

import random

secretNumber = random.randint(1, 100)

# While loop
while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess > secretNumber:
        print("Too high")
    elif guess < secretNumber:
        print("Too low")
    else:
        break

print("Well done, Correct! The number was", secretNumber)