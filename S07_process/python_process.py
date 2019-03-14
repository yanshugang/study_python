# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午6:14

"""
多进程编程
"""
import multiprocessing

import time


def get_html(n):
    time.sleep(n)
    print("sub_process success")
    return n


if __name__ == '__main__':
    process = multiprocessing.Process(target=get_html, args=(2,))
    process.start()
    print(process.pid)
    process.join()
    print("end")
