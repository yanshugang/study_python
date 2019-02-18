# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/18 下午3:12


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


if __name__ == '__main__':
    b = B()

# 既然我们重写B的构造函数，为什么还要去掉用super？
# super到底执行顺序是什么样的？涉及到MRO算法。
