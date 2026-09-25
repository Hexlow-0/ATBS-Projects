



# ==================================
# PRINTS THE MAIN MENU
# ==================================

def print_main_menu():

    print("=" * 40)
    print("CONTACT BOOK".center(40))
    print("=" * 40)
    print()
    print("1. Add a contact.")
    print("2. Look up a contact.")
    print("3. View all contacts.")
    print("4. Delete a contact.")
    print("5. Quit.")
    print()


# ==================================
# PART 1 - ADD CONTACTS TO BOOK
# ==================================

def add_contact(contact_book):

    print("=" * 40)
    print("ADD CONTACT".center(40))
    print("=" * 40)
    print()

    while True:

        print("Enter a name for your contact (blank to exit):\n")

        name = input('> ').title()

        if name == '':
            print("Saving changes, returning to menu.")
            return contact_book
        if name in contacts:
            print(f"'{name}' is already in contacts. Try again.")


        try:
            phone = int(input('Enter phone number: '))
        except ValueError:
            print("Phone number must be numbers only. Try again.")
            continue

        print()
        print("Enter contacts email:\n")

        email = input('> ').lower()

        print()
        print("Enter contacts city:\n")

        city = input('> ').upper()

        contact_book[name] = {'phone': phone, 'email': email, 'city': city}

        print()
        print("Contact book updated:")
        print(f"Name: {name}")
        print(f"number: {phone}")
        print(f"email: {email}")
        print(f"city: {city}\n")


# ==================================
# PART TWO - LOOK UP BY CONTACT
# ==================================

def lookup_contact(contact_book):

    if not contact_book:
        print("Contact book is empty. Fill with entries first.")
        return

    print("=" * 40)
    print("LOOK UP CONTACT".center(40))
    print("=" * 40)
    print()

    view_contact_names(contact_book)

    while True:

        print("Enter one of your contact names to see their details (blank to quit):")

        look_up = input('> ').title()

        if look_up == '':
            print("Returning to menu!")
            break
        elif look_up not in contact_book:
            print(f"'{look_up}' does not exist in contact book. Try again.")
            continue

        print()
        print(f"{look_up}'s info:")
        print(f"Number: {contact_book.get(look_up, {}).get('phone')}")
        print(f"Email: {contact_book.get(look_up, {}).get('email')}")
        print(f"City: {contact_book.get(look_up, {}).get('city')}\n")

# ==================================
# PRINT CONTACT INFORMATION
# ==================================

def view_contact_names(contact_book):

    if not contact_book:
        print("Contact book is empty. Fill with entries first.")
        return

    print("=" * 40)
    print("CONTACT NAMES".center(40))
    print("=" * 40)
    print()

    for contact_name, contact_data in contact_book.items():

        print(f"Name: {contact_name}")

    print()

def view_contacts(contact_book):

    if not contact_book:
        print("Contact book is empty. Fill with entries first.")
        return

    print("=" * 40)
    print("PRINT ALL CONTACTS".center(40))
    print("=" * 40)
    print()

    for contact_name, contact_data in contact_book.items():

        phone = contact_data['phone']
        email = contact_data['email']
        city = contact_data['city']

        print(f"Name: {contact_name}")
        print(f"Number: {phone}")
        print(f"Email: {email}")
        print(f"City: {city}\n")


# ==================================
# PART FOUR - DELETE BY CONTACT NAME
# ==================================

def delete_contact(contact_book):

    if not contact_book:
        print("Contact book is empty - try adding to it first.")
        return

    print("=" * 40)
    print("DELETE CONTACTS".center(40))
    print("=" * 40)
    print()

    view_contact_names(contact_book)

    while True:

        print("Enter a name from contacts to delete their info (blank to quit).")

        name = input('> ').title()

        if name == '':
            print("Saving contacts, returning to menu!")
            return contact_book
        elif name not in contact_book:
            print(f"'{name}' not in contact book - try again.")
            continue

        del contact_book[name]

        print(f"'{name}' successfully deleted from contacts.\n")


# ==================================
# MAIN FUNCTION TO POWER PROGRAM
# ==================================

def main():

    contact_book = {
    "Alice Johnson": {
        "phone": "555-123-4567",
        "email": "alice.johnson@example.com",
        "city": "Sydney"
    },
    "Bob Smith": {
        "phone": "555-234-5678",
        "email": "bob.smith@example.com",
        "city": "Melbourne"
    },
    "Carol Lee": {
        "phone": "555-345-6789",
        "email": "carol.lee@example.com",
        "city": "Brisbane"
    },
    "David Brown": {
        "phone": "555-456-7890",
        "email": "david.brown@example.com",
        "city": "Perth"
    },
    "Emma Wilson": {
        "phone": "555-567-8901",
        "email": "emma.wilson@example.com",
        "city": "Adelaide"
    }
}

    while True:

        print_main_menu()

        try:
            option = int(input('> '))
        except ValueError:
            print("Enter a number between 1 - 5. Try again.")
            continue

        if option == 1:
            contact_book = add_contact(contact_book)
        elif option == 2:
            lookup_contact(contact_book)
        elif option == 3:
            view_contacts(contact_book)
        elif option == 4:
            contact_book = delete_contact(contact_book)
        elif option == 5:
            print("Exiting program. Good bye! :)")
            break
        else:
            print("Enter a number between 1 - 5. Try again.")

main()
