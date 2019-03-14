# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/12 下午2:58

"""
线程间通信
"""
import time
import threading
from queue import Queue


def get_detail_html(q):
    while True:
        url = q.get()  # 取数据，阻塞，没有数据会一直等。
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


def get_detail_url(q):
    while True:
        url = q.put()
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


def main():
    q = Queue(maxsize=100)
    url_thread = threading.Thread(target=get_detail_url, args=(q,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(q,))
        html_thread.start()

    q.task_done()
    q.join()
