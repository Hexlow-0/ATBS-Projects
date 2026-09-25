
title = ["the", "great", "gatsby"]
tags = ["python", "beginner", "project", "coding"]
messy = "   too    many    spaces   in    here   "
csv_row = "john,smith,28,sydney,premium"

print(" ".join(title).title())

tags = ["#" + word for word in tags]
print(' '.join(tags))

print(' '.join(messy.split()))

print()
csv_row = csv_row.split(',')
print(f"Name: {csv_row[0]}")
print(f"Last name: {csv_row[1]}")
print(f"Age: {csv_row[2]}")
print(f"City: {csv_row[3]}")
print(f"Membership: {csv_row[4]}")

full_name = " ".join([csv_row[0], csv_row[1]])

print(full_name)
