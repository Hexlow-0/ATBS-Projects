
staff = [
    {"id": "S001", "name": "  alice  ", "salary": "$*85,000"},
    {"id": "S002", "name": "BOB", "salary": "seventy thousand"},
    {"id": "S001", "name": "Alice", "salary": "$85,000"},
    {"id": "S003", "name": None, "salary": "$62,000"},
    {"id": "S002", "name": "Bob", "salary": "$70,000"},
]

seen = set()
unique = []

for sta in staff:

    ID = sta.get('id')

    name = (sta.get('name') or "").strip().capitalize()

    if not name: # intentional btw i wanted the record
        name = 'unknown'

    try:
        salary = int((sta.get('salary') or '0').replace("$", "").replace("*", "").replace(",", ""))
    except (ValueError, TypeError):
        salary = 0


    if ID in seen:
        continue

    seen.add(ID)
    unique.append({'ID': ID, 'name': name, 'salary': salary})

for item in unique:

    print(item)
