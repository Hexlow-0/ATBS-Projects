
employees = [
    {"name": "Alice", "department": "Engineering", "performance": "92", "tenure_years": "5"},
    {"name": "Bob", "department": "HR", "performance": "seventy", "tenure_years": "3"},
    {"name": "Carol", "department": "Engineering", "performance": "88", "tenure_years": None},
    {"name": "Dan", "department": "HR", "performance": "95", "tenure_years": "7"},
    {"name": "Eve", "department": "Engineering", "performance": None, "tenure_years": "2"},
]

cleaned = []


for emp in employees:

    name = emp.get('name')

    dept = emp.get('department')

    try:
        performance = int((emp.get('performance') or "0"))
    except (ValueError, TypeError):
        performance = 0

    try:
        tenure_years = int((emp.get('tenure_years') or '0'))
    except (ValueError, TypeError):
        tenure_years = 0

    cleaned.append({'name': name,
                    'dept': dept,
                    'performance': performance,
                    'tenure_years': tenure_years
                    })

by_performance = sorted(cleaned, key=lambda x: x['performance'], reverse=True)

print("Performance:\n")

for emp in by_performance:

    print(f"Name: {emp['name']} | Performance: {emp['performance']}")

print()


by_tenure = sorted(cleaned, key=lambda x: x['tenure_years'])

print("By tenure years:\n")

for emp in by_tenure:

    print(f"Name: {emp['name']} | Tenure years: {emp['tenure_years']}")

print()

by_dept_perf = sorted(cleaned, key=lambda x: (x['dept'], -x['performance']))

print("By department performance:\n")

for emp in by_dept_perf:

    print(f"Dept: {emp['dept']} | Performance: {emp['performance']}")

