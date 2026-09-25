
inventory_a = [
    {"id": "I001", "item": "  sword  ", "type": "WEAPON", "weight": "3.5", "value": "$*150"},
    {"id": "I002", "item": "SHIELD", "type": "armor", "weight": "5.2", "value": "$*80"},
    {"id": "I003", "item": "Potion", "type": "CONSUMABLE", "weight": "0.5", "value": "$25"},
]

inventory_b = [
    {"id": "I002", "item": "Shield", "type": "Armor", "weight": "5.2", "value": "$80"},
    {"id": "I004", "item": "  bow  ", "type": "WEAPON", "weight": "2.1", "value": "$*120"},
    {"id": "I001", "item": "Sword", "type": "weapon", "weight": "3.5", "value": "$150"},
]

merged = inventory_a + inventory_b

seen = set()
unique = []

for items in merged:

    ID = (items.get('id') or "")

    item = (items.get('item') or "").strip().capitalize()

    equipped = (items.get('type') or "").strip().capitalize()

    try:
        weight = float((items.get('weight') or '0'))
    except (ValueError, TypeError):
        weight = 0

    try:
        value = float((items.get('value') or '0').replace("$", "").replace("*", ""))
    except (ValueError, TypeError):
        value = 0

    if ID in seen:
        continue

    seen.add(ID)

    cleaned = {'id': ID,
                'item': item,
                'type': equipped,
                'weight': weight,
                'value': value
                }

    unique.append(cleaned)

# ==========================================
# VALUE DESCENDING
# ==========================================

value_decend = sorted(unique, key=lambda x: x['value'], reverse=True)

print()


print("By Value:\n")
for item in value_decend:
    print(f"{item['id']} | {item['item']} | Type: {item['type']} | {item['weight']} | ${item['value']}")

# ==========================================
# WEIGHT ASCENDING
# ==========================================

weight_decend = sorted(unique, key=lambda x: x['weight'])

print()

print("By Weight:\n")
for item in weight_decend:
    print(f"{item['id']} | {item['item']} | Type: {item['type']} | {item['weight']} | ${item['value']}")

# ==========================================
# TYPE ALPHABETICALLY & VALUE DECEND
# ==========================================

print()

type_alpha_value_decend = sorted(unique, key=lambda x: (x['type'], -x['value']))

print("By type alphabetically and value decend:\n")
for item in type_alpha_value_decend:
    print(f"{item['id']} | {item['item']} | Type: {item['type']} | {item['weight']} | ${item['value']}")
