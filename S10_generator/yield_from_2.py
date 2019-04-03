# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/3 下午4:33

"""
使用yield from 实现生成器嵌套

    1、调用方：调用委派生成器的客户端（调用方）代码
    2、委托生成器：包含yield from表达式的生成器函数
    3、子生成器：yield from后面加的生成器函数
"""


# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total / count


# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)  # 预激生成器
    print(calc_average.send(10))  # 10
    print(calc_average.send(20))  # 15
    print(calc_average.send(30))  # 20


if __name__ == '__main__':
    main()

"""
委托生成器的作用是：在调用方与子生成器之间建立一个双向通道。

所谓的双向通道是什么意思呢？
调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方。

"""