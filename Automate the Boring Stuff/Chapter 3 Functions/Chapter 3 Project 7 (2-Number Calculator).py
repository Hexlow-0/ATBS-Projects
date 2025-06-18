"""
Ask the user for two numbers.
Ask what operation they want to perform: add, subtract, multiply, or divide.
Use a function with parameters to perform the calculation and return the result.
Use a separate function without parameters to say goodbye when they type "q".
"""

# Function does the calculation depending on the users chosen operator
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Farewell message appears upon program exit
def farewell():
    print("Thanks for using the calculator. Goodbye!")

# Start a loop so the user can keep using the calculator
while True:
    operator = input("Enter operation (+, -, *, /) or enter 'q' to quit: ").strip()

    if operator.lower() == "q":
        farewell()
        break

    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator. Please try again.")
        continue

    # Get the numbers from the user
    try:
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))
    except ValueError:
        print("Numbers only, please. Try again.")
        continue

# Call the function and print the result
    result = calculate(input1, input2, operator)
    print(f"The result is: {result}!")