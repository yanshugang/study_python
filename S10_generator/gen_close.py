# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/7/17 下午2:38


def gen_func():
    try:
        yield 1
    except GeneratorExit as e:
        print(e)
    yield 2
    yield 3
    return "over"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    print(next(gen))
