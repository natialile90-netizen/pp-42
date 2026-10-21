class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity > 0 and quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold {quantity} {self.name}, remaining: {self.stock}")
        else:
            print("Not enough stock or invalid quantity")


name = input("Enter product name: ")
price = float(input("Enter price: "))
stock = int(input("Enter stock: "))

product1 = Product(name, price, stock)

quantity = int(input("Enter quantity to sell: "))
product1.sell(quantity)

print("Remaining stock:", product1.stock)
