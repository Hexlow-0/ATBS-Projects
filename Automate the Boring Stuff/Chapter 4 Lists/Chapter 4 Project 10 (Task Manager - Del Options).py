# VENDING MACHINE

import sys

# ==================================
# Prints the main menu for user
# ==================================
def menu():

    print("Welcome to vending machine".center(30))
    print("=" * 30)
    print("1. View items.")
    print("2. Pay for items.")
    print("3. See summary.")
    print("4. See wallet amount.")
    print("5. Print menu again.")
    print("=" * 30)

# ==================================
# Allows user to view items in the list
# ==================================

def view_item(vend_mach):

    for index, item in enumerate(vend_mach, 1):
        print(f'{str(index)}. {item}')

# ==================================
# User can pay for items in vending machine list
# ==================================

def pay_item(vend_mach, wallet):

    # Prints the list so user can see options
    for index, item in enumerate(vend_mach, 1):
        print(f'{str(index)}. {item}')

    while True:

        print("Select the item you wanna buy (1-4): ")

        try: # Catches case where user enters something unexpected
            item = int(input("(Enter '0' to quit): "))
            money = int(input("Enter how much money you wanna insert ('0' to quit): "))
        except ValueError:
            print("Enter an option between 1-4")
            continue

        # If the money they inserted is greater than the amount in their wallet, handle that case.
        if money > wallet:
            print(f"You only have ${wallet} in your wallet! Try again.")

        # If either option is zero, return to menu
        if money == 0 or item == 0:
            print("Returning to menu.")
            return wallet
            break

        # If-elif block handles payment
        if item == 1: # Item 1 in list
            if wallet < 1.5: # If user hasn't got enough money, send them back to menu
                print("You don't have enough!")
                break # Breaks the loop
            print(f"'{vend_mach[item - 1]}' bought!") # Informs user of their purchase
            vend_mach.pop(item - 1) # Removes purchased item from list
            wallet -= money # Subtracts user entered money from wallet
            change = money - 1.5 # Calculates change of item
            print(f"Your change: {change}") # Informs user of their change
            wallet += change # Adds change back to their wallet
        elif item == 2: # Same case as above
            if wallet < 43:
                print("You don't have enough!")
                break
            print(f"'{vend_mach[item - 1]}' bought!")
            vend_mach.pop(item - 1)
            wallet -= money
            change = money - 43
            print(f"Your change: {change}")
            wallet += change
        elif item == 3:
            if wallet < 3:
                print("You don't have enough!")
                break
            print(f"'{vend_mach[item - 1]}' bought!")
            vend_mach.pop(item - 1)
            wallet -= money
            change = money - 3
            print(f"Your change: {change}")
            wallet += change
        elif item == 4:
            if wallet < 45:
                print("You don't have enough!")
                break
            print(f"'{vend_mach[item - 1]}' bought!")
            vend_mach.pop(item - 1)
            wallet -= money
            change = money - 45
            print(f"Your change: {change}")
            wallet += change
        else: # In any other case, prompt user to try again.
            print("Item number must be between 1 - 4 only. Try again.")

# ==================================
# Display the amount of money remaining in wallet
# ==================================

def wallet_amount(wallet):

    print()
    print(f"Wallet amount: {wallet}\n")

# ==================================
# Summarize everything and exit
# ==================================

def summary(wallet, vend_mach):

    print("=" * 30)
    print("SUMMARY:".center(20))
    print("=" * 30)
    print()
    print(f"Money left: {wallet}")
    print(f"Items left in vending machine:")
    print(vend_mach)
    print()
    print("=" * 30)
    print()
    print("Thank you!")

    sys.exit()

# ==================================
# Main function / menu
# ==================================

def main():

    # Items in vending machine (totals $92.5)
    vend_mach = ["apple ($1.5)", "boogers ($43)", "apples #2 ($3)", "a vending machine ($45)"]

    # Amount in wallet
    wallet = 90

    # Calls menu function, printing it
    menu()

    # Powers main options
    while True:

        try: # Catches unexpected input and handles it
            option = int(input('> '))
        except ValueError:
            print("Enter a number between 1-5 only.")

        # If elif block determines which function is called based on user input
        if option == 1: # Prints items currently in vending machine
            view_item(vend_mach)
        elif option == 2: # Lets user buy items
            wallet = pay_item(vend_mach, wallet)
        elif option == 3: # Shows a summary and exits program
            summary(wallet, vend_mach)
        elif option == 4: # Shows the amount left in wallet
            wallet_amount(wallet)
        elif option == 5: # Prints the menu again
            menu()
        else: # Otherwise, prompts user to try again
            print("Pick a number between 1 - 5. Try again.")

# Calls main function, starting the program
main()



