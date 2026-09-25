
report = """NAME:Alice Smith | GRADE:A | SCORE:95 | SUBJECT:Mathematics
name:Bob Jones|GRADE:C| SCORE : 61 | SUBJECT: English
NAME : Charlie Brown | Grade:B | SCORE:78|SUBJECT:Science
NAME:Diana Prince | GRADE=A | SCORE:92 | SUBJECT:History
NAME:Ed Norton | GRADE:F | SCORE:43 | SUBJECT:MATHS
NAME: Frank Miller | GRADE:B | SCORE: 84
NAME:Grace Lee | GRADE:A | SCORE:N/A | SUBJECT:Physics"""

from collections import defaultdict

# I wanted math patched so the cubject average was at least a LITTLE meaningful
look_up_patch = {'Maths': 'Mathematics'}

def safe_int(value, default=None):

    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_string(value, default=None):

    try:
        return value.strip().title()
    except (ValueError, TypeError, AttributeError):
        return default

def clean_data(r):

    records = {}

    for fields in r.split('|'):
        fields = fields.replace('=', ':')
        key, value = fields.split(':')

        records[key.strip().upper()] = value # upper/strip fixes keys, normalizing data

    # Every .get() filtered through helper function
    name = safe_string(records.get('NAME'))

    if not name:

        return {'ok': False,
                'field': 'name',
                'record': records,
                'reason': 'missing or invalid name'
                }

    grade = safe_string(records.get('GRADE'))

    if grade not in ['A','B','C','D','F']:

        return {'ok': False,
                'field': 'grade',
                'record': records,
                'reason': 'missing or invalid grade'
                }

    score = safe_int(records.get('SCORE'))

    if score is None:

        return {'ok': False,
                'field': 'score',
                'record': records,
                'reason': 'missing or invalid score'
                }

    subject = safe_string(records.get('SUBJECT'))

    if subject in look_up_patch: # patch maths to mathamatics
        subject = look_up_patch[subject]

    if not subject:

        return {'ok': False,
                'field': 'subject',
                'record': records,
                'reason': 'missing or invalid subject'
                }

    return {'ok': True,
            'data': {'name': name,
                    'grade': grade,
                    'score': score,
                    'subject': subject
                    }
                }

def calculate_sub_av(cleaned):

    sub_av = defaultdict(list)

    for data in cleaned:

        subject = data['subject']
        score = data['score']

        sub_av[subject].append(score)

    return sub_av

def print_data(cleaned, subject_average, errors):

    print('=' * 40)
    print("STUDENT GRADES".center(40))
    print('=' * 40)
    print()

    col1, col2 = 16, 6 # idk how to do this cleaner

    print("Names".ljust(col1) + "Grade".ljust(col2) + "Score".ljust(col2) + "Subject")
    print(("-" * 5).ljust(col1) + ("-" * 5).ljust(col2) + ("-" * 5).ljust(col2) + ("-" * 7)) # <- big and ugly

    # clumsy way to calculate average bc im dumb
    total = 0
    num_of_scores = 0

    for data in cleaned:

        name = data['name']
        grade = data['grade']
        score = data['score']
        subject = data['subject']

        print(f"{name:<16}{grade:<6}{score:<6}{subject}")

        total += score
        num_of_scores += 1

    average = total / num_of_scores

    print()

    print(f"Class average: {average:.2f}")


    print()
    print('=' * 40)
    print("AVERAGE PER SUBJECT".center(40))
    print('=' * 40)
    print()

    for subject, scores in subject_average.items():

        print(f"{subject:<14}{sum(scores) / len(scores)}")

    print()


    print('=' * 40)
    print("ERRORS".center(40))
    print('=' * 40)
    print()

    for i, e in enumerate(errors, start = 1):

        field = e['field']
        reason = e['reason']
        record = e['record']

        print(f"Error {i}:")
        print(f"Field: {field}")
        print(f"Reason: {reason}")
        print(f"Record: {record}\n")


    print('=' * 40)
    print("PROGRAM FINISHED".center(40))
    print('=' * 40)
    print()

def main():

    # somehow my list comprehension skills are gone so now this is ugly and chunky
    cleaned = []
    errors = []

    for r in report.splitlines():

        result = clean_data(r)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    subject_average = calculate_sub_av(cleaned)

    print_data(cleaned, subject_average, errors)

main()
