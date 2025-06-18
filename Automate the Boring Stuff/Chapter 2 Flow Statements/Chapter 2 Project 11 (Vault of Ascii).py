"""
Mini-Project: The Vault of Ascii
You are a master codebreaker trying to bypass a three-layered security system on the "Vault of Ascii." To get in, you must correctly guess three secret numbers in a row. Each number is between 1 and 25. Are you up to the challenge?

Project Goal
Your mission is to write a Python script that functions as a multi-stage number guessing game. The program must successfully guide a player through three consecutive rounds of guessing a secret number. If the player fails at any stage, the vault's defenses activate, and the game is over.

Rules & Requirements
Three Stages: The game must consist of three sequential stages. The player must clear all three to win.
Secret Numbers: Before each stage, the program must generate a new random integer between 1 and 25 (inclusive). You'll need to use the random module for this.
Limited Guesses: The player only gets five attempts to guess the secret number at each stage.
Hints: After every incorrect guess, the program must provide a hint, telling the player whether their guess was "Too high!" or "Too low!".
Input Validation: The program must check if the player's guess is within the valid range of 1 to 25. If the player enters a number outside this range (e.g., 0 or 26), it should print an error message like "Invalid range. Guess must be between 1 and 25." This guess should not count as one of their five attempts.
Stage Progression:
If the player guesses the number correctly within five attempts, a success message like "Stage 1 Cleared! Moving to the next level..." should be displayed. The game then immediately proceeds to the next stage with a new secret number.
If the player fails to guess the number in five attempts, the game ends immediately. A failure message must be shown, revealing the secret number (e.g., "System lockdown! The correct number was 17. Better luck next time.").
Winning the Game: If the player successfully clears all three stages, a final victory message should be displayed, for example: "Access Granted! You have successfully bypassed all three security layers of the Vault of Ascii."
Required Concepts Checklist
Your final code must make meaningful use of the following concepts and only these concepts (plus basic operators and the print() and input() functions):

[ ] import statement (specifically import random)
[ ] for loops and the range() function
[ ] while loops
[ ] if, elif, and else statements
[ ] break statements
[ ] continue statements
Challenge Tip: Think about how you can use nested loops. An outer loop could manage the three stages of the game, while an inner loop handles the five guesses for each stage. Where would break and continue be most effective in controlling these loops? Good luck! 🧐
"""

# Import the random module
import random

# Define secret numbers for each stage
secret1 = random.randint(1, 25)
secret2 = random.randint(1, 50)
secret3 = random.randint(1, 100)

# Set attempt numbers for each stage
attempts1 = 0
attempts2 = 0
attempts3 = 0

# Ask the user if they wanna play
while True:
    play = input("Welcome to the Vault of Ascii! Ready to play (y/n)").lower()
    if play == "y":
        print("Have fun!")
        break # Breaks loop, moves onto Stage One
    elif play == "n":
        print("Pussy")
        exit()
    else:
        print("Invalid input. Please try again. Enter a 'y' for yes or 'n' for no.")


# Introduction to the game
print("There are three stages...")
print("You get 5 tries to guess the secret number...")
print("Failure on any stage will lock the vault for good!")
print("If you succeed? The clout is yours.")

# STAGE ONE
while attempts1 < 5:
    try: # Catches non-integer inputs
        guess1 = int(input("Enter a number between 1 and 25: "))
    except ValueError:
        print("Numbers only, no letters or symbols!")
        continue

    # Keeps guesses between the defined range
    if guess1 < 1 or guess1 > 25:
        print("Nice try - numbers gotta be between 1 and 25. Try again.")
        continue

    # Check the users guess against the secret number
    if guess1 > secret1:
        attempts1 += 1
        print("Too high!")
        continue
    elif guess1 < secret1:
        attempts1 += 1
        print("Too low!")
        continue
    else: # Correct guess
        print("Stage 1 Cleared! Moving to the next level...")
        break

# Breaks the loop if the users guess is above 5 guesses
else:
    print("System lockdown! The correct number was", str(secret1), "Better luck next time!")
    exit()

# Congrats on passing stage one
print("Congrats! Stage one passed...")
print("Since that was a piece of cake, the difficulty is amping up...")
print("The secret is between 1 and 50, 7 guesses.")
print("Best of luck!")

# STAGE TWO
while attempts1 < 8:
    try:  # Catches non-integer inputs
        guess2 = int(input("Enter a number between 1 and 50: "))
    except ValueError:
        print("Numbers only, no letters or symbols!")
        continue

    # Keeps guesses between the defined range
    if guess2 < 1 or guess2 > 50:
        print("Nice try - numbers gotta be between 1 and 50. Try again.")
        continue

    # Check the users guess against the secret number
    if guess2 > secret2:
        attempts2 += 1
        print("Too high!")
        continue
    elif guess2 < secret2:
        attempts2 += 1
        print("Too low!")
        continue
    else:  # Correct guess
        print("Stage 2 Cleared! Moving to the next level...")
        break

# Breaks the loop if the users guess is above 7 guesses
else:
    print("System lockdown! The correct number was", str(secret2), "Better luck next time!")
    exit()

print("Well done, stage 2 is comlplete!")
print("One more stage to go...10 guesses. Good luck!")

# STAGE THREE
while attempts3 < 10:
    try:  # Catches non-integer inputs
        guess3 = int(input("Enter a number between 1 and 100: "))
    except ValueError:
        print("Numbers only, no letters or symbols!")
        continue

    # Keeps guesses between the defined range
    if guess3 < 1 or guess3 > 100:
        print("Nice try - numbers gotta be between 1 and 100. Try again.")
        continue

    # Check the users guess against the secret number
    if guess3 > secret3:
        attempts3 += 1
        print("Too high!")
        continue
    elif guess3 < secret3:
        attempts3 += 1
        print("Too low!")
        continue
    else:  # Correct guess
        print("Stage 3 Cleared, Vault of Ascii has unlocked, and the clout it yours!!!")
        break

# Breaks the loop if the users guess is above 10 guesses
else:
    print("System lockdown! The correct number was", str(secret3), "Better luck next time!")
    exit()