
text = "Hello World 123 !!!"

total_char = len(text)

total_letter = 0
total_number = 0
total_spaces = 0
other_char = 0

for char in text:
    if char.isalpha():
        total_letter += 1
    elif char.isdigit():
        total_number += 1
    elif char.isspace():
        total_spaces += 1
    else:
        other_char += 1

print(f"Total characters: {total_char}\n")
print(f"Letters: {total_letter} - {total_letter / total_char:.1%}")
print(f"Digits: {total_number} - {total_number / total_char:.1%}")
print(f"Spaces: {total_spaces} - {total_spaces / total_char:.1%}")
print(f"Other: {other_char} - {other_char / total_char:.1%}")
