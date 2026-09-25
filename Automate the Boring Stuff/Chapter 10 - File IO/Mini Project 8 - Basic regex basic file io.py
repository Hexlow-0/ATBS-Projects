
from pathlib import Path
import re

phone = re.compile(r'\d{3}-\d{4}')
date = re.compile(r'\d{2}/?-?\d{2}/?-?\d{4}')
email = re.compile(r'(\w+)@(\w+)\.(\w+)') # (a-zA-Z+) doesnt work for some fking reason

base = Path.home() / "Documents" / "python_sandbox"

path = base / "file0.txt"
contents = path.read_text(encoding='utf-8')
print(contents)

print()

phone_matches = phone.findall(contents)
date_matches = date.findall(contents)
email_matches = email.findall(contents)

print(f"Date(s): {date_matches}")
print(f"Phone numbers: {phone_matches}")
print(f"Email matches: {email_matches}")
