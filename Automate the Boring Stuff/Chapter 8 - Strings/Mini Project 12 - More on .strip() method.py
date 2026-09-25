
entries = [
    "###alice smith###",
    "...28...",
    "///sydney///",
    "   premium   ",
    "---01/06/2026---",
    "***eng004***",
    "   ###   mixed...mess   ###   "
]

for i, entry in enumerate(entries, start = 1):

    entry = entry.strip('#./-* ')

    print(f"Entry {i}: {entry}")



