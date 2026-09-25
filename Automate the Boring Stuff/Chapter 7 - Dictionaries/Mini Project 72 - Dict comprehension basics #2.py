
products = [
    {"name": "Widget", "price": 25.0, "stock": 15, "category": "hardware"},
    {"name": "Gadget", "price": 149.0, "stock": 0, "category": "electronics"},
    {"name": "Doohickey", "price": 8.0, "stock": 3, "category": "hardware"},
    {"name": "Thingamajig", "price": 299.0, "stock": 0, "category": "electronics"},
    {"name": "Whatsit", "price": 55.0, "stock": 7, "category": "hardware"},
]

# Task 1 - name: price
name_price = {prod['name']: prod['price'] for prod in products}
print(name_price)
print()

# Task 2 - name: stock if out of stock
name_stock = {prod['name']: prod['stock'] for prod in products if prod['stock'] == 0}

print(name_stock)
print()

# Task 3 - name: price but 20% discount
name_price_discount = {prod['name']: prod['price'] * 0.80 for prod in products}

print(name_price_discount)
print()

# Task 4 - name: available or unavailable
available_or_unavailable = {prod['name']: 'available' if prod['stock'] > 0 else 'unavailable' for prod in products}

print(available_or_unavailable)
print()

# Task 5 - category: list of names
list_of_names = {prod['category']: [prod['name']] for prod in products}

print(list_of_names)
print()
