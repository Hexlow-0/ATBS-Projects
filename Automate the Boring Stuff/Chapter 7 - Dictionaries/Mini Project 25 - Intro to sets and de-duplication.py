

names = ["alice", "bob", "alice", "carol", "bob", "diana", "carol"]

seen = set()
for name in names:
    if name in seen:
        continue        # already seen, skip
    seen.add(name)
    print(name)         # first time seeing this — do something with it
