from student import Student
from validation import Validation


class StudentManager:
    def __init__(self, storage):
        self.students = []
        self.courses = ["Python", "C#", "JavaScript", "Java", "C++"]
        self.validation = Validation()
        self.storage = storage

    def save(self):
        return self.storage.save_students(self.students)

    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student

        return None

    def choose_course(self):
        print("\n===== პროგრამირების კურსები =====")

        for index, course in enumerate(self.courses, 1):
            print(index, "-", course)

        choice = input("აირჩიეთ კურსი (1-5): ").strip()

        if not choice.isdigit():
            print("კურსის ნომერი არასწორია!")
            return None

        choice = int(choice)

        if 1 <= choice <= len(self.courses):
            return self.courses[choice - 1]

        print("კურსის ნომერი არასწორია!")
        return None

    def add_student(self):
        name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()
        surname = input("შეიყვანეთ სტუდენტის გვარი: ").strip()
        age = input("შეიყვანეთ ასაკი: ").strip()
        roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()

        if not self.validation.validate_name(name):
            print("სახელი არასწორია!")
            return

        if not self.validation.validate_name(surname):
            print("გვარი არასწორია!")
            return

        if not self.validation.validate_age(age):
            print("ასაკი უნდა იყოს 16-დან 70 წლამდე!")
            return

        if not self.validation.validate_roll_number(roll_number):
            print("სტუდენტის ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს!")
            return

        if self.find_student(roll_number):
            print("სტუდენტი ამ ნომრით უკვე არსებობს!")
            return

        course = self.choose_course()

        if course is None:
            return

        try:
            student = Student(
                name,
                surname,
                int(age),
                roll_number,
                course
            )

        except (ValueError, TypeError) as error:
            print("სტუდენტის შექმნის შეცდომა:", error)
            return

        self.students.append(student)

        if self.save():
            print("სტუდენტი წარმატებით დაემატა!")
        else:
            print("სტუდენტი დაემატა, მაგრამ ფაილში ვერ შეინახა!")

    def show_students(self):
        if not self.students:
            print("სტუდენტები არ მოიძებნა!")
            return

        for student in self.students:
            student.show_info()

    def search_student(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        student = self.find_student(roll_number)

        if student:
            student.show_info()
        else:
            print("სტუდენტი ვერ მოიძებნა!")

    def delete_student(self):
        roll_number = input(
            "შეიყვანეთ წასაშლელი სტუდენტის ნომერი: "
        ).strip()

        student = self.find_student(roll_number)

        if student:
            self.students.remove(student)

            if self.save():
                print("სტუდენტი წარმატებით წაიშალა!")
            else:
                print("სტუდენტი სიიდან წაიშალა, მაგრამ ფაილში ვერ შეინახა!")
        else:
            print("სტუდენტი ვერ მოიძებნა!")

    def update_student(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        student = self.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        new_name = input("შეიყვანეთ ახალი სახელი: ").strip()
        new_surname = input("შეიყვანეთ ახალი გვარი: ").strip()
        new_age = input("შეიყვანეთ ახალი ასაკი: ").strip()

        if not self.validation.validate_name(new_name):
            print("სახელი არასწორია!")
            return

        if not self.validation.validate_name(new_surname):
            print("გვარი არასწორია!")
            return

        if not self.validation.validate_age(new_age):
            print("ასაკი უნდა იყოს 16-დან 70 წლამდე!")
            return

        new_course = self.choose_course()

        if new_course is None:
            return

        try:
            student.name = new_name
            student.surname = new_surname
            student.age = int(new_age)
            student.course = new_course

        except (ValueError, TypeError) as error:
            print("მონაცემების განახლების შეცდომა:", error)
            return

        if self.save():
            print("სტუდენტის მონაცემები წარმატებით განახლდა!")
        else:
            print("მონაცემები შეიცვალა, მაგრამ ფაილში ვერ შეინახა!")

    def show_students_by_course(self):
        course = self.choose_course()

        if course is None:
            return

        print("\n=====", course, "- სტუდენტები =====")

        count = 0

        for student in self.students:
            if student.course == course:
                student.show_info()
                count += 1

        if count == 0:
            print("ამ კურსზე სტუდენტები არ მოიძებნა!")

        print("სტუდენტების რაოდენობა:", count)

    def total_students(self):
        print(
            "სტუდენტების საერთო რაოდენობა:",
            len(self.students)
        )

    def top_student(self):
        best_student = None
        highest_average = -1

        for student in self.students:
            if student.grades:
                average = student.get_average()

                if average > highest_average:
                    highest_average = average
                    best_student = student

        if best_student:
            print("საუკეთესო სტუდენტი:")
            best_student.show_info()
        else:
            print("შეფასებული სტუდენტები არ მოიძებნა!")

    def course_statistics(self):
        print("\n===== კურსების სტატისტიკა =====")

        for course in self.courses:
            count = 0

            for student in self.students:
                if student.course == course:
                    count += 1

            print(
                course,
                "- სტუდენტების რაოდენობა:",
                count
            )

        print("სულ სტუდენტები:", len(self.students))
