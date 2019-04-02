# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/2 下午5:00

"""
对比几种并发模式的效率

四种场景：
    CPU计算密集型
    磁盘IO密集型
    网络IO密集型
    模拟IO密集型

三种模式：
    单线程
    多线程
    多进程
"""
from multiprocessing import Process
from threading import Thread

import requests
import time


# cpu计算密集型
def count(x=1, y=1):
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y


# 定义磁盘读写IO密集型
def io_disk():
    with open("file_io_disk", "w") as fw:
        for x in range(500000):
            fw.write("python concurrent\n")


# 网络IO密集型
def io_requuest():
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36", }
    url = "https://www.tieba.com/"
    try:
        response = requests.get(url, headers=headers).content
        return
    except Exception as e:
        return {"error": e}


# 模拟IO密集型
def io_simulation():
    time.sleep(2)


# 定义一个时间计时器
def timer(mode):
    def wrapper(func):
        def deco(*args, **kwargs):
            type = kwargs.setdefault("type", None)
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time()
            cost_time = t2 - t1
            print("{}-{}花费时间: {}s".format(mode, type, cost_time))

        return deco

    return wrapper


# 单线程
@timer("[单线程]")
def single_thread(func, type=""):
    for i in range(10):
        func()


# 多线程
@timer("[多线程]")
def multi_thread(func, type=""):
    thread_list = []
    for i in range(10):
        t = Thread(target=func)
        thread_list.append(t)
        t.start()
    e = len(thread_list)

    while True:
        for th in thread_list:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break


# 多进程
@timer("[多进程]")
def multi_process(func, type=""):
    process_list = []
    for x in range(10):
        p = Process(target=func)
        process_list.append(p)
        p.start()
    e = len(process_list)

    while True:
        for pr in process_list:
            if not pr.is_alive():
                e -= 1
        if e <= 0:
            break


def main():
    print("=========={}==========".format("单线程"))
    single_thread(count, type="cpu计算密集型")
    single_thread(io_disk, type="磁盘IO密集型")
    single_thread(io_requuest, type="网络IO密集型")
    single_thread(io_simulation, type="模拟IO密集型")

    # print("=========={}==========".format("多线程"))
    # multi_thread(count, type="cpu计算密集型")
    # multi_thread(io_disk, type="磁盘IO密集型")
    # multi_thread(io_requuest, type="网络IO密集型")
    # multi_thread(io_simulation, type="模拟IO密集型")
    #
    # print("=========={}==========".format("多进程"))
    # multi_process(count, type="cpu计算密集型")
    # multi_process(io_disk, type="磁盘IO密集型")
    # multi_process(io_requuest, type="网络IO密集型")
    # multi_process(io_simulation, type="模拟IO密集型")


if __name__ == '__main__':
    main()
