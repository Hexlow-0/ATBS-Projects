
employees = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Carol", "dept": "Engineering"},
    {"name": "Dan", "dept": "HR"},
    {"name": "Eve", "dept": "Engineering"},
]

grouped_by_dept = {}

for emp in employees:

    name = emp.get('name')
    dept = emp.get('dept')

    if dept not in grouped_by_dept:
        grouped_by_dept[dept] = []

    grouped_by_dept[dept].append(name)


print(grouped_by_dept)
