from dataclasses import dataclass
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


json_data = '{"name": "Perfume", "price": 180.0, "in_stock": true}'

data = json.loads(json_data)

restored_product = Product(**data)

print(restored_product)
print(restored_product.name)
print(restored_product.price)
print(restored_product.in_stock)