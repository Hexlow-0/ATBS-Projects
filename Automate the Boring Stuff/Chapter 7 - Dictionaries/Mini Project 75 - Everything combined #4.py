
scan_data = [
    {"host": "  web-server-01  ", "ip": "10.0.0.1", "ports": [80, 443, 8080], "os": "LINUX", "vulnerabilities": {"critical": 2, "high": 3, "low": 8}},
    {"host": "DB-SERVER", "ip": "10.0.0.2", "ports": [3306, 22], "os": "linux", "vulnerabilities": {"critical": 0, "high": 1, "low": 4}},
    {"host": None, "ip": "10.0.0.3", "ports": [22, 80], "os": "WINDOWS", "vulnerabilities": {"critical": 5, "high": 2, "low": 1}},
    {"host": "web-server-01", "ip": "10.0.0.1", "ports": [80, 443, 8080], "os": "Linux", "vulnerabilities": {"critical": 2, "high": 3, "low": 8}},
    {"host": "  mail-server  ", "ip": "10.0.0.4", "ports": [25, 587], "os": "LINUX", "vulnerabilities": None},
    {"host": "WORKSTATION-A", "ip": "10.0.0.5", "ports": [], "os": "windows", "vulnerabilities": {"critical": 0, "high": 0, "low": 2}},
]

port_services = {
    80: 'HTTP', 443: 'HTTPS', 22: 'SSH',
    3306: 'MySQL', 25: 'SMTP', 587: 'SMTP',
    8080: 'HTTP-ALT'
}

expected_keys = {'host', 'ip', 'ports', 'os', 'vulnerabilities'}


def clean_host(data):

    # Set data as is
    actual = set(data)

    # Store the extra keys (take away the expected, whats left is new)
    extra_keys = actual - expected_keys

    # Get the host, capitalised with no white space
    host = (data.get('host') or "").strip().title()

    # Richer return, as task requests
    if not host:

        return {'ok': False,
                'field': 'host',
                'reason': 'missing host',
                'record': data
                }

    # Get the ip, catch potential none value
    ip = (data.get('ip') or "")

    # Store ip as 'unknown' if missing, like tasl said
    if not ip:

        ip = 'unknown'

    # Collect the ports - catch case of empty list
    ports = (data.get('ports') or [])

    # Store service names from port service lookup using comprehension
    service_names = [port_services.get(port) for port in ports]

    # Store OS, lowered, default unknown if not expected value
    os = (data.get('os') or "").lower()

    if os not in ['linux', 'windows']:

        os = 'unknown'

    vulnerability = (data.get('vulnerabilities') or {})

    critical_vul = vulnerability.get('critical', 0)
    high_vul = vulnerability.get('high', 0)
    low_vul = vulnerability.get('low', 0)



    # Calculate risk level based on task description
    if critical_vul > 0:
        risk_level = 'critical'
    elif high_vul > 0:
        risk_level = 'high'
    else:
        risk_level = 'low'

    # Return all the relevant data
    return {'ok': True,
            'data': {'host': host,
                    'ip': ip,
                    'ports': ports,
                    'service_names': service_names,
                    'os': os,
                    'vulnerabilities': vulnerability,
                    'risk_level': risk_level,
                    'extra_keys': extra_keys
                    }
                }

def deduplicate(processed):

    cleaned = []
    seen = set()

    for data in processed:

        # Deduplicate by ip and host combined like task says
        key = (data['ip'], data['host'])

        if key in seen:
            continue

        seen.add(key)
        cleaned.append(data)

    return cleaned


def print_report(cleaned, errors):

    print("Valid record (as is):\n")

    for record in cleaned:

        host = record['host']
        ip = record['ip']
        ports = record['ports']
        service_names = record['service_names']
        os = record['os']
        vulnerabilities = record['vulnerabilities']
        risk_level = record['risk_level']
        extra_keys = record['extra_keys']

        print(f"Host: {host} | OS: {os}")
        print(f"It's IP: {ip} | ports: {ports}")
        print(f"Service names: {service_names}")
        print(f"Vulnerabilities: {vulnerabilities}")
        print(f"Risk level: {risk_level}")
        print(f"Extra keys: {extra_keys}\n")

    print()

    print("Sorted by risk level:\n")

    # Note that what was required for this part was outside the scope of what I knew - i worked with what i had though
    organised = sorted(cleaned, key=lambda x: x['risk_level'])

    for record in organised:

        host = record['host']
        ip = record['ip']
        ports = record['ports']
        service_names = record['service_names']
        os = record['os']
        vulnerabilities = record['vulnerabilities']
        risk_level = record['risk_level']
        extra_keys = record['extra_keys']

        print(f"Host: {host} | OS: {os}")
        print(f"It's IP: {ip} | ports: {ports}")
        print(f"Service names: {service_names}")
        print(f"Vulnerabilities: {vulnerabilities}")
        print(f"Risk level: {risk_level}")
        print(f"Extra keys: {extra_keys}\n")

    print("Errors:\n")

    if len(errors) < 1:

        print("No errors caught.")

    else:

        for i, error in enumerate(errors, start = 1):

            print(f"Error {i}")
            print(f"Field: {error['field']}")
            print(f"Reason: {error['reason']}")
            print(f"Record: {error['record']}\n")

def main():

    errors = []
    processed = []

    for data in scan_data:

        result = clean_host(data)

        if not result['ok']:
            errors.append(result)
            continue

        processed.append(result['data'])

    cleaned = deduplicate(processed)

    print_report(cleaned, errors)

main()
