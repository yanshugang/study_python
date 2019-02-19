# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/18 下午6:33

"""
python的dict是C语言写的，so, 不建议继承list和dict。
可以选择继承collections中的UserDict。
"""

from collections import UserDict
from collections import defaultdict


class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)

# defaultdict
my_dict = defaultdict(dict)
my_value = my_dict["haha"]
print(my_dict)

# TODO: __missing__魔法函数
