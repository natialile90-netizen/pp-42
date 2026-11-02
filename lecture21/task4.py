
import requests
from requests.exceptions import HTTPError, ConnectTimeout, ReadTimeout

BASE_URL = "https://crudcrud.com/api/3490a8db33904208b18be9a8a129444b"

product_id = "6ae8d387284cd203e810be09"

updated_product = {
    "name": "Laptop",
    "price": 3000,
    "in_stock": True
}

try:
    response = requests.put(
        f"{BASE_URL}/products/{product_id}",
        json=updated_product,
        timeout=10
    )

    response.raise_for_status()

    print(response.status_code)

except HTTPError as error:
    print(error)

except ConnectTimeout as error:
    print(error)

except ReadTimeout as error:
    print(error)
