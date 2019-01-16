"""
执行完某个协程之后，执行callback逻辑
"""

import asyncio

import time
from functools import partial


async def get_html(url):
    print("start get url")
    # time.sleep(3)
    await asyncio.sleep(2)
    print("end get url")
    return "bobby"


# 使用偏函数实现回调的传参
def callback(url, future):
    print(url)
    print("senf email to bobby")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()

    task = loop.create_task(get_html("http://baidu.com"))
    task.add_done_callback(partial(callback, "http://baidu.com"))

    loop.run_until_complete(task)
    print(task.result())

    print(time.time() - start_time)
