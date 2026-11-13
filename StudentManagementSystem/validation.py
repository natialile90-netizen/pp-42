class Validation:

    def validate_name(self, name):
        name = name.strip()

        if not name:
            return False

        return all(
            part.isalpha()
            for part in name.split()
        )

    def validate_age(self, age):
        if not age.isdigit():
            return False

        age = int(age)

        return 16 <= age <= 70

    def validate_roll_number(self, roll_number):
        return roll_number.isdigit()

    def validate_grade(self, grade):
        if not grade.isdigit():
            return False

        grade = int(grade)

        return 0 <= grade <= 100