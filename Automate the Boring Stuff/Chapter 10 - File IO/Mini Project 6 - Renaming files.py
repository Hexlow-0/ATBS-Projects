
from pathlib import Path

base = Path.home() / "Documents" / "python_sandbox"

old_path = base/ "draft.txt"
new_path = base / "final.txt"

# gotta rename DRAFT to FINAL (so content makes sense)
draft = """FINAL
This is the last final last draft
Vinal v6.7 part 3 (updated) (dont edit)
Ooga booga"""

print("Creating file...\n")

with open(old_path, 'w', encoding='utf-8') as f:
    f.write(draft)

if new_path.exists():
    print("You've already run the program. Clearing last renamed file...")
    new_path.unlink()

print("Renaming files...\n")

try:
    old_path.rename(new_path)
    print(f"File renamed. Path is now: {new_path}\n")
except FileNotFoundError:
    print(f"Can't find draft path, check path: {old_path}\n")
except FileExistsError:
    print(f"Can't rename — {new_path} already exists.\n")

print("Files in directory: \n")

files = []

for file in base.iterdir():
    files.append(file.name)

print(files)

