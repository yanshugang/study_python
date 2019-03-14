# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午4:51

"""
concurrent.futures

    1、concurrent.futures相比线程池的优势：
        a) 主线程中可以获取某个线程的状态或者某个任务的状态，以及返回值。当一个线程完成的时候主线程能够立即知道；
        b) concurrent.futures可以让多进程和多线程编码接口一致；
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_html(times):
    time.sleep(times)
    print("get page-{} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)

task_1 = executor.submit(get_html, 3)
task_2 = executor.submit(get_html, 2)

# done方法用于判定某个任务是否完成
print(task_1.done())
# 取消任务(未执行时可以取消)
print(task_1.cancel())
# 返回执行结果
print(task_1.result())

