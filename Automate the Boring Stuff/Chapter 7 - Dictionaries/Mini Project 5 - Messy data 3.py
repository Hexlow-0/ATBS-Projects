


members = [
    {"name": "chris", "age": "34", "membership": "gold", "sessions_attended": "12"},
    {"name": "SAM", "age": None, "membership": "", "sessions_attended": "seven"},
    {"name": "Riley", "age": "twenty", "membership": "silver", "sessions_attended": 9},
    {"name": "", "age": "29", "membership": "bronze", "sessions_attended": "4"},
    {"name": "Drew", "age": "41", "membership": None, "sessions_attended": None},
]


for member in members:

    name = member.get('name')

    # if not x always means skip record entirely?
    if not name:
        continue

    try:
        age = int(member.get('age', 0))
    except (ValueError, KeyError, TypeError):
        age = 0

    membership = member.get('membership', 'standard') or 'standard'

    try:
        sessions_attended = int(member.get('sessions_attended', 0))
    except (ValueError, KeyError, TypeError):
        sessions_attended = 0

    print(f"{name.capitalize()} | Age: {age} | Membership: {membership} | Sessions: {sessions_attended}")

