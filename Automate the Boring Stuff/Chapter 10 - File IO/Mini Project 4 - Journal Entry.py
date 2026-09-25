
from pathlib import Path

base = Path.home() / "Documents"
path = base / "journal.txt"

print("Enter your journal entry below ('q' to quit):\n")

def main():

    while True:

        entry = input('> ').lower()

        if entry == 'q':
            print("Journal additions saved. Bye!")
            break

        with open(path, "a", encoding="utf-8") as journal:
            journal.write(f"{entry}\n")

    print("=" * 40)
    print("JOURNAL".center(40))
    print("=" * 40)
    print()

    with open(path, "r", encoding="utf-8") as journal:
        print(journal.read())

    print()
    print("=" * 40)

main()

