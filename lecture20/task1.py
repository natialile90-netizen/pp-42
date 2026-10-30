from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


product1 = Product("Dress", 250.0, True)
product2 = Product("Jeans", 150.0, False)
product3 = Product("Jacket", 400.0, True)

print(product1)
print(product2)
print(product3)