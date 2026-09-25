
import re

pattern = re.compile('\d\d\d\d')

sentences = [
    "The event happened in 1987 during summer.",
    "No date mentioned here.",
    "She was born in 2003 in Sydney.",
]

for s in sentences:

    match = pattern.search(s)

    if match:
        print(f"Year found: {match.group()}")
    else:
        print(f"No year found in record: '{s}'")
