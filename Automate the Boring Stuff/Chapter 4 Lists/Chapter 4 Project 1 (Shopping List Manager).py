"""
Create a program that lets a user build and manage a shopping list. The user should be able to:

Add an item to the list
Remove an item from the list
View the current list (with numbered entries)
Exit the program
"""

# Shopping list
shoppingList = []

# This function runs if the user wants to add an item to the shopping list
def add_item():
    add = input("Enter an item you want to add to the list: ").lower()

    if add in shoppingList: # Ensures no duplicates
        print("You already have that item on the list.")
    else:
        shoppingList.append(add)

# This function runs if the user wants to remove an item from their list
def remove_item():
    remove = input("Enter the item you want to remove from the list: ").lower()

    if remove not in shoppingList: # Ensures the user removes something that exists
        print("That item doesn't exist.")
    else:
        shoppingList.remove(remove)

# This function runs when the user wants to view their current list (with numbered entries)
def view(shoppingList):
    for index, item in enumerate(shoppingList):
        print(f"{index}. {item}")

# Says goodbye and exits the program
def exit_program():
    print("Thank you and goodbye!")
    exit()

# User menu - welcomes user and offers a choice
print("Welcome to the shopping list manager :) ")
print()
print("Choose from one of the following options:")
print()
print("1. Add an item to the list")
print("2. Remove an item from the list")
print("3. View the current list")
print("4. Exit the program")

# While loop powers the program
while True:
    try: # Catches string entries
        choice = int(input("Enter your choice (1 - 4): "))
        if choice < 1 or choice > 4:
            print("Please enter a valid choice, between 1 and 4.")
            continue

        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view(shoppingList)
        elif choice == 4:
            exit_program()

    except ValueError:
        print("Numbers only, from 1 - 4.")




