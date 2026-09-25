
from pathlib import Path


home = Path.home()

filename = input("Enter a file name: ")

text = input("Type a note: ")

path = home / f"{filename}.txt"

file = open(path, "w", encoding="utf-8")
file.write(text)
file.close()

print("=" * 40)
print("Note saved! Here's what was written:")
print("=" * 40)
print()

file = open(path, "r", encoding="utf-8")
contents = file.read()
file.close()

print(contents)

print()
print("=" * 40)






