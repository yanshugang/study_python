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
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return "ttt-ttt-ttt"


# 也可以添加一个callback
def func_callback(url, future):
    print("url: {} - get success".format(url))


if __name__ == '__main__':
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html("http://www.baidu.com"))
    # print(time.time() - start_time)

    # 使用task
    # start_time = time.time()
    # loop = asyncio.get_event_loop()  # 定义一个事件循环
    # tasks = [get_html("http://www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))  # 一次性提交多个任务时，使用wait
    # print(time.time() - start_time)

    # 获取协程的返回值-使用asyncio.ensure_future
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # 获取协程的返回值-使用loop.create_task，asyncio.ensure_future和loop.create_task等效
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.baidu.com"))
    # 也可以为task添加一个callback
    # task.add_done_callback(func_callback)
    task.add_done_callback(partial(func_callback, "http://www.baidu.com"))  # 如果callback方法需要传参，需要使用偏函数包装一下
    loop.run_until_complete(task)
    print(task.result())
