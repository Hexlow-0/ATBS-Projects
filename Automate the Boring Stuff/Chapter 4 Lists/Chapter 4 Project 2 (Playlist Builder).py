"""
Playlist program allowed you to add songs to a list, remove them, shuffle the list,
list the songs in the list, and exit the program
"""

# Import random for playlist shuffle function
import random

# Playlist variable is global
playlist = []

# Add a song to the playlist
def add_song():
    while True: # Continues to add songs until user is finished
        add = input("Add your song to the playlist or press 'q' to return to menu: ").strip()

        if add in playlist: # Checks for duplicates
            print("Song is already in playlist")
        elif add.lower() == 'q':
            # Quits back to menu when user is finished
            print("-" * 30) # Section divider
            break
        else: # Otherwise continues to allow user to add songs
            playlist.append(add.title())

# Removes a song from a playlist
def remove_song():
    while True: # Continues to ask user to remove songs until they're finished
        remove = input("Remove a song from playlist or press 'q' to return to menu: ").strip()

        if remove not in playlist: # Ensures song exists in playlist
            print("Song is not in playlist")
        elif remove.lower() == 'q':
            # Quits back to menu when user is finished
            print("-" * 30) # Section divider
            break
        else:
            playlist.remove(remove.title()) # Otherwise continues to allow user to remove songs
            print(f"'{remove}' removed from playlist.")

# Shuffles the playlist index
def shuffle_list():
    if playlist:
        random.shuffle(playlist)
        print("Playlist shuffled successfully")
        print("-" * 30) # Section divider
    else:
        print("Your playlist is empty. Nothing to shuffle.")

# Lists out all the items in the list, starting at 1
def view_playlist():
    if playlist:
        print("-" * 30)  # Section divider
        for index, song in enumerate(playlist, start=1):
            print(f"{index}) {song}")
        print("-" * 30) # Section divider

    else:
        print("Your playlist is empty.")

# Exits the program when called
def exit_program():
    print("Goodbye!")
    print("-" * 30) # Section divider
    exit()

# User UI Menu
print("Welcome to the Playlist Builder!")
print()
print("1. Add songs to the playlist")
print("2. Remove songs from the playlist")
print("3. Shuffle the playlist")
print("4. List the songs in the playlist")
print("5. Exit the program")
print()

# While loop powers the program
while True:
    try: # Catches string inputs
        choice = int(input("Enter your choice (1-5): "))

        # Ensures input is between 1 and 5
        if choice < 1 or choice > 5:
            print("Please enter a number from 1 to 5")
            continue

        # Calls correct function depending on user input
        if choice == 1:
            add_song()
        elif choice == 2:
            remove_song()
        elif choice == 3:
            shuffle_list()
        elif choice == 4:
            view_playlist()
        elif choice == 5:
            exit_program()

    # Catches errors and sends user back to enter a valid choice
    except ValueError:
        print("Please enter numbers only, between 1 and 5.")
        continue