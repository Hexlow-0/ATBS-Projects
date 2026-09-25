
from pathlib import Path
from datetime import datetime

base = Path.home() / "Documents" / "python_sandbox" / "test"
path_to_summary_file = base / "file_summary.txt"

file_data = []

for file in base.rglob('*'):
    if file.is_file():
        file_data.append({
            'name': file.name,
            'size_mb': file.stat().st_size / (1024 * 1024),
            'modified': datetime.fromtimestamp(file.stat().st_mtime)
        })

sorted_data = sorted(file_data, key=lambda x: x['size_mb'], reverse=True)

with open(path_to_summary_file, 'w', encoding='utf-8') as f:
    for item in sorted_data:

        name = item.get('name', '')
        size = item.get('size_mb', 0)
        modified = item.get('modified', '')


        print(f"File: {name}", file=f)
        print(f"Size: {size:.4f} MB", file=f) # copied syntax from older project
        print(f"Last modified: {modified.strftime('%d %B %Y, %H:%M')}", file=f) # copied syntax from older project
        print(file=f)

print("Finished!")

print(Path.cwd())
