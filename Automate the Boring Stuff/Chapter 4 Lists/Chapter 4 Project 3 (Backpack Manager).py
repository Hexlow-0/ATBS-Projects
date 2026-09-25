"""
Step 1: Simple coin flip - generate a list of 100 random H/T values

To create a list, use a for loop that appends a randomly selected 'H' or
'T' to a list 100 times.

Step 2: Check if a specific streak exists (like checking if 'HHHHHH' appears in your list)
Step 3: Count how many times ANY streak of 6 appears
Step 4: Put it in the 10,000 experiment loop and calculate percentage
"""

import random

numberOfStreaks = 0
list = []
tStreak = 0
hStreak = 0

def flip(list):

    for i in range(100):
        coin = random.randint(0, 1)

        if coin == 0:
            list.append('T')
        else:
            list.append('H')

flip(list)

print(list)
