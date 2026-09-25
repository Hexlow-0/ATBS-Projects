
from pathlib import Path
import datetime

base = Path.home() / "Documents" / "python_sandbox"
path = base / "journal.txt"

def main_menu():

    print("=" * 40)
    print(f"JOURNAL".center(40))
    print(f"=" * 40 + "\n")

    print("Enter an option:")
    print("1. Add journal entry.")
    print("2. Search journal by key word")
    print("3. Print menu again.")
    print("4. Exit program.\n")


def format_entry(entry):

    print()
    print(f"Adding content to journal...\n")

    with open(path, 'a', encoding='utf-8') as journal:

        time = datetime.datetime.now().strftime('%d %B %Y, %H:%M')

        journal.write(f"Journal entry: {time}")
        journal.write('\n')
        journal.write(f"{entry}\n")

        journal.write('\n')
        journal.write("=" * 40)
        journal.write('\n')

def read_back():

    print("=" * 40)
    print(f"JOURNAL UPDATED".center(40))
    print(f"=" * 40 + "\n")

    with open(path, 'r', encoding='utf-8') as journal:
        contents = journal.read()
        print(contents)


def search_word():

    print("=" * 40)
    print("SEARCH WORD".center(40))
    print("=" * 40 + "\n")

    print("Enter the word you're looking for:\n")

    word_search = input('> ').lower()

    print()
    print("Searching...\n")

    line_count = 0
    found = False

    with open(path) as journal:
        for line in journal:

            line_count += 1

            if word_search in line.lower():
                found = True
                print(f"'{word_search}' found in journal on line {line_count}")

    if not found:
        print(f"'{word_search}' not found in journal.\n")

def add_entry():

    print("=" * 40)
    print("ADD ENTRY".center(40))
    print("=" * 40 + "\n")

    print("Enter what you'd like to add.\n")

    entry = input('> ')

    return entry

def main():

    path.touch()

    main_menu()

    while True:

        print("Enter option:")

        try:
            choice = int(input('> '))
        except ValueError:
            print("Must be a number between 1 - 4. Try again.")
            continue


        if choice == 1:
            entry = add_entry()
            format_entry(entry)
            read_back()
        elif choice == 2:
            search_word()
        elif choice == 3:
            main_menu()
        elif choice == 4:
            print("\nExiting program. Good bye!\n")
            break
        else:
            print("\nMust be a number between 1 -4. Try again.\n")
            continue

main()








