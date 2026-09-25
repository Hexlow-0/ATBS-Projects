"""
Idea:
The user enters how they’re feeling, and the program returns a suggestion for an activity
or phrase based on a mix of emotion strength + category.
"""

# Suggest feedback function provides the user with an activity or phrase depending on their emotion and it's strength
def suggest_feedback(emotion, strength):

    # If the emotion strength is equal to or greater than 7, print this:
    if emotion == "sad" and strength >= 7:
        print("That's a deep sadness...try get some rest or talk to a friend. :)")
    elif emotion == "happy" and strength >= 7:
        print("That's awesome, ride that wave! Go do something you love. :)")
    elif emotion == "angry" and strength >= 7:
        print("That's okay, take some time for yourself and get some fresh air. :)")
    elif emotion == "scared" and strength >= 7:
        print("Oh, you're terrified...Those are just your survival instincts kicking in. Whatever it is, you've got this!")

        # If the emotion strength is less than 7, print this:
    elif emotion == "sad" and strength < 7:
        print("A little sad, huh? That's okay, it'll pass. Maybe eat your favourite food. :)")
    elif emotion == "happy" and strength < 7:
        print("Not super happy, I see. Smile! Fake it till you make it.")
    elif emotion == "angry" and strength < 7:
        print("So you're a little angry...maybe get some fresh air! It'll pass sooner than you think.")
    elif emotion == "scared" and strength < 7:
        print("To be a little scared is to be very normal - square those shoulders! You've got this")

        # If the emotion fits neither of these, print this:
    else:
        print("That's either not an emotion or...this program isn't big enough to handle it...Try again!")
        print("Are you happy? Sad? Scared? Angry? Enter the emotion.")

    # Store the results in a variable named accordingly
    result = emotion, strength
    return result

# Infinite loop that powers the program
while True:
    emotion = input("Enter what emotion you're feeling or enter 'q' to quit: ").lower()

    # If the user enters "q", the program ends
    if emotion.lower() == "q":
        print("Goodbye!")
        break

    # Try/except statement catches string value errors, advising the user to enter only numbers
    try:
        strength = int(input("On a scale of 1 - 10, enter how strong the emotion you're feeling is: "))
        if strength < 1 or strength > 10: # Checks if number is between 1 and 10. If not, prints this:
            print("Enter a number between 1 and 10")
            continue # Continues the program by sending the user back to the top of the while loop to try again
    except ValueError:
        print("Numbers only.")
        continue

    # Calls the suggest_feedback function and passes the user entered arguments; emotion and strength
    suggest_feedback(emotion, strength)


