
from pathlib import Path

base = Path.home() / "Documents" / "python_sandbox" / "test"


"""
Requirements: (delete before pasting)
- Track files per ext
- Sum of file sizes per ext
- Track largest file per ext

1. Collect raw data and group
2. Do calculations seperately << maybe simplify and just print straight away tbh
3. Print output

What you'd need in a dict to calculate that:
- File names as a list per ext
- Size of file next to file name
"""



def scan_data():

    data = {}

    for file in base.rglob('*'):

        if file.is_file():

            key = file.suffix.lower().replace('.', '')
            size = float(file.stat().st_size / 1024)

            if key == '':
                continue

            if key not in data:
                data[key] = []

            data[key].append({'name': file.name, 'size': size})

    return data

def calculate_data(raw_data):

    for ext_type, file_data in raw_data.items():

        print(ext_type)
        print(f"No. of files: {len(file_data)}")

        ext_type_total_size = 0
        largest_file_name = ''
        largest_file_size = 0

        for data in file_data:

            name = data.get('name', 'UNKNOWN')
            size = data.get('size', 0)

            if size > largest_file_size:
                largest_file_size = size
                largest_file_name = name

            ext_type_total_size += size

        print(f"Total ext type size: {ext_type_total_size / 1024:.2f} MB")
        print(f"Largest file: {largest_file_name} ({largest_file_size:.2f} KB)\n")

def main():

    raw_data = scan_data()
    calculate_data(raw_data)

    print("Finished!")

main()
