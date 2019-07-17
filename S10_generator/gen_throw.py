# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/7/17 下午2:48


def gen_func():
    try:
        yield 1
    except Exception as e:
        print(e)
    yield 2
    yield 3


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
