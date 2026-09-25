
logs = [
    "2026-06-15 09:23:11 ERROR database connection failed",
    "2026-06-15 09:45:02 INFO user alice logged in",
    "2026-06-15 10:01:55 WARNING disk space below 10%",
    "2026-06-15 10:15:33 ERROR timeout on request to payment API",
    "2026-06-15 11:02:44 INFO backup completed successfully",
]

errors = set()

for log in logs:


    date = log[:10]
    time = log[11:19]
    level_end = log.find(" ", 20)
    level = log[20:level_end]
    message = log[level_end + 1:]

    if level == 'ERROR':

        errors.add(message)

    print(f"Date: {date} | Time: {time} | Level: {level} | Message: {message}")


print()
print("ERRORS ONLY:")

for error in errors:
    print(error)


