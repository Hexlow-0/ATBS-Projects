
from collections import Counter

settings = [
    {'theme': 'light', 'font': 'Arial'},
    {'font': 'Helvetica', 'size': 12},
    {'theme': 'dark', 'notifications': True},
    {'size': 14, 'language': 'en'},
]


merged = {}

for config in settings:

    merged.update(config)

print("Merged result:\n")

for k, v in merged.items():

    print(f"{k}: {v}")

print()

print("Keys that appeared in more than one dict:\n")

seen = set()
overwritten = set()

for config in settings:
    for key in config.keys():
        if key in seen:
            overwritten.add(key)  # seen it before — it's a conflict
        seen.add(key)

print()

print("These keys were seen:")

print(seen)

print()

print("These keys were overwritten:")

print(overwritten)
