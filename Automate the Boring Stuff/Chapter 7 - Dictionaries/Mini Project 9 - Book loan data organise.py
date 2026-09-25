
from collections import defaultdict

applications = [
    {"name": "  alice  ", "role": "ENGINEER", "experience_years": "5", "salary_expectation": "$85,000"},
    {"name": "Bob", "role": "designer", "experience_years": "three", "salary_expectation": "$*72,000"},
    {"name": "  ", "role": "MANAGER", "experience_years": "8", "salary_expectation": "$95,000"},
    {"name": "DIANA", "role": "CHEF", "experience_years": None, "salary_expectation": "$60,000"},
    {"name": "Eve", "role": "engineer", "experience_years": "3", "salary_expectation": "$*78,000"},
]

def clean_data(app):


    name = app.get('name', "").strip().capitalize()

    if not name:
        return None

    role = app.get('role', 'unknown').lower()

    if role not in ['engineer', 'designer', 'manager']:
        role = 'unknown'

    try:
        experience = int(app.get('experience_years', 0))
    except (ValueError, TypeError):
        experience = 0

    try:
        salary = int(app.get('salary_expectation', 0).replace(",", "").replace("$", "").replace("*", ""))
    except (ValueError, TypeError):
        salary = 0

    clean_data = {
                'name': name,
                'role': role,
                'experience': experience,
                'salary': salary
                }

    return clean_data





def main(applications):

    for app in applications:

        result = clean_data(app)

        if result is None:

            continue

        print(result)

main(applications)
