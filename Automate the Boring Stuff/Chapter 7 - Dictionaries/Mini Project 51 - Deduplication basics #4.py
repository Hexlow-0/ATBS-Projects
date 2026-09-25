
team_a = [
    {"id": "T001", "name": "  alice  ", "role": "ENGINEER", "salary": "$*90,000"},
    {"id": "T002", "name": "BOB", "role": "designer", "salary": "$75,000"},
    {"id": "T003", "name": "Carol", "role": "MANAGER", "salary": "$*110,000"},
]

team_b = [
    {"id": "T002", "name": "Bob", "role": "Designer", "salary": "$75,000"},
    {"id": "T004", "name": "  diana  ", "role": "engineer", "salary": "$*85,000"},
    {"id": "T001", "name": "Alice", "role": "engineer", "salary": "$90,000"},
]

merged = team_a + team_b

seen = set()
unique = []

for team in merged:

    ID = team.get('id')

    name = (team.get('name') or "").strip().capitalize()

    if not name:
        name = 'unknown'

    role = (team.get('role') or "").capitalize()

    try:
        salary = int((team.get('salary') or "0").replace('$', '').replace('*', '').replace(',', ''))
    except (ValueError, TypeError):
        salary = 0

    if ID in seen:
        continue

    seen.add(ID)
    unique.append({'id': ID, 'name': name, 'role': role, 'salary': salary})

for item in unique:

    print(item)
