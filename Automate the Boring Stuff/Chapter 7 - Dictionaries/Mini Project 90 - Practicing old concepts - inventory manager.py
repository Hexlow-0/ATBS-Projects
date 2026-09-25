
inventory = {
    "apple": {"price": 1.20, "stock": 50},
    "banana": {"price": 0.80, "stock": 35},
    "bread": {"price": 3.50, "stock": 12},
    "milk": {"price": 2.75, "stock": 18},
}

# =======================================
# Prints the main menu
# =======================================

def main_menu():
    """Prints the list of options for user to call from to use program"""

    print("=" * 40)
    print("INVENTORY MANAGER".center(40))
    print("=" * 40)
    print()
    print("1. Get price of an item")
    print("2. Restock an item")
    print("3. Add an item")
    print("4. Remove an item")
    print("5. Low stock report.")
    print("6. View whole inventory")
    print("7. Quit the program.")
    print("8. Print main menu again.\n")

# =======================================
# PHASE 1 - RETURN PRICE OF AN ITEM
# =======================================

def return_price():
    """
    Return price function:
    - User enters name of item
    - Check if user wants to return to menu
    - Check if item is already in dict
    - Otherwise, print the price of the item
    """

    # Print purpose of section
    print("=" * 40)
    print("GET PRICE OF ITEM".center(40))
    print("=" * 40)
    print()

    # Print the items currently in inventory
    view_items_only()

    print()

    print("Enter an item from the list to see it's price (blank to exit).\n")

    # While loop allows user to check price of multiple items
    while True:

        # Prompt user for theur input
        item_name = input('> ').lower()

        # Elif block handles exit and exception
        if item_name == '': # If empty string, return to menu
            print("Returning to menu.")
            break
        elif item_name not in inventory: # If item not in inventory, try again
            print(f"'{item_name}' not in inventory. Try again.")
            continue

        # Prints the price of the user entered item
        print(f"Price of {item_name}: ${inventory.get(item_name, {}).get('price')}")

# =======================================
# PHASE TWO - RESTOCK ITEM BY AMOUNT
# =======================================

def restock():
    """
    Lets the user restock specific item
    - Asks for the item they want to restock
    - Checks if it exists
    - Asks them for the amount they want to add stock-wise
    - Performs the same exception handling
    - Adds user specified amount to specific items stock
    """

    # Print purpose of this section
    print("=" * 40)
    print("RESTOCK AN ITEM".center(40))
    print("=" * 40)
    print()

    # Print items currently in list for user to see
    view_items_only()

    print()

    print("Enter an item from the list to restock (blank to exit).\n")

    # While loop allows user to restock multiple items
    while True:

        # Prompt the user for the item they want to restock
        restock_item = input('> ').lower()

        # If elif block handles exit and exception
        if restock_item == '': # If empty string, return to menu
            print("Returning to menu.")
            break
        elif restock_item not in inventory: # If item not in inventory, try again
            print(f"'{restock_item}' not in inventory. Try again.")
            continue

        print()
        print("Enter the amount you want to add to the items stock.\n")

        try: # Prompts the user for the amount they want to add
            amount = int(input('> '))
        except ValueError: # If user enters unexpected value, try again
            print("Enter a number to adjust stock. Try again")
            continue

        # If elif block handles exit and exception
        if amount == '': # Return to menu if empty string
            print("Returning to menu.")
            break
        elif amount < 0: # If amount less than zero, try again
            print(f"The amount to restock an item must be greater than zero.")
            continue

        # Adds user specified amount to the stock of user specified item
        inventory[restock_item]['stock'] += amount

        # Updates user on successful operation
        print(f"'{amount}' added to '{restock_item}'.")
        print(f"Updated items stock is now: {inventory.get(restock_item, {}).get('stock')}\n")

# =======================================
# PHASE THREE - ADD ITEM TO INVENTORY
# =======================================

def add_item():
    """
    Add am item, price and it's stock to the inventory
    - Prompts user for a new item
    - Check if that item already exists
    - Prompts the user for the items price and stock count
    - Adds the item and its values to the inventory
    """

    # Print purpose of this section
    print("=" * 40)
    print("ADD ITEMS TO INVENTORY".center(40))
    print("=" * 40)
    print()

    # Print items currently in inventory
    view_items_only()

    print()

    print("Enter an item to add to inventory (blank to exit).\n")

    # While loop allows user to add multiple items to inventory
    while True:

        # Prompts the user for the item they want to add
        new_item = input('> ').lower()

        # If elif block handes return and exception
        if new_item == '': # If empty string, return to menu
            print("Returning to menu.")
            break
        elif new_item in inventory: # If item already IN inventory, try again
            print(f"'{new_item}' is already in inventory. Try again.")
            continue

        print(f"Enter the price for {new_item}.\n")

        try: # Prompts the user for the price for that item
            price = float(input('> '))
        except ValueError: # If user enters something unexpected - handle that case
            print("Price must be a number - try again.")
            continue

        # If elif block handes return and exception
        if price == '': # If empty string, return to menu
            print("Returning to menu.")
            break
        elif price < 0: # If price less than zero, try again
            print(f"The price of an item must be a positive number.")
            continue

        print(f"Price set at {price}. Add the stock of that item.\n")

        try: # Prompts the user for the stock for that item
            stock = int(input('> '))
        except ValueError: # If user enters something unexpected - handle that case
            print("Price must be a number - try again.")
            continue

        # If elif block handes return and exception
        if stock == '': # If empty string, return to menu
            print("Returning to menu.")
            break
        elif stock < 0: # If price less than zero, try again
            print(f"The stock of an item must be a positive number.")
            continue

        # Add the item to inventory, stock price and stock in a nested dict
        inventory[new_item] = {'price': price, 'stock': stock}

        # Update user on the successful operation
        print()
        print("Inventory updated!")
        print(f"Item added: {new_item}")
        print(f"Price: ${price}")
        print(f"Stock: {stock}\n")

