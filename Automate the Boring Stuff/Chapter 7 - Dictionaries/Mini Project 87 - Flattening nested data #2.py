
employees = [
    {"id": "E001", "name": "Alice", "department": {"name": "Engineering", "floor": 3}, "contact": {"email": "alice@co.com", "phone": "0412345678"}},
    {"id": "E002", "name": "Bob", "department": {"name": "HR"}, "contact": None},
    {"id": "E003", "name": "Carol", "department": None, "contact": {"email": "carol@co.com"}},
    {"id": "E004", "name": None, "department": {"name": "Engineering", "floor": 2}, "contact": {"email": "dan@co.com", "phone": "0498765432"}},
]

def clean_int(value, default=0):

    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def clean_str(value, default='unknown'):

    if not value:
        return default
    else:
        return value.strip().title()

def flatten_data(emp):

    dept = (emp.get('department') or {})
    contact = (emp.get('contact') or {})

    return {
        'id': (emp.get('id') or ""),
        'name': clean_str(emp.get('name')),
        'dept_name': dept.get('name', 'unknown'),
        'floor': clean_int(dept.get('floor')),
        'email': contact.get('email', 'unknown'),
        'phone': contact.get('phone', 'unknown')
        }

flattened = [flatten_data(emp) for emp in employees]

for record in flattened:

    print(record)
