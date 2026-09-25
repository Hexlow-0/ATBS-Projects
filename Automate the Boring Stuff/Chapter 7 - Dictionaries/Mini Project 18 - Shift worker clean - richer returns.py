

shifts = [
    {"worker": "  dan  ", "role": "PICKER", "hours": "8", "pay_rate": "$*12,50"},
    {"worker": "Faye", "role": "packer", "hours": "six", "pay_rate": "$15"},
    {"worker": None, "role": "PICKER", "hours": "7", "pay_rate": "$*13,00"},
    {"worker": "  ", "role": "supervisor", "hours": "9", "pay_rate": "$*20,00"},
    {"worker": "Greg", "role": "CLEANER", "hours": None, "pay_rate": "$11"},
    {"worker": "Hana", "role": "packer", "hours": "8", "pay_rate": "free"},
]




def clean_record(work):

    worker = (work.get('worker') or "").strip().capitalize()

    if not worker:
        return {'ok': False, 'record': work, 'field': 'worker', 'reason': 'missing worker'}

    role = (work.get('role') or "").strip().lower()

    if role not in ['picker', 'packer', 'supervisor']:

        return {'ok': False, 'record': work, 'field': 'role', 'reason': 'invalid role'}

    try:
        hours = int((work.get('hours') or 0))
    except (ValueError, TypeError):
        hours = 0

    try:
        pay_rate = float((work.get('pay_rate') or "0").replace("$", "").replace("*", "").replace(",", "."))
    except (ValueError, TypeError):
        pay_rate = 0.0

    return {'ok': True,
            'data': {'worker': worker,
                    'role': role,
                    'hours': hours,
                    'pay_rate': pay_rate
                    }
                }

def print_results(cleaned, errors):

    for work in cleaned:

        name = work['worker']
        role = work['role']
        hours = work['hours']
        pay_rate = work['pay_rate']

        print(f"{name} | Role: {role} | {hours} hours | ${pay_rate}")

    print()

    for i, error in enumerate(errors, start=1):
        print(f"Error {i}: {error['field']} - {error['reason']}")
        print(f"Record: {error['record']}")

def main():

    errors = []
    cleaned = []

    for work in shifts:

        result = clean_record(work)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_results(cleaned, errors)

main()
