"""
多线程
    生产者 -> Q1 -> 中间处理者 -> Q2 -> 消费者
"""

import threading
from queue import Queue

import time


class ProducerThread(threading.Thread):
    """
    生产者类
    """

    def __init__(self, q):
        super().__init__(name="生产者")
        self.q = q

    def run(self):
        if self.q.qsize() < 50:
            # 当q未满时，添加任务到q
            for i in range(100):
                time.sleep(0.1)
                self.q.put(i)
                print("添加任务-{}".format(i))


class MiddleHandleThread(threading.Thread):
    def __init__(self, q_1, q_2):
        super().__init__(name="中间处理")
        self.q_1 = q_1
        self.q_2 = q_2

    def run(self):
        while True:
            if self.q_1.qsize() > 10 and self.q_2.qsize() < 50:
                # q_1中的任务多于10个, 并且q_2未满时，开始处理
                data = self.q_1.get()
                self.q_1.task_done()
                print("开始处理-{}".format(data))
                res_data = str(data) + "aaa"

                self.q_2.put(res_data)
                print("处理完成-{}-{}".format(data, res_data))


class CustomerThread(threading.Thread):
    def __init__(self, q, write_handle):
        super().__init__(name="消费者")
        self.q = q
        self.writer = write_handle

    def save(self, data):
        self.writer.write(data + "\n")
        print("保存-{}".format(data))

    def run(self):
        while True:
            if self.q.qsize() > 10:
                # 队列中的结果大于10个时，开始执行
                data = self.q.get()
                self.q.task_done()
                self.save(data)


def main():
    q_1 = Queue(maxsize=50)  # 存储未处理的资源
    q_2 = Queue(maxsize=50)  # 存储已处理的结果

    write_handle = open("./res", "w")

    # 先启动消费者-1个
    c_thread = CustomerThread(q_2, write_handle)
    c_thread.start()

    # 启动中间处理-5个
    for i in range(5):
        print("启动中间处理进程-{}".format(i))
        m_thread = MiddleHandleThread(q_1, q_2)
        m_thread.start()

    # 启动生产者-1个
    p_thread = ProducerThread(q_1)
    p_thread.start()

    q_1.join()
    q_2.join()

    print("==2==", threading.enumerate())
    # c_thread.join()
    # write_handle.close()


if __name__ == '__main__':
    main()
