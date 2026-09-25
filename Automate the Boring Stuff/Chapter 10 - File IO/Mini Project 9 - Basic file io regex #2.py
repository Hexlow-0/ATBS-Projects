
from pathlib import Path
import pyperclip
import re

base = Path.home() / "Documents" / "python_sandbox"
report_path = base / "report.txt"

phone = re.compile(r'\d{3}-\d{4}')
date = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')
email = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

phone_results = {}
date_results = {}
email_results = {}

for file in base.iterdir():
    if file.suffix == '.txt':

        try:
            text = file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"Skipping {file.name} — couldn't decode as text.")
            continue

        phone_matches = phone.findall(text)
        date_matches = date.findall(text)
        email_matches = email.findall(text)

        if phone_matches:
            phone_results[file.name] = phone_matches

        if date_matches:
            date_results[file.name] = date_matches

        if email_matches:
            email_results[file.name] = email_matches


with open(report_path, 'w', encoding='utf-8', errors='ignore') as report_file:

    report_file.write("========== Phone Numbers Found ==========".center(40))

    report_file.write('\n')
    for filename, number in phone_results.items():
        report_file.write(f"{filename}: {number}\n")
    report_file.write('\n')

    report_file.write("========== Dates Found ==========".center(40))

    report_file.write('\n')
    for filename, date in date_results.items():
        report_file.write(f"{filename}: {date}\n")
    report_file.write('\n')

    report_file.write("========== Emails Found ==========".center(40))

    report_file.write('\n')
    for filename, email in email_results.items():
        report_file.write(f"{filename}: {email}\n")
    report_file.write('\n')



with open(report_path, 'r', encoding='utf-8') as report_file:
    contents = report_file.read()
    pyperclip.copy(contents)
    print("Report copied!")
