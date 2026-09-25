
customers = [
    {"name": "Alice", "email": "alice@email.com", "plan": "gold"},
    {"name": "Bob", "email": "bob@email.com", "plan": "silver"},
    {"name": "Alice", "email": "alice2@email.com", "plan": "bronze"},
    {"name": "Carol", "email": "carol@email.com", "plan": "gold"},
    {"name": "Bob", "email": "bob@email.com", "plan": "silver"},
]

seen = set()

for customer in customers:

    name = customer.get('name')
    email = customer.get('email')
    plan = customer.get('plan')

    if name in seen:

        continue

    seen.add(name)

    print(f"{name} | {email} | {plan}")

