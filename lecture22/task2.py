import threading
import time
import requests


def fetch_data(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'

    response = requests.get(url, timeout=10)
    return response.json()


start = time.time()

thread_list = []

for i in range(1, 101):
    thread = threading.Thread(target=fetch_data, args=(i,))
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end = time.time()

print(f"Total time taken: {end - start}")
