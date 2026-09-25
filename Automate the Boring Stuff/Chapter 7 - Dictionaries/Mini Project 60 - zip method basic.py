
headers = ['ip', 'port', 'service', 'status', 'response_time']

scan_results = [
    ['192.168.1.1', 80, 'http', 'open', '120ms'],
    ['192.168.1.1', 443, 'https', 'open', '95ms'],
    ['192.168.1.2', 22, 'ssh', 'open', '45ms'],
    ['192.168.1.3', 3306, 'mysql', 'closed', '200ms'],
    ['192.168.1.4', 80, 'http', 'open', '110ms'],
]

records = []

for scan in scan_results:

    record = dict(zip(headers, scan))

    records.append(record)

for i in records:

    if i['status'] == 'open':

        print(f"{i['ip']}:{i['port']} | {i['service']} | {i['response_time']}")
