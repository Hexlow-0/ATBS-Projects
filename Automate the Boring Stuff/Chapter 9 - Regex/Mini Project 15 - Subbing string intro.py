
import re

text = """
i wanna learn python - but the journey to get there is unbelieviably long. if
i bork this, ill never reach there level im aiming for. every bork is another
setback/extension. borking this leads to more borking. i must become unborkable.
"""

bork = re.compile('bork')
text = bork.sub('****', text)


print(text)

name = "John Smith"

pattern = re.compile(r"(\w+)\s+(\w+)")

result = pattern.sub(r"\2, \1", name)

print(result)
