
from pathlib import Path
import re

nums = re.compile('\d+')

base = Path.home() / "Documents" / "python_sandbox"

even = base / "even"
odd = base / "odd"

even.mkdir(parents=True, exist_ok=True)
odd.mkdir(parents=True, exist_ok=True)

for file in base.iterdir():

    if note file.is_file():
        continue

    match = nums.search(file.name)

    if not match:
        continue

   num = int(match.group())

    if num % 2 == 0:
        file.rename(even / file.name)
    else:
        file.rename(odd / file.name)

