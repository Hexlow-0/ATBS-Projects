
test_strings = [
    "hello",
    "hello there",
    "say hello",
    "goodbye",
    "goodbye!",
    "GOODBYE",
    "hellogoodbye",
]

import re

exact_hi_bye = re.compile(r'^(hello|goodbye)$')

for test in test_strings:

    match = exact_hi_bye.search(test)

    if match:
        print(f"Match found: {match.group()}")
    else:
        print(f"'{test}' not a match.")
