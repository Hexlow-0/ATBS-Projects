
security_events = [
    {"event_id": "E001", "host": "  web-01  ", "severity": "HIGH", "type": "intrusion", "attempts": "5", "metadata": {"analyst": "alice", "reviewed": "YES"}},
    {"event_id": "E002", "host": "DB-SERVER", "severity": "critical", "type": "BRUTEFORCE", "attempts": "twelve", "metadata": {"analyst": "bob", "reviewed": "NO"}},
    {"event_id": "E003", "host": None, "severity": "low", "type": "scan", "attempts": "3", "metadata": None},
    {"event_id": "E001", "host": "web-01", "severity": "HIGH", "type": "intrusion", "attempts": "5", "metadata": {"analyst": "alice", "reviewed": "YES"}},
    {"event_id": "E004", "host": "  mail-01  ", "severity": "MEDIUM", "type": "phishing", "attempts": None, "metadata": {"analyst": None, "reviewed": "NO"}},
    {"event_id": "E005", "host": "WORKSTATION", "severity": "critical", "type": "malware", "attempts": "8", "metadata": {"analyst": "carol", "reviewed": "YES"}},
]

severity_map = {
    'critical': 0,
    'high': 1,
    'medium': 2,
    'low': 3,
}

type_handlers = {
    'intrusion': lambda: print("  → Escalate to IR team"),
    'bruteforce': lambda: print("  → Block source IP"),
    'malware': lambda: print("  → Isolate host"),
    'phishing': lambda: print("  → Alert user"),
    'scan': lambda: print("  → Monitor and log"),
}

def safe_int(value, default=0):

    try:
        return int(value)
    except (ValueError, TypeError, KeyError):
        return default

def clean_event(event):

    event_id = (event.get('event_id') or "")
    host = (event.get('host') or "").strip().capitalize()

    if not host:

        return {'ok': False,
                'field': 'host',
                'reason': 'missing host',
                'record': event
                }

    sev_raw = event.get('severity').lower()
    severity = severity_map.get(sev_raw, 3)
    sev_mapped = severity_map.get(sev_raw, 'low')
    event_type = (event.get('type', 'unknown') or "")
    attempts = safe_int(event.get('attempts'))
    metadata = (event.get('metadata') or {})
    analyst = (metadata.get('analyst', 'unassigned') or "")
    reviewed = (metadata.get('reviewed', 'no') or "").lower()

    return {'ok': True,
            'data': {'event_id': event_id,
                    'host': host,
                    'severity': severity,
                    'sev_mapped': sev_mapped,
                    'event_type': event_type,
                    'attempts': attempts,
                    'analyst': analyst,
                    'reviewed': reviewed
                    }
                }

def deduplicate(processed):

    seen = set()
    cleaned = []

    for record in processed:

        key = record['event_id']

        if key in seen:
            continue

        seen.add(key)
        cleaned.append(record)

    return cleaned

def print_report(cleaned, errors):

    organised = sorted(cleaned, key=lambda x: x['severity'])

    print("=== Valid records ===\n")

    for event in organised:

        event_id = event['event_id']
        host = event['host']
        sev_mapped = event['sev_mapped']
        event_type = event['event_type']
        attempts = event['attempts']
        analyst = event['analyst']
        reviewed = event['reviewed']

        print(f"Event ID: {event_id} | Host: {host} | Severity: {sev_mapped}")
        print(f"Type: {event_type} | Attempts: {attempts}")
        print(f"Analyst: {analyst} | Reviewed: {reviewed}\n")

    print("=== Type handlers ===\n")

    for event in organised:

        handler = type_handlers.get(event.get('event_type'))

        if handler:
            handler()
        else:
            pass # pass silently if not found (intentional, task doesnt suggest alternative)

    print()

    print("=== Errors ===\n")

    for i, error in enumerate(errors, start = 1):

        print(f"Error {i}:")
        print(f"Field: {error['field']}")
        print(f"Reason: {error['reason']}")
        print(f"Record: {error['record']}\n")

def main():

    # had to scroll up (cheated)
    results = [clean_event(event) for event in security_events]
    processed = [r['data'] for r in results if r['ok']]
    errors = [r for r in results if not r['ok']]

    print_report(deduplicate(processed), errors)

main()
