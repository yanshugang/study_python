# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午4:51

"""
concurrent.futures

    1、concurrent.futures优势：
        a) 主线程中可以获取某个线程的状态以及返回值。
        b) 当一个线程完成的时候主线程能够立即知道。
        c) concurrent.futures可以让多进程和多线程编码接口一致；
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


def get_html(url):
    time.sleep(1)
    print("get page-{} success".format(url))
    return url


def main_1():
    executor = ThreadPoolExecutor(max_workers=2)

    # submit，提交任务到线程池，非阻塞。
    task = executor.submit(get_html, 3)

    # done方法用于判定某个任务是否完成
    print(task.done())
    # 取消任务(未执行时可以取消)
    print(task.cancel())
    # 返回执行结果
    print(task.result())


def main_2():
    executor = ThreadPoolExecutor(max_workers=2)

    urls = [3, 4, 5]
    all_task = [executor.submit(get_html, url) for url in urls]

    # as_completed是一个生成器，返回已经完成的任务。
    for future in as_completed(all_task):
        data = future.result()
        print(data)


def main_3():
    executor = ThreadPoolExecutor(max_workers=2)

    urls = [3, 4, 5]

    # 也可以通过executor获取已经完成的task的返回值
    # map() 所返回的值实际上是一个特殊的迭代器，它被主程序迭代时会等待其中的并发任务返回，没返回就一直等待
    # 直接返回执行结果
    for data in executor.map(get_html, urls):
        print("get {}-page success".format(data))


def main_4():
    executor = ThreadPoolExecutor(max_workers=2)
    urls = ["a", "b", "c", "d"]
    # 通过submit函数，提交执行的函数到线程池，submit是立即返回
    all_task = [executor.submit(get_html, url) for url in urls]

    # wait 作用：指定某些task完成后，才继续往下执行，用于阻塞主线程。
    wait(all_task, return_when=FIRST_COMPLETED)

    # as_completed 获取已经成功的task的返回
    for future in as_completed(all_task):
        data = future.result()
        print(data)


if __name__ == '__main__':
    main_2()
