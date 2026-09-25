from pathlib import Path
import shutil

base = Path.home() / "Documents" / "python_sandbox" / "test"
path_to_sorted = base / "SORTED"
path_to_sorted.mkdir(exist_ok=True)

for file in base.rglob('*'):

    if file.is_file():

        ext = file.suffix.replace('.', '').lower()
        dest_folder = path_to_sorted / ext
        dest_folder.mkdir(exist_ok=True)
        shutil.move(file, dest_folder)


