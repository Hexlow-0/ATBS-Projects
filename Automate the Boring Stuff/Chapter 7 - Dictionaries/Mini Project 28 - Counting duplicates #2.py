
logins = [
    {"user": "alice", "ip": "192.168.1.1", "status": "success"},
    {"user": "bob", "ip": "192.168.1.2", "status": "failed"},
    {"user": "alice", "ip": "192.168.1.3", "status": "success"},
    {"user": "carol", "ip": "192.168.1.1", "status": "failed"},
    {"user": "bob", "ip": "192.168.1.2", "status": "success"},
    {"user": "alice", "ip": "192.168.1.4", "status": "failed"},
]

seen = set()

duplicates = 0
unique = 0

for log in logins:

    user = log.get('user')
    ip = log.get('ip')
    status = log.get('status')

    if user in seen:
        duplicates += 1
        continue

    unique += 1
    seen.add(user)

    print(f"{user} | {ip} | {status}")

print(f"Unique users: {unique} | Skipped: {duplicates}")
