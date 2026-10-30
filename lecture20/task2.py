from dataclasses import dataclass, asdict
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


product1 = Product("Perfume", 555.0, True)
product2 = Product("Lipstick", 55.0, True)
product3 = Product("Mascara", 95.0, False)

data1 = asdict(product1)
data2 = asdict(product2)
data3 = asdict(product3)

products = [data1, data2, data3]

json_data = json.dumps(products, indent=4)

print(json_data)