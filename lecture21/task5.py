import requests
from requests.exceptions import HTTPError, ConnectTimeout, ReadTimeout

BASE_URL = "https://crudcrud.com/api/3490a8db33904208b18be9a8a129444b"

product_id = "6ae8d33b284cd203e810be08"

try:
    response = requests.delete(
        f"{BASE_URL}/products/{product_id}",
        timeout=10
    )

    response.raise_for_status()

    print(response.status_code)
    print("Product deleted successfully")

except HTTPError as error:
    print(error)

except ConnectTimeout as error:
    print(error)

except ReadTimeout as error:
    print(error)
