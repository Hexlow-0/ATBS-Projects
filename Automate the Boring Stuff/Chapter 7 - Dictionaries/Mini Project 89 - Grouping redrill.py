
orders = [
    {"id": "O001", "customer": "Alice", "product": "Widget", "amount": 25},
    {"id": "O002", "customer": "Bob", "product": "Gadget", "amount": 149},
    {"id": "O003", "customer": "Alice", "product": "Doohickey", "amount": 8},
    {"id": "O004", "customer": "Carol", "product": "Widget", "amount": 25},
    {"id": "O005", "customer": "Alice", "product": "Gadget", "amount": 149},
]

grouped = {}

for order in orders:

    key = order.get('customer')
    ID = order.get('id')
    product = order.get('product')
    amount = order.get('amount')

    if key not in grouped:
        grouped[key] = []

    grouped[key].append({'id': ID, 'product': product, 'amount': amount})

print(grouped)
