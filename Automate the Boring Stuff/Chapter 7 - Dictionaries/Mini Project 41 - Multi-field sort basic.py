
players = [
    {"name": "Alice", "score": 88, "level": 5},
    {"name": "Bob", "score": 72, "level": 8},
    {"name": "Carol", "score": 88, "level": 3},
    {"name": "Dan", "score": 61, "level": 7},
    {"name": "Eve", "score": 72, "level": 6},
]


score_name = sorted(players, key=lambda x: (x['score'], x['name']), reverse=True)

print("part 1:\n")

for score in score_name:

    print(f"{score['name']} | {score['score']}")

print()

level_score = sorted(players, key=lambda x: (x['level'], x['name']))

print("part 2:\n")

for level in level_score:

    print(f"{level['level']} | {level['score']}")

