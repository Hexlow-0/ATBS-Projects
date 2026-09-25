
employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 95000},
    {"name": "Bob", "dept": "HR", "salary": 58000},
    {"name": "Carol", "dept": "Engineering", "salary": 112000},
    {"name": "Dan", "dept": "HR", "salary": 61000},
    {"name": "Eve", "dept": "Engineering", "salary": 78000},
]

# task 1 - name: salary
name_sal = {emp['name']: emp['salary'] for emp in employees}

print(name_sal)

# task 2 - name: dept
name_dept = {emp['name']: emp['dept'] for emp in employees}

print(name_dept)

# task 3 - name: salary (engineers only)
name_sal_eng = {emp['name']: emp['salary'] for emp in employees if emp['dept'] == 'Engineering'}

print(name_sal_eng)

high_or_low = {emp['name']: 'high' if emp['salary'] > 80000 else 'low' for emp in employees}

print(high_or_low)
