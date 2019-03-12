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
