
employees = [
    {"name": "alice", "department": {"name": "ENGINEERING", "budget": {"annual": "$*120,000", "currency": "USD"}}},
    {"name": "BOB", "department": {"name": "hr", "budget": None}},
    {"name": None, "department": {"name": "Finance", "budget": {"annual": "$95,000", "currency": "GBP"}}},
    {"name": "Diana", "department": None},
    {"name": "  eve  ", "department": {"name": "ENGINEERING", "budget": {"annual": "eighty thousand", "currency": "USD"}}},
]

def clean_employee(emp):

    name = (emp.get('name') or "").strip().title()

    if not name:

        return {'ok': False,
                'field': 'name',
                'reason': 'missing name',
                'record': emp
                }

    dept = (emp.get('department') or {})

    dept_name = (dept.get('name') or 'unknown').capitalize()

    budget = (dept.get('budget') or {})

    try:
        annual = int((budget.get('annual', 0) or "0").replace("$", "").replace("*", "").replace(",", ""))
    except (ValueError, TypeError):
        annual = 0

    currency = budget.get('currency', 'unknown')

    return {'ok': True,
            'data': {'name': name,
                    'dept_name': dept_name,
                    'annual': annual,
                    'currency': currency
                    }
                }

def print_employees(cleaned, errors):

    print("Valid records:\n")

    for emp in cleaned:

        name = emp['name']
        dept_name = emp['dept_name']
        annual = emp['annual']
        currency = emp['currency']

        print(f"{name} | {dept_name} | ${annual:,} | {currency}")

    print()

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        field = error['field']
        reason = error['reason']
        record = error['record']

        print(f"Error: {i}:")
        print(f"Field: {field}")
        print(f"reason: {reason}")
        print(f"record: {record}\n")

def main():

    errors = []
    cleaned = []

    for emp in employees:

        result = clean_employee(emp)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_employees(cleaned, errors)

main()
