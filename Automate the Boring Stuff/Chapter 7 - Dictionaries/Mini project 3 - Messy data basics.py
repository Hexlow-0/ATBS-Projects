


patients = [
    {"name": "Alice", "condition": "Hypertension", "cost": 1200},
    {"name": "Bob", "cost": 800},
    {"condition": "Migraine", "cost": 900},
    {"name": "Diana", "condition": "Heart Disease"},
    {"name": None, "condition": "Epilepsy", "cost": 750},
    {"name": "Frank", "condition": "", "cost": 1100},
    {"name": "Grace", "condition": "Arrhythmia", "cost": 1500}
]

valid_records = 0
total_cost = 0

for patient in patients:

    name = patient.get('name', "unknown")
    condition = patient.get("condition", "Unknown")

    try:
        cost = int(patient.get("cost", 0))
    except (ValueError, TypeError):
        cost = 0


    if not patient.get("name"):
        continue

    if not patient.get("condition"):
        condition = "unknown"


    print(f"{name} - {condition} - ${cost:,}")

    valid_records += 1
    total_cost += cost

print()

print(f"Valid records: {valid_records}")
print(f"Total clost: ${total_cost:,}")


