"""
Asks the user for a number multiple times
Uses a function with a parameter to check whether each number is even or odd
Uses a no-parameter function to print a friendly final message showing how many
evens and odds the user entered.
"""

# Global Variables
even_count = 0
odd_count = 0

# Function 1: With parameter
def check_even_odd(number):
    global even_count, odd_count  # Declare globals at the top of the function

    # Check if number is even or odd
    if number % 2 == 0:
        even_count += 1 # Update even_count or odd_count
        print("Number is even.") # Print whether it was even or odd

    else:
        odd_count += 1
        print("Number is odd.")

# Function 2: No parameters
def final_message():
    print("Thanks! You entered", even_count, "even numbers and", odd_count, "odd numbers.")

# Main loop
while True:
    user_input = input("Enter a number: ").lower()

    # If 'q', call final_message() and break
    if user_input == "q":
        print(final_message())
        break

    try:
        # Convert to int and call check_even_odd()
        number = int(user_input)

        check_even_odd(number)
    except ValueError:
        print("Invalid input. Please enter a number.")