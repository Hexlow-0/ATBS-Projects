
employees = [
    {"name": "Alice", "department": {"name": "Engineering", "floor": 3}},
    {"name": "Bob", "department": None},
    {"name": "Carol"},
    {"name": "Dan", "department": {"name": "HR"}},
]

for employee in employees:
    name = employee.get('name', 'unknown')

    dept = employee.get('department') or {}

    dept_name = dept.get('name', 'unknown')
    floor = dept.get('floor', 'unknown')

    print(f"{name} | {dept_name} | {floor}")
