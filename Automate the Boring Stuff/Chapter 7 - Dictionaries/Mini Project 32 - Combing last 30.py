

logs = [
    {"src_ip": "192.168.1.1", "dst_port": "80", "protocol": "TCP", "status": "allowed", "event": "connection", "user_id": "U001"},
    {"src_ip": "10.0.0.5", "dst_port": "443", "protocol": "udp", "status": "BLOCKED", "event": "connection"},
    {"src_ip": None, "dst_port": "22", "protocol": "TCP", "status": "allowed", "event": "login", "user_id": "U002", "raw_payload": "xyz123"},
    {"src_ip": "192.168.1.1", "dst_port": "80", "protocol": "TCP", "status": "allowed", "event": "connection", "user_id": "U001"},
    {"src_ip": "172.16.0.3", "dst_port": "9999", "protocol": "TCP", "status": "allowed", "event": "connection", "debug_info": "test"},
    {"src_ip": "10.0.0.5", "dst_port": "twenty two", "protocol": "UDP", "status": "suspicious", "event": "scan"},
    {"src_ip": "192.168.1.2", "dst_port": "3306", "protocol": "TCP", "status": "ALLOWED", "event": "db_access", "user_id": "U003"},
]

port_services = {
    80: 'HTTP',
    443: 'HTTPS',
    22: 'SSH',
    3306: 'MySQL',
    21: 'FTP',
}

severity_map = {
    'allowed': 1,
    'blocked': 3,
    'suspicious': 5,
}

expected_keys = {'src_ip', 'dst_port', 'protocol', 'status', 'event'}

def clean_log(log):

    src_ip = (log.get('src_ip') or "")

    if not src_ip:

        return {'ok': False,
                'field': 'src_ip',
                'reason': 'missing src_ip',
                'record': log
                }

    try:
        dst_port = int((log.get('dst_port') or 0))
    except (ValueError, TypeError):
        dst_port = 0

    service = port_services.get(dst_port, 'unknown')

    protocol = (log.get('protocol') or "").lower()

    if protocol not in ['tcp', 'udp']:

        return {'ok': False,
                'field': 'protocol',
                'reason': 'invalid protocol',
                'record': log
                }

    # default 'unknown' if misssing, as said in instructions
    status = (log.get('status', 'unknown') or "").lower()

    severity = severity_map.get(status, 0)

    event = (log.get('event') or "").lower()

    actual = set(log.keys())

    missing = expected_keys - actual
    extra = actual - expected_keys

    return {'ok': True,
            'data': {'src_ip': src_ip,
                    'dst_port': dst_port,
                    'service': service,
                    'protocol': protocol,
                    'status': status,
                    'severity': severity,
                    'event': event,
                    'actual': actual,
                    'missing': missing,
                    'extra': extra
                    }
                }

def print_logs(processed, errors):

    print("Valid records:\n")

    seen = set()

    for log in processed:

        src_ip = log['src_ip']
        dst_port = log['dst_port']

        if (src_ip, dst_port) in seen:
            continue

        seen.add((src_ip, dst_port))

        print(f"{src_ip}:{dst_port} ({log['service']}) | {log['protocol']} | {log['status']} | severity: {log['severity']}")
        print(f"Extra fields: {log['extra']}")
        print(f"Missing fields: {log['missing']}\n")

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        print(f"Error {i}:")
        print(f"Field: {error['field']}")
        print(f"Reason: {error['reason']}")
        print(f"Record: {error['record']}\n")


def main():


    errors = []
    processed = []

    for log in logs:

        result = clean_log(log)

        if not result['ok']:
            errors.append(result)
            continue

        processed.append(result['data'])

    print_logs(processed, errors)

main()



