"""
A program that lets users track cities they’ve visited.

✅ Required Features:

Add a trip — Prompt for city, country, year; store as tuple.
View trips — Show list of trips with numbering.
Sort trips — Alphabetically by country or by year visited (user chooses).
Delete a trip — Remove one by number (not name).
Exit program — Say goodbye, etc.
"""



def add_trip(tripList):
    while True:
        city = input("Enter the city name (or 'q' to quit): ").title().strip()
        if city.lower() == 'q':
            program_divider()
            return tripList

        country = input("Enter the country name: ").title().strip()
        year = input("Enter the year you visited (e.g., 2022): ").strip()

        trip = (city, country, year)

        if trip in tripList:
            print("You've already logged this trip.")
        else:
            tripList.append(trip)
            print(f"{trip} added!")

def view_trips(tripList):
    for index, trip in enumerate(tripList, start=1):
        print(f"{index}. {trip}")

def sort_trips(tripList):
    print("Welcome to the trip sorter!")
    print("\n1. Alphabetically sort by country.")
    print("2. Sort by year visited.")

    while True:
        choice2 = input("Enter your choice (1 - 2) or 'q' to quit: ").lower()

        if choice2 == 'q':
            program_divider()
            print("Back to the main menu!")
            break
        elif choice2 == "1":
            tripList.sort(key=lambda trip: trip[1].lower())  # Sort by country
            print("Successfully sorted trips by country alphabetically!")
            break
        elif choice2 == "2":
            tripList.sort(key=lambda trip: trip[2])  # Sort by year
            print("Successfully sorted trips by year visited!")
            break
        else:
            print("Invalid choice, enter 1 or 2.")

    return tripList

def delete_trip(tripList):
    if not tripList:
        print("Your trip list is empty.")
        return tripList

    print("Here are your trips:")
    for i, trip in enumerate(tripList, start=1):
        print(f"{i}. {trip}")

    while True:
        choice = input("Enter the number of the trip to delete, or 'q' to quit: ").strip().lower()

        if choice == 'q':
            program_divider()
            return tripList
        elif choice.isdigit() and 1 <= int(choice) <= len(tripList):
            removed = tripList.pop(int(choice) - 1)
            print(f"Removed {removed}")
            return tripList
        else:
            print("Invalid input. Please enter a valid number.")


    return tripList

def program_divider():
    print("-" * 30)

def exit_program():
    print("Goodbye!")
    exit()

# - - Welcome Message & Menu - - #
print("Welcome to the Travel Tracker!")

print("\n1. Add a trip.")
print("2. View trips.")
print("3. Sort trips.")
print("4. Delete a trip.")
print("5. Exit.\n")

def main():
    tripList = []

    while True:
        try:
            choice = input("Enter your choice (1 - 5): ")

            if choice == "1":
                add_trip(tripList)
            elif choice == "2":
                view_trips(tripList)
            elif choice == "3":
                sort_trips(tripList)
            elif choice == "4":
                delete_trip(tripList)
            elif choice == "5":
                exit_program()

        except ValueError:
            print("Invalid input, please enter a number between 1 and 5.")
            continue

main()
