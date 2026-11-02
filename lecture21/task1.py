import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/3490a8db33904208b18be9a8a129444b"

product = {
    "name": "Laptop",
    "price": 2500,
    "in_stock": True
}

try:
    response = requests.post(
        f"{BASE_URL}/products",
        json=product,
        timeout=10
    )

    response.raise_for_status()

    print(response.status_code)
    print(response.json())

except HTTPError as error:
    print(error)

except ConnectTimeout as error:
    print("Server took too long")

