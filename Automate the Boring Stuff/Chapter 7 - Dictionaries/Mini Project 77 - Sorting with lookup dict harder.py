
incidents = [
    {"id": "I001", "severity": "high", "status": "open"},
    {"id": "I002", "severity": "critical", "status": "resolved"},
    {"id": "I003", "severity": "low", "status": "open"},
    {"id": "I004", "severity": "critical", "status": "open"},
    {"id": "I005", "severity": "high", "status": "resolved"},
]

severity_map = {'critical': 0, 'high': 1, 'low': 2}
status_map = {'open': 0, 'resolved': 1}

organised = sorted(
        incidents,
        key=lambda x:
            (severity_map[x['severity']],
            status_map[x['status']]
            )
        )

print(organised)

