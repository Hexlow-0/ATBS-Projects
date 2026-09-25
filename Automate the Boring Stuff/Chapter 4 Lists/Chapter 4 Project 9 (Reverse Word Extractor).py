"""
🔧 Prompt:
Write a program that does the following:
Ask the user to enter a sentence.
Split the sentence into a list of words.

Print:
The last word using negative indexing
The second-to-last word using negative indexing
The first three words using slicing
The last three words using slicing
The entire list reversed using slicing
"""

# Function manipulates sentence according to requirements
def list_manipulator(sentence, indx):

    # Checks for empty list
    if not sentence:
        print("No sentence entered, try again!")
        return

    print(f"\nYour sentence as a list: {sentence}") # Shows user their sentence as a list
    print(f"Last word: {sentence[-1]}") # Shows last word in sentence
    print(f"Second-to-last word: {sentence[-2]}") # Shows second last word
    print(f"First three words: {sentence[:3]}") # Shows first three words
    print(f"Last three words: {sentence[-3:]}") # Shows last three words
    print(f"Reversed: {sentence[::-1]}") # Reverses the whole sentence
    print(f"Your sentence with the number of words you want to see: {sentence[:indx]}\n")


# - - WELCOME MESSAGE - - #
print("Welcome to the list manipulator! This program will do the following to your sentence:")

# Menu - show's user what happens to their sentence
print("\n1. Show the last word in your sentence")
print("2. Show the second to last word in your sentence")
print("3. Shows the first three words of your sentence")
print("4. Show the last three words in your sentence")
print("5. Show the whole sentence as a list, except reversed using slicing")
print("6. Enter a number to show x number of words in your sentence\n")

# While loop powers the program
while True:

    # Asks the user for their sentence
    sentence = input("Enter a sentence or enter 'q' to quit: ")

    # Quits if the user wants to and ensures better sentence length
    if sentence == 'q':
        print("Goodbye!")
        break
    elif len(sentence.split()) <= 1:
        print("C'mon, be a little more creative. At least TWO words.")
        continue

    # Splits the sentence into a list using .split() method
    sentence = sentence.split()

    try: # Ask user what number of words they want to print in their sentence
        indx = int(input("Enter the number of words in your sentence you want to see: "))
    except ValueError: # Handles errors gracefully
        print("Please enter a number, no letters or symbols!")
        continue

    # Ensures number is between the lists range
    if indx < 0 or indx > len(sentence):
        print(f"Please enter a number between 1 and {len(sentence)}!")
        continue

    # Calls function and passes arguments
    list_manipulator(sentence, indx)