# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 上午11:16

import threading
from queue import Queue

import time


class ProducerThread(threading.Thread):
    def __init__(self, q):
        super().__init__(name="生产者")
        self.q = q

    def run(self):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        while True:
            time.sleep(3)
            try:
                count = num_list.pop()
                msg = "元素-%s" % str(count)
                self.q.put(msg)
                print("{}: {}".format(threading.current_thread().name, msg))
            except IndexError:
                print("生产完毕")
                break


class CustomerThread(threading.Thread):
    def __init__(self, q):
        super().__init__(name="消费者")
        self.q = q

    def run(self):
        while True:
            if not self.q.empty():
                msg = self.q.get()
                time.sleep(1)
                print("=={}: {}".format(threading.current_thread().name, msg))
                self.q.task_done()
            else:
                print("队列已空")
                break


def main():
    q = Queue(maxsize=100)

    # 启动生产者
    p = ProducerThread(q)
    p.start()

    time.sleep(3)

    # 启动10个消费者
    for i in range(10):
        c = CustomerThread(q)
        c.start()

    q.join()


if __name__ == '__main__':
    main()
