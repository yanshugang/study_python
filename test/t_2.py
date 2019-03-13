# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午3:24
import threading
import time
from queue import Queue


def t1(q):
    while True:
        for i in range(5):
            q.put(i)


def t2(q):
    while True:
        if q.qsize()>0:
            item = q.get()

            print(item)
        else:
            print("empty")
            time.sleep(2)


def main():
    q = Queue()
    thread_1 = threading.Thread(target=t1, args=(q,))
    thread_1.start()

    for i in range(4):
        thread = threading.Thread(target=t2, args=(q,))
        thread.start()


if __name__ == '__main__':
    main()
