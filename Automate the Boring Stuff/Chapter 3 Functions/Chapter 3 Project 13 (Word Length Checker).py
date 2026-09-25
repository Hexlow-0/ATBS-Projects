"""
✅ Requirements:
Function 1: get_word_score(word)
Returns the number of letters in the word

Function 2: give_word_feedback(word, score)
If the word is longer than 10 letters → “Whoa, long word!”
Between 5–10 → “Nice, medium word.”
Below 5 → “Tiny but mighty.”

A while True loop that:
Asks the user for a word (or 'q' to quit)

Calls both functions in order
Prints the result
"""

# Calculates the length of the word entered
def get_word_score(word):
    score = len(word)
    return score # Returns the score (word length)

# This function gives feedback based on what the user entered
def give_word_feedback(word, score):
    if score >= 10:
        print(f"Whoa, '{word}' is a long word!")
    elif score >= 5:
        print(f"Nice, '{word}' is a medium word!")
    elif score < 5:
        print(f"'{word}'...a tiny word, but a mighty one.")

# While loop keeps the program running until the user enters "q"
while True:
    word = input("Enter a word  to get a feedback on it's length or enter 'q' to quit: ")

    if word == 'q':
        print("Thank you for playing!")
        break

    # Calls the functions
    score = get_word_score(word) # Stores get_word_score(word) in the variable "score"
    give_word_feedback(word, score) # Passes both 'word' and 'score' as arguments to the feedback function

