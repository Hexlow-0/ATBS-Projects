
rentals = [
    {"item": "  barbell  ", "condition": "GOOD", "rental_days": "3", "deposit": "$25"},
    {"item": "Dumbbells", "condition": "excellent", "rental_days": "seven", "deposit": "$*10"},
    {"item": "KETTLEBELL", "condition": "poor", "rental_days": "5", "deposit": "15"},
    {"item": "", "condition": "EXCELLENT", "rental_days": "2", "deposit": "$30"},
    {"item": "Treadmill", "condition": "BROKEN", "rental_days": None, "deposit": "$*50"},
]

for rent in rentals:

    item = rent.get('item', "").strip().capitalize()

    if not item:
        continue

    condition = rent.get('condition', 'unknown').lower()

    if condition not in ['good', 'excellent', 'poop']:
        condition = 'unknown'

    try:
        rental_days = int(rent.get('rental_days', 0))
    except (ValueError, TypeError):
        rental_days = 0

    try:
        deposit = int(rent.get('deposit', 0).replace("$", "").replace("*", ""))
    except (ValueError, TypeError):
        deposit = 0

    print(f"{item} | Condition: {condition} | Days: {rental_days} | deposit: ${deposit}")

