
employees = [
    {"id": "E001", "name": "Alice", "dept": "Engineering"},
    {"id": "E002", "name": "Bob", "dept": "HR"},
    {"id": "E001", "name": "Alice", "dept": "Engineering"},
    {"id": "E003", "name": "Carol", "dept": "Engineering"},
    {"id": "E002", "name": "Bob", "dept": "HR"},
]


unique = []
seen = set()

for emp in employees:

    ID = emp.get('id')


    if ID in seen:
        continue

    seen.add(ID)
    unique.append(emp)

for items in unique:

    print(items)
