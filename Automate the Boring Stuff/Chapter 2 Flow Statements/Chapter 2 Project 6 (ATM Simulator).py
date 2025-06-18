"""
Ask the user to log in with a 4-digit PIN.
The correct PIN is hardcoded, e.g. 1234.
Give them 3 attempts before locking them out.

Once logged in, show them a menu with 3 options:
Check Balance
Withdraw Money
Exit

Balance starts at $1000.
If they withdraw:
Ask how much.

If they withdraw more than they have, print an error.
If valid, subtract it and show new balance.
If they exit, say goodbye and end the loop.
"""

# Hardcoded PIN and initial balance
correct_pin = 1234
balance = 1000
attempts = 0

# LOGIN LOOP
while attempts < 3:
    try:
        user_pin = int(input("Enter your PIN: "))
    except ValueError:
        print("PIN must be numbers only.")
        continue  # Go back and try again

    if user_pin == correct_pin:
        print("Login successful!\n")
        break  # Exit the login loop
    else:
        attempts += 1
        print("Incorrect PIN. Attempts left:", 3 - attempts)

else:
    print("Too many incorrect attempts. Account locked.")
    exit()  # Exit the program if 3 failed attempts

# MENU LOOP (only if login was successful)
while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    try:
        choice = int(input("Choose an option (1-3): "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        print("Your current balance is:", balance)

    elif choice == 2:
        try:
            withdraw = int(input("How much would you like to withdraw? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if withdraw > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw
            print("Withdrawal successful. New balance:", balance)

    elif choice == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
