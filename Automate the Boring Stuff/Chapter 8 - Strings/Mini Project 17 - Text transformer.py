
text = "Hello World 123 - This is a Test String!!!"

vowels = ""
not_vowels = ""
digits = ""
swap_case = ""

counter = 0

for char in text:


    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels += char

    if char not in ['a', 'e', 'i', 'o', 'u']:
        not_vowels += char

    if char.isdigit():
        digits += char

    if char.isalpha():
        if counter % 2 == 0:
            swap_case += char.upper()
        else:
            swap_case += char.lower()
        counter += 1
    else:
        swap_case += char

print(vowels)
print(not_vowels)
print(digits)
print(swap_case)

