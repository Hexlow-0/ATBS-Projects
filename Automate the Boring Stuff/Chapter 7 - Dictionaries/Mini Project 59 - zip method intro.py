
headers = ['name', 'age', 'city', 'score']

row_1 = ['Alice', 28, 'Sydney', 88]
row_2 = ['Bob', 32, 'Melbourne', 74]
row_3 = ['Carol', 25, 'Brisbane', 91]

rows = [row_1, row_2, row_3]
records = []

for row in rows:
    record = dict(zip(headers, row))
    records.append(record)

for items in records:
    print(items)
