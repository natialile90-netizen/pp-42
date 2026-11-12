import json
import os

from student import Student
from student_manager import students


FILE_PATH = os.path.join(
    os.path.dirname(__file__), "students.json"
)


def save_students():
    data = []

    for student in students:
        student_data = {
            "name": student.name,
            "surname": student.surname,
            "age": student.age,
            "roll_number": student.roll_number,
            "course": student.course,
            "grades": student.grades
        }

        data.append(student_data)

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("სტუდენტების მონაცემები წარმატებით შეინახა!")


def load_students():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        loaded_students = []

        for index, student_data in enumerate(data, start=1):
            roll_number = student_data.get("roll_number")

            if not roll_number:
                roll_number = "OLD-" + str(index)

            course = student_data.get("course", "არ არის არჩეული")

            student = Student(
                student_data["name"],
                student_data["surname"],
                student_data["age"],
                str(roll_number),
                course
            )

            student.grades = student_data.get("grades", [])
            loaded_students.append(student)

        students.clear()

        for student in loaded_students:
            students.append(student)

        print("სტუდენტების მონაცემები წარმატებით ჩაიტვირთა!")

    except FileNotFoundError:
        print("შენახული მონაცემები არ მოიძებნა!")

    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("შენახული მონაცემები არასწორია!")
