
emails = [
    "alice@email.com",
    "bob.jones@company.org",
    "notanemail",
    "missing@dotcom",
    "charlie@email.com",
    "@nousername.com",
    "nodomain@",
]

for email in emails:

    # 1. does it have an @ at all?
    if "@" not in email:
        print(f"{email} — invalid: no @ symbol")
        continue

    # 2. find where @ lives
    pos = email.find("@")

    # 3. anything before it?
    if pos == 0:
        print(f"{email} — invalid: nothing before @")
        continue

    # 4. anything after it?
    if pos == len(email) - 1:
        print(f"{email} — invalid: nothing after @")
        continue

    # 5. any dot after it?
    if "." not in email[pos:]:
        print(f"{email} — invalid: not dot after @")
        continue

    print(f"{email} - valid")
