
import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/3490a8db33904208b18be9a8a129444b"

product_id = "6ae8d387284cd203e810be09"

try:
    response = requests.get(
        f"{BASE_URL}/products/{product_id}",
        timeout=10
    )

    response.raise_for_status()

    print(response.status_code)
    print(response.json())

except HTTPError as error:
    print(error)

except ConnectTimeout as error:
    print("Server took too long")
