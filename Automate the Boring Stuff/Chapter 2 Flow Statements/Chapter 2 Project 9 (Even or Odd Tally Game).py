"""
Task:
Create a program where the user repeatedly enters numbers. The program should keep track of how many of the numbers are even and how many are odd.

It should:
Keep asking the user to enter numbers until they type 'done'.
If they type something that isn’t a number or 'done', give an error and re-prompt.
At the end, show how many even and how many odd numbers the user entered.

(Stretch): Also tell the user whether they entered more evens or more odds — or if it was a tie.
"""

even = 0
odd = 0

# User is promted for an input
while True:
    input_value = input("Enter a number or type 'done' to finish: ") # Takes input as string

    if input_value == 'done': # Only executes when user types 'done'.
        print("Even:", even)
        print("Odd:", odd)

        if odd > even:
            print("You entered more odds than even!")
        elif even > odd:
            print("You entered more evens than odd!")
        elif even == odd:
            print("The tally of even and odd numbers is equal!")
        break

    try:
        number = int(input_value) # Converts string input to an integer
    except ValueError:
        print("That's not a number, try again.")
        continue

    if number % 2 == 0: # Counts even numbers
        even += 1
    elif number % 2 == 1: # Counts odd numbers
        odd += 1





