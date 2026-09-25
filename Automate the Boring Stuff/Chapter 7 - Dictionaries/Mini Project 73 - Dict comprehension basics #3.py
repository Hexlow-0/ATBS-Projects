
inventory = [
    {"sku": "A001", "item": "Laptop", "price": 999.0, "warehouse": "Sydney"},
    {"sku": "A002", "item": "Mouse", "price": 29.0, "warehouse": "Melbourne"},
    {"sku": "A003", "item": "Keyboard", "price": 79.0, "warehouse": "Sydney"},
    {"sku": "A004", "item": "Monitor", "price": 349.0, "warehouse": "Brisbane"},
    {"sku": "A005", "item": "Headset", "price": 149.0, "warehouse": "Melbourne"},
]

# task 1 - sku: item
sku_item = {inv['sku']: inv['item'] for inv in inventory}

print(sku_item)
print()

# task 2 - sku: price over $100
sku_price = {inv['sku']: inv['price'] for inv in inventory if inv['price'] > 100}

print(sku_price)
print()

# task 3 - item: price with 15% added
item_price_tax = {inv['item']: inv['price'] * 1.15 for inv in inventory}

print(item_price_tax)
print()

# task 4 - sku: expensive or affordable
expense_or_afford = {inv['sku']: 'expensive' if inv['price'] > 100 else 'affordable' for inv in inventory}

print(expense_or_afford)
print()

# task 5 - Flip it
flipped = {v: k for k, v in sku_item.items()}

print(flipped)
print()
