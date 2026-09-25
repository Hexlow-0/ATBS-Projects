
records = [
    {"user": {"name": "Alice", "address": {"city": "Sydney", "postcode": "2000"}}},
    {"user": {"name": "Bob", "address": {"city": "Melbourne"}}},
    {"user": {"name": "Charlie"}},
    {"user": {}},
    {}
]

for record in records:

    name = (record.get('user') or {}).get('name', 'unknown')

    city = (record.get('user') or {}).get('address') or {}.get('city', 'unknown')

    postcode = (record.get('user') or {}).get('address') or {}.get('postcode', 'N/A')

    print(f"{name} - {city} - {postcode}")



