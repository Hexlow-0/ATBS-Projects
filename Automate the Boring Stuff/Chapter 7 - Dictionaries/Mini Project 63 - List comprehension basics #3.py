
products = [
    {"name": "Widget", "price": 25, "stock": 0, "category": "hardware"},
    {"name": "Gadget", "price": 149, "stock": 12, "category": "electronics"},
    {"name": "Doohickey", "price": 8, "stock": 3, "category": "hardware"},
    {"name": "Thingamajig", "price": 299, "stock": 0, "category": "electronics"},
    {"name": "Whatsit", "price": 55, "stock": 7, "category": "hardware"},
]


names = [item['name'] for item in products]

print(names)

in_stock = [item['name'] for item in products if item['stock'] > 0]

print(in_stock)

price_double = [item['price'] * 2 for item in products]

print(price_double)

eletric_products = [item for item in products if item['category'] == 'electronics']

print(eletric_products)
