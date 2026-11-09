from student import Student
from validation import validate_name, validate_age

students = []


def find_student(name):
    for student in students:
        if student.name.lower() == name.strip().lower():
            return student
    return None


def add_student():
    name = input("Enter student name: ").strip()
    surname = input("Enter student surname: ").strip()
    age = input("Enter student age: ")

    if not validate_name(name) or not validate_name(surname):
        print("Invalid name or surname!")
        return

    if not validate_age(age):
        print("Invalid age! Enter a number between 6 and 100.")
        return

    student = Student(name, surname, int(age))
    students.append(student)
    print("Student added successfully!")


def show_students():
    if not students:
        print("No students found!")
        return

    for student in students:
        print(
            "Name:", student.name,
            "| Surname:", student.surname,
            "| Age:", student.age,
            "| Grades:", student.grades
        )


def search_student():
    name = input("Enter student name to search: ")
    student = find_student(name)

    if student:
        print("Name:", student.name)
        print("Surname:", student.surname)
        print("Age:", student.age)
        print("Grades:", student.grades)
    else:
        print("Student not found!")


def delete_student():
    name = input("Enter student name to delete: ")
    student = find_student(name)

    if student:
        students.remove(student)
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def update_student():
    name = input("Enter student name to update: ")
    student = find_student(name)

    if not student:
        print("Student not found!")
        return

    new_name = input("Enter new name: ").strip()
    new_surname = input("Enter new surname: ").strip()
    new_age = input("Enter new age: ")

    if not validate_name(new_name) or not validate_name(new_surname):
        print("Invalid name or surname!")
        return

    if not validate_age(new_age):
        print("Invalid age! Enter a number between 6 and 100.")
        return

    student.name = new_name
    student.surname = new_surname
    student.age = int(new_age)

    print("Student updated successfully!")
