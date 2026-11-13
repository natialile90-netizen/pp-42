import json
import os

from student import Student


class Storage:
    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "students.json"
        )

    def save_students(self, students):
        try:
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

            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            print("მონაცემები წარმატებით შეინახა!")
            return True

        except (OSError, TypeError, ValueError) as error:
            print("მონაცემების შენახვის შეცდომა:", error)
            return False

    def load_students(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON ფაილში უნდა იყოს სია!")

            loaded_students = []

            for index, student_data in enumerate(data, 1):
                roll_number = student_data.get("roll_number")

                if not roll_number:
                    roll_number = "OLD-" + str(index)

                course = student_data.get(
                    "course",
                    "არ არის არჩეული"
                )

                student = Student(
                    student_data["name"],
                    student_data["surname"],
                    student_data["age"],
                    str(roll_number),
                    course
                )

                student.grades = student_data.get("grades", [])

                loaded_students.append(student)

            print("მონაცემები წარმატებით ჩაიტვირთა!")
            return loaded_students

        except FileNotFoundError:
            print("შენახული მონაცემები არ მოიძებნა!")
            return []

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
            AttributeError,
            OSError
        ) as error:
            print("მონაცემების ჩატვირთვის შეცდომა:", error)
            return None
