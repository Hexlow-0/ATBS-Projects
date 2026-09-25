
import zipfile
from datetime import date
from pathlib import Path
import shutil

base = Path.home() / "Documents" / "python_sandbox"

flat = base / "flat"
flat.mkdir(parents=True, exist_ok=True)

for file in base.rglob('*'):
    if file.is_file():
        folder_name = file.suffix.replace('.', '').lower()
        dest_folder = base / folder_name
        dest_folder.mkdir(parents=True, exist_ok=True)
        shutil.move(file, dest_folder)
