
def handle_login(user):
    print(f"  → Processing login for {user}")

def handle_logout(user):
    print(f"  → Processing logout for {user}")

def handle_failed(user):
    print(f"  → Flagging failed attempt for {user}")

def handle_scan(user):
    print(f"  → Logging scan from {user}")

dispatch = {
    'login': handle_login,
    'logout': handle_logout,
    'failed': handle_failed,
    'scan': handle_scan,
}

events = [
    ('login', 'alice'),
    ('failed', 'bob'),
    ('scan', '192.168.1.1'),
    ('unknown', 'carol'),
    ('logout', 'alice'),
    ('brute_force', '10.0.0.5'),
    ('login', 'diana'),
]

for event, action in events:

    do = dispatch.get(event)

    if do:
        do(action)
    else:
        print(f"unknown event: {action}")
