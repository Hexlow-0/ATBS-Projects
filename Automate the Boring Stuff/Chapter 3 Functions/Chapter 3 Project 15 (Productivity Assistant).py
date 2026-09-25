"""
🛠️ Scenario:
You’re building a simple productivity assistant. It asks users how many hours
they worked today and what kind of work they did (e.g. study, chores, exercise, etc). It then:

Categorizes how productive they were
Gives them a “pep talk” or feedback
Logs a short recap for the day

✅ Your program should:
Ask the user:
How many hours they spent being productive today
What kind of work they did (free text: e.g., “studying” or “cleaning”)
Whether they want feedback or not (y/n)

Use three functions:

calculate_productivity(hours)
Returns a rating like: "Low", "Moderate", or "High"

give_pep_talk(rating)
Prints a message based on the productivity level

log_day_summary(hours, work_type)
Prints a little recap, like:
"You spent 4 hours doing studying today. Well done."

Let the user repeat this process daily (while loop). If they enter 'q', exit.
Optional stretch: Validate inputs (e.g., no negative hours)
"""

# Returns a rating based on the number of hours the user was productive for
def calculate_productivity(hours):
    if hours <= 2:
        rating = "Low"
    elif hours <= 6:
        rating = "Moderate"
    else:  # hours >= 7
        rating = "High"
    return rating

# Provides a mini pep-talk based on the rating
def give_pep_talk(rating):
    if rating == "Low":
        pep1 = "Everyone has days like that, at least you got out of bed! Chin up, and get ready to tackle tomorrow!"
        pep2 = "Keep trying!"
    elif rating == "Moderate":
        pep1 = "Not half bad! One step closer to success, keep going!"
        pep2 = "Good job!"
    elif rating == "High":
        pep1 = "Amazing job!"
        pep2 = "FANTASTIC job, you're well ahead of others!"

    print(pep1) # Prints the pep1
    return pep2 # Carries pep2 as an argument to the log_day_summary

# Provides a summary for the user, with an appropriate finishing comment relevant to their effort
def log_day_summary(hours, work_type, pep2):
    print(f"You spent {hours} hours {work_type}. {pep2}")

# While loop powers the program
while True:
    user_input = input("Enter how many hours you spent being productive (or 'q' to quit): ")
    if user_input.lower() == 'q': # Quits if the user enters 'q'
        print("Goodbye!")
        break

    try:
        hours = int(user_input)
        if hours < 0: # Tests for a number below 0
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue

    work_type = input("Enter what kind of work you did: ")
q
\
    # Function calling block
    want_feedback = input("Do you want feedback? (y/n): ").lower()
    if want_feedback == 'y':
        rating = calculate_productivity(hours) # Rating is equal to the return value of this function
        pep2 = give_pep_talk(rating) # Pep2 stored in the give_pep_talk(rating) function, passing the returned value through
        log_day_summary(hours, work_type, pep2) # Calls log day and passes values if the user wants feedback
    else:
        log_day_summary(hours, work_type, "Keep it up!")
