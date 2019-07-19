"""
取消future或者task
"""

import asyncio


async def get_html(sleep_time):
    print("...")
    await asyncio.sleep(sleep_time)
    print("done after {}s".format(sleep_time))


if __name__ == '__main__':
    task_1 = get_html(1)
    task_2 = get_html(2)
    task_3 = get_html(3)

    tasks = [task_1, task_2, task_3]

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        # 查看全部task
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            task.cancel()

        loop.stop()
        loop.run_forever()
    finally:
        loop.close()

# 协程中调用子协程的原理
