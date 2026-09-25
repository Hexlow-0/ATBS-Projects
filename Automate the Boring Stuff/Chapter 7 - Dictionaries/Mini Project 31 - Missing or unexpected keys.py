records = [
    {"name": "Alice", "age": 28, "email": "alice@email.com", "ssn": "123-45-6789", "internal_id": "X991"},
    {"name": "Bob", "email": "bob@email.com", "internal_id": "X992"},
    {"name": "Carol", "age": 31, "email": "carol@email.com", "ssn": "987-65-4321"},
    {"name": "Dan", "age": 25, "email": "dan@email.com", "role": "admin", "access_level": "5"},
    {"name": "Eve", "age": 22},
]

expected = {"name", "age", "email"}
cleaned_records = []

for record in records:
    actual = set(record)

    extra = actual - expected
    missing = expected - actual

    cleaned = {k: v for k, v in record.items() if k in expected}
    cleaned_records.append(cleaned)

    print(f"Cleaned: {cleaned}")
    print(f"Extra: {extra}")
    print(f"Missing: {missing}")
    print("-" * 40)

print("\nAll cleaned records:")
print(cleaned_records)
