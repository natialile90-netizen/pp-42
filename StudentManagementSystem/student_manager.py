from student import Student
from validation import validate_name, validate_age, validate_roll_number

students = []

courses = ["Python", "C#", "JavaScript", "Java", "C++"]


def find_student(roll_number):
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None


def choose_course():
    print("\n===== პროგრამირების კურსები =====")

    for index, course in enumerate(courses, 1):
        print(index, "-", course)

    choice = input("აირჩიეთ კურსი (1-5): ").strip()

    if not choice.isdigit():
        print("კურსის ნომერი არასწორია!")
        return None

    choice = int(choice)

    if 1 <= choice <= 5:
        return courses[choice - 1]

    print("კურსის ნომერი არასწორია!")
    return None


def print_student(student):
    if student.grades:
        average = round(sum(student.grades) / len(student.grades), 2)
    else:
        average = "შეფასებები არ აქვს"

    print("სტუდენტის ნომერი:", student.roll_number)
    print("სახელი:", student.name)
    print("გვარი:", student.surname)
    print("ასაკი:", student.age)
    print("კურსი:", student.course)
    print("შეფასებები:", student.grades)
    print("საშუალო შეფასება:", average)
    print("-" * 45)


def add_student():
    name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()
    surname = input("შეიყვანეთ სტუდენტის გვარი: ").strip()
    age = input("შეიყვანეთ ასაკი: ")
    roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()

    if not validate_name(name) or not validate_name(surname):
        print("სახელი ან გვარი არასწორია!")
        return

    if not validate_age(age):
        print("ასაკი უნდა იყოს 16-დან 70 წლამდე!")
        return

    if not validate_roll_number(roll_number):
        print("სტუდენტის ნომერი არ შეიძლება იყოს ცარიელი!")
        return

    if find_student(roll_number):
        print("სტუდენტი ამ ნომრით უკვე არსებობს!")
        return

    course = choose_course()

    if course is None:
        return

    student = Student(
        name, surname, int(age), roll_number, course
    )

    students.append(student)

    from storage import save_students
    save_students()

    print("სტუდენტი წარმატებით დაემატა!")


def show_students():
    if not students:
        print("სტუდენტები არ მოიძებნა!")
        return

    for student in students:
        print_student(student)


def search_student():
    roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()
    student = find_student(roll_number)

    if student:
        print_student(student)
    else:
        print("სტუდენტი ვერ მოიძებნა!")


def delete_student():
    roll_number = input("შეიყვანეთ წასაშლელი სტუდენტის ნომერი: ").strip()
    student = find_student(roll_number)

    if student:
        students.remove(student)

        from storage import save_students
        save_students()

        print("სტუდენტი წარმატებით წაიშალა!")
    else:
        print("სტუდენტი ვერ მოიძებნა!")


def update_student():
    roll_number = input("შეიყვანეთ სტუდენტის ნომერი: ").strip()
    student = find_student(roll_number)

    if not student:
        print("სტუდენტი ვერ მოიძებნა!")
        return

    new_name = input("შეიყვანეთ ახალი სახელი: ").strip()
    new_surname = input("შეიყვანეთ ახალი გვარი: ").strip()
    new_age = input("შეიყვანეთ ახალი ასაკი: ")

    if not validate_name(new_name) or not validate_name(new_surname):
        print("სახელი ან გვარი არასწორია!")
        return

    if not validate_age(new_age):
        print("ასაკი უნდა იყოს 16-დან 70 წლამდე!")
        return

    new_course = choose_course()

    if new_course is None:
        return

    student.name = new_name
    student.surname = new_surname
    student.age = int(new_age)
    student.course = new_course

    from storage import save_students
    save_students()

    print("სტუდენტის მონაცემები წარმატებით განახლდა!")


def show_students_by_course():
    course = choose_course()

    if course is None:
        return

    print("\n===== " + course + " - სტუდენტები =====")

    count = 0

    for student in students:
        if student.course == course:
            print_student(student)
            count += 1

    if count == 0:
        print("ამ კურსზე სტუდენტები არ მოიძებნა!")

    print("სტუდენტების რაოდენობა:", count)


def total_students():
    print("სტუდენტების საერთო რაოდენობა:", len(students))


def top_student():
    best_student = None
    highest_average = -1

    for student in students:
        if student.grades:
            average = sum(student.grades) / len(student.grades)

            if average > highest_average:
                highest_average = average
                best_student = student

    if best_student:
        print("საუკეთესო სტუდენტი:")
        print("სახელი:", best_student.name)
        print("გვარი:", best_student.surname)
        print("სტუდენტის ნომერი:", best_student.roll_number)
        print("კურსი:", best_student.course)
        print("შეფასებები:", best_student.grades)
        print("საშუალო შეფასება:", round(highest_average, 2))
    else:
        print("შეფასებული სტუდენტები არ მოიძებნა!")


def course_statistics():
    print("\n===== კურსების სტატისტიკა =====")

    for course in courses:
        count = 0

        for student in students:
            if student.course == course:
                count += 1

        print(course, "- სტუდენტების რაოდენობა:", count)

    print("სულ სტუდენტები:", len(students))