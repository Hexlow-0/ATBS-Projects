

data = """NAME:Alice|AGE:25|CITY:NYC
NAME:Bob|AGE:thirty|CITY:LA
NAME:Charlie|CITY:Chicago
NAME:Diana|AGE:28|CITY:NYC|CITY:Boston"""


for d in data.splitlines():

    record = {}

    for field in d.split('|'):
        key, value = field.split(':')
        record[key] = value

    print(record)

    name = (record.get('NAME', 'N/A') or "")

    try:
        age = int(record.get('AGE', 'N/A') or "")
    except ValueError:
        age = 'N/A'

    city = (record.get('CITY', 'N/A') or "")

    print(f"{name:<10}{age:<6}{city}")
