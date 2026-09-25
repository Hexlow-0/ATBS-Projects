

students = [
    {"name": "Alice", "grade": "88", "subject": "Math"},
    {"name": "Bob", "grade": "seventy", "subject": "Science"},
    {"name": "Carol", "grade": "92", "subject": "Math"},
    {"name": "Dan", "grade": None, "subject": "Science"},
    {"name": "Eve", "grade": "78", "subject": "Math"},
]

cleaned = []

for student in students:

    name = student.get('name')

    try:
        grade = int((student.get('grade', 0) or "0"))
    except (ValueError, TypeError):
        grade = 0

    subject = student.get('subject')

    cleaned.append({'name': name, 'grade': grade, 'subject': subject})

sorted_students = sorted(cleaned, key=lambda x: x['grade'], reverse=True)

for student in sorted_students:

    print(f"{student['name']} | {student['subject']} | {student['grade']}")
