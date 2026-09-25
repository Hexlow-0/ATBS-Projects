
products = [
    {"name": "Widget", "price": 25, "stock": 0},
    {"name": "Gadget", "price": 149, "stock": 12},
    {"name": "Doohickey", "price": 8, "stock": 3},
    {"name": "Thingamajig", "price": 299, "stock": 0},
    {"name": "Whatsit", "price": 55, "stock": 7},
]

discon = ['discontinued' if prod['stock'] < 1 else prod['name'] for prod in products]

print(discon)

discount = [0.5 * prod['price'] if prod['stock'] < 1 else prod['price']  for prod in products]

print(discount)

in_stock = ['in stock' if prod['stock'] > 1 else 'out of stock' for prod in products]

print(in_stock)
