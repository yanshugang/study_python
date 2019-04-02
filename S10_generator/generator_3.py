# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/2 下午7:46

"""
向生成器发送消息
"""


def jumping_range(N):
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index  # yield index是将index return给外部调用程序；jump = yield 可以接收外部程序通过send()发送的信息，并赋值给jump;
        if jump is None:
            jump = 1
        index += jump


if __name__ == '__main__':
    itr = jumping_range(5)
    print(next(itr))
    print(itr.send(2))
    print(next(itr))
    print(itr.send(-1))
