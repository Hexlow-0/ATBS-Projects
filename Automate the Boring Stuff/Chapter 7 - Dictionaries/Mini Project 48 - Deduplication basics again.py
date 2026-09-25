
orders_1 = [
    {"order_id": "A001", "customer": "Alice", "item": "Widget"},
    {"order_id": "A002", "customer": "Bob", "item": "Gadget"},
    {"order_id": "A003", "customer": "Carol", "item": "Widget"},
]

orders_2 = [
    {"order_id": "A002", "customer": "Bob", "item": "Gadget"},
    {"order_id": "A004", "customer": "Diana", "item": "Doohickey"},
    {"order_id": "A001", "customer": "Alice", "item": "Widget"},
]

merged = orders_1 + orders_2

unique = []

for item in merged:

    if item in unique:
        continue

    unique.append(item)

for items in unique:

    print(items)
