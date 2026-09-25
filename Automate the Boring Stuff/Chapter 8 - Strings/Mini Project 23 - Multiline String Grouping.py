
orders = """ORD001,Alice,Widget,3
ORD002,Bob,Gadget,1
ORD003,Alice,Gizmo,2
ORD004,Charlie,Widget,5
ORD005,Alice,Widget,1
ORD006,Bob,Widget,2"""

grouped = {}

for o in orders.splitlines():

    order, customer, item, amount = o.split(',')

    grouped.setdefault(customer, {'amount': 0, 'items': []})

    grouped[customer]['amount'] += int(amount)

    if item not in grouped[customer]['items']:
        grouped[customer]['items'].append(item)

for customer, data in sorted(grouped.items()):

    amount = data['amount']
    items = data['items']

    print(f"{customer:<10}{amount} items   ({', '.join((items))})")
