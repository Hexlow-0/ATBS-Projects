
applicants = [
    {"name": "Alice", "role": "pick"},
    {"name": "Bob", "role": "PACKER"},
    {"name": "Clara", "role": "sup"},
    {"name": "Dan", "role": "supervisor"},
    {"name": "Eve", "role": "janitor"},
]

role_map = {
    'picker': 'picker',
    'pick': 'picker',
    'packer': 'packer',
    'pack': 'packer',
    'supervisor': 'supervisor',
    'sup': 'supervisor',
}

for applicant in applicants:

    app_role = applicant.get('role').lower()
    name = applicant.get('name')

    lookup_role = role_map.get(app_role, 'unknown')

    print(f"{name} → {lookup_role}")


