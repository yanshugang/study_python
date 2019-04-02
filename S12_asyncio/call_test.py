"""
call_soon
call_later
call_at
call_soon_threadsafe

"""

import asyncio


def callback(sleep_times):
    print("sleep {} success".format(sleep_times))


def stop_loop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # call_soon 即刻执行
    loop.call_soon(callback, 2)
    loop.call_soon(stop_loop, loop)
    loop.run_forever()
