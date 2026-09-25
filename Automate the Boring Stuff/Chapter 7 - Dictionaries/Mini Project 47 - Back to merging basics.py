
wishlist_1 = [
    {"item": "sword", "price": 150},
    {"item": "shield", "price": 80},
    {"item": "potion", "price": 20},
]

wishlist_2 = [
    {"item": "potion", "price": 20},
    {"item": "helmet", "price": 110},
    {"item": "sword", "price": 150},
]

merged = wishlist_1 + wishlist_2
seen = set()    # ← tracks keys
unique = []     # ← stores records

for item in merged:
    key = (item['item'], item['price'])

    if key in seen:
        continue

    seen.add(key)
    unique.append(item)  # ← append the dict, not the key

for item in unique:
    print(f"{item['item']} | ${item['price']}")
