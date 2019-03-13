# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午5:51
"""
wait
"""

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import time


def do_requests(url):
    time.sleep(2)
    return "{},抓取结果".format(url)


executor = ThreadPoolExecutor(max_workers=2)
urls = ["a", "b", "c", "d"]
# 通过submit函数，提交执行的函数到线程池，submit是立即返回
all_task = [executor.submit(do_requests, url) for url in urls]

# wait 作用：指定某些task完成后，才继续往下执行
wait(all_task, return_when=FIRST_COMPLETED)

# as_completed 获取已经成功的task的返回
for future in as_completed(all_task):
    data = future.result()
    print(data)
