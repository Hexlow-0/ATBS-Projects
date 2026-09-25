
import statistics as stats




# =================================
# PART ONE - CALCULATE AVERAGES
# =================================

def find_average(students):

    averages = {}

    for student, scores in students.items():

        average = stats.mean(scores)

        averages[student] = average

    return averages

# =================================
# SET GRADE BASED ON AVERAGES
# =================================

def set_grade(averages):

    grades = {}

    for student, average in averages.items():

        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'

        grades[student] = grade


    return grades

# =================================
# SET STATUS BASED ON AVERAGES
# =================================

def set_status(averages):

    statuses = {}

    for student, average in averages.items():

        if average >= 60:
            status = 'Pass'
        else:
            status = 'FAIL'

        statuses[student] = status

    return statuses

# =================================
# CALCULATE THE CLASS AVERAGE
# =================================

def calculate_class_average(averages):

    average = stats.mean(averages.values())

    return average

# =================================
# CALCULATE THE TOP STUDENT
# =================================

def calculate_top_student(averages):

    best_student, highest_average = max(averages.items(), key=lambda x: x[1])

    return best_student, highest_average

# =================================
# CALCULATE THE WORST STUDENT
# =================================

def calculate_lowest_student(averages):

    lowest_student, lowest_average = min(averages.items(), key=lambda x: x[1])

    return lowest_student, lowest_average

# =================================
# PRINT THE SUMMARY
# =================================

def summary(averages, student_grades, student_status, class_average, best_student, highest_average, lowest_student, lowest_average):

    print("=" * 40)
    print("GRADE REPORT".center(40))
    print("=" * 40)
    print()

    for student, average in averages.items():

        grade = student_grades[student]
        status = student_status[student]

        print(f"{student} | Avg: {average:.1f} |\t Grade: {grade} | Status: {status}")

    print()

    print("=" * 40)
    print(f"Class average: {class_average}")
    print(f"Top student: {best_student} ({highest_average})")
    print(f"Struggling: {lowest_student} ({lowest_average})")
    print("=" * 40)
    print()

# =================================
# MAIN FUNCTION TO POWER PROGRAM
# =================================

def main():

    students = {
    "Alice": [88, 92, 79, 95, 83],
    "Bob":   [70, 65, 80, 72, 68],
    "Carol": [95, 98, 100, 92, 97],
    "David": [55, 60, 58, 62, 57],
    "Emma":  [78, 82, 80, 85, 79]
}


    averages = find_average(students)
    student_grades = set_grade(averages)
    student_status = set_status(averages)
    class_average = calculate_class_average(averages)
    best_student, highest_average = calculate_top_student(averages)
    lowest_student, lowest_average = calculate_lowest_student(averages)

    summary(averages, student_grades, student_status, class_average, best_student, highest_average, lowest_student, lowest_average)


main()
