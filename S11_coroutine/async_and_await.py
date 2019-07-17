# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/1 下午2:59

"""
python3.5之后，python中增加了原生的协程。
为了将语义变得更加明确，就引入了async和await关键词用来定义原生的协程。
"""
from collections.abc import Coroutine


async def downloader(url):
    return "=====html====={}".format(url)


async def download_url(url):
    html = await downloader(url)  # await只能接收Awaitable对象
    return html


if __name__ == '__main__':
    coro = download_url("http://www.baidu.com")
    print(isinstance(coro, Coroutine))
    coro.send(None)
