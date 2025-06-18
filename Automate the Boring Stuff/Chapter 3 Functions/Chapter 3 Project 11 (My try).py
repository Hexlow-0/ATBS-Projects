# This is my first ever program that I'm building by myself

"""
1. "The Procrastinator’s Time Calculator"
📌 Goal: A function that tells you how much time you’ve wasted (or invested!) in repetitive tasks.

Example:

time_calculator(task, minutes_per_day, days) → calculates total hours spent.

time_calculator("scrolling memes", 120, 365) → "You spent 730.0 hours scrolling memes in a year!"
Twist: Add a function to convert hours into days or even Netflix seasons (assume 1 season = 10 hours).
"""


def time_culculator(task, minutes_per_day, days):
    total_minutes = minutes_per_day * days
    total_hours = total_minutes / 60  # Convert minutes to hours

    return total_hours

while True:
    print("Welcome to the procastinator's time calculator!\n")
    print("You'll be asked how much time you spend on your activity and then be shown how much life you waste in a year!")

    task = input("Enter whatever activity or task you spend time on: ")
    minutes = input("Enter how many minutes you think you spend on it: ")
    days = input("Enter how many days do you want to calculate for: ")

    time_culculator(task, minutes, days)

    print(f"You spent {total hours} hours {task} in {days} days.")