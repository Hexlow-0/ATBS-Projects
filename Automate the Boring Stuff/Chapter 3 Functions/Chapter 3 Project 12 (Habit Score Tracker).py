"""
Get input from the user:
Habit name
Days done
Minutes per day

Have a function called calculate_score(days, minutes_per_day)
It returns the score

Have another function called give_feedback(score)
It returns a string of feedback based on the score

Call the functions and show the final message:
You earned a score of 820 for your 'reading' habit.
💪 You're doing great!

Let the user repeat until they type 'q' for habit name
"""

# Calculates the user's score based on number of days and minutes entered
def calculate_score(days, minutes_per_day):
    score = days * minutes_per_day
    return score  # return the value so it can be used elsewhere

# Shows the final message based on user input
def give_feedback(habit, score):
    print(f"\nYou earned a score of {score} for your '{habit}' habit.")

    if score > 2000:
        print("oh my lawd.!")
    elif score > 1000:
        print("You're on fire, keep going!")
    elif score > 500:
        print("You're doing great!")
    else:
        print("Keep building that habit!")

# This loop continues unless the user enters 'q'.
while True:
    habit = input("Enter whatever habit you want to score, or enter 'q' to quit: ")

    if habit.lower() == 'q':
        print("Thanks for playing!")
        break  

    # Get days and minutes from the user
    try:
        days = int(input("Enter how many days you've done the habit for in a row: "))
        minutes = int(input("Enter how many minutes you spend on your habit per day: "))
    except ValueError:
        print("Numbers only, please. Try again.")
        continue

    # Use the return value
    score = calculate_score(days, minutes)
    give_feedback(habit, score)













