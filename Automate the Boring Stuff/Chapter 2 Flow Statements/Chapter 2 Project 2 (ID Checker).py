# ID Checker
"""
Ask the user their age.

If they enter a non-numeric input, show an error and ask again (hint: try/except).
If the user is under 18, deny access.
If the user is 18 or older, ask if they have a valid ID (yes or no).
If they say "no", deny access.
If they say "yes", let them in.
If they enter anything else, show a custom message (“That’s not a yes or no, try again.”)

Bonus Logic:
If the user is exactly 18, show a custom message: "Just made it!"
If age is greater than 130, say: "That's...unlikely. Try again." and restart
"""

# Ask the user for their input
while True:
    try:
        print("Welcome to the club!")
        age = int(input("What is your age? "))
    except ValueError:
        print("Sorry, that's not a number. Try again.")
        continue

# Check the users age and respond accordingly
    if age > 130:
        print("That's...unlikely. Try again.")
        continue
    elif age < 18:
        print("You're a minor, no entry!")
        break
    elif age == 18:
        print("Just made it!")
    elif age >= 18:
        id = input("Do you have have a valid ID (yes or no): ")
        if id == "yes":
            print("Access granted, come on in!")
            break
        elif id == "no":
            print("Access denied, come back with a valid ID!")
            break
        else:
            print("Sorry, that's not a yes or no. Try again.")
            continue