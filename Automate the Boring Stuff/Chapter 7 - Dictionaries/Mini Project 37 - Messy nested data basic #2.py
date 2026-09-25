
companies = [
    {"company": "Acme", "office": {"location": {"city": "Sydney", "postcode": "2000"}, "floor": 4}},
    {"company": "Globex", "office": {"location": None, "floor": 2}},
    {"company": "Initech", "office": None},
    {"company": "Umbrella", "office": {"location": {"city": "Melbourne"}, "floor": 7}},
    {"company": "Hooli"},
]

for com in companies:

    company = com.get('company')

    office = com.get('office') or {}

    location = office.get('location') or {}

    postcode = location.get('postcode', 'unknown')

    city = location.get('city', 'unknown')

    floor = office.get('floor', 'unknown')

    print(f"{company} | {city} | {postcode} | {floor}")
