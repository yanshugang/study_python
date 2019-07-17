# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/2 下午7:46

"""
send、close、throw


启动生成器的方式：
    1、next
    2、send（在调用send发送非None值之前，必须启动一次生成器。使用next(gen)或者gen.send(None)。）
"""


def gen_func():
    html = yield "http://baidu.com"
    print(html)
    yield 2
    yield 3
    return "over"


def jumping_range(N):
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index  # yield index是将index return给外部调用程序；jump = yield 可以接收外部程序通过send()发送的信息，并赋值给jump;
        if jump is None:
            jump = 1
        index += jump


if __name__ == '__main__':
    # itr = jumping_range(5)
    # print(next(itr))
    # print(itr.send(2))
    # print(next(itr))
    # print(itr.send(-1))

    gen = gen_func()
    url = next(gen)
    # print(url)
    gen.send("html")  # send方法可以传递值进入生成器内部，同时还可以重启生成器执行
