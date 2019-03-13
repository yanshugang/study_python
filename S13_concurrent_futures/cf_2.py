# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午5:48

"""
as_completed
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

# as_completed是一个生成器，返回已经完成的任务。
for future in as_completed(all_task):
    data = future.result()
    print("get {}-page success".format(data))
