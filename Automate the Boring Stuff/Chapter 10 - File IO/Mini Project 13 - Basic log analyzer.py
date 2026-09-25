
from pathlib import Path
import re

error_pattern = re.compile(r'ERROR') # task asked me to use regex, tho it doesnt exact suit here

base = Path.home() / "Documents" / "python_sandbox"
scan = base / "app.log"
errors_path = base / "errors.log"

def scan_log_data():

    print("Scanning data...")

    errors_found = []
    lines_scanned = 0

    with scan.open(encoding="utf-8") as log:
        for line in log:

            lines_scanned += 1
            match = error_pattern.search(line)

            if match:
                errors_found.append(line)

    print("File scanned!")

    return {"errors": errors_found,
            "lines_scanned": lines_scanned
            }

def write_errors_to_file(scan_data):

    print("Writing to error file...")

    errors_path.touch()

    with open(errors_path, 'w', encoding='utf-8') as error_file:
        for error in scan_data["errors"]:
            error_file.write(error)

    print("Finished!\n")

def print_summary(scan_data):

    print("=" * 40)
    print("SUMMARY".center(40))
    print("=" * 40 + "\n")

    error_amount = len(scan_data.get("errors", []))
    num_lines_scanned = scan_data.get("lines_scanned", 0)

    print(f"Scanned {num_lines_scanned} lines. Found {error_amount}. Written to errors.log.\n")

    print("See errors below:\n")
    with open(errors_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(contents)


def main():

    if not scan.exists():
        print("Log file doesn't exist.")
        print(base)
        return

    print("Processing...\n")
    scan_data = scan_log_data()
    write_errors_to_file(scan_data)
    print_summary(scan_data)

main()
