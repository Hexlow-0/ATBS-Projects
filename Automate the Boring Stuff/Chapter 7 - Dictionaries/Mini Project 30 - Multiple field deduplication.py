
logins = [
    {"user": "alice", "ip": "192.168.1.1", "status": "success"},
    {"user": "bob", "ip": "192.168.1.2", "status": "failed"},
    {"user": "alice", "ip": "192.168.1.3", "status": "success"},
    {"user": "carol", "ip": "192.168.1.1", "status": "failed"},
    {"user": "bob", "ip": "192.168.1.2", "status": "success"},
    {"user": "alice", "ip": "192.168.1.4", "status": "failed"},
]


seen = set()

unique = 0
skipped = 0

for log in logins:

    user = log.get('user')
    ip = log.get('ip')
    status = log.get('status')

    key = (user, status)

    if key in seen:
        skipped += 1
        continue

    unique += 1
    seen.add(key)

    print(f"{user} | {status}")

print()

print(f"Unique combinations: {unique} | Skipped: {skipped}")

