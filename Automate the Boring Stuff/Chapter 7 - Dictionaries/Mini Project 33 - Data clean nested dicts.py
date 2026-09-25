
users = [
    {"name": "Alice", "age": "28", "address": {"city": "Tokyo", "postcode": "100-0001"}, "contact": {"email": "alice@email.com", "phone": "080-1234-5678"}},
    {"name": "Bob", "age": "thirty", "address": {"city": "Osaka"}, "contact": {"email": "bob@email.com"}},
    {"name": None, "age": "31", "address": {"city": "Kyoto", "postcode": "600-0001"}, "contact": {"email": "carol@email.com"}},
    {"name": "Diana", "age": "25", "contact": {"email": "diana@email.com", "phone": "090-8765-4321"}},
    {"name": "Eve", "age": "22", "address": None, "contact": None},
]

def clean_user(user):

    name = (user.get('name') or "").capitalize()

    if not name:

        return {'ok': False,
                'field': 'name',
                'reason': 'missing name',
                'record': user
                }

    try:
        age = int((user.get('age') or 0))
    except (ValueError, TypeError):
        age = 0

    city = (user.get('address') or {}).get('city', 'unknown')
    postcode = (user.get('address') or {}).get('postcode', 'unknown')
    email = (user.get('contact') or {}).get('email', 'unknown')
    phone = (user.get('contact') or {}).get('phone', 'unknown')

    return {'ok': True,
            'data': {'user': name,
                    'age': age,
                    'city': city,
                    'postcode': postcode,
                    'email': email,
                    'phone': phone
                    }
                }

def print_users(cleaned, errors):

    print("Valid records:\n")

    for user in cleaned:

        name = user['user']
        age = user['age']
        city = user['city']
        postcode = user['postcode']
        email = user['email']
        phone = user['phone']


        print(f"{name} | Age: {age} | City: {city} | PC: {postcode} | Email: {email} | Ph: {phone}")

    print()

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        field = error['field']
        reason = error['reason']
        record = error['record']

        print(f"Error {i}:")
        print(f"Field: {field}")
        print(f"Reason: {reason}")
        print(f"Record: {record}\n")

def main():

    errors = []
    cleaned = []

    for user in users:

        result = clean_user(user)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_users(cleaned, errors)


main()
