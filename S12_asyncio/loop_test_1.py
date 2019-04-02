# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/2 下午3:18
"""
wait和gather区别：
    # gather更加high-level,使用更加灵活;
    # gather可以实现task分组;
    # gather可以成批取消任务;
"""
import asyncio
import time


async def get_html(url):
    print("start get: {}".format(url))
    await asyncio.sleep(2)
    print("end get: {}".format(url))


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks = [get_html("http://www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))  # wait
    # loop.run_until_complete(asyncio.gather(*tasks))  # gather

    # gather可以实现task分组
    tasks_1 = [get_html("http://www.baidu.com") for i in range(10)]
    tasks_2 = [get_html("http://www.imooc.com") for i in range(10)]
    tasks_3 = [get_html("http://www.google.com") for i in range(10)]

    # 也可以取消任务
    tasks_3 = asyncio.gather(*tasks_3)
    tasks_3.cancel()

    loop.run_until_complete(asyncio.gather(*tasks_1, *tasks_2, * tasks_3))
    print(time.time() - start_time)
