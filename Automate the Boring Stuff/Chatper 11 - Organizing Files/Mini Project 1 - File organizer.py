
from pathlib import Path
import shutil

base = Path.home() / "Documents" / "python_sandbox"

FOLDERS = {
    'images':      ['.png', '.jpg', '.jpeg', '.gif', '.webp'],
    'documents':   ['.pdf', '.docx', '.txt'],
    'archives':    ['.zip', '.gz'],
    'executables': ['.exe'],
    'code':        ['.py'],
}

def get_destination(ext):
    for folder, extensions in FOLDERS.items():
        if ext.lower() in extensions:
            return folder
    return 'other'

for file in base.iterdir():
    if not file.is_file():
        continue

    dest_name = get_destination(file.suffix)
    dest = base / dest_name
    dest.mkdir(exist_ok=True)
    shutil.move(file, dest / file.name)
