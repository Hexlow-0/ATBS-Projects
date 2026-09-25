

sales = """North,Jan,1000
South,Jan,1500
North,Feb,1200
South,Feb,1100
North,Mar,1400
South,Mar,1600"""


result = {}

for s in sales.splitlines():

    region, month, amount = s.split(',')

    amount = int(amount)

    if region not in result:
        result[region] = {'region_total': amount, 'best_month': month, 'best_amount': amount}
    else:
        if amount > result[region]["best_amount"]:
            result[region]['best_month'] = month
            result[region]['best_amount'] = amount

        result[region]['region_total'] += amount

for region, sale_data in result.items():

    regional_total = result[region]['region_total']
    best_month = result[region]['best_month']
    month_amount = result[region]['best_amount']

    print(f"{region:<8}${regional_total:<7,}(best: {best_month}, ${month_amount:,})")
