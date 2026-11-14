from datetime import datetime
from finance_manager import FinanceManager
from validation import read_amount, read_text, read_number, read_date, read_month, read_type, type_name, normalize_date


def clear_screen():
    print("\n" * 40)


def pause():
    input("\nდააჭირეთ Enter-ს მთავარ მენიუში დასაბრუნებლად...")


def heading(title):
    print("=" * 48)
    print(title)
    print("=" * 48)


def show_transactions(transactions):
    if not transactions:
        print("ტრანზაქციები ვერ მოიძებნა.")
        return

    for number, transaction in enumerate(transactions, start=1):
        print("-" * 40)
        print("ნომერი:", number)
        print("თანხა:", transaction.amount, "ლარი")
        print("კატეგორია:", transaction.category)
        print("ტიპი:", type_name(transaction.transaction_type))
        print("თარიღი:", normalize_date(transaction.date))
        print("კომენტარი:", transaction.comment)


def show_summary(manager, transactions=None):
    income, expense, balance = manager.summary(transactions)
    print("შემოსავალი:", income, "ლარი")
    print("გასავალი:", expense, "ლარი")
    print("ბალანსი:", balance, "ლარი")


def show_budget_warning(manager, category):
    limit = manager.budget_for(category)

    if limit is None:
        return

    month = datetime.now().strftime("%m.%Y")
    spent = manager.category_expense_for_month(category, month)

    print("\nკატეგორიის თვიური ლიმიტი:", limit, "ლარი")
    print("ამ თვეში დახარჯულია:", spent, "ლარი")

    if spent > limit:
        print("გაფრთხილება! ლიმიტს გადააჭარბეთ",
              round(spent - limit, 2), "ლარით.")
    else:
        print("დარჩენილი ლიმიტი:",
              round(limit - spent, 2), "ლარი")


def add_transaction(manager, transaction_type):
    heading("ტრანზაქციის დამატება")

    amount = read_amount()
    category = read_text("შეიყვანეთ კატეგორია: ")
    comment = input("შეიყვანეთ კომენტარი (არასავალდებულო): ").strip()

    if manager.add_transaction(amount, category, transaction_type, comment):
        print("ტრანზაქცია წარმატებით დაემატა!")
        print("თარიღი:", datetime.now().strftime("%d.%m.%Y"))

        if transaction_type == "expense":
            show_budget_warning(manager, category)
    else:
        print("ტრანზაქცია ვერ შეინახა.")


def filter_menu(manager):
    heading("ტრანზაქციების გაფილტვრა")

    print("1. კატეგორიით")
    print("2. თარიღით")
    print("3. ტიპით")

    choice = read_number("აირჩიეთ: ", 1, 3)

    if choice == 1:
        category = read_text("კატეგორია: ")
        result = manager.filter_transactions(category=category)

    elif choice == 2:
        date = read_date()
        result = manager.filter_transactions(date=date)

    else:
        transaction_type = read_type()
        result = manager.filter_transactions(
            transaction_type=transaction_type
        )

    show_transactions(result)


def edit_transaction(manager):
    heading("ტრანზაქციის რედაქტირება")
    show_transactions(manager.transactions)

    if not manager.transactions:
        return

    number = read_number(
        "შეიყვანეთ შესაცვლელი ნომერი: ",
        1,
        len(manager.transactions)
    )

    old = manager.transactions[number - 1]

    print("ახალი მონაცემები (ტიპი და თარიღი უცვლელი დარჩება)")

    amount = read_amount("ახალი თანხა: ")
    category = read_text("ახალი კატეგორია: ")
    comment = input("ახალი კომენტარი: ").strip()

    if manager.update_transaction(number - 1, amount, category, comment):
        print("ტრანზაქცია განახლდა!")

        if old.transaction_type == "expense":
            show_budget_warning(manager, category)
    else:
        print("ცვლილება ვერ შეინახა.")


