
data = [
    {"company": "Acme", "office": {"location": {"address": {"street": "123 Main St", "postcode": "2000"}, "city": "Sydney"}, "floor": 4}},
    {"company": "Globex", "office": {"location": {"address": {"street": "456 High St"}, "city": "Melbourne"}, "floor": 2}},
    {"company": "Initech", "office": {"location": None, "floor": 3}},
    {"company": "Umbrella", "office": None},
    {"company": "Hooli"},
]

for d in data:

    company = d.get('company', 'unknown')

    office = (d.get('office') or {})

    location = (office.get('location') or {})

    address = (location.get('address') or {})

    street = address.get('street', 'unknown')

    city = location.get('city', 'unknown')

    floor = office.get('floor', 'unknown')

    postcode = address.get('postcode', 'unknown')

    print(f"{company} - {city} - {street} - {postcode} - {floor}")
