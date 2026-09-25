
shopping = """Bread,3.50
Milk,2.20
Eggs,4.00
Bread,3.50
Cheese,6.50
Milk,2.20"""

from collections import defaultdict

result = defaultdict(dict)

for s in shopping.splitlines():

    item, price = s.split(',')

    price = float(price)

    if item not in result:
        result[item] = price
    else:
        result[item] += price

for item, price in sorted(result.items()):

    print(f"{item:<8}${price:.2f}")
