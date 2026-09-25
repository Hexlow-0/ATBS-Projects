
greetings = [
    "hi there!",
    "hi!!! how are you?",
    "hi, nice to meet you.",
    "oh hi!!!!!!",
]

laughing = 'ahahah haha ha hha ahah ha haha hahaha hahahahaha ahah haha ha aha hah ah aha hha'

import re

laugh = re.compile('ha*')
exclamation = re.compile('hi!*')

for text in greetings:

    match = exclamation.search(text)

    if match:
        print(f"match: {match.group()}")
    else:
        print("No greeting found.")

print()

# real edge case encounted - wont stress about yet

match = laugh.findall(laughing)

print(match.group)

print()

test = re.compile('(ha)*')
print(test.findall('hahaha'))
