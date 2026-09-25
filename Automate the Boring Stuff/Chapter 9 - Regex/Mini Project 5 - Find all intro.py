
import re

text = "The cat sat on the mat. The dog chased the cat, but the cat ran away."
codes = "a1 b2 c3 d4"

# Patterns
cat_match_pattern = re.compile('cat')
code_match_pattern = re.compile('([a-z])(\d)')

# Normalize it or whatever
text = text.lower()

# Part 1
cat_match = cat_match_pattern.findall(text)
print(f"How many times 'cat' appears in text: {len(cat_match)} times\n")


# Part 2 - returns list of tuples
code_match = code_match_pattern.findall(codes)

# Iterate through list
for match in code_match:

    # Unpack tuples
    letter, number = match

    # Print em.
    print(f"Letter: {letter}, Number: {number}")




