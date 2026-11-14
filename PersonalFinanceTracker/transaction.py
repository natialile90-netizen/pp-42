from datetime import datetime


class Transaction:
    def __init__(self, amount, category, transaction_type, date=None, comment=""):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type

        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = date

        self.comment = comment

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type,
            "date": self.date,
            "comment": self.comment
        }