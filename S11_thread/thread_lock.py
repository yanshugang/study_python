# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 上午11:57
"""
保证三个任务按顺序执行
"""
from threading import Thread, Lock
from time import sleep


class Task_1(Thread):
    def run(self):
        while True:
            if lock1.acquire():  # 对锁1上锁
                print('---task_1---')
                sleep(0.5)
                lock2.release()  # 开锁2


class Task_2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('---task_2---')
                sleep(0.5)
                lock3.release()


class Task_3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('---task_3---')
                sleep(0.5)
                lock1.release()


# 创建锁1,并保持打开状态
lock1 = Lock()

# 创建锁2,锁定
lock2 = Lock()
lock2.acquire()

# 创建锁3,锁定
lock3 = Lock()
lock3.acquire()

if __name__ == '__main__':
    t1 = Task_1()
    t2 = Task_2()
    t3 = Task_3()

    t1.start()
    t2.start()
    t3.start()
