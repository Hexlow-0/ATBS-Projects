
registrations = [
    {"name": "  alice  ", "ticket_type": "VIP", "price_paid": "$120", "age": "28"},
    {"name": "BOB", "ticket_type": "general", "price_paid": "85", "age": "twenty"},
    {"name": "Clara", "ticket_type": "PREMIUM", "price_paid": "$*45", "age": "31"},
    {"name": "", "ticket_type": "vip", "price_paid": "$60", "age": "25"},
    {"name": "Drew", "ticket_type": "backstage", "price_paid": "$200", "age": None},
]

for reg in registrations:

    name = reg.get('name', "").strip().capitalize()

    if not name:
        name = "unknown"

    try:
        age = int(reg.get('age', 0))
    except (ValueError, TypeError):
        age = 0


    try:
        price_paid = reg.get('price_paid').replace("$", "").replace("*", "")
        int(price_paid)
    except (ValueError, TypeError):
        price_paid = 0

    ticket_type = reg.get('ticket_type', 'general').lower()

    if ticket_type not in ['vip', 'general', 'premium']:
        ticket_type = 'general'

    print(f"{name} | Ticket: {ticket_type} | Price: ${price_paid} | Age: {age}")

