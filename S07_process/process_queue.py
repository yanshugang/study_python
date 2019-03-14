# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/14 下午4:56
"""

"""
import time
from multiprocessing import Process, Queue


def producer(q):
    q.put("a")
    time.sleep(2)


def consumer(q):
    time.sleep(2)
    data = q.get()
    print(data)


if __name__ == '__main__':
    q = Queue(10)
    my_producer = Process(target=producer, args=(q,))
    my_consumer = Process(target=consumer, args=(q,))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()
