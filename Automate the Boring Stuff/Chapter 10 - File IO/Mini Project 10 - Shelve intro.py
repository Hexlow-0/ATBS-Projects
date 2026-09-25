
from pathlib import Path
import shelve

base = Path.home() / "Documents" / "python_sandbox"

with shelve.open(str(base / "check_mod")) as db:

    for file in base.iterdir():
        if file.name not in db:
            print(f"{file.name} is new — scanning.")
            db[file.name] = file.stat().st_mtime
        elif db[file.name] == file.stat().st_mtime:
            print(f"{file.name} unchanged — skipping.")
        else:
            print(f"{file.name} modified! Time: {file.stat().st_mtime}")
            db[file.name] = file.stat().st_mtime

