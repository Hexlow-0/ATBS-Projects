
usernames = [
    "ab3c9",
    "HELLO",
    "a1!2b",
    "z9z9z",
    "ab",
]

import re

valid_user = re.compile('[a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9]')
not_valid_user = re.compile('([^a-z0-9])')

for user in usernames:

    valid_match = valid_user.search(user)
    not_valid = not_valid_user.search(user)

    if valid_match:
        print(f"Matched user: {valid_match.group()}")
    else:
        print(f"Invalid user: {not_valid.group()}")
