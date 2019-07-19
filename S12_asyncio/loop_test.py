"""
1、如何使用asyncio定义一个协程
2、如何获取协程返回值
3、如何添加callback逻辑
"""
import time
import asyncio
from functools import partial


# 使用async定义一个协程
async def get_html(url):
    # 模拟html请求
    print("start get url")
    await asyncio.sleep(5)
    print("end get url")
    return "ttt-ttt-ttt"


# 也可以添加一个callback
def my_callback():
    print("url success")


if __name__ == '__main__':

    url = "http://www.baidu.com"
    coro = get_html(url)
    loop = asyncio.get_event_loop()  # 定义一个事件循环
    loop.run_until_complete(coro)

    # 一次提交多个任务
    url_list = ["http://www.baidu.com", "http://www.xinlang.com"]
    coro_list = [get_html(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(coro_list))

    # 获取协程的返回值，方法一：asyncio.ensure_future
    url = "http://www.baidu.com"
    coro = get_html(url)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(coro)
    loop.run_until_complete(future)
    print(future.result())  # 获取协程的运行结果

    # 获取协程的返回值，方法二：loop.create_task，asyncio.ensure_future和loop.create_task等效
    url = "http://www.baidu.com"
    coro = get_html(url)
    loop = asyncio.get_event_loop()
    task = loop.create_task(coro)
    # 也可以为task添加一个callback
    task.add_done_callback(my_callback)  # 如果callback需要传参，使用偏函数. task.add_done_callback(partial(my_callback, "xxx"))
    loop.run_until_complete(task)
    print(task.result())
