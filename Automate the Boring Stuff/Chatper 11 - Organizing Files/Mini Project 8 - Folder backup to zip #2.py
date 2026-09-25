
from pathlib import Path
import zipfile

base = Path.home() / "Documents" / "python_sandbox" / "test"
folder_path = base / "text_files" # just a folder with a bunch of random text files
zip_backup_path = base / "txt_backups.zip"

files_zipped = 0
total_file_sizes = 0

print("Creating zip...")
with zipfile.ZipFile(base / "txt_backups.zip", "w") as txt_zip:

    print("Adding files...")
    for file in folder_path.rglob('*'):

        if file.is_file():

            print(f"'{file.name} added to backup.")
            txt_zip.write(folder_path / file, arcname=file.relative_to(folder_path), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

            total_file_sizes += file.stat().st_size
            files_zipped += 1

print()
print("Calculating zip size...\n")

zip_size = zip_backup_path.stat().st_size

print("*" * 30)
print("Summary".center(30))
print("*" * 30)
print()

print(f"Total files zipped: {files_zipped}")
print(f"File sises added together: {total_file_sizes / 1024:.2f} KB")
print(f"Zip file size: {zip_size / 1024:.2f} KB\n")

print("*" * 30)
