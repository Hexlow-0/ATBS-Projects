
from pathlib import Path

base = Path.home() / "Documents" / "python_sandbox"

count_words = {}

for file in base.iterdir():
    if file.suffix == '.txt':
        with open(file) as f:
            for line in f:
                words = line.lower().replace('.', "").replace(',', "").replace('!', "").split()
                for word in words:
                    if len(word) > 4:
                        if word.isalpha():
                            count_words[word] = count_words.get(word, 0) + 1

top_five_sorted = sorted(count_words.items(), key=lambda x: x[1], reverse=True)

for i, (word, count) in enumerate(top_five_sorted[:5], start=1):
    print(f"{i}. {word:<12}Count: {count}")

