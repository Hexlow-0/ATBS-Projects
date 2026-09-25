
inventory = """Widget,150,2.50
Gadget,75,8.00
Gizmo,200,1.25
Widget,50,2.50
Gizmo,30,1.25"""

grouped = {}

for line in inventory.splitlines():

    item, qty, price = line.split(',')

    qty = int(qty)
    price = float(price)

    if item not in grouped:
        grouped[item] = [qty, price]
    else:
        grouped[item][0] += qty


for item, data in sorted(grouped.items()):

    qty = data[0]
    price = data[1]
    rev = price * qty

    print(f"{item:<10}{qty:<10}${rev:.2f}")
