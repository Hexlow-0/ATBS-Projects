
from pathlib import Path

base = Path.home()

def main_menu():

    print("=" * 40)
    print("DIRECTORY SCANNER".center(40))
    print("=" * 40)
    print()

    print("Select a subfolder to scan:\n")

    print("1. Downloads")
    print("2. Documents")
    print("3. Desktop")
    print("4. Favourites")
    print("5. Recent")
    print("6. Onedrive")
    print("7. Print main menu")
    print("8. Exit.\n")

def request_extension():

    print("=" * 40)
    print("ENTER EXTENTION".center(40))
    print("=" * 40)
    print()

    while True:

        ext = input('> ').strip().lower()

        if not ext.replace(".", "").isalnum():
            print("Invalid extension, try again.")
            continue
        elif len(ext) > 12: # Unusually long
            print("Too long, likely an invalid extension - try again.")
            continue
        else:
            break # Must be valid

    return ext

def scan_files(sub_folder, ext):

    folder_search = base / sub_folder

    file_data = {}
    file_count = 0
    total_file_size = 0

    print("Calculating...")

    for file in folder_search.rglob(f"*.{ext}"):

        size = file.stat().st_size / 1024 # Convert to KB
        name = file.name

        file_count += 1 # Add to file count
        total_file_size += size # Calculate file size

        # Cut the length off of chunky names
        if len(name) > 15:
            name = name[:15]
            name = name + "..."

        # Store data
        file_data[name] = size

    return {'file_data': file_data,
            'file_count': file_count,
            'summed_file_size': total_file_size
            }

def print_summary(scanned, ext, sub_folder):

    print("=" * 40)
    print("SUMMARY".center(40))
    print("=" * 40)
    print()

    count = scanned.get('file_count')
    total_size = scanned.get('summed_file_size')

    print(f"Found {count} .{ext} files in {sub_folder}:\n")

    for file_name, file_size in scanned['file_data'].items():

        print(f"  {file_name:<25}{file_size:.2f} KB")

    print()
    print("=" * 40)
    print(f"Total size: {total_size:,.2f} KB")
    print("=" * 40)
    print()

def main():

    main_menu()

    while True:

        try:
            option = int(input('> '))
        except ValueError:
            print("Option must be between 1 - 8, numbers only. Try again.")
            continue

        if option == 1:
            sub_folder = "Downloads"
        elif option == 2:
            sub_folder = "Documents"
        elif option == 3:
            sub_folder = "Desktop"
        elif option == 4:
            sub_folder = "Favourites"
        elif option == 5:
            sub_folder = "Recent"
        elif option == 6:
            sub_folder = "Onedrive"
        elif option == 7:
            main_menu()
            continue
        elif option == 8:
            print("Exiting program. Good bye!")
            break
        else:
            print("Number must be between 1 - 8. Try again.")
            continue

        # Call main functions
        ext = request_extension()
        scanned = scan_files(sub_folder, ext)
        print_summary(scanned, ext, sub_folder)

        # Exit program upon completion
        break

main()

