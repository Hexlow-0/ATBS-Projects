
required_ports = {22, 80, 443, 3306, 8080}
open_ports =     {80, 443, 8080, 9999, 4444}

sus = open_ports - required_ports

required_not_open = required_ports - open_ports

required_and_open = required_ports & open_ports

print(sus)

print(required_not_open)

print(required_and_open)
