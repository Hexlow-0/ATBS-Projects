
ports = [80, 443, 22, 21, 8080, 3306, 9999, 25]

port_services = {
    80: 'HTTP',
    443: 'HTTPS',
    22: 'SSH',
    21: 'FTP',
    8080: 'HTTP-ALT',
    3306: 'MySQL',
    25: 'SMTP'
}

for port in ports:

    port_num = port_services.get(port, 'unknown')

    print(f"Port {port}: {port_num}")
