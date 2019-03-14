# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 上午11:16

import threading
from queue import Queue

import time


class ProducerThread(threading.Thread):
    def __init__(self, q):
        super().__init__(name="生成者")
        self.q = q

    def run(self):
        count = 0
        while True:
            if self.q.qsize() < 100:
                for i in range(100):
                    count += 1
                    msg = "元素-%s" % str(count)
                    self.q.put(msg)
                    print("{}: {}".format(threading.current_thread().name, msg))
                time.sleep(1)


class CustomerThread(threading.Thread):
    def __init__(self, q):
        super().__init__(name="消费者")
        self.q = q

    def run(self):
        while True:
            if self.q.qsize() > 10:
                for i in range(3):
                    msg = self.q.get()
                    print("{}: {}".format(threading.current_thread().name, msg))
                time.sleep(2)


def main():
    q = Queue(maxsize=100)

    # 启动10个消费者
    for i in range(10):
        c = CustomerThread(q)
        c.start()

    # 启动3个生成者
    for i in range(3):
        p = ProducerThread(q)
        p.start()


if __name__ == '__main__':
    main()
