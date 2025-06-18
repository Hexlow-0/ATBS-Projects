"""
📋 Requirements:
Ask the user to enter their test score.
Make sure the score is a number between 0 and 100. If not, ask again.

Once a valid score is entered, grade it based on:
90–100: A
80–89: B
70–79: C
60–69: D
<60:   F

After printing the grade, ask: “Do you want to enter another score? (y/n)”
'y' → Restart
'n' → Exit
Anything else → Error message and ask again
"""

# Ask user for their score
while True:
    try:
        grade = float(input("Enter your test score: "))
    except ValueError:
        print("Sorry, enter only numbers. Try again.")
        continue

# Give the use a grade based on their score
    if grade > 100:
        print("Whoa! Extra credit? Let’s stick to 0–100.")
    elif grade >= 90:
        print("Your grade is 'A', well done!")
    elif grade >= 80:
        print("Your grade is 'B', not bad!")
    elif grade >= 70:
        print("Your grade is 'C', you passed!")
    elif grade >= 60:
        print("Your grade is 'D', you... should have studied more.")
    elif grade >= 0:
        print("Your grade is 'F', you failed.")
    else:
        print("That doesn’t seem like a valid score.")


# Ask user if they wanna enter another number
    again = input("Do you want to enter another score? (y/n)")
    if again == 'y':
        continue
    elif again == 'n':
        print("Thanks!")
        break
    else:
        print("Error, enter a 'y' or 'n' only, try again.")
        continue