# =======================================
# PHASE 4 - REMOVE ITEM FROM INVENTORY
# =======================================

def remove_item():
    """
    Removed a specific item from the inventory
    - Asks the user for a specific item
    - Checks if it exists
    - Removes the item from the inventory
    """

    # Print purpose of this section
    print("=" * 40)
    print("REMOVE AN ITEM".center(40))
    print("=" * 40)
    print()

    # Print items currently in inventory
    view_items_only()

    print()

    print("Enter an item from the list to remove it (blank to exit).\n")

    # While loop allows user to remove multiple items
    while True:

        # Prompt user for the item they want to remove
        remove_item = input('> ').lower()

        # If elif block handes exit and exception case
        if remove_item == '': # If empty string, return to menu
            print("Returning to menu.")
            break
        elif remove_item not in inventory: # If item not in inventory, try again
            print(f"'{remove_item}' not in inventory. Try again.")
            continue

        # Delete user specified item from inventory
        del inventory[remove_item]

        # Update user on successful operation
        print()
        print(f"'{remove_item} successfully removed.\n")


# =======================================
# PHASE FIVE - PRINT LOW STOCK ITEMS
# =======================================

def low_stock_report():
    """
    Prints items with stock less than a user specified amount
    - Prompts user for a threshold number
    - Handles exceptions (greater than zero, etc)
    - Prints items in inventory filtered through condition
    - Returns to menu once finished
    """

    # Print purpose of this section
    print("=" * 40)
    print("LOW STOCK REPORT".center(40))
    print("=" * 40)
    print()

    # Explain how this section works
    print("The number you enter will show items in the inventory that have stock")
    print("less than that number. A report will print accordingly. Enter blank to exit.\n")

    # While loop helps in handling expection cases - user can make mistakes
    while True:

        try: # Prompts user for threshold number
            threshold = int(input('> '))
        except ValueError: # If user enters something unexpected - handle gracefully
            print("Must be a number - try again.")
            continue

        # If elif block handles return and exception case
        if threshold == '': # If empty string, return to menu
            print("Returning to menu.")
            break
        elif threshold < 0: # If threshold not a postive number, try again
            print("Number must be positive - try again.")
            continue

        print()

        # For each item and its data in inventory dict...
        for item, item_data in inventory.items():

            # Stock proce and stock in variables
            price = item_data['price']
            stock = item_data['stock']

            # If the stock count is LESS THAN the threshold...
            if stock < threshold:

                # Then print each item and it's price and stock
                print(f"Item: {item} | ${price} | Stock: {stock}")

        # Report complete
        print("=" * 40)
        print("REPORT COMLETE".center(40))
        print("=" * 40)
        print()

        # Returns the user to the menu
        print("Returning to menu.")

        break

# =======================================
# VIEW INVENTORY ITEM FUNCTIONS
# =======================================

def view_items_only():

    # Prints each item in the inventory - nothing else
    for item, item_data in inventory.items():

        print(f"Item: {item}")

def view_whole_inventory():
    """
    Prints the entire inventory
    - Prints the item, pirce and stock of each item
    """

    # Print purpose of this section
    print("=" * 40)
    print("FULL INVENTORY".center(40))
    print("=" * 40)
    print()

    # For each item and its data in inventory dict...
    for item, item_data in inventory.items():

        # Stock proce and stock in variables
        price = item_data['price']
        stock = item_data['stock']

        # Print every item, price and it's stock in the inventory
        print(f"Item: {item} | ${price} | Stock: {stock}")

    print()

# =======================================
# MAIN MENU PROGRAM
# =======================================

def main():
    """
    Main menu powers the program
    - Prompts the user for a number from a list of options
    - If-elif block calls a function based on number
    """

    # Print the main menu
    main_menu()

    # While loop powers the main program
    while True:

        print("Select an option from above by entering a number. Enter 8 to see menu again.\n")

        try: # Prompt the user for a number out of provided options
            option = int(input('> '))
        except ValueError: # If user enters something unexpected - handle gracefully
            print("Must be a number between 1 - 8. Try again.")
            continue

        # If elif block decides which function to call based on user input
        if option == 1:
            return_price() # Prints price of user specified item
        elif option == 2:
            restock() # Restock specific item
        elif option == 3:
            add_item() # Add am item to inventory
        elif option == 4:
            remove_item() # Remove specific item
        elif option == 5:
            low_stock_report() # Print items less than user specified stock amount
        elif option == 6:
            view_whole_inventory() # Print the whole inventory
        elif option == 7:
            print("Exiting program. Thank you! :)")
            break # Exit the program
        elif option == 8:
            main_memu() # Print the main menu for user to see options again
        else: # In any other case, prompt user to try again
            print("Enter a number between 1 - 8. Try again.")

# Call main function, starting the program
main()
