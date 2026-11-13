class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        print("სახელი:", self.name)
        print("გვარი:", self.surname)
        print("ასაკი:", self.age)


class Student(Person):
    def __init__(self, name, surname, age, roll_number, course):
        super().__init__(name, surname, age)

        self.roll_number = roll_number
        self.course = course
        self._grades = []

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, new_grades):
        if not isinstance(new_grades, list):
            raise ValueError("შეფასებები უნდა იყოს სიაში!")

        for grade in new_grades:
            if type(grade) != int or grade < 0 or grade > 100:
                raise ValueError("შეფასება უნდა იყოს 0-დან 100-მდე!")

        self._grades = new_grades

    def get_average(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def show_info(self):
        print("სტუდენტის ნომერი:", self.roll_number)

        super().show_info()

        print("კურსი:", self.course)
        print("შეფასებები:", self.grades)

        if self.grades:
            print("საშუალო შეფასება:", round(self.get_average(), 2))
        else:
            print("საშუალო შეფასება: შეფასებები არ აქვს")

        print("-" * 45)
