# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/8 下午3:16

"""
异步爬取boss直聘

    1、使用多搜索词：数据开发、大数据开发、数据开发工程师、大数据开发共工程师、python数据开发、spark;
    2、根据job_id去重;
    3、结果输出到json;
    4、开发小工具：json to excel;


职位列表页：根据page-next获取下一页的link
"""
import aiohttp
import asyncio

# 存放列表页url
from lxml import etree

job_list_dict = {}  # 所有key的初始value为0，做过extract的key标记为1
job_info_urls = set()


# 相当于异步requests
async def fetch(session, url):
    async with session.get(url) as resp:
        print(resp.status)
        if resp.status in [200, 201]:
            data = await resp.content()
            return etree.HTML(data)


# 提取列表页url
def extract_list_url(html):
    next_page_link = html.xpath("//a[@ka='page-next']/@href")
    if next_page_link:
        url = "https://www.zhipin.com" + next_page_link
        job_list_dict[url] = 0


# 生产者, 抓取job_list_url。
# 从job_list_dict中get一个标记为0的url，去获取它的下一页，如果有下一页，就添加到job_list_dict。
async def product():
    while True:
        pass


# 消费者，从job_info_urls中
async def consumer():
    pass


async def main(loop, kw_list):
    # 文件句柄
    fw = open("./res", "w")

    url_list = ["https://www.zhipin.com/c101010100/?query={}".format(kw) for kw in kw_list]

    # 初始化url
    async with aiohttp.ClientSession() as session:
        for url in url_list:
            html = await fetch(session, url)
            extract_list_url(html)
            job_list_dict[url] = 1

    # 生产者
    asyncio.ensure_future(product())

    fw.close()


if __name__ == '__main__':
    search_kw_list = ["数据开发", "大数据开发", "数据开发工程师", "大数据开发工程师", ]

    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop, search_kw_list))
    loop.run_forever()

# 请求数 = 搜索词数量 * 310
