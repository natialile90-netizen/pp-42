class Payment:
    def process_payment (self, amount):
       print ("Payment is being processed...")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"Credit Card Payment: {amount} GEL")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print (f"Pay Pal Payment: {amount} GEL")

credit_card =CreditCardPayment()
paypal =PayPalPayment()

amount = float(input("Enter payment amount: "))

credit_card.process_payment(amount)
paypal.process_payment(amount)