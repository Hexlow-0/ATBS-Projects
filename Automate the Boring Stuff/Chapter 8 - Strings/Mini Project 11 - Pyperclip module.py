
import pyperclip

raw = "  hello   this is some MESSY    text that needs   CLEANING up  "

cleaned = ' '.join(raw.lower().split())

pyperclip.copy(cleaned)

print(f"Copied to clipboard: {cleaned}")

print(f"Clipboard contains: {pyperclip.paste()}")
