# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/14 下午2:51

"""
线程同步-RLOCK-可重入的锁
    在同一个线程里面，可以连续调用多次acquire，但一定注意acquire和release次数要相等。
"""
import threading

total = 0
lock = threading.RLock()


def do_something(lock):
    lock.acquire()
    lock.release()


def add():
    global total
    global lock

    for i in range(1000000):
        lock.acquire()
        do_something(lock)
        total += 1
        lock.release()


def desc():
    global total
    global lock

    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


t_1 = threading.Thread(target=add)
t_2 = threading.Thread(target=desc)

t_1.start()
t_2.start()

t_1.join()
t_2.join()
print(total)
