# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/12 下午2:26
"""
通过实例化Thread实现多线程
"""

import time
import threading


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


if __name__ == '__main__':
    t_1 = threading.Thread(target=get_detail_html, args=("",))
    t_2 = threading.Thread(target=get_detail_url, args=("",))

    # t_1.setDaemon(True)  # True: 将子线程1设置为守护线程，当主线程退出时，子线程会被kill掉
    # t_2.setDaemon(True)

    start_time = time.time()
    t_1.start()
    t_2.start()

    t_1.join()  # 等待子线程执行完成再往下执行。
    t_2.join()

    print(time.time() - start_time)
