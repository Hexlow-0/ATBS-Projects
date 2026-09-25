
from pathlib import Path
import shutil

base = Path.home() / "Documents" / "python_sandbox" / "test"
sorted_folders = base / "SORTED"
sorted_folders.mkdir(exist_ok=True)

# Collect ext names
ext_folders = []
for file in base.rglob('*'):

    if file.is_file():
        ext_folders.append(sorted_folders / file.suffix.replace('.', '').lower())

# Build folders
for ext in ext_folders:
    ext.mkdir(exist_ok=True, parents=True)

for file in base.rglob('*'):

    if file.is_file():


