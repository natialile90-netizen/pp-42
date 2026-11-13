from validation import Validation


class GradeManager:
    def __init__(self, student_manager):
        self.student_manager = student_manager
        self.validation = Validation()

    def add_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        grade = input("შეიყვანეთ შეფასება (0-100): ").strip()

        if not self.validation.validate_grade(grade):
            print("შეფასება უნდა იყოს 0-დან 100-მდე!")
            return

        try:
            student.grades.append(int(grade))

            if self.student_manager.save():
                print("შეფასება წარმატებით დაემატა!")
            else:
                print("შეფასება დაემატა, მაგრამ ფაილში ვერ შეინახა!")

        except (ValueError, TypeError) as error:
            print("შეფასების დამატების შეცდომა:", error)

    def grade_category(self, grade):
        if grade >= 91:
            return "შესანიშნავი"
        elif grade >= 81:
            return "ძალიან კარგი"
        elif grade >= 71:
            return "კარგი"
        elif grade >= 61:
            return "დამაკმაყოფილებელი"
        elif grade >= 51:
            return "ჩაბარებული"
        else:
            return "არადამაკმაყოფილებელი"

    def average_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        if not student.grades:
            print("სტუდენტს შეფასებები არ აქვს!")
            return

        try:
            average = student.get_average()

            print("სტუდენტი:", student.name, student.surname)
            print("კურსი:", student.course)
            print("შეფასებები:", student.grades)
            print("საშუალო შეფასება:", round(average, 2))
            print("შედეგი:", self.grade_category(average))

            if average >= 51:
                print("სტატუსი: ჩაბარებული")
            else:
                print("სტატუსი: ჩაჭრილი")

        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("საშუალო შეფასების გამოთვლის შეცდომა:", error)

    def edit_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        if not student.grades:
            print("სტუდენტს შეფასებები არ აქვს!")
            return

        for index, grade in enumerate(student.grades, 1):
            print(index, "-", grade)

        choice = input(
            "აირჩიეთ შესაცვლელი შეფასების ნომერი: "
        ).strip()

        if not choice.isdigit():
            print("არასწორი ნომერი!")
            return

        choice = int(choice)

        if choice < 1 or choice > len(student.grades):
            print("არასწორი ნომერი!")
            return

        new_grade = input(
            "შეიყვანეთ ახალი შეფასება (0-100): "
        ).strip()

        if not self.validation.validate_grade(new_grade):
            print("შეფასება უნდა იყოს 0-დან 100-მდე!")
            return

        try:
            student.grades[choice - 1] = int(new_grade)

            if self.student_manager.save():
                print("შეფასება წარმატებით შეიცვალა!")
            else:
                print("შეფასება შეიცვალა, მაგრამ ფაილში ვერ შეინახა!")

        except (ValueError, TypeError, IndexError) as error:
            print("შეფასების შეცვლის შეცდომა:", error)

    def delete_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        if not student.grades:
            print("სტუდენტს შეფასებები არ აქვს!")
            return

        for index, grade in enumerate(student.grades, 1):
            print(index, "-", grade)

        choice = input(
            "აირჩიეთ წასაშლელი შეფასების ნომერი: "
        ).strip()

        if not choice.isdigit():
            print("არასწორი ნომერი!")
            return

        choice = int(choice)

        if choice < 1 or choice > len(student.grades):
            print("არასწორი ნომერი!")
            return

        try:
            student.grades.pop(choice - 1)

            if self.student_manager.save():
                print("შეფასება წარმატებით წაიშალა!")
            else:
                print("შეფასება წაიშალა, მაგრამ ფაილში ვერ შეინახა!")

        except (IndexError, TypeError) as error:
            print("შეფასების წაშლის შეცდომა:", error)
