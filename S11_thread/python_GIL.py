"""
线程GIL锁, Global interpreter lock

python中的一个线程对应c语言中一个线程，gil使得同一时刻只有一个线程在一个cpu上执行字节码
这样是为了保证线程数据安全
python无法将多个线程映射到多个cpu上

python多线程为什么慢，是否是真的慢？

解释器:
    cpy:有GIL
    pypy:没有GIL

GIL会根据执行的字节码行数以及时间片释放，在遇到io操作的时候会主动释放。
"""
import threading

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread_1 = threading.Thread(target=add)
thread_2 = threading.Thread(target=desc)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(total)  # 每次结果不一样
"""
为什么每次结果不一样：
    从字节码的角度解释：a += 1
        1. load a
        2. load 1
        3. +
        4. 赋值给a
    因为GIL会根据执行的字节码的长度和时间片释放，所以多个线程执行时容易造成混乱。
    为了解决这个问题，python提供了线程同步机制，即几种锁的机制。
"""
