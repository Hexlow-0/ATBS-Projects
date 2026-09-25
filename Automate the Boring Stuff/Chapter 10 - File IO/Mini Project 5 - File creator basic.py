
from pathlib import Path

base = Path.home() / "Documents" / "python_sandbox"
old_path = base / "old_file.txt"
new_path = base / "new_file.txt"

print("Creating file...\n")
with open(old_path, 'w') as f:
    f.write("some content")

if new_path.exists():
    new_path.unlink()
    print("Cleared old new_file.txt before renaming.\n")

print("Renaming file...\n")
try:
    old_path.rename(new_path)
    print(f"File now renamed - path: {new_path}")
except FileNotFoundError:
    print(f"Can't find specified path: {old_path}")
except FileExistsError:
    print(f"Can't rename — {new_path} already exists.")
