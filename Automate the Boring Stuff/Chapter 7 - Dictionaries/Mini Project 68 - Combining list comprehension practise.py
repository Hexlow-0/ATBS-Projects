
employees = [
    {"name": "  alice  ", "dept": "ENGINEERING", "salary": 95000, "years": 3},
    {"name": "BOB", "dept": "hr", "salary": 58000, "years": 7},
    {"name": "  carol  ", "dept": "Engineering", "salary": 112000, "years": 1},
    {"name": "Dan", "dept": "HR", "salary": 61000, "years": 5},
    {"name": "  eve  ", "dept": "ENGINEERING", "salary": 78000, "years": 9},
]

clean_names = [emp['name'].strip().title() for emp in employees]

print(clean_names)

eightyk = [emp['name'].strip().title() for emp in employees if emp['salary'] > 80000]

print(eightyk)

sen_or_jun = ['senior' if emp['years'] >= 5 else 'junior' for emp in employees]

print(sen_or_jun)

ten_percent = [emp['salary']* 1.1 for emp in employees]

print(ten_percent)

eng_dept = [emp for emp in employees if emp['dept'].lower() == 'engineering']

print(eng_dept)
