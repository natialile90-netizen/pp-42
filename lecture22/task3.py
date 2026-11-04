import time
import requests
from concurrent.futures import ThreadPoolExecutor


def fetch_data(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'

    response = requests.get(url, timeout=10)
    return response.json()


post_ids = range(1, 101)

start = time.time()

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_data, post_ids))

end = time.time()

print(f"ThreadPoolExecutor time: {end - start}")
print(f"Total results: {len(results)}")
