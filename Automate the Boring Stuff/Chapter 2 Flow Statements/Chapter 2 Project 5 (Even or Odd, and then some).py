"""
Enter a number: 8
That number is even.
And it's divisible by 4 — neat!

Do you want to enter another number? (y/n): y

Enter a number: 97
That number is odd.
Also... bit of a weird number. What are you, a philosopher?

Do you want to enter another number? (y/n): n
Thanks for playing!
"""

# User enters their number
while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input, numbers only. Please try again.")
        continue

# These elif statements decide the output
    if number % 2 == 0 and number % 4 == 0:
        print("The number is even!")
        print("And it's divisible by 4!")
    elif number % 2 == 0:
        print("The number is even!")
    elif number % 1 == 0 and number > 50:
        print("The number is odd!")
        print("Also...it's a bit of a weird number!")
    elif number % 2 != 0:
        print("The number is odd!")

# Ask the user if they want to play again
    again = input("Do you want to enter another number? (y/n): ")
    if again == "y":
        continue
    elif again == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input, try again.")
        continue



