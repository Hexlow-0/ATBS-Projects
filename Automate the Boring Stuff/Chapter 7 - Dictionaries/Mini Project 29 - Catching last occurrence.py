
logins = [
    {"user": "alice", "ip": "192.168.1.1", "status": "success"},
    {"user": "bob", "ip": "192.168.1.2", "status": "failed"},
    {"user": "alice", "ip": "192.168.1.3", "status": "success"},
    {"user": "carol", "ip": "192.168.1.1", "status": "failed"},
    {"user": "bob", "ip": "192.168.1.2", "status": "success"},
    {"user": "alice", "ip": "192.168.1.4", "status": "failed"},
]

seen = {}

for log in logins:

    user = log.get('user')
    ip = log.get('ip')
    status = log.get('status')

    seen[user] = log

for log in seen.values():

    print(f"{log['user']} | {log['ip']} | {log['status']}")
