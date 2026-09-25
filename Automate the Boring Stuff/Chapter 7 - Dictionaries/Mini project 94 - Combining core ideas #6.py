
from collections import defaultdict

sales = [
    {"product": "Laptop", "category": "Electronics", "qty": 3, "price": 1200},
    {"product": "laptop", "category": "electronics", "qty": None, "price": 1200},
    {"product": "Mouse", "category": "Accessories", "qty": 5, "price": 40},
    {"product": "MOUSE", "category": "accessories", "qty": 2, "price": None},
    {"product": "Monitor", "category": "Electronics", "qty": 1, "price": 350},
    {"product": "monitor", "category": "Electronics", "qty": 4, "price": 350},
    {"product": "Keyboard", "category": "Accessories", "qty": "", "price": 85},
    {"product": "Keyboard", "category": "Accessories", "qty": 3, "price": 85},
    {"product": "Phone", "category": "Electronics", "qty": 2, "price": 900},
    {"product": "phone", "category": "electronics", "qty": 1, "price": 900},
]

def safe_int(value, default=None):
    try:
        return int(value)
    except (ValueError, TypeError, KeyError):
        return default

def clean_sales(sale):

    product = (sale.get('product') or "").strip().capitalize()

    category = (sale.get('category') or "").strip().capitalize()

    qty = safe_int(sale.get('qty'))

    if qty is None:

        return {'ok': False,
                'field': 'quantity',
                'reason': 'missing quantity or None value',
                'record': sale
                }

    price = safe_int(sale.get('price'))

    if not price:

        return {'ok': False,
                'field': 'price',
                'reason': 'missing price or None value',
                'record': sale
                }

    return {'ok': True,
            'data': {'product': product,
                    'category': category,
                    'qty': qty,
                    'price': price
                    }
                }


def calculate_category_revenue(processed):

    category_revenue = defaultdict(int)

    for (product, category), data in processed.items():
        revenue = data['qty'] * data['price']
        category_revenue[category] += revenue

    return category_revenue

def calculate_units_sold_per_product(processed):

    sold_per_product = defaultdict(int)

    for (product, category), data in processed.items():
        sold_per_product[product] += data['qty']

    return sold_per_product

def print_summary(processed, category_rev, units_sold, errors):

    print("=" * 40)
    print("SUMMARY".center(40))
    print("=" * 40)
    print()

    print("DATA".center(40, '='))
    print()

    for (product, category), data in processed.items():
        price = data['price']
        qty = data['qty']

        print(f"{product} | Cat: {category} | Qty: {qty} | ${price:,}")

    print()

    print("CATEGORY REVENUE".center(40, '='))
    print()

    for category, revenue in category_rev.items():
        print(f"{category} - Revenue: ${revenue:,}")

    top_category, rev = max(category_rev.items(), key=lambda x: x[1])

    print()
    print(f"Top category: {top_category} with ${rev:,}")

    print()
    print("UNITS SOLDS".center(40, '='))
    print()

    for product, sold in units_sold.items():
        print(f"{product} \tx {sold} sold")


    top_product, units = max(units_sold.items(), key=lambda x: x[1])

    print()
    print(f"Top product: {top_product} with x{units} sold")
    print()
    print("ERRORS".center(40, '='))
    print()

    if len(errors) < 1:

        print("No errors :)")

    else:

        for i, error in enumerate(errors, start=1):

            print(f"Error {i}:")
            print(f"Field: {error['field']}")
            print(f"Reason: {error['reason']}")
            print(f"Record: {error['record']}\n")


    print("PROGRAM END".center(40, '='))
    print()

def main():

    errors = []
    processed = {}

    for sale in sales:

        result = clean_sales(sale)

        if not result['ok']:
            errors.append(result)
            continue

        data = result['data']
        key = (data['product'], data['category'])

        if key not in processed:
            processed[key] = {'qty': 0, 'price': data['price']}

        processed[key]['qty'] += data['qty']


    category_rev = calculate_category_revenue(processed)

    units_sold = calculate_units_sold_per_product(processed)

    print_summary(processed, category_rev, units_sold, errors)

main()
