from student_manager import (
    add_student,
    show_students,
    search_student,
    delete_student,
    update_student
)

from grades import add_grade, average_grade
from storage import save_students, load_students


def main():
    load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Add Grade")
        print("7. Average Grade")
        print("8. Save Students")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            update_student()

        elif choice == "6":
            add_grade()

        elif choice == "7":
            average_grade()

        elif choice == "8":
            save_students()

        elif choice == "0":
            save_students()
            print("Goodbye!")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
