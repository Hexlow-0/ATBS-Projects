""""
TASK: HABIT HELPER.

You're going to build a simple tool that helps users reflect on their daily habit routines. It'll:
Ask the user for a habit name
Ask how many minutes they spent on it today
Ask how satisfying the session felt (scale of 1–10)

Use that info to:
Give feedback
Score the day
Suggest something motivational
"""


def score_day(minutes, satisfaction):
    if minutes < 5 and satisfaction < 5:
        score = "Low"
    elif minutes >= 10 and satisfaction >= 5:
        score = "Moderate"
    elif minutes >= 30 and satisfaction >= 8:
        score = "High"

    return score

def get_motivation(score):
    if score == "Low":
        print("Keep trying!")
    elif score == "Moderate":
        print("Good job!")
    elif score == "High":
        print("You crushed it!")

def log_summary(habit, minutes, score):
    print(f"You spent {minutes} {habit} today. {score}: ")


while True:

    habit = input("Enter your habit name or enter 'q' to quit: ")
    if habit.lower() == "q":
        print("Goodbye!")
        break

    try:

        user_input = input("Enter how many minutes have spent on your habit today: ")
        minutes = int(user_input)
        if minutes < 0:  # Tests for a number below 0
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue

    user_input2 = input("Enter your satisfying session felt on a scale of one to ten: ")
    satisfaction = int(user_input2)

    score = score_day(minutes, satisfaction)
    get_motivation(score)
    log_summary(habit, minutes, score)

