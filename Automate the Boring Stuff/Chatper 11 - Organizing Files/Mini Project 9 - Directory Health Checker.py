
# Import modules
from pathlib import Path
from collections import defaultdict
import textwrap
import sys
import pyperclip

# ======================================
# PRINTS THE MAIN MENU
# ======================================

def menu():
    """Main menu for basic user CLI"""

    print("=" * 40)
    print("Directory Health Check".center(40))
    print("=" * 40)
    print()

    print("1. Help")
    print("2. Manual")
    print("3. Default")
    print("4. Exit program\n")

# ======================================
# CHECKS IF FILES EXIST IN PATH
# ======================================

def has_files(path):
    """Returns true if there are files in the folder - returns false otherwise"""
    return any(path.iterdir()) # any() returns true if a file exist, false otherwise

# ======================================
# CONFIGURE PROGRAM MANUALLY
# ======================================

def manual():
    """
    Allows user to configure filter:
    - Manually set the path to scan
    - Set what defines a "large file"
    - Choose where to save summary file
    """

    print(" Manual Setup ".center(40, "="))
    print()

    # While True loop allows user to enter again should they make a mistake
    while True:

        # Prompts user for their input
        print("Enter a path:")
        path = input('> ')
        print()

        # Changes string to Path object
        path = Path(path)

        # If-elif block checks dir() exists and has files
        if not path.exists(): # True if path doesn't exist
            print(f"'{path}' does not exist. Try again")
            continue
        elif not path.is_dir(): # Try if path is not a folder
            print(f"'{path}' is not a folder. Try again.")
            continue
        elif not has_files(path): # True if there are no files in directory
            print(f"'{path}' is an empty directory. Try again.")
            continue
        else: # Otherwise path is selected
            print(f"\nPath selected: {path}\n")


        print("Set large file size number (MB):")

        try: # Prompt for users large file size threshold
            set_size = float(input('> '))
            print()
        except ValueError: # If input is not a number, handles gracefully
            print("Enter a positive number. Try again.\n")
            continue

        # If-else block checks number is posive - otherwise sets it
        if set_size < 0:
            print("Number must be positive. Try again.\n")
            continue
        else:
            print(f"Large file size set at: {set_size} MB\n")

        # Prompts user for summary file path
        print("Enter a location to save summary file:")
        summary_path = input('> ')
        print()

        # Turns input to Path object
        summary_path = Path(summary_path)

        # If-elif block checks path exists/is a directory
        if not summary_path.exists(): # True if path doesn't exist
            print(f"'{summary_path}' does not exist. Try again")
            continue
        elif not summary_path.is_dir(): # True path isn't a directory
            print(f"'{summary_path}' is not a folder. Try again.")
            continue
        else: # Otherwise path is set
            print(f"Save path selected: {summary_path}\n")

        # Returns data in a dict
        return {'path': path, 'large_file_size': set_size, 'summary_path': summary_path}

# ======================================
# CONFIGURE PROGRAM TO DEFAULT
# ======================================

def default():
    """
    Configues directory scan to default:
    - Path = home directory
    - "Large file" set at 1 megabyte
    - Summary file saved to home directory
    """

    path = Path.home()
    set_size = 1
    summary_path = Path.home()

    # Returns data in a dict
    return {'path': path, 'large_file_size': set_size, 'summary_path': summary_path}

# ======================================
# COLLECT DATA/SCAN DIRECTORY
# ======================================

def collect_data(PATH, LARGE_SIZE):
    """
    Collects file/directory data for analysis/writing later. Key details include:
    - Total number of files
    - Sum of all file sizes
    - Any file names that appear twice (duplicates)
    - Files that exceed 'large file' threshold
    - Any empty files
    - Files missing an extension

    Everything is saved to dicts using defaultdict from the built-in
    collections module in one sweep. All dicts with related data are returned
    in a single dictionary called 'raw_data' for analysis.
    """

    print("Collecting data (may take a while)...")

    # This block tracks/sorts data
    num_of_files = 0 # Total number of files
    total_size = 0 # Sum of all file sizes
    seen_names = defaultdict(list) # Files that are seen are saved here to duplicate sorting
    large_files = {} # Saves files if they are higher than 'large file' size threshold
    empty_files = {} # Saves empty files
    no_ext = {} # Saves files missing data
    duplicates = {} # Duplicates

    # Iterates through user specified directory revursively
    for file in PATH.rglob('*'):
        if file.is_file(): # Checks if file is a file

            # Skips file if it's the directory summary file itself
            if file.name == 'DIR_HEALTH_SUMMARY.txt':
                continue

            # Stores size of every file
            size = file.stat().st_size

            # If file name appears again, it's path will be stored as a value
            seen_names[file.name].append(file)

            # Checks if file size is greather than 'large size' threshold (megabytes)
            if size / (1024 * 1024) > LARGE_SIZE:
                large_files[file.name] = size # Stores file name as key and size as value

            # If file size is zero, store as empty file
            if size == 0:
                empty_files[file.name] = file

            # If file is missing extension, store file name and path
            if not file.suffix:
                no_ext[file.name] = file

            num_of_files += 1 # Increases for every file that appears
            total_size += size # Adds size for total sum

    # Filters seen names for duplicates
    for file, path in seen_names.items():
        if len(path) > 1: # Anything with a name that appeared more than once will be added as a duplicate
            duplicates[file] = path

    print("Finished!")

    # Returns data in a dict
    return {'duplicates': duplicates,
            'large_files': large_files,
            'empty_files': empty_files,
            'no_extension': no_ext,
            'files_counted': num_of_files,
            'total_size': total_size
            }

