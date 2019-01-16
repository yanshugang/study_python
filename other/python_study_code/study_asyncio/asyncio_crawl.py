"""
aiohttp实现高并发爬虫
asyncio爬虫、去重、入库(aiomysql)

题外：sanic可以实现高并发服务器
"""

import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

stopping = False
start_url = "http://www.jobbole.com/"
waitting_urls = []
seen_urls = set()  # 对于大数据量(上亿条),需要使用布隆过滤器


async def fetch(url, session):
    try:
        async with session.get(url) as resp:
            print(resp.status)
            if resp.status in [200, 201]:
                data = await resp.text()
                return data
    except Exception as e:
        print(e)


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)

    return urls


async def init_urls(url):
    html = await fetch(url)
    extract_urls(html)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue

            url = waitting_urls.pop()

            if re.match("http://.*?jobbole.com/\d+/", url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url))


async def article_handler(url, session, pool):
    # 获取文章详情，并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into t_table(title) VALUES ('{}')".format(title)
            await cur.execute(insert_sql)


async def main(loop):
    # 建立mysql连接
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='mysql', loop=loop,
                                      charset='utf8', autocommit=True)
    asyncio.ensure_future(init_urls(start_url))
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
