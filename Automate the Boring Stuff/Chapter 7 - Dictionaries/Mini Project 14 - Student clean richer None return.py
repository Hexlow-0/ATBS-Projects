
enrollments = [
    {"student": "  lisa  ", "course": "PYTHON", "level": "beginner", "fee": "$150"},
    {"student": "Mike", "course": "javascript", "level": "EXPERT", "fee": "$*200"},
    {"student": "  ", "course": "SQL", "level": "intermediate", "fee": "$175"},
    {"student": "ANNA", "course": "python", "level": "ADVANCED", "fee": "$*225"},
    {"student": "Tom", "course": "", "level": "beginner", "fee": "$100"},
]

def clean_enrollment(enrol):

    student = enrol.get('student', "").strip().capitalize()

    course = enrol.get('course', "").strip().capitalize()

    if not student or not course:

        return {'ok': False,
                'reason': 'empty or missing field',
                'record': enrol,
                'field': 'student or course',
                'severity': 'no biggie👌👌👌'
                }

    level = enrol.get('level', "").lower()

    if level not in ['beginner', 'intermediate', 'advanced']:

        level = 'invalid level'

    try:
        fee = int(enrol.get('fee', 0).replace("$", "").replace("*", ""))
    except (ValueError, TypeError):
        fee = 0

    return {
        'ok': True,
        'data': {
            'student': student,
            'course': course,
            'level': level,
            'fee': fee
            }
        }


def print_enrollments(cleaned, errors):


    for student in cleaned:

        name = student['student']
        course = student['course']
        level = student['level']
        fee = student['fee']

        print(f"{name} | Course: {course} | {level} | Fee: ${fee}")


    print()

    print("errors:\n")

    for index, error in enumerate(errors):

        status = error['ok']
        reason = error['reason']
        record = error['record']
        field = error['field']
        severity = error['severity']

        print(f"Error: {index + 1}.")
        print(f"Status: {status}")
        print(f"reason: {reason}")
        print(f"record: {record}")
        print(f"field: {field}")
        print(f"severity: {severity}\n")




    print()



def main():

    cleaned = []
    errors = []

    for enrol in enrollments:

        result = clean_enrollment(enrol)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])


    print_enrollments(cleaned, errors)

main()
