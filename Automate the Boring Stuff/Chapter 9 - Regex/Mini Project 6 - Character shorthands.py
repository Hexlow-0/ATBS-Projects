
import re

text = "John is 25 years old. Sarah is 31. Contact: 555 1234. Mike turned 40 today."

two_digit = re.compile('\d\d')
char_space = re.compile('\w ')

digit_match = two_digit.findall(text)
char_space_match = char_space.findall(text)

print(f"Digits in digit_match: {digit_match}")
print(f"Chatacters followed by a space: {char_space_match}")

