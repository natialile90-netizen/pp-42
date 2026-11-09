from student_manager import find_student
from validation import validate_grade


def add_grade():
    name = input("Enter student name: ")
    student = find_student(name)

    if not student:
        print("Student not found!")
        return

    grade = input("Enter grade (0-100): ")

    if not validate_grade(grade):
        print("Invalid grade! Enter a number between 0 and 100.")
        return

    student.grades.append(int(grade))
    print("Grade added successfully!")


def grade_category(grade):
    if grade >= 91:
        return "Excellent"
    elif grade >= 81:
        return "Very Good"
    elif grade >= 71:
        return "Good"
    elif grade >= 61:
        return "Satisfactory"
    elif grade >= 51:
        return "Pass"
    else:
        return "Fail"


def average_grade():
    name = input("Enter student name: ")
    student = find_student(name)

    if not student:
        print("Student not found!")
        return

    if not student.grades:
        print("Student has no grades!")
        return

    average = sum(student.grades) / len(student.grades)

    print("Grades:", student.grades)
    print("Average Grade:", round(average, 2))
    print("Performance:", grade_category(average))

    if average >= 51:
        print("Status: Passed")
    else:
        print("Status: Failed")
