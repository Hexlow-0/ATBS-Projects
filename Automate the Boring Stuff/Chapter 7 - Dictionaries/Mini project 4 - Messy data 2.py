



products = [
    {"name": "Widget", "price": "9.99", "stock": 5, "category": "hardware"},
    {"name": "", "price": 4.49, "stock": "twelve", "category": "software"},
    {"name": "Gadget", "price": None, "stock": 3},
    {"name": "Doohickey", "price": "free", "stock": None, "category": "hardware"},
    {"name": "Thingamajig", "price": "14.99", "stock": "7", "category": ""},
]

for product in products:

    name = product.get('name', '')

    if not name:
        continue

    try:
        price = float(product.get('price', 0.0))
    except (ValueError, KeyError, TypeError):
        price = 0.0

    try:
        stock = int(product.get('stock', 0))
    except (ValueError, KeyError, TypeError):
        stock = 0

    category = product.get('category', '') or 'uncategorised'




    print(f"{name} | ${price} | Stock: {stock} | {category}")
