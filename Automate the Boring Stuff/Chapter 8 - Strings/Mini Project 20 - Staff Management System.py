
import pyperclip
import sys

# AI gave me this post completion
from textwrap import dedent


staff = {
    "alice": {"full_name": "Alice Smith", "department": "Engineering", "email": "alice.smith@company.com", "city": "Sydney"},
    "bob": {"full_name": "Bob Jones", "department": "Marketing", "email": "bob.jones@company.com", "city": "Melbourne"},
    "charlie": {"full_name": "Charlie Brown", "department": "HR", "email": "charlie.brown@company.com", "city": "Brisbane"},
}

# =============================
# SEE STAFF ON LIST
# =============================

def see_staff():

    print("Staff on list:\n")

    for names in staff.keys():

        print(f"Name: {names}")

    print()

# =============================
# GET AND VALIDATE STAFF NAME
# =============================

def get_name():

    print("=" * 40)
    print("ENTER STAFF NAME".center(40))
    print("=" * 40)
    print()

    see_staff()

    print("Enter 'q' to quit.\n")

    while True:

        # Don't remember how to check if digit is in a string - Not Googling bc that's cheating
        name = input('> ').strip().strip('0123456789').lower()

        if name == '':
            print("No empty strings - try again.")
            continue

        if name == 'q':
            print("Exiting program")
            sys.exit()

        if name not in staff: # Use to be it's own function - put in here AFTER developing code myself - ai pointed out logic error
            print("Name does not exist. Try again.")
            continue

        return name

# =============================
# PRINT A SUMMARY OF USER
# =============================

def print_summary(name):

    print("=" * 40)
    print("STAFF DETAILS".center(40))
    print("=" * 40)
    print()

    data = staff[name]

    full_name = data['full_name']
    dept = data['department']
    email = data['email']
    city = data['city']

    col1, col2 = 15, 10

    print("Full name:".ljust(col1) + full_name.ljust(col2))
    print("Department:".ljust(col1) + dept.ljust(col2))
    print("Email:".ljust(col1) + email.ljust(col2))
    print("City:".ljust(col1) + city.ljust(col2))
    print()

    return {
        'name': full_name,
        'dept': dept,
        'email': email,
        'city': city,
    }


# =============================
# DEFINE MESSAGE TEMPLATES
# =============================

def message_template(staff_member):

    print("=" * 40)
    print("MESSAGE TEMPLATES".center(40))
    print("=" * 40)
    print()

    # =============================
    # STORE STAFF DATA AT TOP
    # =============================

    name = staff_member.get('name')
    dept = staff_member.get('dept')
    email = staff_member.get('email')
    city = staff_member.get('city')

    # =============================
    # MEETING INVITE TEMPLATE
    # =============================

    # ai had the dedent idea
    meeting_invite = dedent(f"""
    Subject: Meeting Invitation

    Dear {name},

    You are invited to attend your upcoming meeting with management, scheduled for
    next week. Please use the link below to select a suitable time and add the
    meeting to your calendar.

    <link>

    These regular meetings help ensure effective communication across departments
    and provide an opportunity to discuss updates, challenges, and upcoming work.

    Please come prepared to discuss any agenda items you would like to raise and
    provide updates on any action items assigned during previous meetings.

    Note - this message is addressed to {name}. Details:

    City: {city}
    Dept: {dept}
    Email: {email}

    If you believe you have received this message in error, please disregard it.

    Kind regards,
    Management
    """)

    # =============================
    # POLICY REMINDER TEMPLATE
    # =============================

    policy_reminder = dedent(f"""
    Subject: Policy Reminder

    Dear {name},

    This is a friendly reminder to review and comply with company policies and
    procedures relevant to your role.

    Maintaining compliance with workplace policies helps ensure a safe,
    professional, and productive environment for all employees.

    If you have any questions regarding company policies or require clarification,
    please speak with your manager or the Human Resources team.

    Note - this message is addressed to {name}. Details:

    City: {city}
    Dept: {dept}
    Email: {email}

    If you believe you have received this message in error, please disregard it.

    Kind regards,
    Management
    """)

    # =============================
    # WELCOME MESSAGE TEMPLATE
    # =============================

    welcome_message = dedent(f"""
    Subject: Welcome to the Team

    Dear {name},

    Welcome to [Company Name]. We are pleased to have you join our team and look
    forward to working with you.

    As discussed during the recruitment process, your onboarding materials and
    account setup instructions will be sent to your registered work email. Please
    use the link below to access the onboarding portal:

    <link>

    If you experience any issues accessing your account or onboarding resources,
    please contact the IT Support team for assistance.

    Note - this message is addressed to {name}. Details:

    City: {city}
    Dept: {dept}
    Email: {email}

    If you believe you have received this message in error, please disregard it.

    Kind regards,
    Management
    """)

    # =============================
    # PROMPT USER TO PICK A TEMPLATE
    # =============================

    print("Which template would you like?\n")

    print("1. Meeting invite.")
    print("2. Policy Reminder.")
    print("3. Welcome Message.")

    while True:

        try:
            option = int(input('> '))
        except ValueError:
            print("Must be a digit between 1 - 3. Tr again.")
            continue

        # If elif block determines what message to return
        if option == 1:
            return meeting_invite
        elif option == 2:
            return policy_reminder
        elif option == 3:
            return welcome_message
        else:
            print("Must be a number between 1 - 3. Try again.")

# =============================
# GENERATE MESSAGE AND COPY
# =============================

def generate_message(message, staff_member):

    print("=" * 40)
    print("YOUR MESSAGE".center(40))
    print("=" * 40)
    print()

    print(message)

    print("=" * 40)
    print()

    pyperclip.copy(message)

    print("Message copied to clipboard!\n")

    print("=" * 40)
    print("PROGRAM FINISHED".center(40))
    print("=" * 40)
    print()


# =============================
# MAIN FUNCTIONS TO POWER PROGRAM
# =============================

def main():

    name = get_name()
    staff_member = print_summary(name)
    message = message_template(staff_member)
    generate_message(message, staff_member)

main()

