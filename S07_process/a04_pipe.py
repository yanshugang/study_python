# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/14 下午6:48

"""
通过pipe实现进程间通信
"""
import time
from multiprocessing import Pipe, Process


def producer(pipe):
    pipe.send("a")
    time.sleep(2)


def consumer(pipe):
    time.sleep(2)
    data = pipe.recv()
    print(data)


if __name__ == '__main__':
    recevide_pipe, send_pipe = Pipe()
    my_producer = Process(target=producer, args=(recevide_pipe,))
    my_consumer = Process(target=consumer, args=(send_pipe,))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()
