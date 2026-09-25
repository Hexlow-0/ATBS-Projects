"""
🎯 Mini Project: Flashcard Tracker

You’ll build a text-based flashcard program that lets users:

Create a flashcard (question + answer)
View all flashcards (as a list of strings)
Change a flashcard at a given index
Delete a flashcard by name or index
Show a list of the first few cards
Reverse the card order
Show a replicated list (to simulate spaced repetition)

"""
def create_flashcard(flashcards):

    print("Welcome to the flashcard creator!")
    print("\nFirst, add your question.")
    print("Next, you'll be prompted for an answer to that question.")
    print("When finished, enter 'q' to return to menu at any time.\n")

    while True:
        question = input("Add your question or enter 'q' to quit: ").strip()

        if question == 'q':
            print("Returning to menu.")
            print_menu()
            return flashcards

        if question == "":
            print("You have to enter both a question and answer. Try again.")
            continue

        answer = input("Add your answer to that question or enter 'q' to quit: ").strip()

        if answer == 'q':
            print("Returning to menu.")
            print_menu()
            return flashcards

        if answer == "":
            print("You have to enter both a question and answer. Try again.")
            continue

        else:
            result = (question, answer)
            flashcards.append(result)
            print("Your flashcard has been added.")


def view_flashcards(flashcards):
    print("Here are all your flashcards: ")

    for index, item in enumerate(flashcards, start=1):
        print(f"{index}. Q: {item[0]}  |  A: {item[1]}")


def change_flashcard(flashcards):
    if not flashcards:
        print("No flashcards added yet.")
        return

    print("\nHere are your current flashcards:\n")
    for index, (question, answer) in enumerate(flashcards, start=1):
        print(f"{index}. Q: {question}  |  A: {answer}")

    try:
        choice = int(input("\nEnter the number of the flashcard you want to edit: "))

        if choice < 1 or choice > len(flashcards):
            print("Invalid number. Please choose a number from the list.")
            return

        new_question = input("Enter the new question: ").strip()
        new_answer = input("Enter the new answer: ").strip()

        if new_question == "" or new_answer == "":
            print("Both question and answer are required.")
            return

        # Replace the tuple at the given index
        flashcards[choice - 1] = (new_question, new_answer)
        print("Flashcard updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def delete_flashcard():
    pass

def show_first_few_cards(flashcards):
    if not flashcards:
        print("No flashcards added yet.")
        return

    print("These are the first three flashcards:")

    if len(flashcards) < 3:
        print("You need at least four flashcards, returning to menu.")
        return
    else:
        for index, (question, answer) in enumerate(flashcards[:3], start=1):
            print(f"{index}. Q: {question}  |  A: {answer}")

def reverse_card_order(flashcards):
    if not flashcards:
        print("No flashcards added yet.")
        return

    print("Current flashcard order:\n")
    for index, (question, answer) in enumerate(flashcards, start=1):
        print(f"{index}. Q: {question}  |  A: {answer}")


    print("Reversed flashcard order:\n")
    for index, (question, answer) in enumerate(flashcards[::-1], start=1):
        print(f"{index}. Q: {question}  |  A: {answer}")

    return

def show_replicated_list():
    pass

def print_menu():
    print("\n1. Create a flashcard (question + answer)")
    print("2. View all flashcards")
    print("3. Change a flashcard")
    print("4. Delete a flashcard")
    print("5. Show a list of the first few cards")
    print("6. Reverse the card order")
    print("7. Show a replicated list of the cards")
    print("8. Exit program")

# - - WELCOME MESSAGE - - #
print("Welcome to Flashcard Tracker!")

print_menu()

def main():

    flashcards = []

    while True:
        try:
            choice = int(input("\nEnter your choice (1 - 8): "))

            if choice == 1:
                flashcards = create_flashcard(flashcards)
            elif choice == 2:
                view_flashcards(flashcards)
            elif choice == 3:
                change_flashcard(flashcards)
            elif choice == 4:
                delete_flashcard()
            elif choice == 5:
                show_first_few_cards(flashcards)
            elif choice == 6:
                reverse_card_order(flashcards)
            elif choice == 7:
                show_replicated_list()
            elif choice == 8:
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Numbers 1 - 8 only.")

if __name__ == "__main__":
    main()




