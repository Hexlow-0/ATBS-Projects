
sentence = "The quick brown fox jumps over 2 lazy dogs!"

import re

pattern = re.compile('[a-zA-Z]+')

word = pattern.findall(sentence)

for i in word:

    print(f"Word: {i} | Length: {len(i)}")
