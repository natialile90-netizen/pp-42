import requests
import aiohttp
import asyncio
import time

url = "https://jsonplaceholder.typicode.com/todos/{}"

start = time.time()

for i in range(1, 11):
    response = requests.get(url.format(i))
    response.json()

sync_time = time.time() - start
print("Synchronous:", sync_time)

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[fetch_data(session, url.format(i)) for i in range(1, 11)]
        )

    async_time = time.time() - start
    print("Asynchronous:", async_time)

    if sync_time > async_time:
        print(f"Asynchronous version was {sync_time - async_time:.2f} seconds faster!")
    else:
        print(f"Asynchronous version was not faster. Difference: {async_time - sync_time:.2f} seconds")


asyncio.run(main())
