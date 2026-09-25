
tickets = [
    {"user": "  alice  ", "priority": "HIGH", "status": "open", "category": "billing"},
    {"user": "BOB", "priority": "urgent", "status": "CLOSED", "category": "TECH"},
    {"user": None, "priority": "low", "status": "open", "category": "billing"},
    {"user": "Diana", "priority": "medium", "status": "pending", "category": "hr"},
    {"user": "Eve", "priority": "critical", "status": "OPEN", "category": "tech"},
    {"user": "Frank", "priority": "high", "status": "resolved", "category": "BILLING"},
]

priority_map = {
    'low': 'low',
    'medium': 'medium',
    'high': 'high',
    'urgent': 'high',       # maps to high
    'critical': 'high',     # maps to high
}

status_map = {
    'open': 'open',
    'closed': 'closed',
    'pending': 'pending',
    'resolved': 'closed',   # maps to closed
}


def clean_ticket(ticket):

    user = (ticket.get('user') or "").strip().capitalize()

    if not user:

        return {'ok': False,
                'record': ticket,
                'field': 'user',
                'reason': 'missing user'
                }

    raw_priority = (ticket.get('priority') or "").lower()

    priority = priority_map.get(raw_priority)

    if not priority:

        return {'ok': False,
                'record': ticket,
                'field': 'priority',
                'reason': 'invalid priority'
                }

    raw_status = (ticket.get('status') or "").lower()

    status = status_map.get(raw_status)

    if not status:

        return {'ok': False,
                'record': ticket,
                'field': 'status',
                'reason': 'invalid status'
                }

    category = (ticket.get('category') or "").lower()

    if category not in ['billing', 'tech', 'hr']:

        category = 'general (patched)'

    return {'ok': True,
            'data': {'user': user,
                    'priority': priority,
                    'status': status,
                    'category': category
                    }
                }
def print_tickets(cleaned, errors):

    for ticket in cleaned:

        user = ticket['user']
        priority = ticket['priority']
        status = ticket['status']
        category = ticket['category']

        print(f"{user} | {priority} | {status} | {category}")

    print()

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        print(f"Error {i}:")
        print(f"Reason: {error['reason']}")
        print(f"Field: {error['field']}")
        print(f"Record: {error['record']}\n")

def main():

    errors = []
    cleaned = []

    for ticket in tickets:

        result = clean_ticket(ticket)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_tickets(cleaned, errors)

main()
