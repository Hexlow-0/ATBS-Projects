
staff = [
    ("Alice Smith", "Engineering", "Sydney"),
    ("Bob Jones", "Marketing", "Melbourne"),
    ("Charlie Brown", "HR", "Brisbane"),
    ("Diana Prince", "Engineering", "Sydney"),
    ("Ed Norton", "Marketing", "Perth"),
]

col1, col2, col3 = 20, 17, 12

print("Name".ljust(col1) + "Department".ljust(col2) + "City".ljust(col3))
print(("-" * 4).ljust(col1) + '----------'.ljust(col2) + '----'.ljust(col3))

for name, dept, city in staff:

    print(f"{name}".ljust(col1) + f"{dept}".ljust(col2) + f"{city}".ljust(col3))




