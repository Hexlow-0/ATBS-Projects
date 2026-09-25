
records = [
    {"name": "Alice", "age": "28", "email": "alice@email.com", "score": "88", "ssn": "123-45-6789"},
    {"name": "BOB", "age": "thirty", "email": "bob@email.com", "score": "72"},
    {"name": None, "age": "31", "email": "carol@email.com", "score": "95", "internal_id": "X991", "debug": "test"},
    {"name": "Dan", "age": "25", "score": "61", "role": "admin", "access_level": "5"},
    {"name": "  eve  ", "age": "22", "email": "eve@email.com", "score": "88"},
]

expected_keys = {'name', 'age', 'email', 'score'}

def clean_record(rec):

    actual_keys = set(rec.keys())
    extra = actual_keys - expected_keys

    name = (rec.get('name') or "").strip().title() # title better maybe?

    if not name:

        return {'ok': False,
                'field': 'name',
                'reason': 'missing name',
                'record': rec
                }

    try:
        age = int((rec.get('age') or 0))
    except (ValueError, TypeError):
        age = 0

    email = (rec.get('email') or "")

    if not email:

        email = 'unknown'

    try:
        score = int((rec.get('score') or 0))
    except (ValueError, TypeError):
        score = 0

    return {'ok': True,
            'data': {'name': name,
                    'age': age,
                    'email': email,
                    'score': score,
                    'extra_keys': extra
                    }
                }

def sort_data(processed):

    cleaned = sorted(processed, key=lambda x: x['score'], reverse=True)

    return cleaned

def print_records(cleaned, errors):

    print("Valid records:\n")

    for rec in cleaned:

        name = rec['name']
        age = rec['age']
        email = rec['email']
        score = rec['score']
        extra_keys = rec['extra_keys']

        print(f"{name} | {age} | {email} | {score}")

        if rec['extra_keys']:
            print(f"⚠️ unexpected fields: {rec['extra_keys']}")

    print()

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        field = error['field']
        record = error['record']
        reason = error['reason']

        print(f"Error {i}:")
        print(f"Field: {field}")
        print(f"record: {record}")
        print(f"reason: {reason}\n")

def main():

    errors = []
    processed = []

    for rec in records:

        result = clean_record(rec)

        if not result['ok']:
            errors.append(result)
            continue

        processed.append(result['data'])

    cleaned = sort_data(processed)

    print_records(cleaned, errors)

main()
