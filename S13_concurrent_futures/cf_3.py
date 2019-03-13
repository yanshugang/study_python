# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午5:48
"""
map
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_html(times):
    time.sleep(times)
    print("get page-{} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)

urls = [3, 4, 5]
all_task = [executor.submit(get_html, url) for url in urls]

# 也可以通过executor获取已经完成的task的返回值
# map() 所返回的值实际上是一个特殊的迭代器，它被主程序迭代时会等待其中的并发任务返回，没返回就一直等待
for future in executor.map(get_html, urls):
    data = future.result()
    print("get {}-page success".format(data))
