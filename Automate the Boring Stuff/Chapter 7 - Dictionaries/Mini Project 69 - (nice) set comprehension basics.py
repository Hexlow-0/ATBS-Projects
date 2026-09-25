
orders = [
    {"customer": "Alice", "city": "Sydney", "category": "electronics"},
    {"customer": "Bob", "city": "Melbourne", "category": "furniture"},
    {"customer": "Carol", "city": "Sydney", "category": "electronics"},
    {"customer": "Dan", "city": "Brisbane", "category": "furniture"},
    {"customer": "Eve", "city": "Melbourne", "category": "electronics"},
]

unique_cities = {i['city'] for i in orders}

print(unique_cities)

unique_categories = {i['category'] for i in orders}

print(unique_categories)

elec_cities = {i['city'] for i in orders if i['category'] == 'electronics'}

print(elec_cities)
