
from pathlib import Path

base = Path.home() / "Documents" / "python_sandbox"
src = base / "file0.txt"
dst = base / "file0_copy.txt"

def safe_copy(src, dst):

    if not src.exists():
        raise FileNotFoundError(f"'{src}' does not exist.")

    file_size = src.stat().st_size

    with open(src, 'rb') as f_in:
        with open(dst, 'wb') as f_out:

            f_out.write(f_in.read())


    print(f"Done! Copied {file_size} bytes.")

safe_copy(src, dst)