def delete_transaction(manager):
    heading("ტრანზაქციის წაშლა")
    show_transactions(manager.transactions)

    if not manager.transactions:
        return

    number = read_number(
        "შეიყვანეთ წასაშლელი ნომერი: ",
        1,
        len(manager.transactions)
    )

    answer = input(
        "ნამდვილად გსურთ წაშლა? (დიახ/არა): "
    ).strip().lower()

    if answer == "დიახ":
        if manager.delete_transaction(number - 1):
            print("ტრანზაქცია წაიშალა.")
        else:
            print("წაშლა ვერ შეინახა.")
    else:
        print("წაშლა გაუქმდა.")


def budget_menu(manager):
    heading("კატეგორიის თვიური ლიმიტი")

    category = read_text("კატეგორია: ")
    amount = read_amount("ლიმიტი ლარებში: ")

    if manager.set_budget(category, amount):
        print("ლიმიტი წარმატებით შეინახა!")
        show_budget_warning(manager, category)
    else:
        print("ლიმიტი ვერ შეინახა.")


def show_budgets(manager):
    heading("კატეგორიების თვიური ლიმიტები")

    if not manager.budgets:
        print("ლიმიტები ჯერ არ არის დაყენებული.")
        return

    month = datetime.now().strftime("%m.%Y")

    for category, limit in manager.budgets.items():
        spent = manager.category_expense_for_month(category, month)

        print("-" * 40)
        print("კატეგორია:", category)
        print("ლიმიტი:", limit, "ლარი")
        print("დახარჯულია:", spent, "ლარი")

        if spent > limit:
            print("გადაჭარბება:",
                  round(spent - limit, 2), "ლარი")
        else:
            print("დარჩენილია:",
                  round(limit - spent, 2), "ლარი")


def monthly_summary(manager):
    heading("თვიური შეჯამება")

    month = read_month()
    show_summary(manager, manager.monthly_transactions(month))


def category_summary(manager):
    heading("კატეგორიების მიხედვით შეჯამება")

    totals = manager.category_summary()

    if not totals:
        print("მონაცემები არ არის.")

    for category, amounts in totals.items():
        print("-" * 40)
        print("კატეგორია:", category)
        print("შემოსავალი:",
              round(amounts["income"], 2), "ლარი")
        print("გასავალი:",
              round(amounts["expense"], 2), "ლარი")


def show_menu():
    heading("პირადი ფინანსების მართვის სისტემა")

    print("1. შემოსავლის დამატება")
    print("2. გასავლის დამატება")
    print("3. ყველა ტრანზაქციის ნახვა")
    print("4. ტრანზაქციების გაფილტვრა")
    print("5. ბალანსის ნახვა")
    print("6. კატეგორიების მიხედვით შეჯამება")
    print("7. თვიური შეჯამება")
    print("8. ტრანზაქციის წაშლა")
    print("9. ტრანზაქციის რედაქტირება")
    print("10. კატეგორიის ლიმიტის დაყენება")
    print("11. ლიმიტების ნახვა")
    print("0. პროგრამიდან გასვლა")


def main():
    try:
        manager = FinanceManager()

    except (ValueError, KeyError, TypeError, OSError) as error:
        print("მონაცემების ჩატვირთვა ვერ მოხერხდა:", error)
        return

    while True:
        clear_screen()
        show_menu()

        choice = read_number("აირჩიეთ მოქმედება: ", 0, 11)

        if choice == 0:
            print("ნახვამდის!")
            break

        clear_screen()

        if choice == 1:
            add_transaction(manager, "income")

        elif choice == 2:
            add_transaction(manager, "expense")

        elif choice == 3:
            heading("ყველა ტრანზაქცია")
            show_transactions(manager.transactions)

        elif choice == 4:
            filter_menu(manager)

        elif choice == 5:
            heading("მიმდინარე ბალანსი")
            show_summary(manager)

        elif choice == 6:
            category_summary(manager)

        elif choice == 7:
            monthly_summary(manager)

        elif choice == 8:
            delete_transaction(manager)

        elif choice == 9:
            edit_transaction(manager)

        elif choice == 10:
            budget_menu(manager)

        elif choice == 11:
            show_budgets(manager)

        pause()


if __name__ == "__main__":
    main()