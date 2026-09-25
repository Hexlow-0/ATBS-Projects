staff = [
    {"first_name": "Alice", "last_name": "Smith", "age": "31", "department": "Engineering"},
    {"first_name": "Bob2", "last_name": "Jones", "age": "twenty", "department": "Marketing"},
    {"first_name": "", "last_name": "Brown", "age": "25", "department": "HR"},
    {"first_name": "Diana", "last_name": "Pr!nce", "age": "28", "department": "Legal"},
    {"first_name": "Eve", "last_name": "Taylor", "age": "19", "department": "Engineering"},
]

for person in staff:
    first_name = person["first_name"]
    last_name = person["last_name"]
    age = person["age"]

    # Validate first_name
    if not first_name:
        reason = "first_name is empty"

    elif not first_name.isalpha():
        reason = "first_name must contain letters only"

    # Validate last_name
    elif not last_name:
        reason = "last_name is empty"

    elif not last_name.isalpha():
        reason = "last_name must contain letters only"

    # Validate age
    elif not age.isdigit():
        reason = "age must contain digits only"

    else:
        username = f"{first_name.lower()}.{last_name.lower()}"
        print(f"Account created: {username}")
        continue

    print(f"Account failed: {first_name} {last_name} — {reason}")
