
records = [
    {"name": "Alice", "address": {"city": "Sydney", "country": "AU"}, "scores": {"math": 88, "english": 92}},
    {"name": "Bob", "address": {"city": "Melbourne", "country": "AU"}, "scores": {"math": 74, "english": 81}},
    {"name": "Carol", "address": None, "scores": {"math": 95, "english": 88}},
]

def flatten(record):

    return {
        'name': record.get('name'),
        'city': (record.get('address') or {}).get('city'),
        'country': (record.get('address',) or {}).get('country'),
        'math_score': (record.get('scores') or {}).get('math'),
        'english_score': (record.get('scores') or {}).get('english')
        }

output = [flatten(record) for record in records]

for record in output:

    print(record)
