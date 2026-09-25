
"""
# nested dict field — ALWAYS do this:
value = (record.get('key') or {}).get('inner_key', 'unknown')

# nested list field — ALWAYS do this:
items = (record.get('key') or [])
"""

orders = [
    {"id": "A001", "customer": {"name": "Alice", "city": "Tokyo"}, "items": ["Widget", "Gadget"]},
    {"id": "A002", "customer": {"name": "Bob"}, "items": []},
    {"id": "A003", "customer": None, "items": ["Doohickey"]},
    {"id": "A004", "items": ["Widget"]},
]


for order in (orders):

    ID = order.get('id')

    name = (order.get('customer') or {}).get('name', 'unknown customer')

    if name == 'unknown customer':
        print(f"{ID} | unknown customer")
        continue

    city = (order.get('customer') or {}).get('city', 'unknown')

    items = (order.get('items') or [])

    items_display = items if items else 'no items'

    print(f"{ID} | {name} | {city} | {items_display}")
