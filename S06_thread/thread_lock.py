# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/14 下午2:20

"""
线程同步-LOCK
    1、获取锁、释放锁会影响性能；
    2、锁会引起死锁（两种情况：同一把锁连续acquire两次；两个线程互相等待；）

"""
import threading

total = 0
lock = threading.Lock()


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()  # 获取锁
        total += 1
        lock.release()  # 释放锁


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


thread_1 = threading.Thread(target=add)
thread_2 = threading.Thread(target=desc)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(total)  # 每次结果不一样
