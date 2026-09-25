
from pathlib import Path
import zipfile
import textwrap
import random
import sys

def add_word(vocab_trainer_path, words_and_definitions):

    print('=' * 40)
    print("ADD WORDS".center(40))
    print('=' * 40)

    while True:

        print()
        print("Enter word to add:")
        word = input('> ').strip().lower()
        print()

        if not word.isalpha():
            print("Only enter letters for the word (no spaces in word).")
            continue
        elif word in words_and_definitions.keys():
            print(f"'{word}' already added to trainer. Try again")
            continue

        print("Enter definition of word:")
        definition = input('> ').strip().lower().replace('|', '')
        print()

        # justification for isalmum: B2B, 2day, m8, l8r, etc
        if not definition.isalnum():
            print("Only enter letters for the definition.")
            continue
        elif definition in words_and_definitions.values():
            print(f"An identical definition already exists in trainer. Try again")
            continue


        enterted_data = f"""
        ======================
        Word: {word}
        Definition: {definition}
        ======================
        """

        print(textwrap.dedent(enterted_data))

        print("Continue (any) or re-enter (r)?")
        answer = input('> ').strip().lower()
        print()

        if answer == 'r':
            continue
        else:
            with open(vocab_trainer_path, 'a', encoding='utf-8') as f:
                print(f"{word}|{definition}", file=f)

            print("Word and definition saved! Returning to menu.")
            words_and_definitions = load_data(vocab_trainer_path)
            return words_and_definitions




def view_saved_words(result):

    if not result:
        print("Vocab trainer empty - add words/definitions first.")
        return

    print('=' * 40)
    print("WORDS IN TRAINER".center(40))
    print('=' * 40)
    print()


    for i, words in enumerate(result.keys()):
        print(f"{i + 1}. {words}")

    print()

def see_answers(words_and_definitions):

    print('=' * 40)
    print("ANSWERS".center(40))
    print('=' * 40)
    print()

    for words, definition in words_and_definitions.items():
        print(f"Word: {words:<6}")
        print(f"Definition: {definition:<6}\n")

    print()

def start_quiz(words_and_definitions):

    print('=' * 40)
    print("QUIZ STARTED".center(40))
    print('=' * 40)
    print()

    correct = 0
    wrong = 0

    items = list(words_and_definitions.items())
    random.shuffle(items)

    for word, definition in items:
        print(f"Definition: {definition}")
        guess = input('> ')
        if guess.lower().strip() == word.lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong. The word was: {word}")
            wrong += 1

    percent_score = correct / len(list(words_and_definitions.keys())) * 100

    print("STATS".center(40, "="))
    print()
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"You scored %{percent_score:.2f}!")

def quiz_mode(words_and_definitions):

    if not words_and_definitions:
        print("Vocab trainer empty - add words/definitions first.")
        return

    print('=' * 40)
    print("QUIZ MODE".center(40))
    print('=' * 40)
    print()

    print("1. See instructions")
    print("2. Start quiz")
    print("3. CHEEEEEEAT")
    print("4. Return to menu")

    instructions = """INSTRUCTIONS:

    You'll be shown a definition from your vocab trainer dictionary. Enter
    the word that matches the definition. You'll see your score at the end
    of the quiz.

    Good luck!"
    """

    while True:

        try:
            quiz_option = int(input('> '))
        except ValueError:
            print("Numbers only - try again (1-4).\n")
            continue

        if quiz_option == 1:
            print(textwrap.dedent(instructions))
        elif quiz_option == 2:
            start_quiz(words_and_definitions)
        elif quiz_option == 3:
            see_answers(words_and_definitions)
        elif quiz_option == 4:
            print("Returning to menu.")
            return
        else:
            print("Number must be between 1 - 4. Try again.")
            continue


def menu():

    print('=' * 40)
    print("VOCAB TRAINER".center(40))
    print('=' * 40)
    print()

    print("1. Add word/definition")
    print("2. View all words")
    print("3. Quiz mode")
    print("4. Print menu again.")
    print("5. Backup trainer")
    print("6. Exit\n")

def load_data(vocab_trainer_path):

    words_and_definitions = {}

    with open(vocab_trainer_path, 'r', encoding='utf-8') as f:
        for line in f:
            word, definition = line.split('|')
            words_and_definitions[word] = definition

    return words_and_definitions

def backup(vocab_trainer_path, backups):

    print("Backing up vocab trainer...")

    with zipfile.ZipFile(backups / 'vocab_backup.zip', 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.write(vocab_trainer_path, arcname=vocab_trainer_path.name)

    print(f"Done! Vocal trainer backed up at: {backups}\n")

def main():

    base = Path.home() / "Documents" / "python_sandbox" / "vocab_trainer"
    base.mkdir(exist_ok=True, parents=True)

    backups = base / "backups"
    backups.mkdir(exist_ok=True, parents=True)

    vocab_trainer_path = base / "vocab_trainer_dict.txt"

    words_and_definitions = load_data(vocab_trainer_path)
    menu()

    while True:

        try:
            option = int(input('> '))
        except ValueError:
            print("Numbers only - try again (1-6).\n")
            continue


        if option == 1:
            words_and_definitions = add_word(vocab_trainer_path, words_and_definitions)
        elif option == 2:
            view_saved_words(words_and_definitions)
        elif option == 3:
            quiz_mode(words_and_definitions)
        elif option == 4:
            menu()
        elif option == 5:
            backup(vocab_trainer_path, backups)
        elif option == 6:
            print("Exiting program. Good bye!")
            sys.exit()
        else:
            print("Number must be between 1 - 6. Try again.")

main()
