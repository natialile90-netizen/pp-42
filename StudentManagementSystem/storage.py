import json
from pathlib import Path

from student import Student
from student_manager import students


FILE_PATH = Path(__file__).with_name("students.json")


def save_students():
    data = []

    for student in students:
        student_data = {
            "name": student.name,
            "surname": student.surname,
            "age": student.age,
            "grades": student.grades
        }
        data.append(student_data)

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Students saved successfully!")


def load_students():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        students.clear()

        for student_data in data:
            student = Student(
                student_data["name"],
                student_data["surname"],
                student_data["age"]
            )

            student.grades = student_data.get("grades", [])
            students.append(student)

        print("Students loaded successfully!")

    except FileNotFoundError:
        print("No saved students found!")

    except json.JSONDecodeError:
        print("Saved file is empty or invalid!")
