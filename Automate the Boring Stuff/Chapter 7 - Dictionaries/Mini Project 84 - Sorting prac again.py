
incidents = [
    {"id": "I001", "severity": "low", "status": "open", "type": "scan"},
    {"id": "I002", "severity": "critical", "status": "resolved", "type": "intrusion"},
    {"id": "I003", "severity": "high", "status": "open", "type": "malware"},
    {"id": "I004", "severity": "medium", "status": "open", "type": "scan"},
    {"id": "I005", "severity": "critical", "status": "open", "type": "intrusion"},
]

severity_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
status_order = {'open': 0, 'resolved': 1}

severity = sorted(incidents, key=lambda x: severity_order[x['severity']])
status = sorted(incidents, key=lambda x: status_order[x['status']])
both = sorted(incidents, key=lambda x: (severity_order[x['severity']], status_order[x['status']]))

for i in severity:

    print(i)

print()

for i in status:

    print(i)

print()

for i in both:

    print(i)

print()

