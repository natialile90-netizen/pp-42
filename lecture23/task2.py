import aiohttp
import asyncio

url = "https://jsonplaceholder.typicode.com/posts"

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        posts = await fetch_data(session, url)

        for post in posts[:20]:
            if post["userId"] == 1:
                print(post["title"])

if __name__ == "__main__":
    asyncio.run(main())
