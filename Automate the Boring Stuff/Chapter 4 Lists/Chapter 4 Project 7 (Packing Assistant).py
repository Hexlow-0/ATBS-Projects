# Program description and requirements
"""
Goal: Help the user manage their packing list with some precise list features you haven’t used as much yet. You must:

Functional Requirements:

View a slice of the list (user picks start & stop indexes).
Insert an item at a specific position (user provides index).
Swap two items using multiple assignment.
Find the index of an item (with .index()).
Exit the program.
"""

# Function to add an item to the packing list
def add_item(pack):
    # Loop to allow multiple item additions
    while True:
        # Prompt user for item input or quit option
        add = input("Add an item to the backpack or enter 'q' to quit: ").lower()

        # Check if user wants to quit
        if add == 'q':
            # Print visual separator
            print("-" * 30)
            # Return the updated packing list
            return pack
        # Check for duplicate items
        elif add in pack:
            # Inform user item already exists
            print("You already have that item in the backpack.")
        # Add new item to the list
        else:
            pack.append(add)
            # Confirm item addition
            print(f"{add} added to backpack.")

# Function to view a slice of the packing list
def view_slice(pack):
    # Check if list is empty
    if check_if_list_is_empty(pack):
        return

    # Main loop for slice viewing
    while True:
        try:
            # Introduce slice feature
            print("Welcome to the Pack List slicer! One thing to note:")

            # Display list size and valid index range
            print(f"List has {len(pack)} items. Use index numbers 0 through {len(pack)-1}.\n")

            # Get start and end indices from user
            start = int(input("Enter the START index: "))
            end = int(input("Enter the END index: "))

            # Validate index range
            if not (0 <= start < len(pack)) or not (0 < end <= len(pack)):
                # Inform user of invalid index
                print(f"Index must be between 0 and {len(pack)}.")
                continue

            # Display the requested slice
            print(pack[start:end])
            return

        # Handle non-integer inputs
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to insert an item at a specific index
def insert_item(pack):
    # Check if list is empty
    if check_if_list_is_empty(pack):
        return

    # Main loop for item insertion
    while True:
        # Introduce insertion feature
        print("This will allow you to insert an item at a specific position. Here is your list:\n")

        # Display current list with indices
        show_pack() # Shows items and their indexes

        # Get item and index from user
        thing = input("Enter the item you want to insert: ")
        try:
            indx = int(input("Enter the index of the item you want to insert: "))
            # Validate index is non-negative
            if indx < 0:
                print("Index must be greater than or equal to zero.")
                continue
            # Validate index is within list bounds
            elif indx > len(pack):
                print("Index must be less than or equal to", len(pack))
                continue

        # Handle non-integer inputs
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Insert item at specified index
        pack.insert(indx, thing)
        # Confirm insertion
        print(f"{thing} inserted at {indx}.")
        return

# Function to swap two items in the list
def swap_items(pack):
    # Check if list is empty
    if check_if_list_is_empty(pack):
        return

    # Main loop for swapping items
    while True:
        # Introduce swap feature
        print("This program will let you swap two items places!\n")

        # Display current list with indices
        show_pack()

        try:
            # Get indices of items to swap
            indx1 = int(input("Enter the index of the first item you want to swap: "))
            indx2 = int(input("Enter the index of the second item you want to swap: "))

            # Validate indices are non-negative
            if indx1 < 0 or indx2 < 0:
                print("Index must be greater than or equal to zero.")
                continue
            # Validate indices are within list bounds
            elif indx1 >= len(pack) or indx2 >= len(pack):
                print("Index must be less than or equal to", len(pack))
                continue

        # Handle non-integer inputs
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Store swapped items for confirmation
        item1 = pack[indx1]
        item2 = pack[indx2]
        # Swaps
        pack[indx1], pack[indx2] = pack[indx2], pack[indx1]
        # Confirm swap
        print(f"{item1} swapped with {item2}.")

        # Display updated list
        show_pack()

        return

# Function to find the index of an item
def find_index(pack):
    # Check if list is empty
    if check_if_list_is_empty(pack):
        return

    # Main loop for finding item index
    while True:
        # Introduce index finding feature
        print("This program will let you find the index of an item in your pack list!\n")

        # Get item to find or quit option
        indx3 = input("Enter the item you want to find (or 'q' to quit): ").lower()

        # Check if user wants to quit
        if indx3 == 'q':
            # Confirm return to menu
            print("Returning to menu.")
            # Display menu
            print_menu()
            return
        # Check if item exists in list
        if indx3 in pack:
            # Display item index
            print(f"Index of that item is: {pack.index(indx3)}")
            return
        # Handle item not found
        elif indx3 not in pack:
            print(f"{indx3} not in the list.")
            continue

# I was going to add this too, but as it's not in the requirements...I'm skipping for now.
def del_index():
    pass

# Function to display the packing list with indices
def show_pack(pack):
    for index, item in enumerate(pack):
        print(f'Index {index} in pack list is: {item}')

# Function to display the main menu
def print_menu():
    print()
    print("1. Add items to your packing list.")
    print("2. View a slice of your packing list.")
    print("3. Insert an item at a specific position of your packing list.")
    print("4. Swap two items in your packing list.")
    print("5. Find the index of an item in your packing list.")
    print("6. Delete a specific item from your packing list.")
    print("7. Exit the program.")
    print()

# Function to check if the packing list is empty
def check_if_list_is_empty(pack):
    # Check if list is empty and inform user
    if not pack:
        print("The list is empty. Add some items first.")
        return True
    return False

# Function to exit the program
def exit_program():
    print("Goodbye!")
    exit()

# Welcome message
print("Welcome to the Packing Assistant!")

# Display initial menu
print_menu()

# Main program function
def main():

    # Initialize empty packing list
    pack = []

    # Main program loop
    while True:
        try:
            # Get user menu choice
            choice = int(input("Enter your choice: "))

            # Handle menu selections
            if choice == 1:
                pack = add_item(pack)
            elif choice == 2:
                view_slice(pack)
            elif choice == 3:
                insert_item(pack)
            elif choice == 4:
                swap_items(pack)
            elif choice == 5:
                find_index(pack)
            elif choice == 6:
                # Delete item (not implemented)
                del_index(pack)
            elif choice == 7:
                exit_program()

        # Handle non-integer inputs
        except ValueError:
            print("Invalid input, enter numbers only.")

# Start the program
main()