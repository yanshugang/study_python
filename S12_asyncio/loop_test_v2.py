"""
wait\gather区别：
    # gather更加ligh-level,使用更加灵活;
"""

import asyncio

import time


async def get_html(url):
    print("start get url")
    # time.sleep(3)
    await asyncio.sleep(2)
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("hhhh") for i in range(10)]

    # 可以实现任务分组
    group_1 = [get_html("hhhhh") for i in range(2)]
    group_2 = [get_html("ggggg") for i in range(2)]

    group_1 = asyncio.gather(*group_1)
    group_2 = asyncio.gather(*group_2)

    # 可以取消任务
    # group_2.cancel()

    loop.run_until_complete(asyncio.gather(group_1, group_2))

    print(time.time() - start_time)
