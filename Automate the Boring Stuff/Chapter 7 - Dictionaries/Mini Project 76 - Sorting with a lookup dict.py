
tickets = [
    {"id": "T001", "priority": "low"},
    {"id": "T002", "priority": "critical"},
    {"id": "T003", "priority": "high"},
    {"id": "T004", "priority": "low"},
    {"id": "T005", "priority": "critical"},
]

lookup = {'critical': 0, 'high': 1, 'low': 2}

organised = sorted(tickets, key=lambda x: lookup[x['priority']])

print(organised)
