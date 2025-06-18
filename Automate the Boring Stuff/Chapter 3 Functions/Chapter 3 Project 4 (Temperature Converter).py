"""
🎯 Mini Project: Temperature Converter with Menu
You’ll build a small program where the user can:

Choose whether they want to convert:

Celsius to Fahrenheit, or
Fahrenheit to Celsius

Input the temperature
See the converted result
Be prompted to convert another temperature or quit
"""

def C_to_F(temp):
    return (temp * 9 / 5) + 32

def F_to_C(temp):
    return (temp - 32) * 5 / 9

def farewell():
    print("Goodbye!")

while True:
    user_input = input("Enter 'F' to convert from Fahrenheit, 'C' from Celsius, or 'Q' to quit: ").lower()

    if user_input == "q":
        farewell()
        break

    temp_input = input("Enter the temperature to convert: ")

    try:
        temp = float(temp_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_input == "f":
        converted = F_to_C(temp)
        print(f"{temp}°F is {round(converted, 2)}°C")

    elif user_input == "c":
        converted = C_to_F(temp)
        print(f"{temp}°C is {round(converted, 2)}°F")

    else:
        print("Invalid option. Please try again.")






