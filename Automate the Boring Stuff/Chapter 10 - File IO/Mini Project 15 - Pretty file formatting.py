
from pathlib import Path

students = [
    {"name": "Aiko Tanaka", "subject": "Math", "score": 92},
    {"name": "Liam O'Connor", "subject": "Math", "score": 78},
    {"name": "Priya Sharma", "subject": "Science", "score": 88},
    {"name": "Diego Fernandez", "subject": "Science", "score": 95},
    {"name": "Wei Chen", "subject": "History", "score": 67},
]

base = Path.home() / "Documents" / "python_sandbox"
report = base / "report.txt"

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


def write_report(students, report):

    total = 0
    score_count = 0

    title = "STUDENT REPORT"
    with open(report, 'w', encoding='utf-8') as f:

        print(title, file=f)
        print("=" * len(title), file=f)
        print(file=f)
        print(f"{'Name':<20}{'Subject':<12}{'score':>8}", file=f)
        print('-' * 40, file=f)

        for s in students:

            name = safe_string(s.get("name"))

            if name is None:
                continue

            subject = safe_string(s.get("subject"))

            if subject is None:
                continue

            score = safe_int(s.get("score"))

            if score is None:
                continue

            total += score
            score_count += 1

            print(f"{name:<20}{subject:<12}{score:>8}", file=f)

        average = total / score_count if score_count else 0

        print('-' * 40, file=f)
        print(f"Average score: {average:.1f}", file=f)

write_report(students, report)

