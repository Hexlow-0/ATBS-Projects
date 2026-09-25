

products_a = [
    {"sku": "P001", "name": "  widget  ", "category": "HARDWARE", "price": "$*25,00"},
    {"sku": "P002", "name": "GADGET", "category": "electronics", "price": "$49,99"},
    {"sku": "P003", "name": "Doohickey", "category": "HARDWARE", "price": "$*15,00"},
]

products_b = [
    {"sku": "P002", "name": "Gadget", "category": "Electronics", "price": "$49,99"},
    {"sku": "P004", "name": "  thingamajig  ", "category": "software", "price": "$*99,00"},
    {"sku": "P001", "name": "Widget", "category": "hardware", "price": "$25,00"},
]

merged = products_a + products_b

seen = set()
unique = []

for items in merged:

    sku = (items.get('sku') or "")

    name = (items.get('name') or "").strip().capitalize()

    category = (items.get('category') or "").capitalize()

    if not sku or not name or not category:
        sku = 'unknown'
        name = 'unknown'
        category = 'unknown'

    try:
        price = int((items.get('price') or "0").replace('$', '').replace('*', '').replace(',', ''))
    except (ValueError, TypeError):
        price = 0


    if sku in seen:
        continue

    seen.add(sku)

    cleaned = {'sku': sku,
                'name': name,
                'category': category,
                'price': price
                }

    unique.append(cleaned)

by_price = sorted(unique, key=lambda x: x['price'], reverse=True)
by_category = sorted(unique, key=lambda x: (x['category'], x['price']))

print("By price:\n")
for item in by_price:
    print(f"{item['sku']} | {item['name']} | ${item['category']} | ${item['price']}")

print()

print("By category:\n")
for item in by_category:
    print(f"{item['sku']} | {item['name']} | ${item['category']} | ${item['price']}")
