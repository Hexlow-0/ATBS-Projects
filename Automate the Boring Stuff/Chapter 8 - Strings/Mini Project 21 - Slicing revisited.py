
messages = [
    "FROM:alice@email.com | SUBJECT:Meeting Tomorrow | BODY:Don't forget the meeting at 9am",
    "FROM:bob@email.com | SUBJECT:Quick Question | BODY:Can you send me the Q3 report?",
    "FROM:charlie@email.com | SUBJECT:Urgent | BODY:The server is down please check immediately",
]

col1, col2 = 9, 1

for line in messages:

    parts = line.split('|')

    email = parts[0][parts[0].find(':') + 1:].strip()
    subject = parts[1][parts[1].find(':') + 1:].strip()
    body = parts[2][parts[2].find(':') + 1:].strip()

    print('=' * 40)
    print("From".ljust(col1) + email.ljust(col2))
    print("Subject:".ljust(col1) + subject.ljust(col2))
    print("Body:".ljust(col1) + body.ljust(col2))
    print('=' * 40)




