from datetime import datetime


def read_amount(message="შეიყვანეთ თანხა: "):
    while True:
        try:
            amount = float(input(message))

            if amount > 0:
                return amount

            print("თანხა უნდა იყოს ნულზე მეტი.")

        except ValueError:
            print("შეიყვანეთ სწორი რიცხვი.")


def read_text(message):
    while True:
        text = input(message).strip()

        if text:
            return text

        print("ველი არ უნდა იყოს ცარიელი.")


def read_number(message, minimum, maximum):
    while True:
        try:
            number = int(input(message))

            if minimum <= number <= maximum:
                return number

            print("აირჩიეთ რიცხვი", minimum, "-დან", maximum, "-მდე.")

        except ValueError:
            print("შეიყვანეთ მთელი რიცხვი.")


def read_date():
    while True:
        date = input("შეიყვანეთ თარიღი (დღე.თვე.წელი): ")

        try:
            valid_date = datetime.strptime(date, "%d.%m.%Y")
            return valid_date.strftime("%Y-%m-%d")

        except ValueError:
            print("თარიღის არასწორი ფორმატი.")


def read_month():
    while True:
        month = input("შეიყვანეთ თვე (თვე.წელი): ")

        try:
            valid_month = datetime.strptime(month, "%m.%Y")
            return valid_month.strftime("%m.%Y")

        except ValueError:
            print("თვე არასწორად არის მითითებული.")


def read_type():
    while True:
        print("1. შემოსავალი")
        print("2. გასავალი")

        choice = input("აირჩიეთ ტიპი: ")

        if choice == "1":
            return "income"

        elif choice == "2":
            return "expense"

        print("არასწორი არჩევანი.")


def type_name(transaction_type):
    if transaction_type == "income":
        return "შემოსავალი"

    elif transaction_type == "expense":
        return "გასავალი"

    return transaction_type


def normalize_date(date):
    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d")
        return valid_date.strftime("%d.%m.%Y")

    except ValueError:
        return date