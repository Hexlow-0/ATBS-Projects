
players = [
    {"name": "Alice", "score": 88, "level": 5},
    {"name": "Bob", "score": 72, "level": 8},
    {"name": "Carol", "score": 95, "level": 3},
    {"name": "Dan", "score": 61, "level": 7},
    {"name": "Eve", "score": 88, "level": 6},
]

# sort the whole list first
ascending = sorted(players, key=lambda x: x['score'])

print("Ascending:\n")

for player in ascending:
    print(f"{player['name']} | Score: {player['score']} | Level: {player['level']}")

print()

print("Descending:\n")

descending = sorted(players, key=lambda x: x['score'], reverse=True)

for player in descending:
    print(f"{player['name']} | Score: {player['score']} | Level: {player['level']}")

print()

print("Alphabetical:\n")

alphabetical = sorted(players, key=lambda x: x['name'])

for player in alphabetical:
    print(f"{player['name']} | Score: {player['score']} | Level: {player['level']}")

print()
