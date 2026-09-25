"""
🧩 Requirements
The initial list of spies is hardcoded:
["Ghost", "Shadow", "Viper", "Phantom", "Wraith"]

Ask the user for:

The code name of the new spy.
The index where they want to insert the spy.
Validate that the index:
Is a number.
Is in range (0 through len(list)).
Insert the spy at the correct index using insert().

Print the new list with index numbers clearly shown, like:

0: Ghost
1: Shadow
2: Whisper
3: Viper
...
Keep asking if they want to add another spy. Loop until they type 'q'.
"""

# Global List
spies = ["Ghost", "Shadow", "Viper", "Phantom", "Wraith"]

# Function that runs the program
def code_name(spies):
    while True:
        spy_Name = input("Enter the name of the new spy you want to insert (or 'q' to quit): ").lower()

        # if elif block checks if the user wants to quit and ensures the spy name isn't taken
        if spy_Name == "q":
            print("Goodbye!")
            break
        elif spy_Name in spies:
            print("That spy already exists! Try again.")
            continue

        # Provides the user with what spy is at what index
        for index, item in enumerate(spies):
            print(f'Index {index} in pack list is: {item}')

        try: # Asks the user at what index they want their name to be set at
            indx = int(input(f"At which index do you want to insert '{spy_Name}'"))

            # Ensures chosen index is within the lists range
            if indx < 0 or indx > len(spies):
                print("Error, that index does not exist, try again!")
                continue

            # Insert user determined name at user determined index
            spies.insert(indx, spy_Name)

            # Shows the user the new list
            for index, item in enumerate(spies):
                print(f'Index {index} in pack list is: {item}')

        # Handles invalid input errors gracefully
        except ValueError:
            print("Please enter a number.")
            continue

# Calls function and starts program
code_name(spies)

