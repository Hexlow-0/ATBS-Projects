

records = [
    {"name": "Alice", "score": "88"},
    {"name": None, "score": "72"},
    {"name": "Carol", "score": "ninety"},
    {"name": "Dan", "score": "95"},
    {"name": "", "score": "61"},
]

def clean_record(record):
    name = (record.get('name') or "").strip().capitalize()
    if not name:
        return {'ok': False, 'reason': 'missing name', 'record': record}
    try:
        score = int(record.get('score') or 0)
    except (ValueError, TypeError):
        score = 0
    return {'ok': True, 'data': {'name': name, 'score': score}}

def print_records(processed, errors):

    print(processed)

    print()

    print(errors)

def main():

    results = [clean_record(record) for record in records]
    errors = [r for r  in results if not r['ok']]
    processed = [r['data'] for r in results if r['ok']]

    print_records(processed, errors)

main()

