

from pathlib import Path

base = Path.home() / "Documents" / "python_sandbox" / "test"
file_summary_2_path = base / "folder_report.txt"

grouped_exts = {}
empty_files = {}

for file in base.rglob('*'):

    if file.is_file():

        key = file.suffix.replace('.', '').lower()
        size_bytes = file.stat().st_size
        size_mb = file.stat().st_size / (1024 * 1024)

        if size_bytes == 0:
            empty_files[file.name] = file

        grouped_exts.setdefault(key, []).append({'name': file.name, 'size': size_mb})


with open(file_summary_2_path, 'w', encoding='utf-8') as f:


    for ext, file_data in grouped_exts.items():

        print(f" {ext} ".upper().center(40, "="), file=f)
        print(f"No. of files:    {len(file_data)}", file=f)

        total_size = 0
        largest_file = ''
        largest_file_size = 0

        for data in file_data:

            name = data.get('name', 'unknown')
            size = data.get('size', 0)

            total_size += size


            if size > largest_file_size:
                largest_file_size = size
                largest_file = name


        print(f"Total size:      {total_size:.2f} MB", file=f)
        print(f"Largest file:    '{largest_file}'", file=f)
        print(f"Size of file:    {largest_file_size:.2f} MB\n", file=f)

    print("=" * 40, file=f)
    print("EMPTY FILES".center(40), file=f)
    print("=" * 40, file=f)
    print(file=f)

    for file_name, path in empty_files.items():

        print(f"Name: {file_name}", file=f)
        print(f"Path: {path}\n", file=f)

    print("Finished!")
