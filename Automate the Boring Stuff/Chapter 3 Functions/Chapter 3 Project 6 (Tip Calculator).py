"""
📋 Requirements
Ask the user for:
The total bill amount (e.g., $56.78)
How much tip they want to leave (e.g., 15%)

Use a function calculate_tip(bill, tip_percent) to:
Return the tip amount (not print it)

Use another function print_result() (no parameters) to:
Display the tip amount and total amount (bill + tip)
Repeat until the usr types 'q' when asked if they want to calculate another tip.
"""

"""
def calculate_tip(bill, tip_percent):
    # calculate the tip amount
    return tip_amount

def print_result(bill, tip):
    # print formatted message with tip and total

while True:
    # ask for bill amount or 'q' to quit
    # ask for tip percentage
    # handle errors (e.g. non-numeric input)
    # call your functions
"""

def calculate_tip(bill, tip_percent):
    tip_amount = bill * (tip_percent / 100)
    return tip_amount

def print_result(tip_percent, total_bill):
    print(f"You tipped {tip_percent}%. Your total bill is ${total_bill:.2f}.")

while True:
    bill_input = input("Enter your bill or enter 'q' to quit: ").lower()
    if bill_input == "q":
        break

    tip_input = input("Enter your tip percentage or enter 'q' to quit: ").lower()
    if tip_input == "q":
        break

    try:
        bill = float(bill_input)
        tip_percent = float(tip_input)

        tip = calculate_tip(bill, tip_percent)
        total = bill + tip

        print_result(tip_percent, total)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
