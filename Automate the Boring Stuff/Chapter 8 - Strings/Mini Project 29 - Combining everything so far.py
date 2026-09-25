
data = """product:Widget|price:9.99|qty:5
product:Gadget|price:invalid|qty:3
product:Gizmo|qty:2
product:Thing|price:4.50|qty:abc"""

from collections import defaultdict

output = defaultdict(dict)

for d in data.splitlines():

    result = {}

    for field in d.split('|'):
        try:
            key, value = field.split(':')
        except ValueError:
            continue

        result[key] = value

    product = (result.get('product', 'N/A') or "")

    try:
        qty = int(result.get('qty', 'N/A') or "")
    except ValueError:
        qty = 'N/A'

    try:
        price = float(result.get('price') or "")
    except ValueError:
        price = 'N/A'

    if price == 'N/A' or qty == 'N/A':
        total_value = 'N/A'
    else:
        total_value = qty * price

    output[product] = total_value

for product, value in output.items():

    print(f"{product:<8}${value}")
