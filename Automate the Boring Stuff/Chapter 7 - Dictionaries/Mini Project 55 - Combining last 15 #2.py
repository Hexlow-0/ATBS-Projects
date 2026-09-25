
warehouse_a = [
    {"id": "W001", "product": "  laptop  ", "category": "ELECTRONICS", "stock": "45", "price": "$*899,00", "supplier": {"name": "TechCorp", "location": {"city": "Sydney", "country": "AU"}}},
    {"id": "W002", "product": "KEYBOARD", "category": "electronics", "stock": "120", "price": "$*49,99", "supplier": {"name": "peripherals inc", "location": {"city": "Melbourne", "country": "AU"}}},
    {"id": "W003", "product": "Desk", "category": "FURNITURE", "stock": "twelve", "price": "$*250,00", "supplier": {"name": "OfficeCo", "location": None}},
]

warehouse_b = [
    {"id": "W002", "product": "Keyboard", "category": "Electronics", "price": "$49,99", "stock": "120", "supplier": {"name": "Peripherals Inc", "location": {"city": "Melbourne", "country": "AU"}}},
    {"id": "W004", "product": "  monitor  ", "category": "ELECTRONICS", "stock": "30", "price": "$*349,00", "supplier": {"name": "ScreenTech", "location": {"city": "Brisbane", "country": "AU"}}},
    {"id": "W005", "product": "Chair", "category": "furniture", "stock": "8", "price": "$*189,00", "supplier": None},
]

category_map = {
    'electronics': 'Electronics',
    'furniture': 'Furniture',
    'clothing': 'Clothing',
}

def merge_data(warehouse_a, warehouse_b):

    return warehouse_a + warehouse_b

def clean_product(product):

    ID = (product.get('id') or "")

    if not ID:

        return {'ok': False,
                'field': 'ID',
                'reason': 'missing ID',
                'record': product
                }

    prod = (product.get('product') or "").strip().capitalize()

    if not prod:

        return {'ok': False,
                'field': 'product',
                'reason': 'missing product',
                'record': product
                }

    category = (product.get('category') or "").lower()

    cat_map = (category_map.get(category) or "")

    if cat_map:
        category = cat_map
    else:
        category = 'uncategorised'


    try:
        stock = int((product.get('stock') or 0))
    except (ValueError, TypeError):
        stock = 0

    try:
        price = float((product.get('price') or '0').replace("$", "").replace("*", "").replace(",", "."))
    except (ValueError, TypeError):
        price = 0

    supplier = (product.get('supplier') or {})

    supplier_name = (supplier.get('name') or "")

    if not supplier_name:

        supplier_name = 'unknown'

    location = (supplier.get('location') or {})

    supplier_city = (location.get('city') or "")

    if not supplier_city:

        supplier_city = 'unknown'

    return {'ok': True,
            'data': {'id': ID,
                    'product': prod,
                    'category': category,
                    'stock': stock,
                    'price': price,
                    'supplier_name': supplier_name,
                    'supplier_city': supplier_city
                    }
                }
def deduplicinator_5000(processed):

    cleaned = []
    seen = set()

    for products in processed:

        key = products.get('id')

        if key in seen:
            continue

        seen.add(key)

        cleaned.append(products)

    return cleaned

def print_report(cleaned, errors):

    organised = sorted(cleaned, key=lambda x: x['price'], reverse=True)

    for product in organised:

        ID = product['id']
        prod = product['product']
        category = product['category']
        stock = product['stock']
        price = product['price']
        supplier_name = product['supplier_name']
        supplier_city = product['supplier_city']

        print(f"ID: {ID} | ${price}")
        print(f"Product: {prod} | Category: {category}")
        print(f"Stock: {stock}")
        print(f"Supplier: {supplier_name} | Location: {supplier_city}\n")

    print("Errors:\n")

    if len(errors) < 1:

        print("No errors")

    else:

        for i, error in enumerate(errors, start = 1):

            field = error['field']
            reason = error['reason']
            record = error['record']

            print(f"Error {i}:")
            print(f"Field: {field}")
            print(f"reason: {reason}")
            print(f"record: {record}\n")

def main():

    errors = []
    processed = []

    merged = merge_data(warehouse_a, warehouse_b)

    for product in merged:

        result = clean_product(product)

        if not result['ok']:
            errors.append(result)
            continue

        processed.append(result['data'])

    cleaned = deduplicinator_5000(processed)

    print_report(cleaned, errors)

main()
