
products = [
    {"name": "Widget", "price": "29.99", "stock": "15"},
    {"name": "Gadget", "price": "bad", "stock": "twelve"},
    {"name": "Doohickey", "price": "8.50", "stock": None},
    {"name": "Thingamajig", "price": None, "stock": "7"},
]

def safe_float(value, default=-1):

    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def safe_int(value, default=0):

    try:
        return int(value)
    except (ValueError, TypeError):
        return default

name_price = {prod['name']: safe_float(prod['price']) for prod in products}

stock = [safe_int(prod['stock']) for prod in products]

print(name_price)
print(stock)
