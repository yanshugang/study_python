# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/21 下午6:37

"""
python函数的工作原理
"""


def foo():
    bar()


def bar():
    pass

# python.exe会用一个pyEval_EvalFramEx(C函数)去执行foo函数，首先会创建一个栈帧
