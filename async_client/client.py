import aiohttp
import asyncio

from confit import URL, BASE_URL


async def query_get(session: aiohttp.ClientSession, url: str):
    params = {"url": url}
    async with session.get(
            f"{BASE_URL}", params=params
    ) as response:
        return await response.json()


async def query_post(
        session: aiohttp.ClientSession,
        url: str
):
   data = {"url": url}
   async with session.post(
           f"{BASE_URL}", json=data
   ) as response:
       return await response.json()


async def shortening_links(url: str):
    async with aiohttp.ClientSession() as session:
       shortened_url = await asyncio.gather(
           query_post(session=session, url=url)
       )
       print(shortened_url)
       url = await asyncio.gather(
           query_get(session=session, url=shortened_url[0]["url"]),
       )
       print(url)


asyncio.run(shortening_links(url=URL))
