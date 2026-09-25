
import re

greedy = re.compile('\[.*\]')
non_greedy = re.compile('\[.*?\]')

sentence = "[this is] a [pretty cool sentence] which [happens] [] to [have brackets] wrapping some [of the words] []"

greedy_match = greedy.findall(sentence)
non_greedy_match = non_greedy.findall(sentence)

print(greedy_match)
print(non_greedy_match)
