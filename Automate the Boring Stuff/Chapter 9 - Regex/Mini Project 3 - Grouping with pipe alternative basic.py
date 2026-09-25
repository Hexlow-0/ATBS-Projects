
import re

posts = [
    "I just adopted a dog yesterday!",
    "My fish died last week, RIP.",
    "Thinking about getting a hamster.",
    "She has three cats and a bird.",
]

pet_pattern = re.compile("cat|dog|bird|fish")

for pets in posts:

    match = pet_pattern.search(pets)

    if match:
        print(f"Animal found: {match.group()}")
    else:
        print("No recognized pet mentioned")


