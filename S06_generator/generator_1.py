# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/21 下午5:43


"""
生成器：next、send
"""


# 生成器函数：只要有yield，就是生成器函数。
def gen_func():
    yield 1
    yield 2


def func():
    return 1


if __name__ == '__main__':
    gen = gen_func()  # 返回生成器对象
    for v in gen:
        print(v)
        # re = func()  # 返回结果值
        # pass
