
employees = """Alice,Engineering,85000
Bob,Sales,62000
Charlie,Engineering,95000
Diana,Marketing,71000
Ed,Sales,58000
Frank,Engineering,78000
Grace,Marketing,69000"""

result = {}

for emp in employees.splitlines():

    name, dept, salary = emp.split(',')

    salary = int(salary)

    key = dept

    if key not in result:
        result[key] = []

    result[key].append({'name': name, 'sal': salary})

count = {}

for dept, info in result.items():

    for i in info:

        count[dept] = count.get(dept, 0) + 1

dept_count = 0

for dept, info in result.items():


    if count[dept] < 3:
        continue

    total = 0

    for i in info:

        sal = i['sal']

        total += sal

    average = total / count[dept]

    print(f"{dept:14}${average:.2f}")







