"""
Even Index Extractor
Write a function that returns only the items at even indexes in a list.

List Reverser (Manual)
Write a function that takes a list and returns a new list in reverse order — without using reverse() or slicing.

Count Occurrences
Given a list of items, return how many times each item appears in a human-readable format:
['apple', 'banana', 'apple']
→ "apple: 2 times, banana: 1 time"

Total String Length
Take a list of strings and return the total number of characters across all items.
"""

# User creates a list to test with
def create_list(lst):
    print("Create your list!")

    while True:
        add = input("Enter an item you wanna add to the list or enter 'q' to quit: ")

        if add == 'q':
            print("Returning to menu!")
            return lst # Returns their created list
        else:
            lst.append(add)
            continue # Lets them keep adding items until they quit

# Prints only the items that appear at even indexes
def even_extractor(lst):
    if not lst: # Ensures list is not empty
        print("List is empty, create it (option 1) first.")
        return

    for index, item in enumerate(lst):
        if index % 2 == 0: # Even indexes only
            print(f"Even index item: {item}")

# Reverses the order of the list without reverse() method
def list_reverser(lst):
    if not lst: # Ensures list is not empty
        print("List is empty, create it (option 1) first.")
        return

    start = 0
    end = len(lst) - 1

    # Continues swapping indexes until start > end, where by the list will be fully reversed
    while start < end:
        # Swap
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst

# Come back to this later
def count_occurrences(lst):
    pass

# Determines the total amount of characters in the list
def total_string_length(lst):
    if not lst: # Ensures list is not empty
        print("List is empty, create it (option 1) first.")
        return

    total_characters = sum(len(item) for item in lst)
    print(f"Total characters:", {total_characters})

# Prints the menu when called
def print_menu():
    print("Pick one of the mini programs!")

    print("1. Even Index Extractor - returns items at even indexes.")
    print("2. List Reverser - returns items in reverse order.")
    print("3. Count Occurrences - returns how many times an item appears in the list.")
    print("4. Total String Length - returns total number of characters across all items.")
    print("5. Print the menu again.")
    print("6. Exit")

# Exits the program when called
def exit_program():
    print("Goodbye!")
    exit()

# - - WELCOME MESSAGE - - #
print("FIRST, create a least, then pick one of the mini programs!")

print("\n1. Create your list (do this first).")
print("2. Even Index Extractor - returns items at even indexes.")
print("3. List Reverser - returns items in reverse order.")
print("4. Count Occurrences - returns how many times an item appears in the list.")
print("5. Total String Length - returns total number of characters across all items.")
print("6. Print the menu again.")
print("7. Exit")

# Powers the main program
def main():

    lst = []  # Single shared list

    while True:
        try:
            choice = int(input("Enter your choice (1 - 7): "))

            # if elif block determines which function gets called depending on users input
            if choice == 1:
                lst = create_list(lst)
            elif choice == 2:
                even_extractor(lst)
            elif choice == 3:
                lst = list_reverser(lst)
                print("List reversed:")
                print(lst)
            elif choice == 4:
                count_occurrences(lst)
            elif choice == 5:
                total_string_length(lst)
            elif choice == 6:
                print_menu()
            elif choice == 7:
                exit_program()

        # Handles errors gracefully
        except ValueError:
            print("Please enter a number, no letters or symbols.")
            continue
main()