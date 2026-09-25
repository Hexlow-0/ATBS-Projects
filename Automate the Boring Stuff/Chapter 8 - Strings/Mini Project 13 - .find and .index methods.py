
logs = """INFO: server started successfully
ERROR: connection timeout on port 8080
INFO: user alice logged in
ERROR: failed to read config file
WARNING: disk space below 20%
INFO: backup completed
ERROR: database connection lost"""

errors = 0

for lines in logs.splitlines():

    position = lines.find("ERROR")
    if position != -1:
        print(lines.replace("ERROR: ", ""))
        errors += 1


        print(f"Pos: {position}")


print()
print("Errors:")
print(errors)
