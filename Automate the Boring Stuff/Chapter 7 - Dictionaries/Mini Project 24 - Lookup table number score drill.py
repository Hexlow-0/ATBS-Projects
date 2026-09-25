
incidents = [
    {"type": "port_scan", "source": "external"},
    {"type": "failed_login", "source": "internal"},
    {"type": "ddos", "source": "external"},
    {"type": "unknown_traffic", "source": "external"},
    {"type": "failed_login", "source": "external"},
]

severity_scores = {
    'port_scan': 3,
    'failed_login': 2,
    'ddos': 9,
    'unknown_traffic': 5,
}

for incident in incidents:

    inc_type = incident['type']
    source = incident['source']

    severity = severity_scores.get(inc_type, 0)

    print(f"{inc_type} ({source}) - severity: {severity}")
