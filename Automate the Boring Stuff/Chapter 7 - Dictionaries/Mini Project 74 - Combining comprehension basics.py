
logs = [
    {"ip": "192.168.1.1", "event": "login", "status": "SUCCESS", "attempts": "1"},
    {"ip": "192.168.1.2", "event": "login", "status": "FAILED", "attempts": "5"},
    {"ip": "192.168.1.1", "event": "scan", "status": "SUCCESS", "attempts": "1"},
    {"ip": "192.168.1.3", "event": "login", "status": "FAILED", "attempts": "twelve"},
    {"ip": "192.168.1.2", "event": "login", "status": "SUCCESS", "attempts": "1"},
    {"ip": "192.168.1.4", "event": "scan", "status": "FAILED", "attempts": "3"},
]

unique_ips = {log['ip'] for log in logs}

print(unique_ips)

ip_status = {log['ip']: log['status'].lower() for log in logs}

print(ip_status)

failed_status = {log['ip']: log['status'] for log in logs if log['status'].lower() == 'failed'}

print(failed_status)

cleaned_attempts = [int(log['attempts']) for log in logs]

print(cleaned_attempts)

sus_vs_clean = {log['ip']: 'suspicious' if log['status'].lower() == 'failed' else 'clean' for log in logs}

print(sus_vs_clean)
