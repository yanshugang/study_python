# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/7/18 下午4:48


def coroutine_example(name):
    print('start coroutine...name:', name)
    x = yield name  # 调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
    print('send值:', x)
    return "over"


coro = coroutine_example('Zarten')

print('next的返回值:', next(coro))
try:
    coro.send("haha")
except StopIteration as e:
    print(e.value)
