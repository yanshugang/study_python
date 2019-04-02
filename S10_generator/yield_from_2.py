# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/1 下午2:00

"""
yield from背后的原理

    _i: 子生成器，同时也是一个迭代器
    _y: 子生成器产生的值
    _r: yield from 表达式最终的值
    _s: 调用方通过send()发送的值
    _e: 异常对象
"""
import sys

_i = iter(EXPR)  # EXPR是一个可迭代对象，_i其实是子生成器；
try:
    _y = next(_i)  # 预激子生成器，把产出的第一个值存在_y中；
except StopIteration as e:
    _r = _e.value  # 如果抛出了StopIteration异常，则将异常对象的value值赋值给_r；
else:
    while True:  # 尝试执行这个循环，委托生成器会阻塞；
        _s = yield _y  # 生产子生成器的值，等待调用方send()值，发送过来的值将保存在_s;
        try:
            _y = _i.send(_s)  # 转发_s, 并尝试向下执行；
        except StopIteration as _e:
            _r = _e.value
            break
RESULT = _r  # _r就是整个yield from表达式返回的值；

"""
1、子生成器可能只是一个迭代器，并不是一个作为协程的生成器，所以它不支持throw()和close()方法；
2、如果子生成器支持throw()和close()方法，但是在子生成器内部，这两个方法都会抛出异常；
3、调用方让子生成器自己抛出异常；
4、当调用方使用next()或者send(None)时，都要在子生成器上调用next()函数，当调用方使用send()发送非None值时，才调用子生成器的send()方法；
"""

_i = iter(EXPR)  # EXPR是一个可迭代对象，_i其实是子生成器；
try:
    _y = next(_i)  # 预激子生成器，把产出的第一个值存在_y中；
except StopIteration as e:
    _r = _e.value  # 如果抛出了StopIteration异常，则将异常对象的value值赋值给_r；
else:
    while True:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError as _e:
                raise _e
            else:
                try:
                    y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break

ReSULT = _r

"""
总结：
    1、子生成器生产的值，都是直接传给调用方的；
        调用方通过send()发送的值都是直接传递给子生成器的；
        如果发送的是None，会调用子生成器的__next__()方法，如果不是None，会调用子生成器的send()方法；
    2、子生成器退出的时候，最后的return EXPR，会触发一个StopIteration(EXPR)异常；
    3、yield from表达式的值，是子生成器终止时，传递给StopIteration异常的第一个参数；
    4、如果调用的时候出现StopIteration异常，委托生成器会恢复运行，同时其他的异常会向上"冒泡"；
    5、传入委托生成器的异常里，除了GeneratorExit之外，其他的所有异常全部传递给子生成器的throw()方法；
        如果调用throw()时出现了StopIteration异常，那么就恢复委托生成器的运行，其他的异常全部去向上"冒泡"；
    6、如果在委托生成器上调用close()或者传入GenaratorExit异常，会调用子生成器的clsoe()方法，没有的话就不调用。
        如果在调用clsoe()时抛出异常，那么就向上冒泡，否则的话委托生成器会抛出GeneratorExit异常。
"""