# ======================================
# ANALYSE DATA COLLECTED IN DIR
# ======================================

def analyse_data(raw_data, LARGE_SIZE):
    """
    This function seperates basic data collection from analysis/calculation.

    - Calculates num of files that exceeded 'large file' threshold
    - Total sum of large file sizes
    - How much space large files take up in users path
    - Number of empty files
    - Number of files missing an extension
    - Number of duplicate occurrences

    'large_file_percent_of_dir' wrapped in try statement to catch the case
    where no files in the users path exceeded the 'large file' threshold.

    All data is returned in a dict labelled 'analysed'.
    """

    print("Calculating data...")

    # Stores the number of large files
    num_of_large_files = len(raw_data.get('large_files', 0))

    # Calculates the total size of large files together
    large_size_sum = 0
    for size in raw_data['large_files'].values():
        large_size_sum += size

    try: # Calculates what percentage the large files take up in the user path
        large_file_percent_of_dir = large_size_sum / raw_data.get('total_size', 0) * 100
    except ZeroDivisionError: # Catches case where no file exceeded large file size threshold
        large_file_percent_of_dir = 0 # Sets to 0%

    # Calculates number of empty files, files missing ext and duplicates
    num_of_empty_files = len(raw_data.get('empty_files', 0))
    num_of_no_ext_files = len(raw_data.get('no_extension', 0))
    num_of_duplicates = len(raw_data.get('duplicates', 0))

    print("Finished!")

    # Returns data in a dict
    return {'empty_file_count': num_of_empty_files,
            'no_ext_count': num_of_no_ext_files,
            'large_file_count': num_of_large_files,
            'large_file_size_sum': large_size_sum,
            'large_file_size_percent_of_dir': large_file_percent_of_dir,
            'num_of_duplicates': num_of_duplicates
            }

# ======================================
# WRITE DATA TO SUMMARY FILE
# ======================================

def write_data(raw_data, analysed, PATH, SUMMARY_PATH):
    """
    Retrieves data from raw_data and analysed dicts, formats and writes to
    the summary file.

    The top lines use the .get() method to safely retrive the relevant data.
    'DIR_HEALTH_SUMMARY.txt' is written directly to SUMMARY_PATH — no
    temp file or move step needed, since 'open(..., "w")' overwrites
    automatically if the file already exists.
    """

    # This block retrieves relevant details for the summary at the top
    num_of_files = raw_data.get('files_counted', 0)
    total_size = raw_data.get('total_size', 0)
    large_file_count = analysed.get('large_file_count', 0)
    total_large_file_size_sum = analysed.get('large_file_size_sum', 0)
    large_file_percent_of_dir = analysed.get('large_file_size_percent_of_dir', 0)
    num_of_empty_files = analysed.get('empty_file_count', 0)
    num_of_files_missing_ext = analysed.get('no_ext_count', 0)
    num_of_duplicates = analysed.get('num_of_duplicates', 0)

    print("Writing data...")

    # Builds the full destination path up =
    dest_file = Path(SUMMARY_PATH) / 'DIR_HEALTH_SUMMARY.txt'

    # Opens the file directly at its final location — 'w' mode overwrites
    # automatically if it already exists, so no shutil needed at all
    with open(dest_file, 'w', encoding='utf-8') as f:

        # MAIN SUMMARY AT TOP
        print("=" * 40, file=f)
        print("Directory Health Check".center(40), file=f)
        print("=" * 40, file=f)
        print(file=f)

        print(f"PATH: {PATH}\n", file=f)

        print(f"Total num of files: {num_of_files:>11,} files", file=f)
        print(f"Total size: {total_size / (1024 * 1024):>22,.2f} MB", file=f)
        print(f"Num of large files: {large_file_count:>11,} files", file=f)
        print(f"Total large file size: {total_large_file_size_sum / (1024 * 1024):>11,.2f} MB ({large_file_percent_of_dir:.2f}% of folder)", file=f)
        print(f"Num of empty files: {num_of_empty_files:>11,} files", file=f)
        print(f"Num of files missing ext: {num_of_files_missing_ext:>5,} files", file=f)
        print(f"Num of duplicates: {num_of_duplicates:>12,} files", file=f)


        # ======================
        # DUPLICATES SECTION
        # ======================

        print(file=f)
        print("=" * 40, file=f)
        print("DUPLICATES FOUND".center(40), file=f)
        print("=" * 40, file=f)
        print(file=f)

        for d_file_name, d_paths in raw_data['duplicates'].items():
            print(f"File name:", file=f)
            print(f"    {d_file_name}", file=f)
            print(f"    Num of duplicates: {len(d_paths):,}\n", file=f)

            print("Duplicate paths:", file=f)
            for d_path in d_paths:
                print(f" - {d_path}", file=f)

            print(file=f)

        # ======================
        # EMPTY SECTION
        # ======================

        print(file=f)
        print("=" * 40, file=f)
        print("EMPTY FILES".center(40), file=f)
        print("=" * 40, file=f)
        print(file=f)

        for e_file_name, e_path in raw_data['empty_files'].items():
            print(f"File name: {e_file_name}", file=f)
            print(f"Path: {e_path}\n", file=f)

        print(file=f)
        print("=" * 40, file=f)
        print("FILES MISSING EXT".center(40), file=f)
        print("=" * 40, file=f)
        print(file=f)

        # ======================
        # NO EXT SECTION
        # ======================

        for n_file_name, n_path in raw_data['no_extension'].items():
            print(f"File name: {n_file_name}", file=f)
            print(f"Path: {n_path}\n", file=f)

    # Copy all contents of the summary file to clipboard
    with open(dest_file, 'r', encoding='utf-8') as f:
        contents = f.read()
        pyperclip.copy(contents)

    # Prints the program finishing with the destination for the summmary file
    print("Finished!\n")
    print("Summary file saved to:")
    print(dest_file)

