

volunteers = [
    {"name": "  sarah  ", "role": "DRIVER", "hours_available": "6", "contact": "sarah@email.com"},
    {"name": "TOM", "role": "coordinator", "hours_available": "three", "contact": "tom@email.com"},
    {"name": None, "role": "DRIVER", "hours_available": "4", "contact": "anon@email.com"},
    {"name": "  ", "role": "helper", "hours_available": None, "contact": "mei@email.com"},
    {"name": "Priya", "role": "CHEF", "hours_available": "5", "contact": "priya@email.com"},
    {"name": "Carl", "role": "driver", "hours_available": "8", "contact": "carl@email.com"},
]

def clean_volunteers(vol):

    name = (vol.get('name') or "").strip().capitalize()

    if not name:

        return {'ok': False,
                'record': vol,
                'field': 'name',
                'reason': 'missing name'
                }

    role = (vol.get('role') or "").strip().lower()

    if role not in ['driver', 'coordinator', 'helper']:

        return {'ok': False,
                'record': vol,
                'field': 'role',
                'reason': 'invalid role'
                }

    try:
        hours = int((vol.get('hours_available') or 0))
    except (ValueError, TypeError):
        hours = 0

    contact = (vol.get('contact') or "")

    return {'ok': True,
            'data': {'name': name,
                    'role': role,
                    'hours': hours,
                    'contact': contact
                    }
                }

def print_cleaned(cleaned, errors):

    print("Valid records:\n")

    for vol in cleaned:

        name = vol['name']
        role = vol['role']
        hours = vol['hours']
        contact = vol['contact']

        print(f"{name} | {role} | {hours} | {contact}")

    print()

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        print(f"Error {i}:")
        print(f"record {error['record']}")
        print(f"field {error['field']}")
        print(f"reason {error['reason']}\n")

def main():

    errors = []
    cleaned = []

    for vol in volunteers:

        result = clean_volunteers(vol)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_cleaned(cleaned, errors)

main()
