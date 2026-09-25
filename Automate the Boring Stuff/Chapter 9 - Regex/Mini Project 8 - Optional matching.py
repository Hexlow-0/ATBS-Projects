
sentences = [
    "I love the color blue.",
    "She painted it a lovely colour.",
    "There was no clour at all.",
    "What a strange colur choice.",
]

import re

number = re.compile('\(?\d{3})?-?\d{3}-\d{4}') # got here but couldnt be bothered make the rest
colour = re.compile('colou?r')

for sentence in sentences:

    match = colour.search(sentence)

    if match:
        print(f"Found: {match.group()}")
    else:
        print("Neither match was found.")
