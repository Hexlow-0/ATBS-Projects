
signups = [
    {"name": "Jack", "age": 28, "has_waiver": True, "membership_type": "Monthly"},
    {"name": "Jill", "age": "seventeen", "has_waiver": True, "membership_type": "Annual"},
    {"name": "  ", "age": 34, "has_waiver": True, "membership_type": "Monthly"},
    {"name": "Bob", "age": 15, "has_waiver": False, "membership_type": "Monthly"},
    {"name": "Alice", "age": 42, "has_waiver": True, "membership_type": "Lifetime"}
]

def clean_data(sign):

    name = (sign.get('name') or "").strip()

    if not name:

        return {'ok': False,
                'record': sign,
                'field': 'name',
                'reason': 'Empty field/missing name'
                }

    try:
        age = int(sign.get('age', 0) or "0")
    except (ValueError, TypeError):
        age = 0

    if age < 16:
        return {'ok': False,
                'record': sign,
                'field': 'age',
                'reason': 'Invalid or under 16 y/o'
                }

    waiver = sign.get('has_waiver')

    if waiver is not True:

        return {'ok': False,
                'record': sign,
                'field': 'waiver',
                'reason': 'Waiver set to False, failed to validate'
                }

    membership = sign.get('membership_type').capitalize()

    if membership not in ['Monthly', 'Annual']:

        return {'ok': False,
                'record': sign,
                'field': 'membership',
                'reason': "membership not 'monthly' or 'annual'"
                }

    return {'ok': True,
            'data': {'name': name,
                    'age': age,
                    'waiver': waiver,
                    'membership': membership
                    }
                }

def print_data(cleaned, errors):

    for data in cleaned:

        name = data['name']
        age = data['age']
        waiver = data['waiver']
        membership = data['membership']

        print(f"{name} | Age: {age} | Waiver: {waiver} | Mem_type: {membership}")

    print()

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        status = error['ok']
        record = error['record']
        reason = error['reason']
        field = error['field']

        print(f"Error {i}:")
        print(f"Status: {status}")
        print(f"Record: {record}")
        print(f"Field: {field}")
        print(f"Reason: {reason}\n")


def main():

    errors = []
    cleaned = []

    for sign in signups:

        result = clean_data(sign)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_data(cleaned, errors)

main()






