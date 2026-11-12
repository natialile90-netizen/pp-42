from student_manager import find_student
from validation import validate_grade


def add_grade():
    roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()
    student = find_student(roll_number)

    if not student:
        print("სტუდენტი ვერ მოიძებნა!")
        return

    grade = input("შეიყვანეთ შეფასება (0-100): ")

    if not validate_grade(grade):
        print("შეფასება უნდა იყოს 0-დან 100-მდე!")
        return

    student.grades.append(int(grade))

    from storage import save_students
    save_students()

    print("შეფასება წარმატებით დაემატა!")


def grade_category(grade):
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


def average_grade():
    roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()
    student = find_student(roll_number)

    if not student:
        print("სტუდენტი ვერ მოიძებნა!")
        return

    if not student.grades:
        print("სტუდენტს შეფასებები არ აქვს!")
        return

    average = sum(student.grades) / len(student.grades)

    print("სტუდენტი:", student.name, student.surname)
    print("კურსი:", student.course)
    print("შეფასებები:", student.grades)
    print("საშუალო შეფასება:", round(average, 2))
    print("შედეგი:", grade_category(average))

    if average >= 51:
        print("სტატუსი: ჩაბარებული")
    else:
        print("სტატუსი: ჩაჭრილი")


def edit_grade():
    roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()
    student = find_student(roll_number)

    if not student:
        print("სტუდენტი ვერ მოიძებნა!")
        return

    if not student.grades:
        print("სტუდენტს შეფასებები არ აქვს!")
        return

    for index, grade in enumerate(student.grades, 1):
        print(index, "-", grade)

    choice = input("აირჩიეთ შესაცვლელი შეფასების ნომერი: ")

    if not choice.isdigit():
        print("არასწორი ნომერი!")
        return

    choice = int(choice)

    if choice < 1 or choice > len(student.grades):
        print("არასწორი ნომერი!")
        return

    new_grade = input("შეიყვანეთ ახალი შეფასება (0-100): ")

    if not validate_grade(new_grade):
        print("შეფასება უნდა იყოს 0-დან 100-მდე!")
        return

    student.grades[choice - 1] = int(new_grade)

    from storage import save_students
    save_students()

    print("შეფასება წარმატებით შეიცვალა!")


def delete_grade():
    roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()
    student = find_student(roll_number)

    if not student:
        print("სტუდენტი ვერ მოიძებნა!")
        return

    if not student.grades:
        print("სტუდენტს შეფასებები არ აქვს!")
        return

    for index, grade in enumerate(student.grades, 1):
        print(index, "-", grade)

    choice = input("აირჩიეთ წასაშლელი შეფასების ნომერი: ")

    if not choice.isdigit():
        print("არასწორი ნომერი!")
        return

    choice = int(choice)

    if choice < 1 or choice > len(student.grades):
        print("არასწორი ნომერი!")
        return

    student.grades.pop(choice - 1)

    from storage import save_students
    save_students()

    print("შეფასება წარმატებით წაიშალა!")
