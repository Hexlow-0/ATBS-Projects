
scan_1 = [
    {"ip": "192.168.1.1", "hostname": "router-01", "port": "80", "service": "http", "status": "UP"},
    {"ip": "192.168.1.2", "hostname": "WORKSTATION-A", "port": "443", "service": "https", "status": "up"},
    {"ip": "192.168.1.3", "hostname": None, "port": "22", "service": "SSH", "status": "UP"},
    {"ip": "192.168.1.4", "hostname": "printer-01", "port": "nine", "service": "unknown", "status": "up"},
]

scan_2 = [
    {"ip": "192.168.1.2", "hostname": "workstation-a", "port": "443", "service": "HTTPS", "status": "UP"},
    {"ip": "192.168.1.5", "hostname": "SERVER-01", "port": "3306", "service": "mysql", "status": "UP"},
    {"ip": "192.168.1.6", "hostname": "workstation-b", "port": "22", "service": "ssh", "status": "DOWN"},
    {"ip": "192.168.1.3", "hostname": "firewall-01", "port": "22", "service": "ssh", "status": "UP"},
]

port_services = {
    80: 'HTTP',
    443: 'HTTPS',
    22: 'SSH',
    3306: 'MySQL',
    21: 'FTP',
}

def clean_asset(scan):

    ip = (scan.get('ip') or "")

    if not ip:

        return {'ok': False,
                'field': 'ip',
                'reason': 'missing ip',
                'record': scan
                }

    hostname = (scan.get('hostname') or "").capitalize()

    if not hostname:

        hostname = 'Unknown'

    try:
        port = int((scan.get('port') or 0))
    except (ValueError, TypeError):
        port = 0

    service = (scan.get('service') or "unknown").lower()

    looked_up = port_services.get(port)

    if looked_up:

        service = looked_up

    status = (scan.get('status').lower())

    if status not in ['up', 'down']:

        status = 'unknown'

    return {'ok': True,
            'data': {'ip': ip,
                    'hostname': hostname,
                    'port': port,
                    'service': service,
                    'status': status
                    }
                }

def merge_scans(scan_1, scan_2):

    return scan_1 + scan_2

def print_report(cleaned, errors):

    sorted_scans = sorted(cleaned, key=lambda x: x['ip'])

    for scan in sorted_scans:

        ip = scan['ip']
        hostname = scan['hostname']
        port = scan['port']
        service = scan['service']
        status = scan['status']

        print(f"{ip} | {port} | {status} | {service} | {hostname}")

    print()

    print("Errors:\n")

    if len(errors) < 1:

        print("No errors.")

    else:

        for i, error in enumerate(errors, start = 1):

            print(f"Error: {i}:")
            print(f"Field: {error['field']}")
            print(f"Reason: {error['reason']}")
            print(f"Record: {error['record']}")


def main():

    deduplicate = set()
    errors = []
    cleaned = []

    asset = merge_scans(scan_1, scan_2)

    for scan in asset:

        result = clean_asset(scan)

        if not result['ok']:
            errors.append(result)
            continue

        key = (result['data']['ip'], result['data']['port'])

        if key in deduplicate:
            continue

        deduplicate.add(key)


        cleaned.append(result['data'])

    print_report(cleaned, errors)

main()







