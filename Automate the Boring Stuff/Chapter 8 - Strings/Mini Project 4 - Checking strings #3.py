


def create_staff():

    while True:

        print("Enter your first name:\n")

        first_name = input('> ').strip().title()

        if not first_name:
            print("Can't be an empty string. Try again.")
            continue

        if not first_name.isalpha():
            print("Only letters for the name - try again.")
            continue

        print()
        print("Enter your last name:\n")

        last_name  = input('> ').strip().title()

        if not last_name:
            print("Can't be an empty string. Try again.")
            continue

        if not last_name.isalpha():
            print("Only letters for the last name - try again.")
            continue

        print()
        print("Enter your age:\n")

        age = input('> ')

        if not age:
            print("Can't be an empty string. Try again.")
            continue

        if not age.isdigit():
            print("Only digits for the age - try again.")
            continue

        print()
        print("Enter your department:\n")

        department  = input('> ').strip().title()

        if not department:
            print("Can't be an empty string. Try again.")
            continue

        if not department.isalpha():
            print("Only letters for the department - try again.")
            continue

        print()
        print("Enter your employee id:\n")

        employee_id  = input('> ')

        if not employee_id:
            print("Can't be an empty string. Try again.")
            continue

        has_whitespace = any(char.isspace() for char in employee_id)

        if has_whitespace == True:
            print("No white space - try again.")
            continue

        print()
        print("Enter your password:\n")

        password = input('> ')

        if len(password) < 6:
            print("Password needs to be at least 6 characters long.")
            continue

        has_number = any(char.isdigit() for char in password)

        if has_number == False:
            print("Password needs at one number - try again.")
            continue

        print(password)

        return {'first_name': first_name,
                'last_name': last_name,
                'age': age,
                'department': department,
                'employee_id': employee_id,
                'password': password
                }

output = create_staff()

print(f"Output:\n")

for k, v in output.items():

    print(f"{k}: {v}")
