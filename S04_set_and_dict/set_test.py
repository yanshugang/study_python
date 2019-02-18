# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/18 下午6:59
"""
set 集合
fronzenset 不可变集合

无序，不重复
"""

t_1 = set("abc")
t_2 = set(["a", "b", "c", "d"])
print(t_1)  # {'c', 'a', 'b'}
print(t_2)  # {'a', 'd', 'b', 'c'}

t_3 = frozenset("abcde")  # frozenset, 不可变，可以作为dict的key。

# 向set添加数据
t_1.add()

# update

# difference 相当于求差集，返回新值，相当于：-

# 集合运算：/ & -

# in： __contains__

# issubset
