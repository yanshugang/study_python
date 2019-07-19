"""
call_soon: 即刻执行
call_later: 延迟执行
call_at: 指定调用时间，以loop内部时间为基准
"""

import asyncio


def callback(sleep_times):
    print("sleep {} success".format(sleep_times))


def stop_loop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.call_later(3, callback, 3)  # 延迟3s调用
    loop.call_later(1, callback, 1)

    loop.call_soon(callback, 2)  # 传入一个函数
    # loop.call_soon(stop_loop, loop)  # 停止loop

    now = loop.time()
    loop.call_at(now + 2, callback, 1)

    loop.run_forever()
