"""
✅ Requirements:
import random at the top (this is allowed in Chapter 3).
Create a function roll_die() that returns a random number between 1 and 6.

Create another function roll_dice() that:
Calls roll_die() twice
Returns both dice and their sum

Create a function check_win(total) that returns True if the total is 7 or 11, else False.

Create a function play_game() that:

Runs the roll
Prints the two dice and total
Prints win/loss message based on check_win()
Use a loop so the user can keep playing or quit by typing 'q'.
"""

import random

# Returns a random number between 1 and 6
def roll_die():
    return random.randint(1, 6)

# Rolls two dice, returns both individual rolls and the total
def roll_dice2():
    num1 = roll_die()
    num2 = roll_die()
    total = num1 + num2
    return num1, num2, total

# Checks if the total wins or loses
def check_win(num1, num2, total):
    print(f"You rolled a {num1} and a {num2} (Total: {total}).")
    if total == 7 or total == 11:
        print("You won! 🎉")
    else:
        print("You lost! 🙁")

# Runs the game
def play_game():
    play = input("Press Enter to roll the dice (or 'q' to quit): ")
    if play.lower() == 'q':
        print("Thanks for playing!")
        exit()
    else:
        num1, num2, total = roll_dice2()
        check_win(num1, num2, total)

# Loops the game
while True:
    play_game()




