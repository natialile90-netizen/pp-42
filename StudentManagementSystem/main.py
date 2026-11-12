from student_manager import (
    add_student,
    show_students,
    search_student,
    delete_student,
    update_student,
    show_students_by_course,
    total_students,
    top_student,
    course_statistics
)

from grades import (
    add_grade,
    average_grade,
    edit_grade,
    delete_grade
)

from storage import save_students, load_students


def show_result(title, function):
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)

    function()

    print("=" * 45 + "\n")


def main():
    load_students()

    while True:
        print("\n===== IT აკადემიის მართვის სისტემა =====")
        print("1. სტუდენტის დამატება")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. სტუდენტის ძებნა")
        print("4. სტუდენტის წაშლა")
        print("5. სტუდენტის მონაცემების შეცვლა")
        print("6. შეფასების დამატება")
        print("7. საშუალო შეფასების ნახვა")
        print("8. სტუდენტების ნახვა კურსის მიხედვით")
        print("9. შეფასების შეცვლა")
        print("10. შეფასების წაშლა")
        print("11. სტუდენტების საერთო რაოდენობა")
        print("12. საუკეთესო სტუდენტი")
        print("13. კურსების სტატისტიკა")
        print("0. გამოსვლა")

        choice = input("აირჩიეთ მოქმედება: ")

        if choice == "1":
            show_result("სტუდენტის დამატება", add_student)

        elif choice == "2":
            show_result("სტუდენტების სია", show_students)

        elif choice == "3":
            show_result("სტუდენტის ძებნა", search_student)

        elif choice == "4":
            show_result("სტუდენტის წაშლა", delete_student)

        elif choice == "5":
            show_result("სტუდენტის განახლება", update_student)

        elif choice == "6":
            show_result("შეფასების დამატება", add_grade)

        elif choice == "7":
            show_result("საშუალო შეფასება", average_grade)

        elif choice == "8":
            show_result("სტუდენტები კურსის მიხედვით", show_students_by_course)

        elif choice == "9":
            show_result("შეფასების შეცვლა", edit_grade)

        elif choice == "10":
            show_result("შეფასების წაშლა", delete_grade)

        elif choice == "11":
            show_result("სტუდენტების რაოდენობა", total_students)

        elif choice == "12":
            show_result("საუკეთესო სტუდენტი", top_student)

        elif choice == "13":
            show_result("კურსების სტატისტიკა", course_statistics)

        elif choice == "0":
            show_result("მონაცემების შენახვა", save_students)
            print("ნახვამდის!")
            break

        else:
            print("\n" + "=" * 45)
            print("არასწორი არჩევანი! სცადეთ თავიდან.")
            print("=" * 45)


if __name__ == "__main__":
    main()