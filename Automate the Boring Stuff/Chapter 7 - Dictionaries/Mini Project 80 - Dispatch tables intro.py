
def scan_host(host):
    print(f"Scanning {host}...")

def block_ip(ip):
    print(f"Blocking {ip}...")

def generate_report(format):
    print(f"Generating {format} report...")

dispatch = {
    'scan': scan_host,
    'block': block_ip,
    'report': generate_report,
}

commands = [
    ('scan', '192.168.1.1'),
    ('block', '10.0.0.5'),
    ('report', 'PDF'),
    ('unknown', 'whatever'),
    ('scan', '192.168.1.2'),
]

for action, argument in commands:

    do = dispatch.get(action)

    if do:
        do(argument)
    else:
        print(f"unknown action: {action}")