# ======================================
# PRINT PROGRAM INFO TO TERMINAL
# ======================================

def info():
    """
    Prints basic info on how the program works. Imported textwrap module
    so that the spacing looked neat in the terminal.
    """

    help_info = """
    This program collects some basic info about a folder on your computer:

    - Calculates total file sizes
    - Catches duplicate files
    - Catches empty files
    - Shows files missing an extension
    - Catches large files (you can determine how large)
    - Saves a summary text file

    You are required to install a third party package called "pyperclip".

    There are two options to start:

    1. Default: This defaults to your HOME directory, so the program will scan any and
    all files from your home directory. The default large file size is set to 1 MB, it will
    collect any file that is bigger than 1 MB. The summary text file will be saved to your
    home directory as well.

    2. Manual: You set your own path to a folder/directory, and you specify how large a file
    to scan for IN MEGABYTES. If you are unsure about file sizes...please refer to Dr. Google.
    If you select the manual option, you will also need to decide on where to save the summary
    file

    Once you've decided on your folder/size (or selected default), the program will begin
    scanning. This is likely to take a few minutes depending on the directory you've chosen.
    If you selected default, the program will be walking through all your documents and downloads,
    etc - it's entirely normal.

    Once the program is finished, it will save the summary file to a directory - and also copy it's
    entire contents to your clipboard
    """

    # Dedent...dedents the text - nicer for printing
    print(textwrap.dedent(help_info))

# ======================================
# MAIN FUNCTION TO POWER PROGRAM
# ======================================

def main():
    """
    Powers main program, calls functions accordingly.

    1. User enters '1' for info on how the program works
    2. '2' is to configure directory scan manually
    3. '3' Configures to program to its default
    4. '4' exits the program

    An if-elif block determines which function is called. Both default and
    manual return data to a 'results' dict. The relevant values are
    retrieved so they can be passed to the functions at the end.
    """

    # Prints the main menu
    menu()

    # While loop powers main program
    while True:

        try: # Prompts user for input on their option
            option = int(input('> '))
        except ValueError: # Catches case where user doesn't enter a number
            print("Enter a number between 1-4. Try again.")
            continue

        # If-elif block determines how program is configured
        if option == 1: # Prints program info
            info()
            menu()
        elif option == 2: # Configure program manually
            result = manual()
            break
        elif option == 3: # Configure program to default
            result = default()
            break
        elif option == 4: # Exit program
            print("Exiting program. Goodbye!")
            sys.exit()
        else: # Otherwise try again
            print("Enter a number between 1-4. Try again.")
            continue

    # Retrives details from results dict (default or manual)
    PATH = result.get('path')
    LARGE_SIZE = result.get('large_file_size')
    SUMMARY_PATH = result.get('summary_path')

    # Calls functions complete program
    raw_data = collect_data(PATH, LARGE_SIZE)
    analysed = analyse_data(raw_data, LARGE_SIZE)
    write_data(raw_data, analysed, PATH, SUMMARY_PATH)

# Starts the main program
main()
