"""
🛠️ Requirements:
Create 4 functions: add(), subtract(), multiply(), and divide(), each accepting two parameters and
returning the result. Use input() to let the user pick an operation (+, -, *, /) and enter two numbers.

Use try/except to handle:
Non-number inputs
Division by zero

Loop the program so the user can perform multiple calculations until they choose to quit.
Use return to send results back to the main part of your code (not print() inside the function).
Use if/elif/else to control which function is called.
"""

# Define functions first
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Welcome the user
print("Welcome to the mini calculator!")
print("**********************************")
print("Enter 'q' at any time to quit.\n")

# Start a loop so the user can keep using the calculator
while True:
    op = input("Enter operation (+, -, *, /): ").strip()

    if op.lower() == "q":
        print("Goodbye!")
        break

    if op not in ["+", "-", "*", "/"]:
        print("Invalid operator. Please try again.")
        continue

    # Get the numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Numbers only, please. Try again.")
        continue

    # Call the correct function based on operator
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)

    print("Result:", result)
    print()
