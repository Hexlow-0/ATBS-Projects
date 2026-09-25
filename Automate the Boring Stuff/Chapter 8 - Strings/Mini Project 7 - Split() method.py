
sentence = "the quick brown fox jumps over the lazy dog"

sentence = sentence.split()

print("Total number of words:")
print(len(sentence))
print()

print("Every word with it's index number:")
for i, word in enumerate(sentence):
    print(f"{i}: {word}")

print()

print(f"First word: {sentence[0]}")
print(f"Last word: {sentence[-1]}\n")

print("Longer than three:")
for char in sentence:
    if len(char) > 3:
        print(char)
