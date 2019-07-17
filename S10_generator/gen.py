# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/21 下午5:43


"""
生成器的实现方式：
    1、列表生成式的[]换成();  生成器表达式。
    2、yield; 生成器函数。
"""

from collections.abc import Generator


# 生成器函数：只要有yield，就是生成器函数。
def gen_func():
    yield 1
    yield 2


def gen_func_1():
    html = yield "http://www.baidu.com"
    print("t", html)

    yield 2
    yield 3
    return "over"


if __name__ == '__main__':
    gen = gen_func()  # 返回生成器对象
    print(gen)  # <generator object gen_func at 0x1077d2f68>
    print(isinstance(gen, Generator))  # True
    for v in gen:
        print(v)

    gen = gen_func_1()
    url = next(gen)

    html = "haha"
    print(gen.send(html))
