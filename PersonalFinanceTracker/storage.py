import json

TRANSACTIONS_FILE = "transactions.json"
BUDGETS_FILE = "budgets.json"


def save_data(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return True

    except OSError:
        print("მონაცემების შენახვისას მოხდა შეცდომა.")
        return False


def load_data(filename, default):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return default

    except json.JSONDecodeError:
        print("JSON ფაილის ფორმატი არასწორია.")
        return default

    except OSError:
        print("ფაილის წაკითხვისას მოხდა შეცდომა.")
        return default


def save_transactions(transactions):
    return save_data(TRANSACTIONS_FILE, transactions)


def load_transactions():
    return load_data(TRANSACTIONS_FILE, [])


def save_budgets(budgets):
    return save_data(BUDGETS_FILE, budgets)


def load_budgets():
    return load_data(BUDGETS_FILE, {})