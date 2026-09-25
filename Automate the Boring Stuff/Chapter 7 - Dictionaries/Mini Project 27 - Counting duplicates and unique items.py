
orders = [
    {"order_id": "A001", "customer": "Alice", "item": "Widget"},
    {"order_id": "A002", "customer": "Bob", "item": "Gadget"},
    {"order_id": "A001", "customer": "Alice", "item": "Widget"},
    {"order_id": "A003", "customer": "Carol", "item": "Doohickey"},
    {"order_id": "A002", "customer": "Bob", "item": "Gadget"},
    {"order_id": "A004", "customer": "Alice", "item": "Widget"},
]

seen = set()

unique = 0
skipped = 0

for order in orders:

    or_id = order.get('order_id')

    if or_id in seen:
        skipped += 1
        continue
    else:
        unique += 1

    seen.add(or_id)

    print(f"{or_id} | {order.get('customer')} | {order.get('item')}")

print(f"Processed: {unique} unique orders, skilled: {skipped} duplicates.")


