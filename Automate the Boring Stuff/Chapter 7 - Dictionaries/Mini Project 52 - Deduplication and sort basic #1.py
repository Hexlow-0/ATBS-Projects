
sales_1 = [
    {"id": "S001", "rep": "  alice  ", "region": "NORTH", "amount": "$*15,000"},
    {"id": "S002", "rep": "BOB", "region": "south", "amount": "$12,500"},
    {"id": "S003", "rep": "Carol", "region": "EAST", "amount": "$*18,000"},
]

sales_2 = [
    {"id": "S002", "rep": "Bob", "region": "South", "amount": "$12,500"},
    {"id": "S004", "rep": "  diana  ", "region": "WEST", "amount": "$*9,000"},
    {"id": "S001", "rep": "Alice", "region": "north", "amount": "$15,000"},
]

region_targets = {
    'north': 14000,
    'south': 11000,
    'east': 17000,
    'west': 8000,
}

merged = sales_1 + sales_2

seen = set()
unique = []

for sales in merged:

    ID = (sales.get('id') or "")

    rep = (sales.get('rep') or "").strip().capitalize()

    if not rep:
        rep = 'unknown'

    region = (sales.get('region') or "").lower()

    region_target = (region_targets.get(region) or "")

    try:
        amount = int((sales.get('amount') or "0").replace('$', '').replace(',', '').replace('*', ''))
    except (ValueError, TypeError):
        amount = 0

    if ID in seen:
        continue

    seen.add(ID)
    unique.append({'id': ID, 'rep': rep, 'region': region, 'region_target': region_target, 'amount': amount})



by_amount = sorted(unique, key=lambda x: x['amount'], reverse=True)
by_region = sorted(unique, key=lambda x: x['region'])

print("By amount:\n")
for item in by_amount:
    print(f"{item['rep']} | {item['region']} | ${item['amount']} | target: ${item['region_target']}")

print()
print("By region:\n")
for item in by_region:
    print(f"{item['rep']} | {item['region']} | ${item['amount']} | target: ${item['region_target']}")


