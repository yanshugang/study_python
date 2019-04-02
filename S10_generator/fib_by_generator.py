# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/21 下午6:26

"""
使用生成器实现斐波拉切
"""


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def fib2(index):
    res_list = []
    n, a, b = 0, 0, 1
    while n < index:
        res_list.append(b)
        a, b = b, a + b
        n += 1
    return res_list


def fib3(index):
    """yield实现"""
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    res = fib(10)
    res2 = fib2(10)
    res3 = fib3(10)

    print(res)
    print(res2)
    print([i for i in res3])
