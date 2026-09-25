
import sys
from pathlib import Path

def main():

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python wordcount.py <path> <-q> (q=quiet)")
        sys.exit()

    quiet_mode = '-q' in sys.argv
    filtered = [a for a in sys.argv[1:] if a != '-q']

    path = Path(filtered[0])

    if not path.exists():
        print("Path does not exist. Try again.")
        sys.exit()
    elif not path.is_file():
        print("Path is not a file. Try again.")
        sys.exit()

    with open(path, 'r', encoding='utf-8') as f:

        lines = f.readlines()
        content = ''.join(lines)

    if not quiet_mode:
        print(f"Lines: {len(lines)}")
        print(f"Chars: {len(content)}")
        print(f"Words: {len(content.split())}")
    else:
        print(f"{len(lines)} lines, {len(content)} chars, {len(content.split())} words")

if __name__ == '__main__':
    main()
