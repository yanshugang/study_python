# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/1 上午11:33

from itertools import chain

my_list = [1, 2, 3]
my_dict = {"a1": "ggggg",
           "a2": "tttttt"}


# 使用生成器函数自己实现chain方法
def my_chain(*args, **kwargs):
    for my_iterabel in args:
        for value in my_iterabel:
            yield value


# 使用yield from实现chain方法
def my_chain_1(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable


# for value in chain(my_list, my_dict, range(5, 10)):
#     print(value)

# for value in my_chain(my_list, my_dict, range(5, 10)):
#     print(value)

for value in my_chain_1(my_list, my_dict, range(5, 10)):
    print(value)
